"""Junta enriquecer/saida*.csv com influencers e times em tabela_enriquecida.csv (uma linha por perfil)."""
import csv, glob, re
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
FIX = {"cstival.pokercoach": "cris.stival", "picharapoker_nivel1": "picharapoker"}  # @ de anuncio que nao existe; perfil real achado pelo agente
RUIM = re.compile(r"homônimo|homonimo|n[aã]o [ée] (de )?poker|xadrez|chess grandmaster|corrida de cavalo|horse|ministério|ministerio|golpe|scam", re.I)
PEND = re.compile(r"nao.pesquis|n[aã]o pesquis|pendente|só planilha|planilha", re.I)


def num(txt):
    m = re.search(r"([\d.,]+)\s*([KkMm]?)\s*(?:Followers|seguidores|followers)", txt or "")
    if not m: return None
    s = m.group(1).replace(",", "").replace(" ", "")
    try: v = float(s)
    except ValueError: return None
    return int(v * {"k": 1e3, "m": 1e6}.get(m.group(2).lower(), 1))


enr = {}
files = sorted(glob.glob(str(ROOT / "enriquecer" / "saida_[0-9]*.csv"))) + sorted(glob.glob(str(ROOT / "enriquecer" / "saida_pend_*.csv")))
for f in files:  # pend_* vem depois e sobrescreve
    for r in csv.DictReader(open(f, encoding="utf-8-sig")):
        ev = (r["papel_evidencia"] or "") + " " + (r["papel"] or "")
        feito = bool((r["papel_evidencia"] or "").strip()) and not PEND.search(ev)
        k = (r["origem"], r["handle"].lower())
        if feito or k not in enr: enr[k] = dict(r, _feito=feito)

rows = []
src = [("influencer", ROOT / "influencers_ig_mtt.csv", "tipo"), ("time", ROOT / "times_stables_mtt.csv", "tipo")]
for origem, p, tcol in src:
    for r in csv.DictReader(open(p, encoding="utf-8-sig")):
        h = r["handle"].lower()
        e = enr.get((origem, h), {})
        ev = (e.get("papel_evidencia") or "") + " " + (e.get("papel") or "")
        n = num(e.get("seguidores_ig_snippet"))
        h2 = FIX.get(h, h)
        rows.append(dict(
            origem=origem, lista=r["lista"], handle=h2, instagram_url=f"https://www.instagram.com/{h2}/" if h2 else "",
            dm_link=f"https://ig.me/m/{h2}" if h2 else "", nome=r["nome"], pais=r["pais"], idioma=r["idioma"],
            tipo_inicial=r[tcol], papel=e.get("papel", ""), papel_evidencia=e.get("papel_evidencia", ""),
            vende_curso_ou_coaching=e.get("vende_curso_ou_coaching", ""), onde_vende=e.get("onde_vende", ""),
            time_que_representa=e.get("time_que_representa", ""), sala_ou_ferramenta=e.get("sala_ou_ferramenta") or r.get("publi") or r.get("publi_sala_ferramenta", ""),
            outras_redes=e.get("outras_redes", ""), seguidores_ig_snippet=e.get("seguidores_ig_snippet", ""), seguidores_ig_num=n or "",
            passa_5k=("sim" if n and n >= 5000 else "nao" if n else "?"), atividade=e.get("atividade", ""),
            idioma_conteudo=e.get("idioma_conteudo", ""), email=r.get("email", ""), site_ou_link=r.get("site_ou_link", ""),
            agencia=r.get("agencia", "") or r.get("agencia_ou_empresario", ""), encaixe_provisorio=r.get("encaixe", ""),
            pesquisado="sim" if e.get("_feito") else "nao", conta_suspeita="sim" if RUIM.search(ev) else "",
            handle_original=h if h2 != h else "", fonte_enriquecimento=e.get("fonte_url", "")))
cols = list(rows[0].keys())
with open(ROOT / "tabela_enriquecida.csv", "w", newline="", encoding="utf-8-sig") as fh:
    w = csv.DictWriter(fh, cols); w.writeheader(); w.writerows(rows)
ps = [r for r in rows if r["pesquisado"] == "sim"]
print(len(rows), "linhas;", len(ps), "pesquisadas;", sum(1 for r in rows if r["seguidores_ig_num"]), "com n de seguidores;",
      sum(1 for r in rows if r["passa_5k"] == "sim"), "passam 5k;", sum(1 for r in rows if r["conta_suspeita"]), "suspeitas;",
      sum(1 for r in rows if r["vende_curso_ou_coaching"].lower().startswith("sim")), "vendem curso")
