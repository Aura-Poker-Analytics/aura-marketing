"""Gera envio.html: lista priorizada com mensagem pronta (editavel), copiar, abrir DM, marcar enviado.
Nada e enviado daqui; quem envia e uma pessoa."""
import csv, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
rows = list(csv.DictReader(open(ROOT / "tabela_enriquecida.csv", encoding="utf-8-sig")))
CONC = re.compile(r"gto wizard|upswing|run it once|raise your edge|pokercoaching|hand2note|postflop\+|simple postflop|pio", re.I)
EXCLUI = ("sala_conta", "outro")
ORG = re.compile(r"\b(poker|team|school|academy|staking|backing|club|coaching|escola|equipo|lab|group|grupo)\b", re.I)


def papel1(p):
    p = (p or "").lower().replace(",", "+")
    for k in ("dono_de_time", "coach", "escola", "jogador_influencer", "ferramenta_site", "midia", "sala_conta", "outro"):
        if k in p:
            return k
    return "indef"


def score(r):
    p = papel1(r["papel"])
    if r["conta_suspeita"] or p in EXCLUI:
        return -1
    s = {"dono_de_time": 5, "escola": 4, "coach": 4, "jogador_influencer": 3, "ferramenta_site": 1, "midia": 1, "indef": 1}[p]
    n = int(r["seguidores_ig_num"] or 0)
    s += 3 if n >= 20000 else 2 if n >= 5000 else 0 if not n else -2
    if (r["vende_curso_ou_coaching"] or "").lower().startswith("sim"):
        s += 1
    if r["email"] or r["site_ou_link"] or r["agencia"]:
        s += 1
    if CONC.search(r["sala_ou_ferramenta"] or ""):
        s -= 2
    if r["atividade"].lower().startswith("inativo"):
        s -= 3
    return s


def curto(nome):
    n = re.sub(r"\(.*?\)", "", nome).strip()
    return n.split()[0] if n else nome


AURA = {
    "pt": "A Aura é uma plataforma de análise de MTT: mostra o que o field de torneios faz (frequências por spot, ranges observados), para você estudar onde explorar.",
    "es": "Aura es una plataforma de análisis de MTT: muestra lo que hace el field de torneos (frecuencias por spot, ranges observados), para estudiar dónde explotar.",
    "en": "Aura is an MTT analysis platform: it shows what the tournament field does (frequencies by spot, observed ranges), to help you study where to exploit.",
}
OPEN = {
    ("pt", "pessoa"): "Fala, {n}! Vi seu perfil de MTT{x} e achei que a Aura pode fazer sentido para o seu público.",
    ("pt", "time"): "Fala, pessoal do {n}! Vi o perfil de vocês{x} e achei que a Aura pode fazer sentido para o público de vocês.",
    ("es", "pessoa"): "¡Hola, {n}! Vi tu perfil de MTT{x} y creo que Aura puede tener sentido para tu audiencia.",
    ("es", "time"): "¡Hola, equipo de {n}! Vi el perfil de ustedes{x} y creo que Aura puede tener sentido para su audiencia.",
    ("en", "pessoa"): "Hey {n}! I came across your MTT profile{x} and thought Aura might fit your audience.",
    ("en", "time"): "Hey {n} team! I came across your team's profile{x} and thought Aura might fit your audience.",
}
EXTRA = {
    "pt": {"coach": ", principalmente o lado de ensino", "escola": ", principalmente o lado de ensino", "dono_de_time": ", principalmente o lado de gestão do time"},
    "es": {"coach": ", sobre todo la parte de enseñanza", "escola": ", sobre todo la parte de enseñanza", "dono_de_time": ", sobre todo la parte de gestión del equipo"},
    "en": {"coach": ", especially the coaching side", "escola": ", especially the coaching side", "dono_de_time": ", especially the team-management side"},
}
CLOSE = {
    "pt": "Queria te mostrar a plataforma e, se fizer sentido, conversar sobre uma parceria. Posso te mandar um acesso para você olhar com calma? Se não for o momento, sem problema.\n\n[seu nome] · Aura Poker Analytics",
    "es": "Me gustaría mostrarte la plataforma y, si tiene sentido, conversar sobre una alianza. ¿Te mando un acceso para que la mires con calma? Si no es el momento, sin problema.\n\n[tu nombre] · Aura Poker Analytics",
    "en": "I'd love to show you the platform and, if it makes sense, talk about a partnership. Can I send you access to look at it in your own time? If now's not the time, no worries.\n\n[your name] · Aura Poker Analytics",
}


def lang(r):
    if r["lista"] == "brasil":
        return "pt"
    l = (r["idioma_conteudo"] or r["idioma"] or "").lower()[:2]
    return l if l in ("pt", "es", "en") else ("es" if r["lista"] == "latam" else "en")


def msg(r):
    L, p = lang(r), papel1(r["papel"])
    kind = "time" if (r["origem"] == "time" or p in ("escola", "midia", "ferramenta_site") or ORG.search(r["nome"])) else "pessoa"
    n = r["nome"] if kind == "time" else curto(r["nome"])
    n = re.sub(r"\(.*?\)", "", n).strip() or r["handle"]
    x = EXTRA[L].get(p, "")
    return f"{OPEN[(L, kind)].format(n=n, x=x)} {AURA[L]}\n\n{CLOSE[L]}"


out = []
for r in rows:
    if not r["handle"]:
        continue
    sc = score(r)
    if sc < 0:
        continue
    out.append(dict(
        id=f"{r['origem']}:{r['handle']}", handle=r["handle"], nome=r["nome"], origem=r["origem"], lista=r["lista"],
        papel=papel1(r["papel"]), seg=r["seguidores_ig_snippet"][:60], segn=int(r["seguidores_ig_num"] or 0), passa=r["passa_5k"],
        curso=(r["vende_curso_ou_coaching"] or "")[:3].lower() == "sim", sala=(r["sala_ou_ferramenta"] or "")[:60],
        email=r["email"].split(";")[0], link=r["site_ou_link"].split(";")[0], pesquisado=r["pesquisado"], score=sc,
        lang=lang(r), msg=msg(r), dm=r["dm_link"], url=r["instagram_url"]))
out.sort(key=lambda d: (-d["score"], -d["segn"], d["handle"]))

HTML = (ROOT / "scripts" / "envio_template.html").read_text(encoding="utf-8")
(ROOT / "envio.html").write_text(HTML.replace("__DATA__", json.dumps(out, ensure_ascii=False)), encoding="utf-8")
print(len(out), "perfis no envio.html;", sum(1 for d in out if d["passa"] == "sim"), ">=5k")
