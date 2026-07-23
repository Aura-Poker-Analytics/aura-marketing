# Análise do orgânico (Insights export) + plano 30 dias revisado

**Autor:** thread Mídia Paga · **Data:** 2026-07-23 · **Fonte:** export CSV do Meta Business Suite (posts + stories, 25/06–22/07), cruzado com o acervo e a curadoria do Rafael (Posted/Alterar).

## 1. Ranking de performance (feed, por alcance)
Hotspot leaks (11/07) **440** · Reel launch (18/07) **366** · Carrossel rebuild (08/07) 253 · Filtros/acv-03 64 · Preflop/acv-01 58 · Tracker-solver 55 · Estude-free 31 · Postflop/acv-02 29 (postado 22/07).

**Flags universais:** `saves=0` em todos os 8 posts; `follows≈0` (só Hotspot: 1). Orgânico não gera bookmark nem cresce base.

**Confound:** posts do launch (08–11/07) pegaram mais alcance por push de novidade — não atribuir 100% ao conteúdo. Amostra pequena (8 posts, conta ~1k) → direcional, não conclusivo.

## 2. Os 2 achados que mudam o plano
1. **Vídeo >> estático.** O reel de launch (366) superou todo card estático fora do dia-do-launch. → plano deve ser **reel-first**, não card-first.
2. **Story-com-link é o motor de clique.** Story do launch (08/07): alcance 923, **11 cliques no link**, 8 visitas ao perfil — mais tráfego que o feed inteiro do mês. Stories seguintes (sem sticker de link): 0 cliques. → **feed = alcance/prova; Story com sticker de link = clique.** O plano anterior era 100% feed — este é o gap.

## 3. Curadoria do Rafael (validada pelos dados)
- **Posted:** acv-01/02/03 (cards de tela real) — alcance modesto (29–64), mas é timing/formato pós-launch, não conteúdo ruim.
- **Alterar:** acv-08/09/10 (ilustrativos + mito) — bom instinto: número ilustrativo vale menos e a Meta implica mais.

## 4. Plano 30 dias — REVISADO
Princípios derivados dos dados:

**a. Reel-first — MAS gargalo de produção (atualizado 23/07, arquitetura nova).** Após a fábrica reorganizar (`content/reels/`, `content/posts/`, triagem `Posted/Alterar/raiz`), o estado real é: **só `reel-01-launch` está renderizado**; `reel-02-tour`, `reel-03-exploit-card`, `reel-04-bubble`, `reel-05-caso-uso` são **só roteiro** e alguns exigem **gravação de tela do app** (não só `build`). `acv-17-mito-mdf` foi deletado (redundante c/ card). → Reel-first depende de produção; **priorizar renderizar `reel-04-bubble`** (ângulo leak, o de maior alcance histórico) como próximo. Enquanto isso, feed = cards da fila.

**b. Story com sticker de link 2–3×/semana.** É o único motor de clique orgânico comprovado. Todo reel/card de feed acompanhado de um Story empurrando + **sticker de link pro `www.aurapoker.com/?utm_source=instagram&utm_medium=bio&utm_campaign=organico`** (UTM pra medir no `tbl_user`). Isso estava faltando.

**c. Liderar com o ângulo que viajou:** leak/Hotspot (440 de alcance, o topo). acv-15-bubble e acv-05-cbet-reaction são dessa veia. Segundo: field-data (acv-04/acv-11).

**d. Corrigir o zero-saves:** dar a alguns cards enquadramento de **referência salvável** ("salva esse range grid") com CTA de save explícito. Não over-indexar (amostra pequena), mas testar.

**e. Cadência sugerida (~15 slots em 30d) — naming novo (`content/reels/` e `content/posts/`):**
| Semana | Reel (⚠️ renderizar antes) | Card filler (fila `posts/`) | Story-link |
|---|---|---|---|
| 1 | **reel-04-bubble** (leak) | cbet-reaction | 2× |
| 2 | reel-03-exploit-card | reg-vs-fish | 2× |
| 3 | reel-05-caso-uso | carrossel-tour-modulos | 3× |
| 4 | reel-02-tour | busca-spots + cta-conta-gratis | 2× |

Ponte imediata (23/07, enquanto reels não renderizam): fixar `hook-two-devices` no perfil; postar `cbet-reaction` → `escala-500m`/`reg-vs-fish`, cada um com Story+link. `reel-01-launch` (único pronto) pode reentrar/impulsionar. Benchados em `Alterar/`: mito-mdf, range-grid, solver-vs-field (ilustrativos).

## 5. O loop que conecta orgânico ↔ pago
**O feed orgânico é também audição de criativo pago.** Reel que performar no orgânico (alcance/engajamento) vira anúncio via "usar publicação existente" **herdando a prova social** — exatamente o que faltava (os cards estáticos têm likes de menos pra herdar; o reel de launch com 2 shares/366 alcance é o melhor candidato hoje). Logo: postar reel no orgânico → o vencedor gradua pro pago.

## 6. Implicação estratégica honesta
Orgânico a ~0,5 cadastro/dia + saves/follows ~0 = **maintenance, não growth engine.** Não construirá a semente de lookalike em tempo hábil. Reforça: **pago é o motor de crescimento; orgânico mantém a conta crível e audita criativo.** Nada aqui muda o gate do pago (só decisão de orçamento do Rafael).
