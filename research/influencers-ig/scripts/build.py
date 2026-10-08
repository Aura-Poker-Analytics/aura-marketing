"""Fase 3: junta raw/*.csv + cache/*.json (API) em influencers_ig_mtt.csv e RESUMO.md.
Sem cache (API indisponivel) as metricas ficam vazias e o filtro de 5 mil fica 'nao_verificado'."""
import csv, json, statistics
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LANGS = [("brasil", "Brasil (pt)"), ("latam", "LatAm (es)"), ("ingles", "Inglês (en)")]
ESTUDO = ("gto wizard", "upswing", "run it once", "raise your edge", "pio", "postflop", "gtowizard", "solver")
MIN_SEG = 5000


def norm(h): return h.strip().lstrip("@").lower().rstrip(".,;/")


def api(h):
    p = ROOT / "cache" / f"{h}.json"
    if not p.exists(): return None, "sem_api"
    d = json.loads(p.read_text(encoding="utf-8"))
    bd = d["resp"].get("business_discovery") if d["status"] == 200 else None
    if not bd: return None, "pessoal_ou_nao_encontrado"
    return bd, "ok"


def metrics(bd):
    fol = bd.get("followers_count") or 0
    posts = (bd.get("media") or {}).get("data") or []
    eng = ppw = None
    if posts and fol:
        eng = sum((p.get("like_count") or 0) + (p.get("comments_count") or 0) for p in posts) / len(posts) / fol
        ts = sorted(datetime.fromisoformat(p["timestamp"].replace("+0000", "+00:00")) for p in posts)
        span = (ts[-1] - ts[0]).total_seconds() / 604800
        ppw = (len(ts) - 1) / span if span > 0 else None
    return fol, bd.get("media_count"), ppw, eng


def fit(r):
    t, pub = r["tipo_provavel"], (r["publi_sala_ferramenta"] or "").lower()
    ferr = any(k in pub for k in ESTUDO)
    if t == "midia": return "baixo", "Mídia/conta institucional: alcance, mas não é voz de estudo individual."
    if t in ("coach", "stable"):
        if ferr: return "médio", "Ensina MTT (público de estudo), mas já divulga ferramenta de estudo concorrente."
        return "alto", "Ensina MTT a um público que estuda, sem ferramenta de estudo concorrente na fonte."
    if ferr: return "médio", "Jogador de MTT com publi de ferramenta de estudo concorrente."
    if r["fonte_tipo"] in ("twitch_youtube", "ads_library"):
        return "alto", "Jogador de MTT que produz conteúdo/estudo em canal próprio."
    return "médio", "Jogador de MTT; falta confirmar se produz conteúdo de estudo."


rows, stats = [], {}
for lang, label in LANGS:
    n = sem_handle = 0
    seen = set()
    for r in csv.DictReader(open(ROOT / "raw" / f"{lang}.csv", encoding="utf-8-sig")):
        n += 1
        h = norm(r["handle"])
        if not h or h in seen:
            sem_handle += 0 if h else 1
            continue
        seen.add(h)
        bd, st = api(h)
        fol, mc, ppw, eng = metrics(bd) if bd else (None, None, None, None)
        f5 = "nao_verificado" if st == "sem_api" else ("sim" if (fol or 0) >= MIN_SEG else ("nao" if bd else "n/a"))
        fi, why = fit(r)
        rows.append(dict(lista=lang, handle=h, nome=r["nome"], pais=r["pais"], idioma=r["idioma"], seguidores=fol,
                         posts_semana=None if ppw is None else round(ppw, 2),
                         engajamento=None if eng is None else round(eng, 4), tipo=r["tipo_provavel"],
                         publi=r["publi_sala_ferramenta"], encaixe=fi, motivo_encaixe=why, status_api=st,
                         filtro_5k=f5, handle_confianca=r["handle_confianca"], fonte_url=r["fonte_url"],
                         motivo_mtt=r["motivo_mtt"]))
    stats[lang] = dict(candidatos=n, com_handle=len(seen), sem_handle=sem_handle)

cols = list(rows[0].keys())
with open(ROOT / "influencers_ig_mtt.csv", "w", newline="", encoding="utf-8-sig") as fh:
    w = csv.DictWriter(fh, cols); w.writeheader(); w.writerows(rows)

rank = {"alto": 0, "médio": 1, "baixo": 2}
out = ["# Varredura de influencers de poker MTT no Instagram", "",
       f"Gerado em {datetime.now():%Y-%m-%d}. Só pesquisa; ninguém foi contatado.", "",
       "## Números", "", "| Lista | Candidatos | Com @ | Sem @ | API ok | Pessoal/não achado | Sem API | ≥ 5 mil (verificado) |",
       "| --- | --- | --- | --- | --- | --- | --- | --- |"]
for lang, label in LANGS:
    rs = [r for r in rows if r["lista"] == lang]
    c = lambda k: sum(1 for r in rs if r["status_api"] == k)
    out.append(f"| {label} | {stats[lang]['candidatos']} | {stats[lang]['com_handle']} | {stats[lang]['sem_handle']} | "
               f"{c('ok')} | {c('pessoal_ou_nao_encontrado')} | {c('sem_api')} | {sum(1 for r in rs if r['filtro_5k']=='sim')} |")
tot_api = sum(1 for r in rows if r["status_api"] == "ok")
if tot_api == 0:
    out += ["", "> **Fase 2 não rodou:** a variável `META_IG_TOKEN` não contém um token (ver STATE/PR). Seguidores, posts por semana e engajamento estão vazios; o filtro de 5 mil está `nao_verificado`; o encaixe e o top 20 são **provisórios**, só por tipo e fonte. Rodar `scripts/enrich.py` e depois `scripts/build.py` completa tudo (o cache evita repetir chamada)."]
for lang, label in LANGS:
    rs = sorted([r for r in rows if r["lista"] == lang and r["filtro_5k"] != "nao"],
                key=lambda r: (rank[r["encaixe"]], -(r["seguidores"] or 0), -(r["engajamento"] or 0), r["handle"]))[:20]
    out += ["", f"## Top 20 para abordar — {label}", "", "| # | @ | Tipo | Seguidores | Eng. | Publi | Encaixe |", "| --- | --- | --- | --- | --- | --- | --- |"]
    for i, r in enumerate(rs, 1):
        out.append(f"| {i} | @{r['handle']} | {r['tipo']} | {r['seguidores'] or '—'} | {r['engajamento'] if r['engajamento'] is not None else '—'} | {r['publi'] or '—'} | {r['encaixe']}: {r['motivo_encaixe']} |")
out += ["", "## Notas de método", "",
        "- Descoberta por busca web, WebSearch restrito a instagram.com, biblioteca de anúncios da Meta e listas públicas; nenhum Instagram aberto logado, nenhuma raspagem de perfil.",
        "- Todo @ veio literalmente de uma fonte lida; `handle_confianca=inferido_da_bio` vem de título/bio indexados e deve ser conferido.",
        "- Metas de 80–150 por idioma não foram atingidas no Brasil; ver contagens acima.",
        "- Engajamento = média de (curtidas + comentários) / seguidores nos últimos 12 posts; posts por semana = intervalo entre o 1º e o 12º post.",
        "- O `ads_library_search` é posto como fonte, mas rendeu pouco nicho."]
(ROOT / "RESUMO.md").write_text("\n".join(out) + "\n", encoding="utf-8")
print(stats, "api_ok", tot_api)
