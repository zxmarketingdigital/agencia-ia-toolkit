# Toolkit Agência IA

> 12 ferramentas + 2 dashboards prontos pra você entregar Agência IA aos seus 3 primeiros clientes.

Produto de entrada da **ZX LAB**. Esse repositório contém todas as skills do Claude Code + os dashboards HTML que vêm com o Toolkit.

---

## Instalar em 15 minutos

```bash
git clone https://github.com/zxmarketingdigital/agencia-ia-toolkit
cd agencia-ia-toolkit
./install.sh
```

O instalador:
- Copia as 12 skills para `~/.claude/skills/` (com backup automático se já existir)
- Cria os diretórios de trabalho em `~/meu-toolkit/`
- Abre os 2 dashboards no seu navegador

Pré-requisito: [Claude Code](https://claude.com/code) instalado.

---

## As 12 skills

### 🔍 Diagnóstico do Cliente (3 skills)
| Comando | O que faz |
|---|---|
| `/diagnostico-cliente` | Faz 8 perguntas sobre o cliente → diagnóstico + 3 oportunidades IA priorizadas + plano 30d |
| `/prototipar-sistema` | Brief técnico + HTML hi-fi do sistema que você vai entregar |
| `/criar-orcamento` | Proposta comercial estruturada em Markdown + PDF |

### 📱 Conteúdo pro Cliente (4 skills)
| Comando | O que faz |
|---|---|
| `/gerar-copy-post` | Copy de post Instagram/LinkedIn (3 variantes com hook + CTA) |
| `/gerar-carrossel` | Carrossel 10 slides com bullets e CTA |
| `/gerar-imagem` | Prompt otimizado pra Midjourney/DALL-E/Leonardo |
| `/meta-creative-brief` | Briefing Meta Ads completo (3 hooks copy + 3 visuais + specs) |

### 🎬 Demos pra Vender (3 skills)
| Comando | O que faz |
|---|---|
| `/demo-qualificacao-bant` | Animação terminal cinematográfica de agente qualificando lead |
| `/demo-configuracao-5-minutos` | Demo "instalei agente WhatsApp em 5min" pra apresentação |
| `/simulador-vendas` | Você treina abordagem e fechamento; Claude simula o cliente |

### 📊 Análise + Arte (2 skills)
| Comando | O que faz |
|---|---|
| `/analise-call` | Cola transcrição da call → análise de objeções + script de follow-up |
| `/criar-thumbnail` | Prompt e direcionamento visual pra thumb de alto CTR |

---

## Os 2 dashboards

### 🎨 [Vitrine de Proposta](dashboards/vitrine-proposta.html)
Cola o output de `/criar-orcamento` e renderiza uma proposta comercial hi-fi pro cliente. Paleta personalizável, exporta PDF (window.print), gera link compartilhável (URL hash).

### 🗂️ [Mini-Pipeline](dashboards/mini-pipeline.html)
Kanban de 5 colunas dos seus clientes: Lead → Diagnóstico → Proposta → Execução → Entregue. Drag-and-drop, valores, próximas ações. Tudo em localStorage, exporta JSON.

Ambos rodam standalone (`file://` ou GitHub Pages do seu domínio).

---

## Fluxo recomendado pra fechar seu próximo cliente

```
1. /diagnostico-cliente            → entende o cliente
2. /prototipar-sistema             → desenha visualmente o que vai entregar
3. /criar-orcamento                → gera proposta comercial
4. dashboards/vitrine-proposta.html → apresenta hi-fi pro cliente
5. Mini-Pipeline                   → acompanha o pipeline
6. /analise-call                   → revisa cada call de vendas
7. /simulador-vendas               → treina pra próxima call
```

---

## Estrutura do repositório

```
agencia-ia-toolkit/
├── install.sh                    # bootstrap
├── README.md
├── area-membros/
│   └── index.html                # área de membros (toolkit.zxlab.com.br)
├── dashboards/
│   ├── vitrine-proposta.html
│   └── mini-pipeline.html
├── skills/                       # 12 skills Claude Code
│   ├── diagnostico-cliente/
│   ├── prototipar-sistema/
│   ├── criar-orcamento/
│   ├── gerar-copy-post/
│   ├── gerar-carrossel/
│   ├── gerar-imagem/
│   ├── meta-creative-brief/
│   ├── demo-qualificacao-bant/
│   ├── demo-configuracao-5-minutos/
│   ├── simulador-vendas/
│   ├── analise-call/
│   └── criar-thumbnail/
└── docs/                         # quickstart, troubleshoot
```

Cada skill é uma pasta com `SKILL.md` (frontmatter + workflow) e arquivos auxiliares.

---

## Onde a skill salva os arquivos

```
~/meu-toolkit/
├── diagnosticos/      → /diagnostico-cliente
├── orcamentos/        → /criar-orcamento
├── conteudo/          → /gerar-copy-post, /gerar-carrossel, etc
└── analises/          → /analise-call
```

---

## Já entregou 3 clientes?

Hora de escalar. **[ZX Control](https://zxlab.com.br/mission-control)** é o sistema completo de operação da ZX LAB — captação automática (WhatsApp + email + LinkedIn), agente BANT, mini-CRM próprio, Guardian Heartbeat 24/7. Quando você sentir a dor de gerenciar 5+ contratos, é o próximo passo natural.

---

## Suporte

- **Grupo WhatsApp:** entra pelo link no rodapé da [área de membros](https://toolkit.zxlab.com.br)
- **Email:** contato@zxlab.com.br
- **Issues técnicas neste repo:** abre uma [issue no GitHub](https://github.com/zxmarketingdigital/agencia-ia-toolkit/issues)

---

## Licença

Uso individual permitido para alunos do Toolkit Agência IA. Não redistribuir o conteúdo (skills + dashboards) como produto próprio. Você pode usar 100% com seus clientes pagantes.

---

**Toolkit Agência IA** · feito com ❤️ + [Claude Code](https://claude.com/code) pela [ZX LAB](https://zxlab.com.br)
