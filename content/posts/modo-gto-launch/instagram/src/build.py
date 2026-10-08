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
    "story-capa-pt": dict(lang="pt", size=(1080, 1920), kind="story", t="Onde o field<br><em>sai do GTO?</em>", s="Novo: Modo GTO", ts=104, emph=True),
    "carrossel-en-01": dict(lang="en", size=(1080, 1350), kind="c1", t="Where does<br>the field<br><em>leave GTO?</em>", s="New: GTO Mode", ts=88, emph=True),
    "carrossel-en-02": dict(lang="en", size=(1080, 1350), kind="c2", t="Same spot,<br><em>two numbers</em>", s="{N1}", ts=96),
    "carrossel-en-03": dict(lang="en", size=(1080, 1350), kind="c3", t="Postflop:<br><em>GTO and range</em>", s="SRP and 3-bet, flop and turn, with raise response.", ts=76),
    "carrossel-en-04": dict(lang="en", size=(1080, 1350), kind="c4", t="Preflop:<br><em>GTO and deviation</em>", s="{c4}", ts=76),
    "carrossel-en-05": dict(lang="en", size=(1080, 1350), kind="c5", t="GTO Mode is<br>a <em>paid plan</em>", s=None, ts=104),
    "carrossel-en-06": dict(lang="en", size=(1080, 1350), kind="c6", t="See <em>GTO Mode</em>", s="Link in bio.", ts=96),
}
N_SLIDES = 6

# ---------------------------------------------------------------- dependencias por arte
def needs(name, n):
    """Lista do que falta para a arte ser final (vazia = pronta)."""
    a = ART[name]
    ex = Ex(n, a["lang"])
    k = a["kind"]
    if k == "feed":
        return ex.missing(with_n1=True)
    if k in ("story", "c1", "c2"):
        return ex.missing(with_n1=True)
    if k == "c3":
        return [] if find_print("postflop-en") else ["print:postflop-en"]
    if k == "c4":
        return n5_missing(n) + ([] if find_print("preflop-en") else ["print:preflop-en"])
    return []


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


def page(lang, h, inner, css="", bg_arc=False, tag=""):
    return f"""<!DOCTYPE html>
<html lang="{lang}"><head><meta charset="UTF-8"><title>Aura Modo GTO</title>
<link rel="stylesheet" href="base.css"><style>{css}</style></head>
<body><div class="page h{h}">
<div class="suits" id="suits"></div>
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


def sub(a, n, cls=""):
    """Linha de apoio (ou vazio). {N1} -> spot; {c4} -> texto fixo do slide 4 (numbers.json)."""
    s = a["s"]
    if s is None:
        return ""
    if s == "{N1}":
        ex = Ex(n, a["lang"])
        return f'<p class="sub fit {cls}">{ex.s_n1()}</p>'
    if s == "{c4}":
        txt = (n.get("textos_com_numero") or {}).get("c4_apoio_en")
        return f'<p class="sub fit {cls}">{txt if lib.has_text(txt) else ph("c4_apoio_en")}</p>'
    return f'<p class="sub {cls}">{s}</p>'


def indicator(i):
    return f'<span class="indicator">{i} / {N_SLIDES}</span>'


def render_html(name, n, miss, test=False):
    a = ART[name]
    lang, (w, h), k = a["lang"], a["size"], a["kind"]
    tag = draft_tag(miss, test)
    ts = a["ts"]
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

    if k in ("story", "c1"):
        story = k == "story"
        ph_story = 430 if lang == "pt" else 360
        if story:
            css = base_css + """.page { padding-top: 250px; padding-bottom: 262px; }
.blk { display: flex; flex-direction: column; }
.sub { margin-top: 24px; font-size: 52px; }
.sticker { margin-top: 30px; height: 120px; }
"""
            cap = (Ex(n, lang).n1 or "[[N1]]") if name == "story-capa-pt" else None   # capa: o spot vira micro-legenda do grafico
            svg, _ = chart_svg(lang, n, ph_h=ph_story - (30 if cap else 0), emphasize=a.get("emph", False), caption=cap)
            stick = ('<div class="sticker z">' + ('<div class="stickph">[STICKER DE LINK · Conhecer o Modo GTO / See GTO Mode]</div>' if tag else "") + "</div>")
            inner = f"""<div class="blk z">{lockup()}</div>
<div class="z" style="margin-top:56px"><h1 class="title">{a['t']}</h1>{sub(a, n)}</div>
<div class="mid z" style="margin-top:44px;display:flex;justify-content:center">{svg}</div>
{stick}
{footer()}"""
            return page(lang, h, inner, css, tag=tag)
        css = base_css + ".t { margin-top: 44px; }\n.mid { margin-top: 28px; display:flex; justify-content:center; }\n.sub { font-size: 44px; }\n"
        ex = Ex(n, lang)
        svg, _ = chart_svg(lang, n, ph_h=300, emphasize=True, caption=ex.n1 or "[[N1]]")   # spot como micro-legenda do grafico; o apoio segue "New: GTO Mode"
        inner = lockup(indicator(1)) + f"""
<div class="z t"><h1 class="title">{a['t']}</h1>{sub(a, n)}</div>
<div class="mid z">{svg}</div>
{footer()}"""
        return page(lang, h, inner, css, tag=tag)

    if k == "c2":
        css = base_css + ".t { margin-top: 44px; }\n.mid { flex: 1; display:flex; align-items:center; justify-content:center; padding-bottom: 8px; margin-top: 26px; }\n"
        svg, _ = chart_svg(lang, n, ph_h=450)
        inner = lockup(indicator(2)) + f"""
<div class="z t"><h1 class="title">{a['t']}</h1>{sub(a, n)}</div>
<div class="mid z">{svg}</div>
{footer()}"""
        return page(lang, h, inner, css, tag=tag)

    if k in ("c3", "c4"):
        i = 3 if k == "c3" else 4
        pname = "postflop-en" if k == "c3" else "preflop-en"
        css = base_css + """.title { white-space: nowrap; }
.sub { font-size: 42px; }
.grp { flex: 1; display: flex; flex-direction: column; justify-content: center; gap: 90px; padding-bottom: 30px; }
.cap { position: relative; margin-left: -84px; margin-right: -84px; }
.cap .glow { position: absolute; left: 50%; top: 50%; width: 1100px; height: 560px; transform: translate(-50%, -50%);
  background: radial-gradient(closest-side, rgba(212,164,24,.20), transparent 100%); pointer-events: none; }
"""
        inner = lockup(indicator(i)) + f"""
<div class="grp z"><div><h1 class="title">{a['t']}</h1>{sub(a, n, 'fit')}</div>
<div class="cap"><div class="glow"></div>{slot(pname, '', n)}</div></div>
{footer()}"""
        return page(lang, h, inner, css, tag=tag)

    if k == "c5":
        css = base_css + """.mid { flex: 1; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; }
.title { margin-top: 56px; }
"""
        lock = """<div style="position:relative;width:260px;height:260px">
<svg style="position:absolute;inset:0" width="260" height="260" viewBox="0 0 220 220" fill="none"><circle cx="110" cy="110" r="104" stroke="rgba(212,164,24,0.7)" stroke-width="2.5" stroke-dasharray="460 190" stroke-linecap="round"/><circle cx="110" cy="110" r="88" stroke="rgba(212,164,24,0.2)" stroke-width="1.5"/></svg>
<svg style="position:absolute;left:70px;top:62px;filter:drop-shadow(0 0 30px rgba(212,164,24,.45))" width="120" height="136" viewBox="0 0 60 68" fill="none">
<path d="M16 30V21a14 14 0 0 1 28 0v9" stroke="#D4A418" stroke-width="5.5" stroke-linecap="round"/>
<rect x="6" y="29" width="48" height="36" rx="8" fill="#D4A418"/>
<circle cx="30" cy="44" r="5" fill="#0F1526"/><rect x="28" y="46" width="4" height="10" rx="2" fill="#0F1526"/></svg></div>"""
        inner = lockup(indicator(5)) + f"""
<div class="mid z">{lock}<h1 class="title">{a['t']}</h1></div>
{footer()}"""
        return page(lang, h, inner, css, tag=tag)

    if k == "c6":
        css = base_css + """.mid { flex: 1; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; }
.big { width: 150px; height: 112px; color: var(--gold); filter: drop-shadow(0 0 40px rgba(212,164,24,.45)); }
.big svg { width: 100%; height: 100%; }
.title { margin-top: 56px; white-space: nowrap; }
.sub { margin-top: 26px; font-size: 48px; }
"""
        inner = lockup(indicator(6)) + f"""
<div class="mid z"><div style="position:relative;width:150px;height:112px;margin-top:10px"><svg style="position:absolute;left:-35px;top:-54px" width="220" height="220" viewBox="0 0 220 220" fill="none"><circle cx="110" cy="110" r="104" stroke="rgba(212,164,24,0.7)" stroke-width="2.5" stroke-dasharray="460 190" stroke-linecap="round"/><circle cx="110" cy="110" r="88" stroke="rgba(212,164,24,0.2)" stroke-width="1.5"/></svg><div class="big" data-icon></div></div>
<h1 class="title">{a['t']}</h1>{sub(a, n)}</div>
{footer()}"""
        return page(lang, h, inner, css, bg_arc=False, tag=tag)
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
