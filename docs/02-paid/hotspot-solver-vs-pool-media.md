# Hotspot solver-vs-pool para mídia — spec pra fábrica

**De:** thread Mídia Paga · **Data:** 2026-07-23 · **Fonte:** `solver-nlhe/data/exploit/*_pooled.json` (runs 25bb completo, 40bb parcial). Números REAIS — colhidos dos exploit outputs já computados (solver GTO × pool da Aura, mesma árvore `aura_tree_v1`).

## ⚠️ FLAG DE PRODUCT-TRUTH — LER ANTES DE PRODUZIR
Este dado é **solver-vs-pool**. O gabarito atual (`docs/00-strategy/product-truth-aura.md`) diz que a Aura **NÃO é solver** e **não mostra overlay solver×pool** — a Aura hoje mostra **field-vs-MDF**. Logo:
- **Não é claim de produto atual.** A Aura não exibe GTO hoje. Um criativo com "GTO folda X%" implica tela que o produto ainda não tem.
- **É TEASER da feature nova** (solver-vs-pool, a construir + tier premium). Enquadrar como **"em breve / próximo módulo"**, nunca como screenshot existente.
- **Depende de decisão do PO** de virar o gabarito. Só produzir criativo público depois desse martelo.

## 🔥 HERO — K♦9♥5♠ · 25bb · UTG vs BB · facing c-bet
Board seco (K-alto, rainbow, desconexo). Run 25bb (completo). `conf: high`.

| C-bet | GTO folda | Field folda | Gap | Field call/raise | n |
|---|---|---|---|---|---|
| 33% pote | 57,1% | **43,9%** | −13,2pp | 44% / 12% | 198.990 |
| 50% pote | 63,0% | **48,7%** | −14,3pp | 41% / 10% | 128.836 |
| 65% pote | 67,6% | **54,8%** | −12,8pp | 38% / 7% | 64.608 |

**Hook:** "No board mais seco do poker, o solver folda 57%. O field folda 44%. Medido em 199 mil mãos." **Takeaway (simples e correto):** o field não respeita o c-bet em board seco → defende ~13pp além do GTO → seu valor imprime. `run_id: K_rainbow_unpaired_disconnected_utg_bb_25bb`.

## Alternates (mesmo padrão, amostra gigante)
- **A♥A♦K♠ · 40bb** (par de ás): GTO 64,3/68,3/71,3% vs field 51,4/54,5/58,6% · Δ≈−13pp · n=265.835/184.598/97.226 · `A_rainbow_paired_disconnected_utg_bb_40bb`. História: "o field tem medo do ás pareado e não folda."
- **J♥J♦7♠ · 40bb** (par de valete): GTO 56,6/62,7/67,2% vs field 45,5/49,3/53,9% · Δ≈−12pp · n=82.795/61.341/35.293 · `J_rainbow_paired_disconnected_utg_bb_40bb`.
- **A♠A♥K♠ · 40bb** (two-tone, par de ás): GTO 59,0/64,5/67,8% vs field 47,7/50,6/54,4% · n até 379.203 (maior amostra).

## Padrão-mãe (a mensagem)
Em todos: **o field folda 11–14pp MENOS que o GTO facing c-bet.** O field é calling station facing c-bet nesses boards. É o pitch da Aura ("onde o pool desvia do ótimo") num número só.

## Descartados (não usar)
Boards de trips (JsJhJd, AsAhAd) têm `total_dev_ev_bb` alto (5,0 / 3,8 bb) mas **sem amostra de pool** — flop de trinca é raríssimo, é artefato estatístico. Não servem pra mídia.

## Procedência / como regerar o ranking
`solver-nlhe`, ordenar `data/exploit/*_pooled.json` por `total_dev_ev_bb`, filtrar `conf:"high"` e n≥1000. Campos: `spot.gto_folds` (solver) · `pool_by_size.{fold,call,raise,n,conf}` (Aura) · `combos[].dev_ev` (por mão). Cobertura completa + ranking: pendente da outra thread (prompt entregue pelo PO).
