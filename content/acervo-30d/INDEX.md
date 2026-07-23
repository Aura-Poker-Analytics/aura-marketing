# ACERVO 30 DIAS — pool pra curadoria do Rafael

**Sobre-produzido de propósito: você escolhe o que entra.** Nada aqui foi publicado nem agendado.
Naming `acv-NN-slug` — o slug vira `utm_content` se a peça for pro pago.
Uso: `organico` (feed BR, só PT) · `paid-br` (PT) · `paid-intl` (EN). ⚠️ EN não vai pro feed orgânico.
Peças "conceito" têm copy pronta; render final sob demanda das selecionadas.

**Triagem (pastas):** `Posted/` = já foi ao ar · `Alterar/` = você rejeitou, precisa mudar · raiz = fila.
**Reels saíram daqui** → agora todos em `content/reels/` (ver `reels/README.md`).

## ✅ Posted/ (já postados — não reagendar)
| id | ângulo | números |
|---|---|---|
| acv-01-preflop-total-grid | 1, 5 | REAL (1.png) |
| acv-02-postflop-total | 2 | REAL (aura-total2) |
| acv-03-filtros-stack | 6 | REAL (filtros1) |

## 🔧 Alterar/ (você rejeitou — precisa mudança antes de usar)
| id | ângulo | números | pendência |
|---|---|---|---|
| acv-08-solver-vs-field | 3 | ILUSTRATIVO | você avaliar o ajuste que fiz (arte já se declara ilustrativa) |
| acv-09-range-grid | 1, 3 | ILUSTRATIVO | idem |
| acv-10-mito-mdf | 8 | REAL (aura-total2) | conceito+copy, sem arte ainda |

## 🟩 Fila — cards de screenshot real (renderizados · copy PT+EN)
| id | ângulo | uso | números |
|---|---|---|---|
| acv-04-postflop-sizings | 2 | org+pbr+pintl | REAL (postflop1, 3.2M) · descritivo §10 |
| acv-05-cbet-reaction | 2 | org+pbr+pintl | REAL (postflop2, 3.2M) |
| acv-06-villain-split | 1 | org+pbr+pintl | REAL (preflop_disag) |
| acv-07-busca-spots | 6 | org+pbr+pintl | REAL (busca) |

## 🟩 Fila — posicionamento/escala
| id | ângulo | uso | números |
|---|---|---|---|
| acv-11-escala-500m | 5 | org+pbr+pintl | REAL (claims §9) · renderizado |

## 🟩 Fila — carrosséis (conceito+copy · render sob demanda)
| id | ângulo | uso | números |
|---|---|---|---|
| acv-18-carrossel-tour-modulos | 6 | organico | REAL |
| acv-19-carrossel-ler-exploit-card | 2, 7 | organico | REAL · descritivo §10 |

## 🟩 Fila — CTA/oferta (conceito+copy)
| id | uso | nota |
|---|---|---|
| acv-20-cta-conta-gratis | org+pbr+pintl | preview, não "completo grátis" |
| acv-21-cta-preview-board | org + retargeting | gating correto: grátis = preview |

## 🎬 Reels → moveram-se pra `content/reels/`
reel-01-launch (produzido PT+EN) · reel-02-tour · reel-03-exploit-card · reel-04-bubble ·
reel-05-caso-uso (era `acv-16`, corrigido: estudo em vez de real-time, spot coerente).
**Deletado:** `acv-17-reel-mito-mdf` (redundante com o card acv-10).

## 🌐 Batch pago EN — ✅ entregue
`paid01-v1/v2/v3` EN em `content/paid/AURA-PAID01/en/` (commit a09ed13). PT na pasta-mãe.

## Correções de verdade feitas na produção
1. `stat-card` default v1: 68% inventado + "GTO folds far less" + "prints" + "12.4M mãos" → card de escala com claims aprovados.
2. `solver-vs-field`: "Measured across 480k real hands" com números ilustrativos → arte agora se declara ilustrativa.
3. `shot-postflop-sizings`: "overfold to attack" → descritivo (§10).

## Regras aplicadas a tudo
Jargão em EN nas duas línguas (RFI, 3bet, ICM, field, MDF) · decimais PT vírgula / EN ponto ·
EN adaptado (não literal) · grátis = preview · zero promessa de lucro/EV · 18+ na arte ·
sem concorrente nominal · MDF sempre descritivo — `docs/00-strategy/pesquisa-mdf-limites.md` §10.
