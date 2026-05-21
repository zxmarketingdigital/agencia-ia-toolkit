#!/usr/bin/env python3
"""
demo-qualificacao-bant — Conversa BANT completa: do oi ao link.
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

def spinner(label, duration=0.8):
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

def digitando(agente, dur=1.0):
    """Simula agente digitando."""
    frames = ["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"]
    end_t = time.time() + dur
    i = 0
    while time.time() < end_t:
        sys.stdout.write(f"\r  {Y}{frames[i%len(frames)]}{R}  {DIM}{agente} digitando...{R}  ")
        sys.stdout.flush()
        time.sleep(0.08)
        i += 1
    sys.stdout.write(f"\r{' ' * 40}\r")
    sys.stdout.flush()

def msg_lead(texto, pausa=0.5):
    w(f"  {C}◀ LEAD{R}  {texto}")
    time.sleep(pausa)

def msg_agente(agente, texto, pausa=0.6, dur_digitando=1.0):
    digitando(agente, dur_digitando)
    w(f"  {P}▶ {agente.upper()}{R}  {texto}")
    time.sleep(pausa)

def tag_bant(etapa, valor):
    w(f"\n  {DIM}┌─ BANT{R}  {Y}{etapa}{R}  {W}{valor}{R}  {DIM}✓ identificado{R}\n")
    time.sleep(0.3)

# ── CONFIGURAÇÃO ─────────────────────────────────────────────────────────────

AGENTE   = "Ana"
LEAD     = "Ricardo"
CHECKOUT = "pay.hotmart.com/T105105999I"
PRODUTO  = "Agente IA WhatsApp 15M"

# ── MAIN ──────────────────────────────────────────────────────────────────────

def main():
    clr()

    # Banner
    w(f"\n{P}  ╔══════════════════════════════════════════════╗{R}")
    w(f"{P}  ║{W}    QUALIFICAÇÃO BANT — AGENTE IA WHATSAPP    {P}║{R}")
    w(f"{P}  ║{DIM}    {AGENTE} qualifica {LEAD} em tempo real{' '*(22-len(AGENTE)-len(LEAD))}{P}║{R}")
    w(f"{P}  ╚══════════════════════════════════════════════╝{R}\n")
    time.sleep(0.4)

    spinner("carregando context BANT", 0.8)
    spinner("agente pronto", 0.6)
    w(f"\n{DIM}  {'─' * 52}{R}\n")
    time.sleep(0.4)

    # ── ABERTURA ────────────────────────────────────────────────────────────
    w(f"  {DIM}[ NEED — identificando necessidade ]{R}\n")

    msg_lead("Oi, quero entender melhor esse agente de IA")
    msg_agente(AGENTE,
        "Oi Ricardo! Sou a Ana 👋 Me conta — qual é seu maior desafio hoje com atendimento no WhatsApp?",
        dur_digitando=1.1)

    msg_lead("Tenho 80+ mensagens por dia e não consigo responder tudo a tempo")
    msg_agente(AGENTE,
        "Entendo. Então você tá perdendo venda porque não tem velocidade de resposta, certo?",
        dur_digitando=0.9)

    msg_lead("Exatamente. Às vezes o cliente some antes de eu responder")

    tag_bant("NEED", "perde vendas por lentidão de resposta")

    # ── BUDGET ──────────────────────────────────────────────────────────────
    w(f"  {DIM}[ BUDGET — verificando viabilidade ]{R}\n")

    msg_agente(AGENTE,
        "Faz sentido. Um agente resolve isso. Você tem investimento previsto pra automação?",
        dur_digitando=1.0)

    msg_lead("Depende do preço. Quanto é?")
    msg_agente(AGENTE,
        "É um investimento único de R$97. Sem mensalidade. Qual o ticket médio dos seus produtos?",
        dur_digitando=0.8)

    msg_lead("Vendo cursos de R$300 a R$500")
    msg_agente(AGENTE,
        "Então 1 venda já paga o agente. E ele fica trabalhando pra você 24 horas por dia 😊",
        dur_digitando=0.9)

    tag_bant("BUDGET", "R$97 viável — 1 venda paga o investimento")

    # ── AUTHORITY ───────────────────────────────────────────────────────────
    w(f"  {DIM}[ AUTHORITY — quem decide ]{R}\n")

    msg_agente(AGENTE,
        "Você é o responsável pelo negócio ou precisa consultar alguém antes de fechar?",
        dur_digitando=0.7)

    msg_lead("Sou eu mesmo, trabalho solo")

    tag_bant("AUTHORITY", "decisor único — sem aprovação necessária")

    # ── TIMELINE ────────────────────────────────────────────────────────────
    w(f"  {DIM}[ TIMELINE — urgência ]{R}\n")

    msg_agente(AGENTE,
        "Ótimo. E quando você precisa resolver esse problema do atendimento?",
        dur_digitando=0.7)

    msg_lead("Quanto antes melhor, tô perdendo venda toda semana")
    msg_agente(AGENTE,
        "Entendo a urgência. Bom — com o agente você configura em 15 minutos e hoje mesmo já tá atendendo.",
        dur_digitando=1.2)

    tag_bant("TIMELINE", "urgente — precisa de solução imediata")

    # ── CLASSIFICAÇÃO ───────────────────────────────────────────────────────
    w(f"{DIM}  {'─' * 52}{R}\n")

    w(f"  {DIM}▸ processando classificação BANT...{R}")
    time.sleep(0.8)

    w(f"\n{P}  ══════════════════════════════════════════════════{R}\n")
    w(f"  {G}●{R}  NEED       {W}perde vendas por lentidão{R}      {G}✓{R}")
    w(f"  {G}●{R}  BUDGET     {W}R$97 viável · 1 venda cobre{R}    {G}✓{R}")
    w(f"  {G}●{R}  AUTHORITY  {W}decisor único{R}                  {G}✓{R}")
    w(f"  {G}●{R}  TIMELINE   {W}urgente{R}                        {G}✓{R}")
    w()
    time.sleep(0.5)

    # Score
    w(f"  {Y}▸ SCORE BANT:{R}  {W}4/4{R}  {G}→  LEAD HOT 🔥{R}\n")
    time.sleep(0.4)

    # Envio do link
    w(f"{DIM}  {'─' * 52}{R}\n")
    digitando(AGENTE, 1.3)

    w(f"  {P}▶ {AGENTE.upper()}{R}  Ricardo, você é exatamente o perfil que o agente resolve.")
    time.sleep(0.3)
    digitando(AGENTE, 0.7)
    w(f"  {P}▶ {AGENTE.upper()}{R}  Garante agora por R$97 e tá respondendo leads hoje:")
    time.sleep(0.3)
    digitando(AGENTE, 0.5)
    w(f"  {P}▶ {AGENTE.upper()}{R}  {C}🔗 {CHECKOUT}{R}")
    time.sleep(0.6)

    w(f"\n{P}  ══════════════════════════════════════════════════{R}\n")
    tw(f"  🔥  LEAD HOT → LINK ENVIADO AUTOMATICAMENTE.", delay=0.035, color=G+W)
    w(f"\n  {DIM}► {CHECKOUT}{R}\n")
    w(f"{P}  ══════════════════════════════════════════════════{R}\n")
    time.sleep(1.0)

if __name__ == "__main__":
    main()
