"""Modo GTO - build das artes de lancamento (mesmo pipeline do Field Trends / Field Ranges).

1. le numbers.json (unica fonte de numero) e as capturas de producao em prints/prod
2. gera os HTMLs-fonte em src/
3. renderiza com Playwright (device_scale_factor=1) -> PNGs em content/posts/modo-gto-launch/instagram/
   e copia para instagram/output/modo-gto-launch/

Cada arte tem suas dependencias. Se faltar qualquer uma, a arte sai com o marcador [[N..]] ou o slot
"[PRINT DE PRODUCAO PENDENTE]" visivel e o arquivo ganha o sufixo -DRAFT. Pronta = nome sem sufixo
(o -DRAFT antigo da mesma arte e apagado).

Uso:  python build.py                 (todas as artes)
      python build.py --only feed-pt  (uma arte; aceita varias, separadas por virgula)
      python build.py --strict        (falha se alguma arte ainda for DRAFT: use antes de publicar)
      python build.py --layout-test   (teste de layout com capturas de TESTE; saida em _layout-test/, nunca publicar)
Depois: python build_email.py

Regra de texto das artes (Rafael, 08/10): por arte, no maximo UM titulo curto (~6 palavras) e UMA linha de apoio
(~10 palavras); a imagem fala. Em toda arte so ficam @aurapokeranalytics e 18+, pequenos. Sem kicker, sem selo,
sem CTA escrito (o link e o sticker/link na bio), sem rodape longo. Nunca "Beta", "overlay", "solver" nem marca de terceiro.
"""
import re
import shutil
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

import lib
from lib import ASSETS, MIRROR, OUT, SRC, TPL, Ex, chart_svg, find_print, n5_missing, ph

# ---------------------------------------------------------------- textos (copy.md, tabela "Texto final de cada arte")
# Apoio = None -> sem linha de apoio. "{N1}" -> spot (numbers.json). Titulo: <em> = trecho em ambar.
ART = {
    "feed-pt": dict(lang="pt", size=(1080, 1350), kind="feed", t="Mesmo spot,<br><em>dois números</em>", s="{N1}", ts=92),
    "feed-en": dict(lang="en", size=(1080, 1350), kind="feed", t="Same spot,<br><em>two numbers</em>", s="{N1}", ts=92),
    "story-pt": dict(lang="pt", size=(1080, 1920), kind="story", t="O field folda<br><em>mais que o GTO?</em>", s="{N1}", ts=80),
    "story-en": dict(lang="en", size=(1080, 1920), kind="story", t="Does the field<br>fold <em>more<br>than GTO?</em>", s="{N1}", ts=88),
    # capa do story (lancamento, 15/10): selo NO AR, preco em R$, sem micro-legenda do spot
    "story-capa-pt": dict(lang="pt", size=(1080, 1920), kind="story", t="Modo GTO<br><em>no ar</em>", s="{t:story_apoio_pt}", ts=120, cover=True, live="NO AR", caption_key="story_grafico_pt"),
    # carrossel EN, 6 slides
    "carrossel-en-01": dict(lang="en", size=(1080, 1350), kind="cover", t="GTO Mode<br>is <em>live</em>", s="{t:c1_apoio_en}", ts=148),
    "carrossel-en-02": dict(lang="en", size=(1080, 1350), kind="c2", t="See where the<br>field breaks<br><em>from GTO</em>", s="{N1}", ts=84),
    "carrossel-en-03": dict(lang="en", size=(1080, 1350), kind="c3", t="GTO on the<br><em>turn and river</em>", s="{t:c3_apoio_en}", ts=84),
    "carrossel-en-04": dict(lang="en", size=(1080, 1350), kind="c4", t="Preflop:<br><em>GTO and deviation</em>", s="{t:c4_apoio_en}", ts=76),
    "carrossel-en-05": dict(lang="en", size=(1080, 1350), kind="price", t="{t:c5_titulo_en}", s="{t:c5_apoio_en}", ts=84),
    "carrossel-en-06": dict(lang="en", size=(1080, 1350), kind="cta", t="Get GTO Mode", s="Link in bio.", ts=76),
}
N_SLIDES = 6

# ---------------------------------------------------------------- dependencias por arte
def needs(name, n):
    """Lista do que falta para a arte ser final (vazia = pronta)."""
    a = ART[name]
    ex = Ex(n, a["lang"])
    k = a["kind"]
    txt = n.get("textos_com_numero") or {}
    m = []
    sk = a["s"][3:-1] if a["s"] and a["s"].startswith("{t:") else None
    if sk and not lib.has_text(txt.get(sk)):
        m.append(sk)
    if k == "feed":
        return ex.missing(with_n1=True)
    if k == "story":
        return ex.missing(with_n1=not a.get("cover")) + m
    if k == "cover":
        return m + ([] if find_print("postflop-en") else ["print:postflop-en"])
    if k == "c2":
        return ex.missing(with_n1=True)
    if k == "c3":
        return m + [f"print:{p}" for p in ("second-barrel", "turn-delayed-cbet") if not find_print(p)]
    if k == "c4":
        return m + n5_missing(n) + ([] if find_print("preflop-en") else ["print:preflop-en"])
    if k == "price":
        return m + [k_ for k_ in ("c5_titulo_en", "c5_numero_en") if not lib.has_text(txt.get(k_))]
    return m


# ---------------------------------------------------------------- HTML
def make_common_js():
    t = TPL.read_text(encoding="utf-8")
    icon = re.search(r"const ICON_PATHS = `(.*?)`;", t, re.S).group(1)
    letters = re.search(r"const AURA_LETTERS = `(.*?)`;", t, re.S).group(1)
    js = f"""const ICON_PATHS = `{icon}`;
const ICON_SVG = `<svg viewBox="0 0 60 45" fill="currentColor" xmlns="http://www.w3.org/2000/svg">${{ICON_PATHS}}</svg>`;
const AURA_LETTERS = `{letters}`;
const WORDMARK_SVG = `<svg viewBox="1 204 594 129" fill="currentColor" xmlns="http://www.w3.org/2000/svg">${{AURA_LETTERS}}</svg>`;
document.querySelectorAll("[data-icon]").forEach(el => el.innerHTML = ICON_SVG);
document.querySelectorAll("[data-wordmark]").forEach(el => el.innerHTML = WORDMARK_SVG);
(function () {{
  const host = document.getElementById("suits");
  if (!host) return;
  const suits = ["\\u2660", "\\u2663", "\\u2666", "\\u2665"];
  const step = 168; let i = 0;
  for (let y = -40; y < 2000; y += step) {{
    for (let x = -40; x < 1160; x += step) {{
      const s = document.createElement("span");
      s.textContent = suits[i % 4];
      s.style.left = (x + ((Math.floor(y / step) % 2) ? step / 2 : 0)) + "px";
      s.style.top = y + "px";
      s.style.fontSize = (34 + (i * 29) % 18) + "px";
      s.style.transform = `rotate(${{(i * 53) % 40 - 20}}deg)`;
      host.appendChild(s); i++;
    }}
  }}
}})();
// linha de apoio: uma linha so; encolhe ate caber (o spot N1 tem comprimento livre)
document.fonts.ready.then(() => {{
  document.querySelectorAll(".fit").forEach(el => {{
    let s = parseFloat(getComputedStyle(el).fontSize);
    while (el.scrollWidth > el.clientWidth && s > 26) {{ s -= 1; el.style.fontSize = s + "px"; }}
  }});
}});
"""
    (SRC / "common.js").write_text(js, encoding="utf-8")


def ring():
    return """<div class="arc" style="top:-110px;left:50%;transform:translateX(-50%)"><svg width="1000" height="1000" viewBox="0 0 1000 1000" fill="none">
<circle cx="500" cy="500" r="470" stroke="url(#g)" stroke-width="3" stroke-linecap="round" stroke-dasharray="2200 750"/>
<circle cx="500" cy="500" r="436" stroke="rgba(212,164,24,0.16)" stroke-width="1.5"/>
<defs><linearGradient id="g" x1="0" y1="0" x2="1000" y2="1000"><stop offset="0" stop-color="#FCD34D"/><stop offset="0.5" stop-color="#D4A418"/><stop offset="1" stop-color="#7A5E0E"/></linearGradient></defs></svg></div>"""


def page(lang, h, inner, css="", bg_arc=False, tag="", cls=""):
    return f"""<!DOCTYPE html>
<html lang="{lang}"><head><meta charset="UTF-8"><title>Aura Modo GTO</title>
<link rel="stylesheet" href="base.css"><style>{css}</style></head>
<body><div class="page h{h} {cls}">
{ring() if bg_arc else ""}
<div class="vignette"></div>
{tag}
{inner}
</div><script src="common.js"></script></body></html>"""


def lockup(right=""):
    return f"""<header><div class="lockup"><span class="icon" data-icon></span><span class="wm" data-wordmark></span></div>{right}</header>"""


def footer():
    """So @handle e 18+, pequenos. Sem 'Dados:', sem ferramenta de estudo."""
    return f"""<footer><div class="handle"><span class="icon" data-icon></span><span>{lib.HANDLE}</span></div><span class="age">18+</span></footer>"""


def draft_tag(miss, test=False):
    if not miss and not test:
        return ""
    txt = ("TESTE · " if test else "") + "DRAFT" + (" · falta " + ", ".join(miss) if miss else "")
    return f'<div class="drafttag">{txt}</div>'


def slot(name, label_for, n):
    """Slot de imagem de producao: a captura (se existir) ou a moldura com o rotulo pendente."""
    p = find_print(name)
    if p:
        dst = ASSETS / f"prod-{name}{p.suffix.lower()}"
        shutil.copyfile(p, dst)
        return f'<div class="shot slotimg"><img src="assets/{dst.name}"></div>'
    extra = ""
    if name == "preflop-en":
        n5 = n.get("N5") or {}
        parts = []
        for key, lab in (("cell", "celula"), ("gto", "GTO"), ("field", "field"), ("deviation", "desvio")):
            v = n5.get(key)
            parts.append(f"{lab}: " + (str(v) if (lib.has_text(v) or lib.is_num(v)) else "[[N5 " + lab + "]]"))
        extra = f'<div class="pexp">destacar na captura (torneio Regular) · {" · ".join(parts)}</div>'
    if name == "postflop-en":
        extra = '<div class="pexp">spot N1 com field (N2) e GTO + faixa (N3); sem reacao a raise de 3-bet CO x BB a 40bb</div>'
    return (f'<div class="slot"><div class="plab">[PRINT DE PRODUÇÃO PENDENTE]</div>'
            f'<div class="pexp">esperado: prints\\prod\\{name}.png</div>{extra}</div>')


def stack(names, big=False):
    """Capturas largas empilhadas (cada uma um card do app, 2232 px de largura), ou o slot pendente."""
    parts = []
    for nm in names:
        p = find_print(nm)
        if not p:
            parts.append(f'<div class="slot" style="height:200px;margin:0 auto;width:1032px;border:4px dashed rgba(251,191,36,.75);border-radius:26px"><div class="plab" style="font-size:36px">[PRINT DE PRODUÇÃO PENDENTE]</div><div class="pexp">esperado: prints-mkt/{nm}.png</div></div>')
            continue
        dst = ASSETS / f"prod-{nm}{p.suffix.lower()}"
        shutil.copyfile(p, dst)
        parts.append(f'<img src="assets/{dst.name}">')
    return '<div class="stack">' + "".join(parts) + "</div>"


def sub(a, n, cls=""):
    """Linha de apoio (ou vazio). {N1} -> spot; {c4} -> texto fixo do slide 4 (numbers.json)."""
    s = a["s"]
    if s is None:
        return ""
    if s == "{N1}":
        ex = Ex(n, a["lang"])
        return f'<p class="sub fit {cls}">{ex.s_n1()}</p>'
    if s == "{N7}":
        return f'<p class="sub fit {cls}">{n["N7"] if lib.has_text(n.get("N7")) else ph("N7")}</p>'
    if s.startswith("{t:"):
        key = s[3:-1]
        txt = (n.get("textos_com_numero") or {}).get(key)
        return f'<p class="sub fit {cls}">{txt if lib.has_text(txt) else ph(key)}</p>'
    return f'<p class="sub {cls}">{s}</p>'


def indicator(i):
    return f'<span class="indicator">{i} / {N_SLIDES}</span>'


def live_pill(label):
    """Selo de lancamento: pilula ambar com ponto (pulso congelado: halo estatico). Nunca 'Beta'."""
    return f'<span class="live"><i class="dot"></i>{label}</span>'


def floatcard(name, rot=-4):
    """Card real do app (captura) flutuando, levemente inclinado: a capa promete o produto."""
    p = find_print(name)
    if not p:
        return '<div class="slot" style="width:900px;height:300px"><div class="plab">[PRINT DE PRODUÇÃO PENDENTE]</div></div>'
    dst = ASSETS / f"prod-{name}{p.suffix.lower()}"
    shutil.copyfile(p, dst)
    return f'<div class="fcard" style="transform: rotate({rot}deg)"><div class="fglow"></div><img src="assets/{dst.name}"></div>'


ARCSVG = """<svg width="{s}" height="{s}" viewBox="0 0 220 220" fill="none"><circle cx="110" cy="110" r="104" stroke="rgba(212,164,24,0.7)" stroke-width="2" stroke-dasharray="460 190" stroke-linecap="round"/><circle cx="110" cy="110" r="88" stroke="rgba(212,164,24,0.22)" stroke-width="1.2"/></svg>"""


def render_html(name, n, miss, test=False):
    a = ART[name]
    lang, (w, h), k = a["lang"], a["size"], a["kind"]
    tag = draft_tag(miss, test)
    ts = a["ts"]
    txt = n.get("textos_com_numero") or {}
    base_css = f".title {{ font-size: {ts}px; line-height: 1.05; }}\n"
    ph_h = 438

    if k == "feed":
        css = base_css + ".page { padding-top: 64px; }\n.t { margin-top: 46px; }\n.mid { margin-top: 34px; display: flex; justify-content: center; }\n"
        svg, _ = chart_svg(lang, n, ph_h=ph_h)
        inner = lockup() + f"""
<div class="z t"><h1 class="title">{a['t']}</h1>{sub(a, n, 'sub-feed')}</div>
<div class="mid z">{svg}</div>
{footer()}"""
        return page(lang, h, inner, css, tag=tag)

    if k == "story":
        cover = a.get("cover")
        ph_story = 430 if lang == "pt" else 360
        if cover:
            ph_story = 300
        css = base_css + """.page { padding-top: 250px; padding-bottom: 262px; }
.blk { display: flex; flex-direction: column; }
.sub { margin-top: 24px; font-size: 52px; }
.sticker { margin-top: 30px; height: 120px; }
.pillrow { margin-top: 44px; display: flex; align-items: center; gap: 22px; }
.titlewrap { position: relative; }
.titlewrap::before { content: ""; position: absolute; left: -140px; top: -90px; width: 1000px; height: 520px; z-index: -1;
  background: radial-gradient(closest-side, rgba(251,191,36,.26), transparent); }
"""
        capt = txt.get(a["caption_key"]) if cover else None
        svg, _ = chart_svg(lang, n, ph_h=ph_story - (30 if capt else 0), emphasize=bool(cover), caption=capt)
        stick = ('<div class="sticker z">' + ('<div class="stickph">[STICKER DE LINK · Conhecer o Modo GTO / See GTO Mode]</div>' if tag else "") + "</div>")
        pill = f'<div class="pillrow z">{live_pill(a["live"])}</div>' if cover else ""
        inner = f"""<div class="blk z">{lockup()}</div>
{pill}
<div class="z titlewrap" style="margin-top:{30 if cover else 56}px"><h1 class="title">{a['t']}</h1>{sub(a, n)}</div>
<div class="mid z" style="margin-top:44px;display:flex;justify-content:center">{svg}</div>
{stick}
{footer()}"""
        return page(lang, h, inner, css, tag=tag, cls="drama" if cover else "")

    if k == "cover":
        css = base_css + """.page { padding-top: 56px; }
.pillrow { margin-top: 40px; display: flex; align-items: center; gap: 22px; }
.titlewrap { position: relative; margin-top: 26px; }
.titlewrap::before { content: ""; position: absolute; left: -160px; top: -110px; width: 1100px; height: 560px; z-index: -1;
  background: radial-gradient(closest-side, rgba(251,191,36,.30), transparent); }
.title { letter-spacing: -0.01em; }
.sub { font-size: 46px; margin-top: 26px; color: #fff; font-weight: 700; }
.fc { flex: 1; display: flex; align-items: center; justify-content: center; padding-bottom: 34px; }
"""
        inner = lockup(indicator(1)) + f"""
<div class="pillrow z">{live_pill("LIVE")}</div>
<div class="z titlewrap"><h1 class="title">{a['t']}</h1>{sub(a, n)}</div>
<div class="fc z">{floatcard("postflop-en", -4)}</div>
{footer()}"""
        return page(lang, h, inner, css, tag=tag, cls="drama")

    if k == "c2":
        css = base_css + ".t { margin-top: 40px; }\n.mid { flex: 1; display:flex; align-items:center; justify-content:center; padding-bottom: 8px; margin-top: 20px; }\n"
        svg, _ = chart_svg(lang, n, ph_h=370)
        inner = lockup(indicator(2)) + f"""
<div class="z t"><h1 class="title">{a['t']}</h1>{sub(a, n)}</div>
<div class="mid z">{svg}</div>
{footer()}"""
        return page(lang, h, inner, css, tag=tag)

    if k in ("c3", "c4"):
        i = 3 if k == "c3" else 4
        css = base_css + """.title { white-space: nowrap; }
.sub { font-size: 42px; }
.grp { flex: 1; display: flex; flex-direction: column; justify-content: center; gap: 70px; padding-bottom: 30px; }
.cap { position: relative; margin-left: -84px; margin-right: -84px; }
.cap .glow { position: absolute; left: 50%; top: 50%; width: 1100px; height: 560px; transform: translate(-50%, -50%);
  background: radial-gradient(closest-side, rgba(212,164,24,.20), transparent 100%); pointer-events: none; }
.micro { position: relative; z-index: 1; padding: 0 24px 16px; font-size: 28px; font-weight: 600; color: var(--ink-soft); letter-spacing: .02em; }
"""
        if k == "c3":
            capture = '<div class="micro">CO × BB · two-tone flop · any turn</div>' + stack(["second-barrel", "turn-delayed-cbet"])
        else:
            capture = slot("preflop-en", "", n)
        inner = lockup(indicator(i)) + f"""
<div class="grp z"><div><h1 class="title">{a['t']}</h1>{sub(a, n, 'fit')}</div>
<div class="cap"><div class="glow"></div>{capture}</div></div>
{footer()}"""
        return page(lang, h, inner, css, tag=tag)

    if k == "price":
        lead = txt.get("c5_titulo_en") or "[[c5_titulo_en]]"
        m = re.match(r"^\s*(US\$)\s*(\d+)\s*/\s*(\w+)", txt.get("c5_numero_en") or "")
        cur, num, per = m.groups() if m else ("US$", "[[c5_numero_en]]", "month")
        css = """.page { padding-top: 64px; }
.mid { flex: 1; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; position: relative; }
.rings { position: absolute; left: 50%; top: 40%; width: 1100px; height: 760px; transform: translate(-50%, -50%); z-index: 0; background: radial-gradient(closest-side, rgba(251,191,36,.30), rgba(251,191,36,.08) 55%, transparent); }
.lead { position: relative; z-index: 2; font-size: 78px; font-weight: 900; letter-spacing: .02em; text-transform: uppercase; color: #fff; }
.lead em { font-style: normal; color: #FBBF24; }
.title { position: relative; z-index: 2; margin-top: 6px; line-height: .9; display: flex; align-items: flex-start; justify-content: center; gap: 18px; }
.title .cur { font-size: 100px; font-weight: 900; margin-top: 44px; color: #fff; }
.title .num { font-size: 400px; font-weight: 900; line-height: .86; background: linear-gradient(180deg,#FCD34D 0%,#FBBF24 45%,#D97706 100%); -webkit-background-clip: text; background-clip: text; color: transparent; filter: drop-shadow(0 12px 40px rgba(245,158,11,.35)); }
.per { position: relative; z-index: 2; font-size: 74px; font-weight: 800; color: #fff; margin-top: 4px; letter-spacing: .02em; }
.sub { position: relative; z-index: 2; margin-top: 40px; font-size: 40px; width: 912px; color: var(--ink-soft); }
"""
        inner = lockup(indicator(5)) + f"""
<div class="mid z"><div class="rings"></div>
<div class="lead">{lead}</div>
<h1 class="title"><span class="cur">{cur}</span><span class="num">{num}</span></h1>
<div class="per">/{per}</div>
{sub(a, n)}</div>
{footer()}"""
        return page(lang, h, inner, css, tag=tag, cls="drama")

    if k == "cta":
        css = base_css + """.mid { flex: 1; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; }
.big { width: 190px; height: 142px; color: var(--gold); filter: drop-shadow(0 0 46px rgba(212,164,24,.5)); }
.big svg { width: 100%; height: 100%; }
.title { margin-top: 74px; display: inline-flex; align-items: center; gap: 26px; white-space: nowrap;
  background: linear-gradient(135deg, #FCD34D, #D97706); color: #0F1526; padding: 34px 72px; border-radius: 999px;
  box-shadow: 0 18px 60px rgba(245,158,11,.45), 0 0 0 10px rgba(251,191,36,.14); }
.sub { margin-top: 34px; font-size: 48px; }
"""
        arrow = '<svg width="54" height="54" viewBox="0 0 24 24" fill="none" stroke="#0F1526" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
        inner = lockup(indicator(6)) + f"""
<div class="mid z"><div style="position:relative;width:190px;height:142px;margin-top:10px"><div style="position:absolute;left:-40px;top:-62px">{ARCSVG.format(s=270)}</div><div class="big" data-icon></div></div>
<h1 class="title">{a['t']} {arrow}</h1>{sub(a, n)}</div>
{footer()}"""
        return page(lang, h, inner, css, tag=tag, cls="drama")
    raise SystemExit(f"tipo desconhecido: {k}")


# ---------------------------------------------------------------- main
def main():
    argv = sys.argv[1:]
    strict = "--strict" in argv
    test = "--layout-test" in argv
    only = None
    if "--only" in argv:
        only = argv[argv.index("--only") + 1].split(",")
    n = lib.load()
    ASSETS.mkdir(parents=True, exist_ok=True)
    out_dir = OUT / "_layout-test" if test else OUT
    out_dir.mkdir(parents=True, exist_ok=True)
    if not test:
        MIRROR.mkdir(parents=True, exist_ok=True)
    make_common_js()
    jobs, report = [], []
    for name, a in ART.items():
        if only and name not in only:
            continue
        miss = needs(name, n)
        draft = bool(miss) or test
        stem = name + ("-DRAFT" if draft else "") + ("-TESTE" if test else "")
        html = SRC / f"{stem}.html"
        html.write_text(render_html(name, n, miss, test), encoding="utf-8")
        png = out_dir / f"{stem}.png"
        # a versao oposta (DRAFT x final) da mesma arte sai de cena, para nao sobrar arquivo velho
        if not test:
            other = OUT / (f"{name}.png" if draft else f"{name}-DRAFT.png")
            other.unlink(missing_ok=True)
            (SRC / (f"{name}.html" if draft else f"{name}-DRAFT.html")).unlink(missing_ok=True)
            (MIRROR / other.name).unlink(missing_ok=True)
        jobs.append((html, png, a["size"], miss, draft))
    with sync_playwright() as p:
        b = p.chromium.launch()
        for html, png, (w, h), miss, draft in jobs:
            pg = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=1)
            pg.goto(html.as_uri())
            pg.evaluate("document.fonts.ready")
            pg.wait_for_timeout(300)
            pg.screenshot(path=str(png), clip={"x": 0, "y": 0, "width": w, "height": h})
            pg.close()
            if not test:
                shutil.copyfile(png, MIRROR / png.name)
            report.append((png.name, "DRAFT: falta " + ", ".join(miss) if miss else ("TESTE" if draft else "final")))
            print("ok", png.name, "->", report[-1][1])
        b.close()
    pend = [r for r in report if r[1] != "final"]
    print(f"\n{len(report) - len(pend)} final, {len(pend)} DRAFT")
    if strict and pend and not test:
        raise SystemExit("--strict: ainda ha arte em DRAFT")


if __name__ == "__main__":
    main()
