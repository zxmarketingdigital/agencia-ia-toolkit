---
name: diagnostico-cliente
description: "Diagnóstico do CLIENTE do aluno (não do aluno). Aluno responde 8 perguntas sobre o negócio do cliente — segmento, dor principal, processos atuais, recursos, urgência, decisor, orçamento, timing. Skill classifica grau de prontidão IA, sugere 3 oportunidades IA priorizadas (impacto×esforço), gera plano de entrega 30d e estimativa de impacto pra colar na proposta. Output em markdown salvo em ~/meu-toolkit/diagnosticos/. Use SEMPRE que o aluno disser: diagnóstico cliente, diagnosticar cliente, oportunidades IA cliente, levantar dor cliente, perfil do cliente, analisar negócio cliente, /diagnostico-cliente."
model: sonnet
effort: medium
---

# Diagnóstico do Cliente (Toolkit Agência IA)

## Resumo

Skill do **Toolkit Agência IA** (R$ 37). Aluno responde 8 perguntas sobre o negócio do cliente que ele tá prospectando ou já fechou. Output: relatório markdown com perfil do cliente + 3 oportunidades IA priorizadas + plano de entrega 30 dias + estimativa de impacto. Insumo direto pra `/prototipar-sistema` e `/criar-orcamento`.

**NÃO confundir com `/diagnostico-empreendedor` do ZX Growth** — aquele diagnostica o aluno como empreendedor. Esta skill diagnostica o **cliente do aluno**.

## Workflow

### 1. Preparação
- Criar diretório: `mkdir -p ~/meu-toolkit/diagnosticos`
- Apresentar contexto em 1 parágrafo:
  > "Vou te fazer 8 perguntas rápidas sobre o negócio do cliente que você tá prospectando. Com isso, eu monto um diagnóstico claro: perfil do cliente + 3 oportunidades IA priorizadas + plano de entrega 30 dias. Você cola isso na proposta. Pronto?"

### 2. Coletar nome do cliente
Perguntar primeiro:
- "Como se chama o cliente (pessoa ou empresa)?"

Salvar em `nome_cliente`. Vai pro nome do arquivo final (slug).

### 3. Chat de 8 perguntas (uma por vez, esperar resposta)

**Q1 — Segmento e tamanho**
"Em uma frase: qual o segmento do cliente e o porte dele? (ex: padaria de bairro 2 funcionários · clínica odontológica 8 dentistas · agência marketing 15 pessoas)"

**Q2 — Dor principal**
"Qual a maior DOR operacional dele hoje? Não o que ele quer, mas o que tá doendo no dia-a-dia. (ex: atendimento perde pedido no WhatsApp · agenda da clínica vive desorganizada · funcionária gasta 3h/dia respondendo as mesmas dúvidas)"

**Q3 — Processo atual**
"Como ele resolve essa dor HOJE? (manual? planilha? sistema legado? não resolve?)"

**Q4 — Recursos disponíveis**
"O que ele já tem que pode ser aproveitado? (WhatsApp Business? site existente? CRM? equipe de TI?)"

**Q5 — Urgência**
"Por que ele tá querendo resolver isso AGORA? Tem algum gatilho? (cresceu rápido · perdeu cliente · concorrente automatizou · multa · pressão interna)"

**Q6 — Decisor e processo de compra**
"Quem decide a contratação? (o próprio dono? gerente? comitê? esposa/sócio?) Já houve compras anteriores nesse perfil?"

**Q7 — Orçamento e expectativa de preço**
"Que faixa de investimento ele já mencionou ou que faz sentido pro porte dele? (sem ideia · até R$1k · R$1-5k · R$5-15k · acima)"

**Q8 — Timing**
"Quando ele quer ver resultado? (essa semana · 30d · 90d · sem urgência)"

### 4. Gerar diagnóstico

Aplicar o framework abaixo. Output em markdown estruturado.

**Critérios de classificação (calculados pela skill, não perguntados):**

#### Grau de Prontidão IA (1 das 4)
- **🟢 Pronto pra IA agora** — tem dor clara + processo manual + recursos disponíveis + urgência alta + decisor claro
- **🟡 Quase pronto** — falta 1-2 dos critérios acima (geralmente urgência ou orçamento)
- **🟠 Precisa de educação** — não vê o problema como problema, OU acha que IA é caro/futuro
- **🔴 Não vale o esforço agora** — sem dor real, sem decisor claro, sem orçamento

#### 3 Oportunidades IA priorizadas (matriz impacto × esforço)
Pra cada oportunidade:
- **Nome** — frase curta (ex: "Agente WhatsApp de pedidos")
- **Impacto esperado** — alto/médio/baixo + métrica concreta ("reduz 70% do tempo de atendimento manual")
- **Esforço de implementação** — baixo/médio/alto + tempo estimado ("3 dias úteis")
- **Stack sugerido** — ferramentas concretas ("Evolution API + Gemini + Google Sheets")
- **Risco** — o que pode dar errado ("se WhatsApp do cliente for pessoal, não funciona — precisa criar Business")

Ordenar por impacto/esforço (Pareto: alto impacto + baixo esforço primeiro).

#### Plano de entrega 30 dias
4 fases (1 semana cada):
- **Semana 1** — descoberta e setup (entrevistas com equipe, captura de dados reais, ambiente)
- **Semana 2** — MVP da oportunidade #1 (a de maior Pareto)
- **Semana 3** — refino + testes em produção controlada
- **Semana 4** — handoff + treinamento da equipe + métricas de baseline

#### Estimativa de impacto financeiro
Tentar quantificar em R$ ou em horas economizadas/semana, baseado na dor relatada. Ser conservador. Mostrar fórmula simples ("3h/dia × 22 dias × R$ 30/h = R$ 1.980/mês economizados").

### 5. Salvar diagnóstico
Arquivo: `~/meu-toolkit/diagnosticos/{slug-cliente}-{YYYY-MM-DD}.md`

Estrutura:
```markdown
# Diagnóstico — {nome_cliente}
*Gerado em {data} · Toolkit Agência IA*

## Perfil
- **Segmento:** ...
- **Porte:** ...
- **Dor principal:** ...
- **Processo atual:** ...
- **Recursos disponíveis:** ...
- **Decisor:** ...
- **Orçamento estimado:** ...
- **Timing:** ...

## Grau de Prontidão IA
**{🟢/🟡/🟠/🔴} {Classificação}** — {justificativa em 1 parágrafo}

## 3 Oportunidades IA priorizadas

### 1. {Nome da oportunidade}
- **Impacto:** ...
- **Esforço:** ...
- **Stack:** ...
- **Risco:** ...

### 2. {...}

### 3. {...}

## Plano de entrega 30 dias

### Semana 1 — Descoberta e setup
- ...

### Semana 2 — MVP {oportunidade #1}
- ...

### Semana 3 — Refino e testes
- ...

### Semana 4 — Handoff
- ...

## Estimativa de impacto
{Fórmula em 1 parágrafo}

**Resultado:** {R$ economizados/mês OU horas/semana liberadas OU % de melhoria}

## Próximos passos
1. Confirmar dor com 2 funcionários do cliente (5min cada)
2. Rodar `/prototipar-sistema` pra desenhar a oportunidade #1
3. Rodar `/criar-orcamento` pra montar a proposta comercial
4. Apresentar via Vitrine de Proposta (dashboard do toolkit)
```

### 6. Confirmação final
Avisar o aluno onde o arquivo foi salvo e sugerir o próximo passo:
> "Diagnóstico salvo em `~/meu-toolkit/diagnosticos/{slug}-{data}.md`. Próximo passo natural: rodar `/prototipar-sistema` pra desenhar a Oportunidade 1 visualmente, depois `/criar-orcamento` pra fechar a proposta."

## Regras

- **8 perguntas, nem mais nem menos.** Não improvise perguntas extras.
- **Não pular perguntas** mesmo se aluno já respondeu indiretamente. Confirmar.
- **Linguagem direta, sem academiquês.** O aluno tá ocupado.
- **Conservador na estimativa de impacto.** Melhor prometer 10h/semana e entregar 15 do que o contrário.
- **Riscos sempre presentes.** Cada oportunidade tem risco — se você não enxerga, pergunta de novo.
- **Slug do nome do cliente:** lowercase, hifenizado, sem acentos. "Padaria do João" → `padaria-do-joao`.

## Exemplos de output condensado

### Cliente Pronto pra IA (🟢)
> Padaria do João · 2 funcionários · perde 8-10 pedidos/dia no WhatsApp por demora · usa só WhatsApp pessoal · dono decide · orçamento R$ 2-4k · urgência alta (cresceu 40% em 3 meses).
> **Oportunidade #1:** Agente WhatsApp de pedidos · alto impacto (8h/dia economizadas) · 3 dias úteis · Evolution+Gemini · risco: usar WhatsApp Business.

### Cliente Precisa Educar (🟠)
> Advogado autônomo · 1 pessoa · "perde tempo respondendo cliente" mas não quantifica · usa email · decisor único · sem orçamento mencionado · timing "quando der".
> Recomendação: agendar reunião de 30min pra mostrar caso real (use `/demo-qualificacao-bant` antes de fechar). Não fazer proposta agora.

## Próximas skills no fluxo
- `/prototipar-sistema` — desenha visualmente a Oportunidade 1
- `/criar-orcamento` — proposta comercial
- Dashboard `vitrine-proposta.html` — apresentação hi-fi pro cliente
