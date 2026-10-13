"""Junta raw/times_*.csv em times_stables_mtt.csv + TIMES.md (links do Instagram e da DM)."""
import csv
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
SALAS = ("ggpoker", "pokerstars", "partypoker", "wpt", "888", "winamax", "natural8", "coinpoker", "acr", "unibet")
CONC = ("gto wizard", "upswing", "run it once", "raise your edge", "pio", "postflop", "hand2note", "solver", "pokercoaching")
rows, seen = [], set()
for lista in ("brasil", "mundo"):
    for r in csv.DictReader(open(ROOT / "raw" / f"times_{lista}.csv", encoding="utf-8-sig")):
        h = r["handle"].strip().lstrip("@").lower()
        if h and h in seen: continue
        seen.add(h)
        txt = " ".join([r["nome"], r["publi_sala_ferramenta"], r["tipo"]]).lower()
        if any(s in h or s in r["nome"].lower() for s in SALAS) and r["tipo"] == "time":
            enc, why = "baixo", "Conta de marca de sala, não é time de jogadores."
        elif any(c in txt for c in CONC) or r["tipo"] == "site_treino":
            enc, why = "médio", "Ferramenta/site de treino: público de estudo, mas concorre ou se sobrepõe à Aura."
        elif r["tipo"] in ("stable", "escola", "rede_coaches", "comunidade", "time"):
            enc, why = "alto", "Time/escola de MTT com público de estudo; um acordo alcança vários jogadores."
        else:
            enc, why = "médio", "Revisar."
        rows.append(dict(lista=lista, handle=h, instagram_url=f"https://www.instagram.com/{h}/" if h else "",
                         dm_link=f"https://ig.me/m/{h}" if h else "", encaixe=enc, motivo_encaixe=why,
                         **{k: r[k] for k in ("nome", "pais", "idioma", "tipo", "tamanho_time", "publi_sala_ferramenta",
                            "email", "site_ou_link", "agencia_ou_empresario", "contato_fonte_url", "handle_confianca",
                            "fonte_url", "motivo_mtt", "obs")}))
with open(ROOT / "times_stables_mtt.csv", "w", newline="", encoding="utf-8-sig") as fh:
    w = csv.DictWriter(fh, list(rows[0].keys())); w.writeheader(); w.writerows(rows)
rk = {"alto": 0, "médio": 1, "baixo": 2}
out = ["# Times, stables e escolas de poker MTT", "", f"{len(rows)} entradas ({sum(1 for r in rows if r['handle'])} com @, {sum(1 for r in rows if r['email'])} com e-mail, {sum(1 for r in rows if r['site_ou_link'])} com site/link). Seguidores ainda indisponíveis (Business Discovery bloqueado). Só pesquisa; ninguém contatado.", ""]
for lista, label in (("brasil", "Brasil"), ("mundo", "Mundo")):
    rs = sorted([r for r in rows if r["lista"] == lista], key=lambda r: (rk[r["encaixe"]], r["handle"]))
    out += [f"## {label} ({len(rs)})", "", "| @ | Nome | Tipo | País | Encaixe | Contato |", "| --- | --- | --- | --- | --- | --- |"]
    for r in rs:
        ig = f"[@{r['handle']}]({r['instagram_url']}) ([DM]({r['dm_link']}))" if r["handle"] else "—"
        ct = r["email"] or r["site_ou_link"] or r["agencia_ou_empresario"] or "—"
        out.append(f"| {ig} | {r['nome']} | {r['tipo']} | {r['pais'] or '—'} | {r['encaixe']} | {ct} |")
    out.append("")
(ROOT / "TIMES.md").write_text("\n".join(out), encoding="utf-8")
print(len(rows))
