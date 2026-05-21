# Toolkit Agência IA — contexto pro Claude Code

> Produto de entrada da ZX LAB (R$ 37). 12 skills + 2 dashboards pra aluno entregar Agência IA aos primeiros 3 clientes.

## Posicionamento (NÃO esquecer ao trabalhar nesse repo)

- **Toolkit = kit de ENTREGA** (artefato pro cliente final do aluno: diagnóstico, proposta, copy, criativo, demo)
- **ZX Control = kit de OPERAÇÃO** (motor de captação + disparo + monitoramento do aluno — fica em outro repo)

**Regra de ouro:** se uma skill automatiza a operação INTERNA do aluno (capta lead, dispara WhatsApp, monitora servidor) → NÃO entra aqui. Se produz ENTREGÁVEL pro cliente final → entra aqui.

## Arquitetura

```
toolkit-agencia-ia/
├── area-membros/index.html      # toolkit.zxlab.com.br (Cloudflare Workers Assets)
├── dashboards/
│   ├── vitrine-proposta.html    # standalone, paleta personalizável, exporta PDF
│   └── mini-pipeline.html       # standalone, kanban localStorage
├── skills/                      # 12 skills Claude Code (copiadas pra ~/.claude/skills/)
└── install.sh                   # bootstrap aluno
```

## Auth = aberta (decisão consciente)

`area-membros/index.html` aceita qualquer email + qualquer senha. Sem webhook, sem edge function, sem INSERT em `purchases`. Trade-off aceito por simplicidade do R$ 37.

## Onde a skill salva no Mac do aluno

`~/meu-toolkit/{diagnosticos,orcamentos,conteudo,analises}/` — criado pelo `install.sh`.

## Próximos passos prováveis (não bloqueiam)

1. Criar repo público `zxmarketingdigital/agencia-ia-toolkit`
2. Deploy `toolkit.zxlab.com.br` via Cloudflare Workers Assets (workaround do bug Pages 502)
3. Hotmart: criar produto R$ 37 + página de obrigado apontando pra `toolkit.zxlab.com.br`
4. Banner âmbar (square + rect) + GIF de demo pro README e pra área de membros
5. Vídeos curtos (3-5min) por skill — adiar até ter validação de venda

## Decisões em aberto (Rafael)

- Substitui Curso R$ 37 atual ou roda paralelo?
- Hospedagem dos dashboards do aluno: ensinamos `gh pages` ou bucket nosso?
- Nome final: "Toolkit Agência IA" / "ZX Delivery Kit" / outro?

Ver plano completo: `~/.claude/plans/como-podemos-transformar-algumas-deep-fern.md`
