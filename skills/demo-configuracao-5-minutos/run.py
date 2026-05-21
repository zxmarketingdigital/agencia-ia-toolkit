#!/usr/bin/env python3
"""
demo-configuracao-5-minutos — Setup completo do agente com timer ao vivo.
Agente IA WhatsApp em 15 Minutos | pay.hotmart.com/T105105999I
"""

import sys, time, os

# ── Cores ANSI ───────────────────────────────────────────────────────────────
R   = "\033[0m"
W   = "\033[1;37m"
DIM = "\033[2m"
P   = "\033[1;35m"
G   = "\033[1;32m"
C   = "\033[1;36m"
Y   = "\033[1;33m"

def clr():   os.system("clear")
def w(t="", end="\n"): print(t, end=end, flush=True)

def tw(text, delay=0.028, color=""):
    for ch in text:
        sys.stdout.write(color + ch + R)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def prog(label, duration=1.8, width=34, color=P):
    w(f"\n    {DIM}{label}{R}")
    for i in range(width + 1):
        bar = "█" * i + "░" * (width - i)
        pct = int(i / width * 100)
        sys.stdout.write(f"\r    {color}[{bar}]{R} {W}{pct}%{R}  ")
        sys.stdout.flush()
        time.sleep(duration / width)
    w()

def spinner(label, duration=0.9):
    frames = ["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"]
    end_t = time.time() + duration
    i = 0
    while time.time() < end_t:
        sys.stdout.write(f"\r    {P}{frames[i % len(frames)]}{R}  {label}  ")
        sys.stdout.flush()
        time.sleep(0.08)
        i += 1
    sys.stdout.write(f"\r    {G}✓{R}  {label}{' ' * 10}\n")
    sys.stdout.flush()

def qr_ascii():
    return [
        "  ██████████████  ████  ██████████████  ",
        "  ██          ██  ████  ██          ██  ",
        "  ██  ██████  ██  ████  ██  ██████  ██  ",
        "  ██  ██████  ██        ██  ██████  ██  ",
        "  ██  ██████  ██  ████  ██  ██████  ██  ",
        "  ██          ██  ████  ██          ██  ",
        "  ██████████████  ██  ████████████████  ",
        "                  ██                    ",
        "  ████████  ████████  ████  ██  ██████  ",
        "    ██  ████  ██  ████  ██  ████  ████  ",
        "  ████  ████████  ████████  ████  ████  ",
        "  ████  ██  ████  ██  ████  ████  ████  ",
        "  ████████  ████████  ████  ████  ████  ",
        "                  ████  ██  ████  ████  ",
        "  ██████████████  ████████  ████  ████  ",
        "  ██          ██  ██  ████  ████  ████  ",
        "  ██  ██████  ██  ████  ██  ████  ████  ",
        "  ██  ██████  ██        ██  ██  ██████  ",
        "  ██  ██████  ██  ████  ████  ████████  ",
        "  ██          ██  ██  ██  ██  ██  ████  ",
        "  ██████████████  ██████████  ████████  ",
    ]

# ── CONFIGURAÇÃO ─────────────────────────────────────────────────────────────

AGENTE   = "Ana"
PRODUTO  = "Agente IA WhatsApp 15M"
CHECKOUT = "pay.hotmart.com/T105105999I"

ETAPAS = [
    {
        "num":   1,
        "titulo": "Definindo a persona do agente",
        "items": [
            ("nome do agente",         "Ana"),
            ("tom de voz",             "informal, consultivo"),
            ("produto a vender",       PRODUTO),
            ("link de checkout",       CHECKOUT),
        ],
        "spinners": ["configurando identidade", "carregando prompt base"],
        "dur_prog": 1.6,
    },
    {
        "num":    2,
        "titulo": "Configurando inteligência BANT",
        "items": [
            ("gatilho de interesse",   "\"quanto custa\" → qualificar"),
            ("gatilho de objeção",     "\"caro\" → contornar com ROI"),
            ("gatilho de fechamento",  "score ≥ 3/4 → enviar link"),
            ("fallback humano",        "\"falar com pessoa\" → transferir"),
        ],
        "spinners": ["mapeando intenções", "criando fluxos de decisão"],
        "dur_prog": 1.8,
    },
    {
        "num":    3,
        "titulo": "Conectando ao WhatsApp",
        "items":  [],
        "spinners": ["inicializando Evolution API", "aguardando pareamento QR"],
        "dur_prog": 1.4,
        "qr": True,
    },
    {
        "num":    4,
        "titulo": "Testando primeira conversa",
        "items": [
            ("mensagem de teste",      "\"Oi, quanto custa?\""),
            ("resposta do agente",     f"✓ gerada em 0.9s"),
            ("link de checkout",       f"✓ enviado automaticamente"),
            ("log registrado",         "✓ SQLite atualizado"),
        ],
        "spinners": ["simulando lead de teste", "validando fluxo completo"],
        "dur_prog": 1.5,
    },
    {
        "num":    5,
        "titulo": "Ativando monitoramento",
        "items": [
            ("LaunchAgent",            "✓ registrado (auto-start)"),
            ("heartbeat",             f"✓ check a cada 5 min"),
            ("logs",                   "✓ ~/.operacao-ia/agente.log"),
            ("status",                 "✓ /status disponível"),
        ],
        "spinners": ["registrando na Mission Control", "agente go live"],
        "dur_prog": 1.3,
    },
]

# ── MAIN ──────────────────────────────────────────────────────────────────────

def main():
    clr()

    # Banner
    w(f"\n{P}  ╔══════════════════════════════════════════════╗{R}")
    w(f"{P}  ║{W}    SETUP AGENTE IA — 5 ETAPAS               {P}║{R}")
    w(f"{P}  ║{DIM}    Promessa: configurado em menos de 15 min  {P}║{R}")
    w(f"{P}  ╚══════════════════════════════════════════════╝{R}\n")
    time.sleep(0.5)

    start_total = time.time()

    for etapa in ETAPAS:
        elapsed = time.time() - start_total
        mins    = int(elapsed // 60)
        secs    = int(elapsed % 60)

        w(f"\n{P}  ▸ ETAPA {etapa['num']}/5{R}  {W}{etapa['titulo']}{R}  {DIM}[{mins:02d}:{secs:02d}]{R}")

        if etapa.get("items"):
            w()
            w(f"  {DIM}┌───────────────────────────────────────────────┐{R}")
            for chave, valor in etapa["items"]:
                w(f"  {DIM}│{R}  {DIM}{chave:<25}{R}  {W}{valor}{R}")
                time.sleep(0.2)
            w(f"  {DIM}└───────────────────────────────────────────────┘{R}")

        prog(f"configurando etapa {etapa['num']}...", duration=etapa["dur_prog"])

        for s in etapa["spinners"]:
            spinner(s, 0.9)

        if etapa.get("qr"):
            w(f"\n  {Y}┌─ Escaneie o QR Code com seu WhatsApp ─────────┐{R}")
            for line in qr_ascii():
                w(f"  {Y}│{R}{line}{Y}│{R}")
                time.sleep(0.04)
            w(f"  {Y}└───────────────────────────────────────────────┘{R}")
            spinner("pareando dispositivo", 1.2)
            w(f"\n  {G}✓{R}  {W}WhatsApp conectado{R}")

        time.sleep(0.3)

    # Tempo total
    total = time.time() - start_total
    mins  = int(total // 60)
    secs  = int(total % 60)

    w(f"\n{DIM}  {'─' * 52}{R}\n")
    w(f"{P}  ══════════════════════════════════════════════════{R}\n")
    w(f"  {G}●{R}  etapas concluídas  {W}5/5{R}")
    w(f"  {G}●{R}  tempo total        {W}{mins:02d}:{secs:02d}{R}  {G}< 15 minutos ✓{R}")
    w(f"  {G}●{R}  agente             {W}{AGENTE} — ONLINE{R}")
    w(f"  {G}●{R}  produto            {W}{PRODUTO}{R}")
    w(f"  {G}●{R}  monitoramento      {W}heartbeat ativo{R}")
    w()

    w(f"{P}  ══════════════════════════════════════════════════{R}\n")
    tw(f"  🟢  CONFIGURADO EM {mins:02d}:{secs:02d}. AGENTE NO AR.", delay=0.035, color=G+W)
    w(f"\n  {DIM}► {CHECKOUT}{R}\n")
    w(f"{P}  ══════════════════════════════════════════════════{R}\n")
    time.sleep(1.0)

if __name__ == "__main__":
    main()
