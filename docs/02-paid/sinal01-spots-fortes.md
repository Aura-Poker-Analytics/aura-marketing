# Spots de flop do Field Exploits que seguem "desvio forte" nas faixas 5, 7/8 e 9 (29/10/2026)

Só leitura. Desvio fora da faixa = |field − GTO| − meia-largura (pp); forte = ≥ 5 pp e faixa não larga.
Todas as linhas são a reação do BB (ou do defensor) ao c-bet, métrica fold. "overfold" = field folda mais que o GTO; "overdefend" = folda menos.

## Os 3 melhores (calendário do Field Exploits, tbl_field_exploit_release 20261026)

| # | Spot | Field fold | GTO centro (5 = 7/8 = 9) | Faixa v5 | Faixa v7/8 | Faixa v9 | Desvio fora v5 / v7-8 / v9 | Direção | n | Card |
|---|------|-----------|--------------------------|----------|-----------|----------|---------------------------|---------|---|------|
| 1 | `btn_sb` (BTN abre, SB defende), 25bb, A-high rainbow desconectado, c-bet 33% | 41,5% | 25,0% | 19,0–31,0 | 19,0–31,0 | 19,0–31,0 | 10,5 / 10,5 / 10,5 | overfold | 9.937 | GRÁTIS, semana de 07/12 (card `flop:1:reaction:btn_sb:6110`, também 40 e 60bb), manchete |
| 2 | `btn_sb` 25bb, A-high two-tone desconectado, c-bet 33% | 38,0% | 25,7% | 19,7–31,7 | 19,7–31,7 | 19,7–31,7 | 6,3 / 6,3 / 6,3 | overfold | 14.793 | Individual, no ar agora (26/10 a 02/11), manchete (`flop:1:reaction:btn_sb:6310`) |
| 3 | `btn_bb` 40bb, low two-tone connected, c-bet 33% (célula class_model) | 23,2% | 30,2% | 28,6–31,9 | 28,6–31,9 | 28,6–31,9 | 5,4 / 5,4 / 5,4 | overdefend | 35.599 | Individual, no ar agora (26/10 a 16/11), manchete (`flop:1:reaction:btn_bb:1312`) |

Nota do par: `btn_sb` = BTN abre e SB defende (o field é o do SB); `btn_bb` = BTN abre e BB defende.

Reserva do spot 1 em outros stacks (mesmo card grátis): 40bb field 38,4% vs GTO 26,3% (faixa v5 24,6–28,0; v7/8 e v9 22,2–30,4), desvio 10,4 / 8,0 / 8,0, n 21.377; 60bb field 38,0% vs 26,9% (20,9–32,9 em todas), desvio 5,2 / 5,2 / 5,2, n 13.706.
Reserva do spot 3 em 60bb: field 22,4% vs 34,9%, faixa v5 28,9–40,9, v7/8 e v9 27,5–42,3, desvio 6,6 / 5,1 / 5,1, n 21.861.

Confirmações:
- Centro igual nas três faixas: para as 6.212 linhas o centro v5 = v7 = v8 (6.212/6.212). Da v8 para a v9 o centro muda em 98 linhas (as 46 células A/K/Q do lote 1, c-bet ≤ 65%); nas 186 manchetes fortes nas três versões, 0 mudam de centro. Os 3 spots acima não estão nas células corrigidas.
- v7 e v8 dão a mesma faixa no flop em todas as 6.212 linhas.
- A faixa só alarga (ou fica igual) de 5 para 7/8; o desvio forte cai para o spot 1 (40bb) e 3, mas continua ≥ 5.

## O spot do post atual NÃO serve para o anúncio

`utg_bb` 25bb, A two-tone OESD, c-bet 50% (GRÁTIS 26/10 a 23/11): field 53,8%. v5 centro 73,5 faixa 67,5–79,5, desvio 13,7 (overdefend); v7/8 centro 73,5 hw 36,5 (larga, 0,0); v9 centro 58,4 hw 16,8 faixa 41,6–75,2 (larga, 0,0). Dentro da faixa nas duas novas. O 60bb idem (6,5 → 0,0).

## Calendário do flop até 31/12 (linha manchete de cada card, todas as versões)

| Data | Plano | Par | bb | Size | Classe | n | Field | GTO v5/7/8 | GTO v9 | hw v5 / v8 / v9 | Desvio v5 / v8 / v9 | Larga v8/v9 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 26/10 | Individual | btn_bb | 40 | 33 | low two-tone connected (class_model) | 35.599 | 23,2 | 30,2 | 30,2 | 1,6 / 1,6 / 1,6 | 5,4 / 5,4 / 5,4 | não |
| 26/10 | Individual | btn_bb | 60 | 33 | low two-tone connected | 21.861 | 22,4 | 34,9 | 34,9 | 6,0 / 7,4 / 7,4 | 6,6 / 5,1 / 5,1 | não |
| 26/10 | Individual | btn_sb | 25 | 33 | A two-tone disconnected | 14.793 | 38,0 | 25,7 | 25,7 | 6,0 / 6,0 / 6,0 | 6,3 / 6,3 / 6,3 | não |
| 26/10 | Individual | btn_sb | 40 | 33 | A two-tone disconnected | 31.299 | 36,0 | 26,5 | 26,5 | 1,7 / 5,8 / 5,8 | 7,8 / 3,7 / 3,7 | não (perde o forte) |
| 26/10 | GRÁTIS | utg_bb | 25 | 50 | A two-tone OESD | 15.674 | 53,8 | 73,5 | 58,4 | 6,0 / 36,5 / 16,8 | 13,7 / 0 / 0 | SIM/SIM |
| 26/10 | GRÁTIS | utg_bb | 60 | 50 | A two-tone OESD | 15.571 | 48,7 | 61,2 | 61,2 | 6,0 / 20,0 / 20,0 | 6,5 / 0 / 0 | SIM/SIM |
| 02/11 | Individual | utg_bb | 25 | 50 | low rainbow OESD | 14.691 | 47,1 | 34,2 | 34,2 | 6,0 / 18,3 / 18,3 | 6,9 / 0 / 0 | SIM/SIM |
| 02/11 | Individual | utg_bb | 40 | 50 | low rainbow OESD | 24.729 | 42,1 | 31,1 | 31,1 | 6,0 / 19,5 / 19,5 | 5,0 / 0 / 0 | SIM/SIM |
| 16/11 | GRÁTIS | co_bb | 40 | 50 | low two-tone connected | 19.621 | 33,5 | 42,5 | 42,5 | 3,3 / 8,7 / 8,7 | 5,7 / 0,3 / 0,3 | não (perde) |
| 23/11 | Individual | co_bb | 60 | 33 | low rainbow paired OESD | 18.018 | 34,6 | 47,2 | 47,2 | 6,0 / 13,3 / 13,3 | 6,6 / 0 / 0 | SIM/SIM |
| 07/12 | GRÁTIS | btn_sb | 25 | 33 | A rainbow disconnected | 9.937 | 41,5 | 25,0 | 25,0 | 6,0 / 6,0 / 6,0 | 10,5 / 10,5 / 10,5 | não |
| 07/12 | GRÁTIS | btn_sb | 40 | 33 | A rainbow disconnected | 21.377 | 38,4 | 26,3 | 26,3 | 1,7 / 4,1 / 4,1 | 10,4 / 8,0 / 8,0 | não |
| 07/12 | GRÁTIS | btn_sb | 60 | 33 | A rainbow disconnected | 13.706 | 38,0 | 26,9 | 26,9 | 6,0 / 6,0 / 6,0 | 5,2 / 5,2 / 5,2 | não |
| 14/12 | Individual | co_bb | 25 | 50 | Q two-tone disconnected | 4.023 | 57,5 | 44,9 | 44,9 | 6,0 / 9,5 / 9,5 | 6,6 / 3,1 / 3,1 | não (perde) |
| 28/12 | GRÁTIS | co_btn | 25 | 50 | low two-tone OESD | 3.648 | 39,6 | 26,4 | 26,4 | 6,0 / 10,1 / 10,1 | 7,2 / 0 / 0 | SIM/SIM |

Das 15 linhas (card x stack) do calendário até dezembro, 6 mantêm ≥ 5 pp nas três faixas (btn_bb 40 e 60, btn_sb 25 two-tone, btn_sb 25/40/60 do 07/12); 9 perdem o forte (6 por faixa larga, 3 porque a faixa alarga e o desvio cai abaixo de 5).

## Reserva fora das próximas semanas (manchete forte nas três faixas, n ≥ 3.000, pote simples; datas do calendário mais adiante)

| Par | bb | Classe (c-bet 33%) | n | Field | GTO | Desvio v5/v8/v9 | Direção | Card |
|---|---|---|---|---|---|---|---|---|
| utg_bb | 25 | Q rainbow connected (class_model) | 4.319 | 42,8 | 62,9 | 18,5 / 18,5 / 18,5 | overdefend | Individual 19/02/2029 |
| utg_bb | 25 | K two-tone connected (class_model) | 6.616 | 45,1 | 63,1 | 16,3 / 16,3 / 16,3 | overdefend | Individual 27/12/2027 |
| utg_bb | 25 | Q two-tone connected (class_model) | 6.077 | 41,6 | 58,4 | 15,2 / 15,2 / 15,2 | overdefend | Individual 17/01/2028 |
| utg_bb | 25 | K rainbow connected (class_model) | 4.604 | 50,3 | 66,9 | 15,0 / 15,0 / 15,0 | overdefend | GRÁTIS 09/07/2029 |
| btn_sb | 40 | A rainbow paired disconnected | 5.201 | 46,2 | 28,3 | 16,1 / 13,8 / 13,8 | overfold | Individual 02/08/2027 |
| btn_sb | 40 | K rainbow paired disconnected | 3.383 | 42,6 | 26,4 | 14,5 / 13,9 / 13,9 | overfold | GRÁTIS 26/03/2029 |

## Contagens que batem com o STATE.md (27/10)

Ranking do flop, 6.212 linhas: fora da faixa 3.957 (v5) → 3.294 (v7/8/9: 3.298); fortes ≥ 5: 2.019 → 1.602 (v9 1.603) contando as faixas largas; manchetes fortes 335 → 206 (v9 207). O STATE diz 1.601; diferença de 1 por arredondamento de borda.
Excluindo as linhas de faixa larga (que o build do Field Exploits descarta: `wide` não ranqueia): fortes 2.019 → 1.453 (v9 1.454), manchetes fortes 335 → 186 (v9 187). Linhas de faixa larga: 1.184 na v7/8, 1.162 na v9. A v5 reproduzida bate com o `deviation_pts` gravado em 6.212/6.212 linhas.
Fortes nas três versões (sem larga): 1.453 linhas; 186 manchetes; 170 com card no calendário (qualquer data).

## Como foi medido

1. Lastro da tag `contract/reference-band-v9-2026-10-29` extraído com `git archive` (sem trocar de branch) para `...\scratchpad\lastro-v9`, usado por PYTHONPATH.
2. Script `...\scratchpad\measure_spots.py` (somente SELECT, sessão read only): lê as 6.212 linhas de `tbl_field_exploit_rank` (flop, 20261026), monta a célula do GTO em `tbl_gto_reference` 20261022 (fold/call/raise/allin, runs colapsados como o build) e chama `lastro.poker.gto_aggregate.reference_band` com uma classe, N = 1, para `band_version` 5, 7, 8 e 9, mantendo o field de cada linha (mesma conta do `diff_band_v9_flop_centro.py` do lastro).
3. Desvio = max(|field − centro| × 100 − meia-largura, 0); forte = ≥ 5 − tol e `wide` falso.
4. Join com `tbl_field_exploit_release` (flop, 20261026) por par, stack e classe para data, plano (free_week) e card.
5. Saídas: `...\scratchpad\spots_all.csv` (todas as 6.212 linhas, todas as versões) e `...\scratchpad\calendario_2026_headline.csv`.
Não foi rodado dotnet test (a conta é a mesma do Python; evita a guarda de RAM). Nenhuma escrita em banco.

## Limites e o que não deu

- Linhas `class_model` (553 células): mantive a faixa gravada (σ do modelo de classe) nas quatro versões, como o contrato diz que a célula class_model fica igual à v8 e sem termo do rep; não recalculei pela API C#. Os spots 3 e várias reservas dependem disso.
- A medição usa a linha manchete do ranking v5 (`is_headline`). Ao refazer o ranking na v7/8, impacto, n e rodízio podem trocar a manchete do card; isso não foi refeito (o próprio lastro avisa o mesmo). Também não existe aqui a lista "8 do Individual": usei o plano (`free_week`) do calendário gravado, sem outra regra de 8 cards.
- Campo e GTO são fold; call/raise do flop não entram no rank.
- Caminho C# `FetchAggregated` não foi executado; as contagens do STATE foram reproduzidas em Python (3.957/3.294, 2.019/1.602, 335/206).
