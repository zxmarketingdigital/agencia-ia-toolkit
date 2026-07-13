# Graph Report - .  (2026-05-22)

## Corpus Check
- 4 files · ~18,268 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 27 nodes · 52 edges · 7 communities detected
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]

## God Nodes (most connected - your core abstractions)
1. `main()` - 12 edges
2. `w()` - 7 edges
3. `gen_image2()` - 6 edges
4. `gen_gemini()` - 6 edges
5. `log()` - 4 edges
6. `main()` - 4 edges
7. `digitando()` - 4 edges
8. `msg_agente()` - 4 edges
9. `codex_lock()` - 3 edges
10. `resize_png()` - 3 edges

## Surprising Connections (you probably didn't know these)
- `msg_agente()` --calls--> `w()`  [EXTRACTED]
  skills/demo-qualificacao-bant/run.py → skills/demo-configuracao-5-minutos/run.py
- `main()` --calls--> `digitando()`  [EXTRACTED]
  skills/demo-configuracao-5-minutos/run.py → skills/demo-qualificacao-bant/run.py
- `main()` --calls--> `msg_lead()`  [EXTRACTED]
  skills/demo-configuracao-5-minutos/run.py → skills/demo-qualificacao-bant/run.py
- `main()` --calls--> `msg_agente()`  [EXTRACTED]
  skills/demo-configuracao-5-minutos/run.py → skills/demo-qualificacao-bant/run.py
- `main()` --calls--> `tag_bant()`  [EXTRACTED]
  skills/demo-configuracao-5-minutos/run.py → skills/demo-qualificacao-bant/run.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.52
Nodes (6): clr(), main(), prog(), qr_ascii(), spinner(), tw()

### Community 1 - "Community 1"
Cohesion: 0.6
Nodes (5): gen_gemini(), load_env_key(), log(), main(), Generate via Google GenAI — gemini-* usa :generateContent, imagen-* usa :predict

### Community 2 - "Community 2"
Cohesion: 0.83
Nodes (3): msg_lead(), tag_bant(), w()

### Community 3 - "Community 3"
Cohesion: 0.67
Nodes (3): gen_image2(), Generate via Codex CLI built-in image_gen tool (gpt-image-2)., resize_png()

### Community 4 - "Community 4"
Cohesion: 0.67
Nodes (3): digitando(), msg_agente(), Simula agente digitando.

### Community 5 - "Community 5"
Cohesion: 1.0
Nodes (0): 

### Community 6 - "Community 6"
Cohesion: 1.0
Nodes (2): codex_lock(), Lock exclusivo entre processos pro trecho critico do gen_image2.

## Knowledge Gaps
- **4 isolated node(s):** `Lock exclusivo entre processos pro trecho critico do gen_image2.`, `Generate via Codex CLI built-in image_gen tool (gpt-image-2).`, `Generate via Google GenAI — gemini-* usa :generateContent, imagen-* usa :predict`, `Simula agente digitando.`
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 5`** (2 nodes): `fetch()`, `worker.js`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 6`** (2 nodes): `codex_lock()`, `Lock exclusivo entre processos pro trecho critico do gen_image2.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `main()` connect `Community 0` to `Community 2`, `Community 4`?**
  _High betweenness centrality (0.095) - this node is a cross-community bridge._
- **Why does `gen_image2()` connect `Community 3` to `Community 1`, `Community 6`?**
  _High betweenness centrality (0.039) - this node is a cross-community bridge._
- **Why does `digitando()` connect `Community 4` to `Community 0`, `Community 2`?**
  _High betweenness centrality (0.037) - this node is a cross-community bridge._
- **What connects `Lock exclusivo entre processos pro trecho critico do gen_image2.`, `Generate via Codex CLI built-in image_gen tool (gpt-image-2).`, `Generate via Google GenAI — gemini-* usa :generateContent, imagen-* usa :predict` to the rest of the system?**
  _4 weakly-connected nodes found - possible documentation gaps or missing edges._