# ACERVO 30 DIAS — pool pra curadoria do Rafael

**Sobre-produzido de propósito: você escolhe o que entra.** Nada aqui foi publicado nem agendado.
Naming `acv-NN-slug` — o slug vira `utm_content` se a peça for pro pago.
Uso: `organico` (feed BR, só PT) · `paid-br` (PT) · `paid-intl` (EN). ⚠️ EN não vai pro feed orgânico.
Peças "conceito" têm copy pronta; render final sob demanda das selecionadas (mais barato que renderizar tudo).

## Cards de screenshot real (renderizados · arte EN, copy PT+EN)

| id | ângulo | uso | números | status |
|---|---|---|---|---|
| acv-01-preflop-total-grid | 1, 5 | org+pbr+pintl | REAL (1.png) | ✅ arte + copy |
| acv-02-postflop-total | 2 | org+pbr+pintl | REAL (aura-total2) | ✅ arte + copy |
| acv-03-filtros-stack | 6 | org+pbr+pintl | REAL (filtros1) | ✅ arte + copy |
| acv-04-postflop-sizings | 2 | org+pbr+pintl | REAL (postflop1, 3.2M) | ✅ arte + copy (descritivo §10) |
| acv-05-cbet-reaction | 2 | org+pbr+pintl | REAL (postflop2, 3.2M) | ✅ arte + copy |
| acv-06-villain-split | 1 | org+pbr+pintl | REAL (preflop_disag) | ✅ arte + copy |
| acv-07-busca-spots | 6 | org+pbr+pintl | REAL (busca) | ✅ arte + copy |

## Cards de posicionamento/conceito

| id | ângulo | uso | números | status |
|---|---|---|---|---|
| acv-08-solver-vs-field | 3 | org+pbr+pintl | ILUSTRATIVO (marcado na arte) | ✅ arte + copy |
| acv-09-range-grid | 1, 3 | org+pbr | ILUSTRATIVO | ✅ arte + copy |
| acv-10-mito-mdf | 8 | org+pbr+pintl | REAL (aura-total2) | 🟡 conceito+copy · render sob demanda |
| acv-11-escala-500m | 5 | org+pbr+pintl | REAL (claims §9) | ✅ arte + copy |

## Reels (formato de maior valor)

| id | ângulo | uso | números | status |
|---|---|---|---|---|
| acv-12-reel-launch | 5, 6 | org+pbr / pintl | REAL | ✅ PRONTOS: PT `lote-final/reels/reel-lancamento-aura-2.0.mp4` · EN `lote-final/reels/en/reel-launch-aura-2.0.mp4` |
| acv-13-reel-tour | 6 | org+pbr+pintl | REAL | 🟡 roteiros PT (`lote-final/reels/04-…`) + EN (`reels/en/04-…`) |
| acv-14-reel-exploit-card | 2, 7 | org+pbr+pintl | REAL | 🟡 roteiros PT (`…/08-…`) + EN (`reels/en/08-…`) |
| acv-15-reel-bubble | 4, 8 | org+pbr+pintl | REAL | 🟡 roteiros PT (`…/11-…`) + EN (`reels/en/11-…`) |
| acv-16-reel-caso-uso | 7 | org+pbr+pintl | REAL (aura-total2) | 🟡 roteiro novo PT+EN nesta pasta |
| acv-17-reel-mito-mdf | 8 | org+pbr+pintl | REAL (aura-total2) | 🟡 roteiro novo PT+EN nesta pasta |

## Carrosséis

| id | ângulo | uso | números | status |
|---|---|---|---|---|
| acv-18-carrossel-tour-modulos | 6 | organico | REAL | 🟡 slides+copy · render sob demanda |
| acv-19-carrossel-ler-exploit-card | 2, 7 | organico | REAL (descritivo §10) | 🟡 slides+copy · render sob demanda |

## CTA / oferta

| id | uso | status |
|---|---|---|
| acv-20-cta-conta-gratis | org+pbr+pintl | 🟡 conceito+copy |
| acv-21-cta-preview-board | org + retargeting | 🟡 conceito+copy (gating correto: grátis = preview) |

## Batch pago (pedido junto) — ✅ JÁ ENTREGUE
`paid01-v1/v2/v3` EN renderizados em `content/paid/AURA-PAID01/en/` (commit a09ed13). PT na pasta-mãe.

## Correções de verdade feitas durante a produção (gabarito venceu de novo)
1. `stat-card` default era da era v1: **68% inventado + "GTO folds far less" + "prints"** (promessa de lucro) + "12.4M mãos" fabricado → substituído pelo card de escala (claims aprovados).
2. `solver-vs-field` afirmava **"Measured across 480k real hands — audited"** com números ilustrativos → agora a própria arte diz "Illustrative numbers…"; gapNote reescrito descritivo.
3. `shot-postflop-sizings` dizia "every red bar is an overfold to attack" → descritivo (§10).

## Regras aplicadas a tudo
Jargão em EN nas duas línguas (RFI, 3bet, ICM, field, MDF) · decimais PT vírgula / EN ponto ·
EN adaptado, não tradução literal · grátis = preview · zero promessa de lucro/EV · 18+ na arte ·
sem concorrente nominal · MDF sempre descritivo (nunca "abaixo do MDF = leak") — `pesquisa-mdf-limites.md` §10.
