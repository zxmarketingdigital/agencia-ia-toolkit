#!/usr/bin/env python3
"""Gerador de imagem ZX LAB — gpt-image-2 primario, Gemini/Imagen fallback.

Uso:
  python3 gerar.py --prompt "..." --output /path/file.png [--size WxH] [--provider auto|image2|gemini|imagen] [--json]
"""
import argparse
import base64
import fcntl
import glob
import json
import os
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request
from contextlib import contextmanager

VALID_SIZES = {
    "1024x1024", "1280x720", "720x1280", "1792x1024", "1024x1792", "1536x1024", "1024x1536",
    "1080x1080", "1080x1350", "1080x1920", "1920x1080",
}
CODEX_GEN_DIR = os.path.expanduser("~/.codex/generated_images")
ENV_DIR = os.path.expanduser("~/.operacao-ia/config")
# Lock soft pra serializar a janela "snapshot pre-dirs / codex exec / snapshot post-dirs / copy".
# Necessario porque chamadas paralelas podiam ver o mesmo conjunto de dirs novos e copiar o mesmo PNG.
GERAR_LOCK = "/tmp/gerar-imagem-codex.lock"


@contextmanager
def codex_lock():
    """Lock exclusivo entre processos pro trecho critico do gen_image2."""
    fd = os.open(GERAR_LOCK, os.O_CREAT | os.O_RDWR, 0o600)
    try:
        fcntl.flock(fd, fcntl.LOCK_EX)
        yield
    finally:
        try:
            fcntl.flock(fd, fcntl.LOCK_UN)
        finally:
            os.close(fd)


def log(msg, json_mode):
    if not json_mode:
        print(msg, file=sys.stderr, flush=True)


def load_env_key(name):
    if os.environ.get(name):
        return os.environ[name]

    candidates = []
    if os.path.isdir(ENV_DIR):
        candidates += sorted(
            os.path.join(ENV_DIR, f)
            for f in os.listdir(ENV_DIR) if f.endswith(".env")
        )
    candidates += [
        os.path.expanduser("~/.zshrc"),
        os.path.expanduser("~/.profile"),
        os.path.expanduser("~/.bashrc"),
        os.path.expanduser("~/.openclaw/.env"),
    ]

    import re
    pattern = re.compile(rf'^\s*(?:export\s+)?{re.escape(name)}\s*=\s*["\']?([^"\'\s#]+)')
    for path in candidates:
        if not os.path.isfile(path):
            continue
        try:
            with open(path) as f:
                for line in f:
                    m = pattern.match(line)
                    if m:
                        val = m.group(1).strip()
                        if val and not val.startswith("$") and val not in {"YOUR_API_KEY", "secret-key", "another-secret"}:
                            return val
        except OSError:
            continue
    return None


def resize_png(path, target_size):
    w, h = target_size.split("x")
    subprocess.run(
        ["sips", "-z", h, w, path],
        check=True, capture_output=True
    )


def gen_image2(prompt, output, size, quality, json_mode):
    """Generate via Codex CLI built-in image_gen tool (gpt-image-2)."""
    if shutil.which("codex") is None:
        raise RuntimeError("codex CLI nao instalado")

    status = subprocess.run(
        ["codex", "login", "status"], capture_output=True, text=True
    )
    combined = (status.stdout or "") + (status.stderr or "")
    if "Logged in" not in combined:
        raise RuntimeError(f"codex nao logado: {combined.strip()}")

    if os.path.exists(output):
        os.remove(output)

    instructions = (
        f"Use case: photorealistic-natural\n"
        f"Primary request: {prompt}\n"
        f"Quality: {quality}. Target size: {size}.\n"
        f"Use the built-in image_gen tool (gpt-image-2). Generate ONE image. "
        f"Save the final PNG to {output}. "
        f"Do not create SVG or vector — must be raster from image_gen. "
        f"At the end print just the absolute path of the saved PNG."
    )

    # Lock ate a copia do PNG. Janela curta — nao bloqueia o codex exec entre processos
    # diferentes, so impede que dois processos confundam o diff de dirs/PNGs.
    with codex_lock():
        # Snapshot ANTES: tanto dirs quanto PNGs. Comparar dirs e mais robusto que comparar PNGs
        # (dir e criado atomicamente pelo codex no inicio da session, PNGs aparecem depois).
        pre_dirs = set()
        if os.path.isdir(CODEX_GEN_DIR):
            pre_dirs = {p for p in os.listdir(CODEX_GEN_DIR)
                        if os.path.isdir(os.path.join(CODEX_GEN_DIR, p))}
        before_pngs = set(glob.glob(f"{CODEX_GEN_DIR}/**/ig_*.png", recursive=True))

        log("[image2] chamando codex exec...", json_mode)
        proc = subprocess.run(
            ["codex", "exec", "--skip-git-repo-check",
             "-c", "mcp_servers={}",
             instructions],
            capture_output=True, text=True, stdin=subprocess.DEVNULL,
            timeout=240
        )

        if proc.returncode != 0:
            raise RuntimeError(f"codex exec falhou: {proc.stderr[-400:]}")

        if not os.path.exists(output):
            # Cada `codex exec` cria um diretorio unico em ~/.codex/generated_images/<session-uuid>/.
            # Estrategia em camadas:
            #  1. Tenta extrair session id do output (caminho rapido se regex bater)
            #  2. Diff de DIRS criados durante a chamada (mais robusto que diff de PNGs)
            #  3. Ultimo recurso: diff de PNGs (com warning — vulneravel a race se sair do lock)
            import re as _re
            combined_io = (proc.stdout or "") + "\n" + (proc.stderr or "")
            session_match = _re.search(r"session id:\s*([0-9a-f-]{36})", combined_io)
            src = None

            if session_match:
                session_id = session_match.group(1)
                session_dir = os.path.join(CODEX_GEN_DIR, session_id)
                session_files = sorted(
                    glob.glob(f"{session_dir}/ig_*.png"),
                    key=os.path.getmtime, reverse=True
                )
                if session_files:
                    src = session_files[0]

            if src is None and os.path.isdir(CODEX_GEN_DIR):
                # Camada 2: diff de DIRS — pega o dir novo mais recente e o PNG dentro dele.
                post_dirs = {p for p in os.listdir(CODEX_GEN_DIR)
                             if os.path.isdir(os.path.join(CODEX_GEN_DIR, p))}
                new_dirs = sorted(
                    post_dirs - pre_dirs,
                    key=lambda d: os.path.getmtime(os.path.join(CODEX_GEN_DIR, d)),
                    reverse=True
                )
                for d in new_dirs:
                    pngs = glob.glob(os.path.join(CODEX_GEN_DIR, d, "ig_*.png"))
                    if pngs:
                        src = sorted(pngs, key=os.path.getmtime, reverse=True)[0]
                        break

            if src is None:
                # Camada 3 (ultimo recurso): diff de PNGs global. Pode pegar PNG de outra
                # chamada se o lock nao funcionou — log explicito pra debugar.
                log("[image2] WARN: caindo no fallback de diff global de PNGs", json_mode)
                after_pngs = set(glob.glob(f"{CODEX_GEN_DIR}/**/ig_*.png", recursive=True))
                new_files = sorted(after_pngs - before_pngs, key=os.path.getmtime, reverse=True)
                if not new_files:
                    raise RuntimeError(
                        "codex executou mas nao achei PNG gerado "
                        "(nem por session id, nem por diff de dirs, nem por diff de PNGs). "
                        f"stdout tail: {proc.stdout[-300:]}"
                    )
                src = new_files[0]

            shutil.copy(src, output)

    resize_png(output, size)
    return "image2"


def gen_gemini(prompt, output, size, model, json_mode):
    """Generate via Google GenAI — gemini-* usa :generateContent, imagen-* usa :predict."""
    key = load_env_key("GEMINI_API_KEY") or load_env_key("GOOGLE_API_KEY")
    if not key:
        raise RuntimeError("GEMINI_API_KEY nao encontrada no env nem em ~/.operacao-ia/config/*.env")

    is_imagen = model.startswith("imagen")
    log(f"[{model}] chamando Google GenAI ({'predict' if is_imagen else 'generateContent'})...", json_mode)

    if is_imagen:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:predict?key={key}"
        payload = {
            "instances": [{"prompt": prompt}],
            "parameters": {"sampleCount": 1},
        }
    else:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"
        payload = {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {"responseModalities": ["IMAGE"]},
        }

    req = urllib.request.Request(
        url, data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"}, method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            data = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"Gemini HTTP {e.code}: {e.read().decode()[:300]}")

    b64 = None
    if is_imagen:
        preds = data.get("predictions") or []
        if preds:
            b64 = preds[0].get("bytesBase64Encoded") or preds[0].get("imageBytes")
    else:
        parts = (data.get("candidates") or [{}])[0].get("content", {}).get("parts", [])
        for p in parts:
            if "inlineData" in p:
                b64 = p["inlineData"].get("data")
                break
            if "inline_data" in p:
                b64 = p["inline_data"].get("data")
                break
    if not b64:
        raise RuntimeError(f"Gemini sem image data. Resposta: {json.dumps(data)[:300]}")

    with open(output, "wb") as f:
        f.write(base64.b64decode(b64))
    resize_png(output, size)
    return model


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--size", default="1024x1024")
    ap.add_argument("--provider", default="auto",
                    choices=["auto", "image2", "gemini", "imagen"])
    ap.add_argument("--quality", default="high",
                    choices=["high", "medium", "low"])
    ap.add_argument("--json", action="store_true",
                    help="output JSON em stdout (silencioso em stderr)")
    args = ap.parse_args()

    if args.size not in VALID_SIZES:
        print(f"ERRO: size '{args.size}' invalido. Use: {sorted(VALID_SIZES)}", file=sys.stderr)
        sys.exit(2)

    os.makedirs(os.path.dirname(os.path.abspath(args.output)) or ".", exist_ok=True)

    if args.provider == "auto":
        chain = [
            ("image2", lambda: gen_image2(args.prompt, args.output, args.size, args.quality, args.json)),
            ("gemini", lambda: gen_gemini(args.prompt, args.output, args.size, "gemini-3.1-flash-image-preview", args.json)),
            ("imagen", lambda: gen_gemini(args.prompt, args.output, args.size, "imagen-4.0-ultra-generate-001", args.json)),
        ]
    elif args.provider == "image2":
        chain = [("image2", lambda: gen_image2(args.prompt, args.output, args.size, args.quality, args.json))]
    elif args.provider == "gemini":
        chain = [("gemini", lambda: gen_gemini(args.prompt, args.output, args.size, "gemini-3.1-flash-image-preview", args.json))]
    elif args.provider == "imagen":
        chain = [("imagen", lambda: gen_gemini(args.prompt, args.output, args.size, "imagen-4.0-ultra-generate-001", args.json))]

    errors = []
    t0 = time.time()
    used = None
    for name, fn in chain:
        try:
            used = fn()
            break
        except Exception as e:
            errors.append(f"{name}: {e}")
            log(f"[{name}] falhou: {e}", args.json)

    elapsed = round(time.time() - t0, 1)

    if used is None:
        result = {
            "ok": False,
            "errors": errors,
            "elapsed_s": elapsed,
        }
        if args.json:
            print(json.dumps(result))
        else:
            print("FALHA — todos os providers falharam:", file=sys.stderr)
            for e in errors:
                print(f"  - {e}", file=sys.stderr)
        sys.exit(1)

    size_bytes = os.path.getsize(args.output)
    result = {
        "ok": True,
        "provider": used,
        "output": os.path.abspath(args.output),
        "size_bytes": size_bytes,
        "elapsed_s": elapsed,
    }
    if args.json:
        print(json.dumps(result))
    else:
        print(f"OK — provider={used} path={args.output} bytes={size_bytes} elapsed={elapsed}s")


if __name__ == "__main__":
    main()
