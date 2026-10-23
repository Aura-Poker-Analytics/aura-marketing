"""Junta diretores/saida_*.csv e novos_times_brasil_pessoas.csv em diretores_times.csv (com links do Instagram e da DM)."""
import csv
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
rows, seen = [], set()
extra = [dict(handle_time="midasteam", time="Midas Team", pessoa="Daniel Almeida", cargo="diretor (segundo matéria do SuperPoker)",
              instagram_handle="", instagram_url="", confianca="baixa", fonte_url="", obs="citado por um agente; sem fonte arquivada nem @, conferir")]
srcs = [ROOT / "diretores" / f for f in ("saida_1.csv", "saida_2.csv", "novos_times_brasil_pessoas.csv")]
for p in srcs:
    for r in csv.DictReader(open(p, encoding="utf-8-sig")):
        if (r.get("pessoa") or "").strip():
            extra.append(r)
for r in extra:
    key = (r["time"].lower(), r["pessoa"].lower())
    if key in seen: continue
    seen.add(key)
    h = (r["instagram_handle"] or "").strip().lstrip("@").lower()
    r["instagram_handle"] = h
    r["instagram_url"] = f"https://www.instagram.com/{h}/" if h else ""
    r["dm_link"] = f"https://ig.me/m/{h}" if h else ""
    rows.append(r)
cols = ["handle_time", "time", "pessoa", "cargo", "instagram_handle", "instagram_url", "dm_link", "confianca", "fonte_url", "obs"]
with open(ROOT / "diretores_times.csv", "w", newline="", encoding="utf-8-sig") as fh:
    w = csv.DictWriter(fh, cols, extrasaction="ignore"); w.writeheader(); w.writerows(rows)
print(len(rows), "pessoas;", sum(1 for r in rows if r["instagram_handle"]), "com @;", len({r['time'].lower() for r in rows}), "times")
