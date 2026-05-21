#!/usr/bin/env bash
# Toolkit Agência IA — instalador
# Copia as 12 skills para ~/.claude/skills/ e abre os 2 dashboards no navegador.

set -e

REPO_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
SKILLS_SRC="$REPO_DIR/skills"
SKILLS_DST="$HOME/.claude/skills"
DASHBOARDS_DIR="$REPO_DIR/dashboards"
TOOLKIT_DIR="$HOME/meu-toolkit"

# ── cores ──
B='\033[1m'; G='\033[32m'; Y='\033[33m'; R='\033[31m'; C='\033[36m'; D='\033[2m'; N='\033[0m'

banner() {
  echo
  echo -e "${C}╔══════════════════════════════════════════════════════════════╗${N}"
  echo -e "${C}║  ${B}Toolkit Agência IA${N}${C} · instalação                          ║${N}"
  echo -e "${C}║  ${D}12 skills Claude Code + 2 dashboards standalone${N}${C}            ║${N}"
  echo -e "${C}╚══════════════════════════════════════════════════════════════╝${N}"
  echo
}

step() { echo -e "${Y}▸${N} $1"; }
ok()   { echo -e "  ${G}✓${N} $1"; }
warn() { echo -e "  ${Y}!${N} $1"; }
err()  { echo -e "  ${R}✗${N} $1"; }

banner

# ── 1. pré-requisitos ──
step "Checando pré-requisitos..."
if ! command -v claude >/dev/null 2>&1; then
  warn "Claude Code não encontrado no PATH."
  warn "Instale em https://claude.com/code antes de continuar."
  warn "O instalador segue copiando os arquivos — quando você instalar o Claude, eles já estarão prontos."
else
  ok "Claude Code instalado"
fi

# ── 2. criar diretórios ──
step "Preparando diretórios..."
mkdir -p "$SKILLS_DST"
mkdir -p "$TOOLKIT_DIR/diagnosticos"
mkdir -p "$TOOLKIT_DIR/orcamentos"
mkdir -p "$TOOLKIT_DIR/conteudo"
mkdir -p "$TOOLKIT_DIR/analises"
ok "Diretórios prontos em ~/.claude/skills/ e ~/meu-toolkit/"

# ── 3. copiar skills ──
step "Copiando as 12 skills..."
SKILLS=(
  diagnostico-cliente
  prototipar-sistema
  criar-orcamento
  gerar-copy-post
  gerar-carrossel
  gerar-imagem
  meta-creative-brief
  demo-qualificacao-bant
  demo-configuracao-5-minutos
  simulador-vendas
  analise-call
  criar-thumbnail
)

INSTALLED=0
SKIPPED=0
for skill in "${SKILLS[@]}"; do
  if [ ! -d "$SKILLS_SRC/$skill" ]; then
    err "$skill — não encontrada em $SKILLS_SRC"
    continue
  fi

  if [ -d "$SKILLS_DST/$skill" ]; then
    # backup antes de sobrescrever
    BACKUP_DIR="$SKILLS_DST/.toolkit-backup-$(date +%s)"
    mkdir -p "$BACKUP_DIR"
    mv "$SKILLS_DST/$skill" "$BACKUP_DIR/$skill"
    warn "$skill já existia — backup em $(basename $BACKUP_DIR)"
  fi

  cp -R "$SKILLS_SRC/$skill" "$SKILLS_DST/$skill"
  ok "$skill"
  INSTALLED=$((INSTALLED + 1))
done

echo
ok "$INSTALLED de ${#SKILLS[@]} skills instaladas"

# ── 4. abrir dashboards ──
step "Abrindo os 2 dashboards no navegador..."

open_url() {
  if [[ "$OSTYPE" == "darwin"* ]]; then
    open "$1" 2>/dev/null || true
  elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    xdg-open "$1" 2>/dev/null || true
  else
    warn "Sistema operacional não suportado pra abrir browser automático."
    warn "Abra manualmente: $1"
  fi
}

if [ -f "$DASHBOARDS_DIR/vitrine-proposta.html" ]; then
  open_url "file://$DASHBOARDS_DIR/vitrine-proposta.html"
  ok "Vitrine de Proposta"
fi

if [ -f "$DASHBOARDS_DIR/mini-pipeline.html" ]; then
  open_url "file://$DASHBOARDS_DIR/mini-pipeline.html"
  ok "Mini-Pipeline"
fi

# ── 5. próximos passos ──
echo
echo -e "${G}╔══════════════════════════════════════════════════════════════╗${N}"
echo -e "${G}║                  ✅ Instalação concluída!                    ║${N}"
echo -e "${G}╚══════════════════════════════════════════════════════════════╝${N}"
echo
echo -e "${B}Próximos passos:${N}"
echo
echo -e "  ${C}1.${N} Abra o Claude Code em qualquer pasta"
echo -e "     ${D}$ claude${N}"
echo
echo -e "  ${C}2.${N} Comece pelo diagnóstico do seu próximo cliente"
echo -e "     ${D}/diagnostico-cliente${N}"
echo
echo -e "  ${C}3.${N} Depois rode na sequência:"
echo -e "     ${D}/prototipar-sistema → /criar-orcamento → vitrine-proposta.html${N}"
echo
echo -e "${B}Diretórios criados:${N}"
echo -e "  ${D}~/.claude/skills/${N}        — onde Claude carrega as skills"
echo -e "  ${D}~/meu-toolkit/${N}            — onde a skill salva diagnósticos, orçamentos etc"
echo -e "  ${D}$DASHBOARDS_DIR${N}"
echo
echo -e "${B}Suporte:${N} https://chat.whatsapp.com/PLACEHOLDER  ${D}(link do grupo no rodapé da área de membros)${N}"
echo
