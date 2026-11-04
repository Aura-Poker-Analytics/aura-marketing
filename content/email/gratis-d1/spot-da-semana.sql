-- Spot grátis da semana, lido no dia do envio (analytics prod, só leitura). Mesma regra do PoolVsGtoRelease.FreeSpot da aura-api (main):
-- card grátis mais recente da janela, no stack de maior desvio absoluto. Os números do e-mail saem daqui, nunca de doc.
-- Se a linha mudar (segunda, 09/11 é a próxima troca), atualizar SPOT em content/email/_template/build_gratis_d1.py e passar de novo pelo casa:revisor.
with snap as (select max(snapshot_date) s from tbl_field_exploit_release),
win as (
  select r.* from tbl_field_exploit_release r, snap
  where r.snapshot_date = snap.s and r.release_date <= current_date and r.retire_date > current_date
),
card as (select card_key from win where free_week order by release_date desc, release_seq limit 1)
select w.card_key, w.release_date, w.stack_bb, w.deviation_pts,
       round((k.field_value * 100)::numeric, 1) as field_pct,
       round((k.gto_value * 100)::numeric, 1)   as gto_pct,
       round((k.gto_lo * 100)::numeric, 1)      as gto_lo_pct,
       round((k.gto_hi * 100)::numeric, 1)      as gto_hi_pct,
       k.direction, k.reference_snapshot
from win w
join card c on c.card_key = w.card_key
join tbl_field_exploit_rank k
  on k.snapshot_date = w.snapshot_date and k.rule_version = w.rule_version and k.street = w.street
 and k.action_id = w.action_id and k.role = w.role and k.solver_pair = w.solver_pair and k.stack_bb = w.stack_bb
 and k.boardflophighcard = w.boardflophighcard and k.boardtone = w.boardtone and k.pairedflop = w.pairedflop
 and k.board_connectedness_fl = w.board_connectedness_fl
order by abs(w.deviation_pts) desc, w.release_seq
limit 1;
