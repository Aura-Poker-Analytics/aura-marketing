# Grátis D1: números verificados

Os números de cada semana saem de `spot-da-semana.sql`, lido no analytics prod no dia. É a mesma regra do `PoolVsGtoRelease.FreeSpot` na `main` da aura-api: o card grátis mais recente da janela, no stack de maior desvio absoluto. Uma linha por semana.

| Semana | card_key | Stack | Liberado em | Snapshot e referência | Field | GTO | Faixa GTO | Direção | Lido em |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 02/11 a 08/11/2026 | `river:31:opening:btn_bb:1311` | 60bb | 02/11 | 20261102 e 20261022 | 27,7% | 50,1% | 43,1% a 57,1% | underbet ("Too passive" na tela) | 04/11, pela consulta e pela leitura direta das tabelas `tbl_field_exploit_release` e `tbl_field_exploit_rank` (`gto_lo` = 0,4313) |

Regime e tipo: GTO chipEV, field de todos os tipos de torneio (Regular, KO e Mystery). A fonte é o FE 1.2, repassado pela HUB em 04/11.

O rótulo "Too passive" é o de `underbet` no i18n do front (`poolVsGto.json`, igual em PT e EN).
