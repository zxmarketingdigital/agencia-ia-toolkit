---
name: gerar-copy-post
description: "Gera legenda + hashtags + CTA pra um post de rede social. Adapta tom e formato por plataforma (Instagram, TikTok, YouTube, LinkedIn). Lê marca.json para manter voz consistente. Use SEMPRE que o aluno disser: copy reel, legenda ig, copy linkedin, descrição yt, copy post, gerar legenda, escrever legenda, copy instagram, copy tiktok, descricao youtube, legenda post, copy para post."
model: sonnet
effort: low
---

# Gerar Copy de Post

Escreve a copy completa (legenda + hashtags + CTA) pronta pra colar no app da plataforma.

## Carregamento de contexto

- `~/.operacao-ia/config/marca.json` — nome, persona, tom, público

## Inputs obrigatórios

1. **Plataforma** — `instagram`, `tiktok`, `youtube`, `linkedin`
2. **Tema/contexto** — sobre o que é o post, ou caminho de um arquivo (vídeo/imagem) que precisa de copy
3. **Tipo de post** (depende da plataforma):
   - Instagram: `reel`, `feed`, `carrossel`
   - TikTok: post (sempre vídeo)
   - YouTube: `descricao_longo`, `descricao_shorts`
   - LinkedIn: `texto_curto`, `carrossel`, `artigo`

## Regras por plataforma

### Instagram (Reel ou Feed)

- **Estrutura:** Hook (1ª linha = atenção) + Corpo (3-5 linhas curtas) + CTA + hashtags
- **Comprimento:** 150-300 caracteres no corpo (não muito)
- **Hashtags:** 8-12, mistura de nicho + amplas, ao final, separadas por espaço
- **Sem emojis em excesso** — máximo 3 por post
- **CTA:** "Salva pra usar depois e me segue pra mais", "Compartilha com quem precisa"

### TikTok

- **Estrutura:** Hook curtíssimo + Punchline + hashtags
- **Comprimento:** máximo 150 caracteres total (caption + hashtags)
- **Hashtags:** 4-6, focadas em trending + nicho
- **Tom:** mais informal que Instagram

### YouTube (Descrição)

- **Longo (8-15min):**
  - 1ª linha = hook que aparece no preview (155 chars)
  - Parágrafo de contexto (150-200 palavras)
  - Capítulos com timestamps (`00:00 Intro`, `02:15 Tópico 1`, etc.) — pedir ao aluno
  - Links: site, redes sociais (de `marca.handles`)
  - Hashtags: 3 ao final (#nicho1 #nicho2 #marca)

- **Shorts:**
  - 1 linha hook + 2-3 hashtags + CTA "Inscreve no canal"

### LinkedIn

- **Texto curto:** 800-1200 caracteres. Hook + framework/insight + CTA
- **Carrossel:** Hook + 2-3 linhas de contexto + "Carrossel abaixo ⬇️" + 3-5 hashtags B2B (ex: `#liderança #estratégia #b2b`)
- **Sem hashtags excessivas** (3-5 max no LinkedIn)
- **Tom:** profissional mas humano. Histórias pessoais funcionam melhor que listas.

## Fluxo

1. Pergunte os inputs em falta.
2. Se o aluno passou um arquivo (vídeo/imagem), confirme que conseguiu identificar o tema. Se for vídeo e quiser, peça permissão pra rodar transcrição rápida via Whisper local (mesma stack do `repurpose-conteudo`).
3. Escreva 2 variantes da copy — A (direta) e B (storytelling/contexto). Mostre ambas.
4. Pergunte: "Quer ajustar, escolher uma, ou gerar uma 3ª variante diferente?"
5. Após aprovação, salve no path do arquivo associado (se houver) com sufixo `.copy.txt`, ou em `~/.operacao-ia/data/social-media/output/copys/YYYY-MM-DD_<slug>.txt`.

## Output

Arquivo `.txt` contendo:

```
PLATAFORMA: {plataforma}
TIPO: {tipo}
TEMA: {tema}
CRIADO: {ISO timestamp}

--- COPY ---

{copy gerada}

--- HASHTAGS ---

{hashtags}
```

## Atualizar galeria (opcional)

Apenas se a copy NÃO está associada a um arquivo de mídia já registrado. Caso contrário, edite a entrada existente do mesmo dia adicionando campo `copy_path`.

Para nova entrada: leia `~/.operacao-ia/data/social-media/gallery.json`, append em `data["items"]`:
```json
{ "type": "copy", "title": "<tema>", "platform": "instagram", "path": "output/copys/...", "created_at": "<ISO>" }
```

## Não fazer

- Não use hashtags genéricas demais (`#love #life #photooftheday`) — diluem o alcance.
- Não copie copy de outros criadores — sempre original baseado em `marca.persona`.
- Não meta CTA agressivo "compra agora" sem contexto (isso é Setup 6 / tráfego pago, não orgânico).
