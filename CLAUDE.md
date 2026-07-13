# Toolkit Agência IA — contexto pro Claude Code

> Produto de entrada da ZX LAB (R$ 37). 12 skills + 2 dashboards pra aluno entregar Agência IA aos primeiros 3 clientes.

## Estado atual (22/Mai/2026) — PRONTO PARA LANÇAMENTO

- ✅ Repo público: `zxmarketingdigital/agencia-ia-toolkit`
- ✅ Deploy: `toolkit.zxlab.com.br` via Cloudflare Workers Assets
- ✅ 12 skills curadas em `skills/` (diagnostico-cliente reescrita para cliente do aluno)
- ✅ 2 dashboards standalone em `dashboards/` (vitrine-proposta.html + mini-pipeline.html)
- ✅ `install.sh` funcional (copia skills → `~/.claude/skills/`, cria `~/meu-toolkit/`)
- ✅ 2 vídeos Bunny Stream lib 629692 (tour embedded, apresentação embed code disponível)
- ✅ Rodapé e CTAs WhatsApp removidos da área de membros
- ✅ Card de instalação local dos dashboards com paths e link GitHub

## Próximo passo EXATO

1. **Hotmart** (manual, Rafael): criar produto "Toolkit Agência IA" R$37 → configurar página de obrigado → `toolkit.zxlab.com.br`
2. **Teste** (Andressa/Victor): `git clone https://github.com/zxmarketingdigital/agencia-ia-toolkit && ./install.sh` + testar 3 skills
3. **Soft launch**: mensagem no grupo Agência IA 50K com link de checkout

## Posicionamento (NÃO esquecer)

- **Toolkit = kit de ENTREGA** (artefato pro cliente final do aluno: diagnóstico, proposta, copy, criativo, demo)
- **ZX Control = kit de OPERAÇÃO** (motor de captação + disparo + monitoramento do aluno — fica em outro repo)

**Regra de ouro:** se uma skill automatiza operação INTERNA do aluno → NÃO entra. Se produz ENTREGÁVEL pro cliente final → entra.

## Arquitetura

```
toolkit-agencia-ia/
├── area-membros/index.html      # toolkit.zxlab.com.br (Workers Assets)
├── dashboards/
│   ├── vitrine-proposta.html    # standalone, paleta personalizável, exporta PDF, shareable link
│   └── mini-pipeline.html       # standalone, kanban 5 colunas, localStorage
├── skills/                      # 12 skills Claude Code
│   ├── diagnostico-cliente/     # reescrita: foca no cliente do aluno (não no aluno)
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
├── public/                      # assets servidos pelo Workers Assets
├── worker.js                    # Cloudflare Worker (ASSETS binding)
├── wrangler.toml                # `toolkit.zxlab.com.br`, custom_domain=true
└── install.sh                   # bootstrap aluno
```

## Auth = aberta (decisão consciente)

`area-membros/index.html` aceita qualquer email + qualquer senha. Email salvo em localStorage (lead-capture futuro). Sem webhook, sem edge function, sem INSERT em `purchases`. Trade-off aceito: fricção mínima R$37, valor só se materializa após install local.

## Vídeos Bunny Stream (lib 629692)

| Vídeo | GUID | Status | Embedded |
|-------|------|--------|----------|
| Tour do Kit (5min) | `c14736f6-df69-4e3a-8a6e-38fb359e0048` | ✅ 4/Finished | Sim (index.html) |
| Apresentação do Curso (4min) | `d8facba1-06cb-4513-9d5e-c3db6a695c9b` | ✅ 4/Finished | Não (embed code disponível) |

Embed template:
```html
<iframe src="https://iframe.mediadelivery.net/embed/629692/{GUID}"
  width="100%" style="aspect-ratio:16/9" frameborder="0"
  allow="autoplay; fullscreen" allowfullscreen></iframe>
```

## Deploy

```bash
cd ~/projetos/toolkit-agencia-ia
npx wrangler deploy   # deploy Workers Assets → toolkit.zxlab.com.br
```

Bug: `wrangler pages deploy` retorna 502 em arquivos >60B — usar `wrangler deploy` com `[assets]` no wrangler.toml.

## Decisões em aberto (Rafael)

- Substitui Curso R$ 37 atual ou roda paralelo?
- Hospedagem dos dashboards do aluno: ensinamos `gh pages` ou bucket nosso?
- Nome final: "Toolkit Agência IA" / "ZX Delivery Kit" / outro?

Ver plano completo: `~/.claude/plans/como-podemos-transformar-algumas-deep-fern.md`
