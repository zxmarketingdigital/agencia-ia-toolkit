---
name: criar-thumbnail
description: "Gera 3 variantes de thumbnail YouTube (1280x720) via skill `gerar-imagem` (gpt-image-2 preferido, Gemini Nano Banana / Imagen 4 como fallback). Variantes: A (rosto+texto), B (conceitual), C (comparação/antes-depois). Lê DESIGN.md para manter identidade visual. Use SEMPRE que o aluno disser: criar thumbnail, gerar thumb, thumb yt, thumbnail youtube, capa do video, capa youtube, thumbnail, miniatura youtube."
model: sonnet
effort: low
---

# Criar Thumbnail YouTube

Gera 3 thumbnails YouTube (1280×720) em estilos diferentes pra o aluno escolher ou testar A/B. Usa `gerar-imagem` como gateway único (gpt-image-2 via Codex CLI / ChatGPT → Gemini Nano Banana → Imagen 4 como fallback).

## Carregamento de contexto

- `~/.operacao-ia/config/marca.json`
- `~/.operacao-ia/data/social-media/DESIGN.md`

## Inputs obrigatórios

1. **Título do vídeo** — ex: "Eu testei IA por 30 dias — esse foi o resultado"
2. **Tipo de vídeo** — `tutorial`, `vlog`, `analise`, `entrevista`, `comparacao`. Default: `tutorial`
3. **Texto curto pra thumb** — 3-5 palavras máximo (default: extrair do título). Ex: "30 DIAS DE IA"
4. **Output dir** — `~/.operacao-ia/data/social-media/output/thumbs/YYYY-MM-DD_<slug>/`

## Fluxo

### 1. Definir as 3 variantes

| Variante | Conceito | Prompt-base |
|---|---|---|
| A | Rosto expressivo + texto grande | "close-up portrait, surprised/intrigued expression, bold text overlay '<texto>'" |
| B | Conceitual/metáfora visual | "metaphorical visual representing '<tema>', no faces, strong visual hook" |
| C | Comparação/contraste | "split composition: before vs after / problem vs solution, visual contrast" |

Use a seção "Para geração de imagem" do DESIGN.md como base estética. Se DESIGN.md tem apenas seção "Para Higgsfield", reusar — o prompt é genérico o suficiente.

### 2. Geração via skill `gerar-imagem`

Para cada variante, chame o helper diretamente (ele escolhe automaticamente o melhor provider disponível):

```bash
python3 ~/.claude/skills/gerar-imagem/scripts/gerar.py \
  --prompt "<prompt completo da variante>" \
  --output "<output_dir>/thumb-<A|B|C>-<conceito>.png" \
  --size 1280x720 \
  --quality high \
  --json
```

Formato do prompt completo (substituir `<...>`):

```
{base_estetica_do_DESIGN.md}, YouTube thumbnail 1280x720,
{conceito_da_variante}, text "<texto>" rendered bold and readable,
high contrast, attention-grabbing, no embedded watermarks
```

O helper imprime JSON com `provider` usado e `elapsed_s`. Loguar isso pra o aluno saber qual provider entregou (gpt-image-2, gemini, imagen, ou higgsfield-fallback).

**Se gerar-imagem falhar em TODOS os providers** (sem Codex logado E sem GEMINI_API_KEY E sem Higgsfield), instrua o aluno:

1. Opção rápida — adicionar Gemini: criar conta grátis em https://aistudio.google.com/apikey, exportar `GEMINI_API_KEY=...` em `~/.operacao-ia/config/gemini.env`
2. Opção robusta — logar no Codex CLI: `codex login` (usa assinatura ChatGPT, sem custo extra)

### 3. Output

Salve:
```
output/thumbs/<YYYY-MM-DD>_<slug>/thumb-A-rosto.png
output/thumbs/<YYYY-MM-DD>_<slug>/thumb-B-conceitual.png
output/thumbs/<YYYY-MM-DD>_<slug>/thumb-C-comparacao.png
output/thumbs/<YYYY-MM-DD>_<slug>/README.txt   # explicação das 3 variantes + recomendação A/B teste + provider usado em cada
```

Se o PNG vier em outro tamanho que não 1280×720, faça resize com Pillow (script já trata, mas validar):

```python
from PIL import Image
img = Image.open('raw.png')
img.thumbnail((1280, 720), Image.LANCZOS)
canvas = Image.new('RGB', (1280, 720), (0, 0, 0))
x = (1280 - img.width) // 2
y = (720 - img.height) // 2
canvas.paste(img, (x, y))
canvas.save('thumb-A.png', 'PNG', optimize=True)
```

### 4. Atualizar galeria

Leia `~/.operacao-ia/data/social-media/gallery.json`, append em `data["items"]`, escreva de volta. Item:

```json
{ "type": "thumbnail", "title": "<título do vídeo>", "path": "output/thumbs/<dir>/", "providers": ["image2", "gemini"], "created_at": "<ISO>" }
```

### 5. Resumo

- Mostre os 3 paths + qual provider gerou cada uma
- Explique brevemente cada estilo
- Sugira: "Comece com a A (rosto). Se o CTR for <3% em 24h, troque pela B."
- Lembre: tamanho final deve ser ≤2MB pra subir no YouTube (se passar, comprimir com `pngquant` ou re-save Pillow com `optimize=True`)

## Não fazer

- Não chame Higgsfield diretamente — use sempre `gerar-imagem` (ele decide o melhor provider).
- Não use Puppeteer ou HTML pra compor — é geração nativa de imagem.
- Não gere thumbnail com rosto do criador real (deep-fake) sem permissão explícita dele.
- Não use textos longos na thumb (>5-6 palavras).
