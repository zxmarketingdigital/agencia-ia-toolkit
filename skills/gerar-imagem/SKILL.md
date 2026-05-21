---
name: gerar-imagem
description: "Gera imagem PNG usando gpt-image-2 (via Codex CLI logado em ChatGPT) como provider principal e Gemini Nano Banana / Imagen 4 como fallback. Use SEMPRE que o usuario disser: gerar imagem, criar thumbnail, gerar thumb, criar imagem, gerar foto, criar arte, gerar criativo, fazer thumbnail, image2, gpt-image, nano banana. Outras skills (youtube-publisher, etc) devem invocar este helper em vez de chamar Gemini direto."
model: haiku
effort: medium
---

# /gerar-imagem — Gerador de Imagens (Image 2 primario, Gemini fallback)

Helper unico para geracao de imagem no ZX LAB. Cobre dois casos:

1. **Chamada interativa** pelo usuario (`/gerar-imagem ...`) → roda o script `scripts/gerar.py` com os args.
2. **Chamada programatica** por outras skills (youtube-publisher, prototipo-agencia-ia, etc) → outras skills executam `python3 ~/.claude/skills/gerar-imagem/scripts/gerar.py ...` direto.

## Cadeia de providers

| Ordem | Provider | Como | Custo |
|-------|----------|------|-------|
| 1 | **gpt-image-2** (OpenAI) | `codex exec` com tool `image_gen` nativa (login ChatGPT) | Assinatura ChatGPT — nao bate no hard limit da API |
| 2 | **gemini-3.1-flash-image-preview** ("Nano Banana") | Google GenAI SDK | Free tier / chave Gemini |
| 3 | **imagen-4.0-ultra-generate-001** | Google GenAI SDK | Free tier / chave Gemini |

A escolha automatica usa o primeiro que estiver disponivel. Para forcar provider: `--provider image2|gemini|imagen`.

## Quando chamar

- Usuario pede: "gere uma imagem de X", "thumbnail pra Y", "criativo Z"
- Outra skill precisa de imagem (youtube thumb, banner LP, criativo Meta)
- Script Python qualquer precisa gerar PNG

NAO usar para: logos vetoriais com texto preciso (preferir SVG manual ou skill `frontend-design`), edicao de imagem existente (skill huashu-design), video (skill gerar-video-mp4).

## Uso

```bash
python3 ~/.claude/skills/gerar-imagem/scripts/gerar.py \
  --prompt "professional youtube thumbnail, robot mascot coral orange, dark background" \
  --output /tmp/thumb.png \
  --size 1280x720
```

Flags:
- `--prompt` (obrigatorio) — descricao da imagem
- `--output` (obrigatorio) — caminho do PNG final
- `--size` — `1024x1024` (default), `1280x720`, `1792x1024`, `1024x1792`
- `--provider` — `auto` (default), `image2`, `gemini`, `imagen`
- `--quality` — `high` (default), `medium`, `low`

Output: imprime path do PNG salvo + provider usado + tempo. Retorna exit 0 em sucesso.

## Cabling com outras skills

**youtube-publisher** chama:
```python
import subprocess, json
result = subprocess.run([
    "python3", os.path.expanduser("~/.claude/skills/gerar-imagem/scripts/gerar.py"),
    "--prompt", THUMB_PROMPT,
    "--output", "/tmp/thumb.png",
    "--size", "1280x720",
    "--json",
], capture_output=True, text=True, check=True)
info = json.loads(result.stdout)
print(f"Thumb gerada via {info['provider']} em {info['elapsed_s']}s")
```

## Detalhes tecnicos

- **Image 2 via Codex**: `codex exec` precisa de login ChatGPT (`codex login status` → "Logged in using ChatGPT"). Imagem nativa sai em `~/.codex/generated_images/{session}/ig_*.png`, o script copia pro destino e roda `sips` para resize.
- **Gemini**: usa `GEMINI_API_KEY` do env ou `~/.operacao-ia/config/*.env`.
- **Codex MCP error noise**: `codex exec` imprime erro do MCP Cloudflare no stderr (auth nao logado). E inocuo, ignorar.

## Referencia
- Codex tem skill interna em `~/.codex/skills/.system/imagegen/` com helper `remove_chroma_key.py` para fundo transparente. Se precisar de transparencia, usar `--provider image2 --transparent`.
