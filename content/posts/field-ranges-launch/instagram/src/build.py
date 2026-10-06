"""Field Ranges - build das artes de lancamento.

1. recorta as capturas brutas (mockups/raw) -> src/assets
2. gera os HTMLs-fonte em src/
3. renderiza com Playwright (device_scale_factor=1) -> PNGs finais

Uso: python build.py
"""
import re
from pathlib import Path
from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[5]
POST = ROOT / "content/posts/field-ranges-launch"
SRC = POST / "instagram/src"
ASSETS = SRC / "assets"
OUT = POST / "instagram"
MOCK = POST / "mockups"
RAW = MOCK / "raw"
TPL = ROOT / "instagram/templates/carrossel-slide.html"

S = 1.44  # as capturas brutas sao 2880 px; as coordenadas abaixo estao em 2000 px


def crop(src, dst, box):
    im = Image.open(RAW / src).convert("RGB")
    x0, y0, x1, y1 = [round(v * S) for v in box]
    im.crop((x0, y0, x1, y1)).save(ASSETS / dst)


def lift_dim_labels(path):
    """Slide 2: so o rotulo das celulas sem massa (cinza apagado, ~2,4:1) sobe para ~7:1.
    O preenchimento das celulas nao muda. Geometria da grade: 13x13 do app, passo 55,6 px (capturas a 2000 px)."""
    import numpy as np
    a = np.asarray(Image.open(path).convert("RGB")).astype(float)
    bg = np.array([15, 23, 42.])
    txt0 = np.array([71, 85, 105.])
    tgt = np.array([148, 163, 184.])  # slate-400
    lum = lambda c: c @ np.array([0.2126, 0.7152, 0.0722])
    n = 0
    for j in range(13):
        for i in range(13):
            cx = round((255 + 55.6 * i - 196) * S)
            cy = round((744 + 55.55 * j - 684) * S)
            if np.abs(a[cy - 30, cx - 30] - bg).sum() > 6:   # nao e celula apagada
                continue
            box = a[cy - 18:cy + 18, cx - 32:cx + 32]
            al = np.clip((lum(box) - lum(bg)) / (lum(txt0) - lum(bg)), 0, 1.4)
            al = np.where(al < 0.08, 0, al)
            box[:] = bg + np.clip(al, 0, 1)[..., None] * (tgt - bg)
            n += 1
    Image.fromarray(a.round().astype("uint8")).save(path)
    print("celulas apagadas com rotulo realcado:", n)


def make_assets():
    for lang in ("pt", "en"):
        # titulo do spot + cartao da grade (sem o painel lateral com percentuais, sem a navegacao)
        crop(f"{lang}-01-grade-allin.png", f"{lang}-a-grade.png", (190, 610, 990, 1520))
        crop(f"{lang}-02-trilha-mesa.png", f"{lang}-b-trilha.png", (176, 160, 1824, 679))
        crop(f"{lang}-03a-bb-vs-ep.png", f"{lang}-c1.png", (190, 610, 990, 1520))
        crop(f"{lang}-03b-bb-vs-co.png", f"{lang}-c2.png", (190, 610, 990, 1520))
        # so o cartao da grade (para os slides)
        crop(f"{lang}-01-grade-allin.png", f"{lang}-card-allin.png", (196, 684, 981, 1513))
        crop(f"{lang}-03b-bb-vs-co.png", f"{lang}-card-bbco.png", (196, 684, 981, 1513))
        lift_dim_labels(ASSETS / f"{lang}-card-allin.png")


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
"""
    (SRC / "common.js").write_text(js, encoding="utf-8")


ARC = """<div class="arc" style="top:{top}px;left:50%;transform:translateX(-50%)">
<svg width="1500" height="1500" viewBox="0 0 1500 1500" fill="none">
<circle cx="750" cy="750" r="700" stroke="url(#g)" stroke-width="3.5" stroke-linecap="round" stroke-dasharray="3300 1099" transform="rotate({rot} 750 750)"/>
<circle cx="750" cy="750" r="656" stroke="rgba(212,164,24,0.16)" stroke-width="1.5" stroke-dasharray="2900 1221" transform="rotate({rot2} 750 750)"/>
<defs><linearGradient id="g" x1="0" y1="0" x2="1500" y2="1500"><stop offset="0" stop-color="#FCD34D"/><stop offset="0.5" stop-color="#D4A418"/><stop offset="1" stop-color="#7A5E0E"/></linearGradient></defs>
</svg></div>"""


def ring():
    return """<div class="arc" style="top:-110px;left:50%;transform:translateX(-50%)"><svg width="1000" height="1000" viewBox="0 0 1000 1000" fill="none">
<circle cx="500" cy="500" r="470" stroke="url(#g)" stroke-width="3" stroke-linecap="round" stroke-dasharray="2200 750"/>
<circle cx="500" cy="500" r="436" stroke="rgba(212,164,24,0.16)" stroke-width="1.5"/>
<defs><linearGradient id="g" x1="0" y1="0" x2="1000" y2="1000"><stop offset="0" stop-color="#FCD34D"/><stop offset="0.5" stop-color="#D4A418"/><stop offset="1" stop-color="#7A5E0E"/></linearGradient></defs></svg></div>"""


def page(lang, h, inner, css="", bg_arc=False, arc_top=-860):
    return f"""<!DOCTYPE html>
<html lang="{lang}"><head><meta charset="UTF-8"><title>Aura Field Ranges</title>
<link rel="stylesheet" href="base.css"><style>{css}</style></head>
<body><div class="page h{h}">
<div class="suits" id="suits"></div>
{ring() if bg_arc else ""}
<div class="vignette"></div>
{inner}
</div><script src="common.js"></script></body></html>"""


def lockup(right=""):
    return f"""<header><div class="lockup"><span class="icon" data-icon></span><span class="wm" data-wordmark></span></div>{right}</header>"""


def footer(T, kind="dec"):
    return f"""<footer><div class="f-left"><div class="handle"><span class="icon" data-icon></span><span>@aurapokeranalytics</span></div>
<div class="sample">{T['sample_' + kind]}</div></div><span class="age">18+</span></footer>"""


KICK = '<div class="kicker">Field Ranges</div>'

T = {
    "pt": {
        "sample_hands": "Dados: Aura · 96,4 mi de mãos com cartas conhecidas · 20bb+ · 18+",
        "sample_dec": "Dados: Aura · 1,42 bi de decisões · 20bb+ · 18+",
        "btn": "BTN", "ep": "EP", "v_btn": "56,9%", "v_ep": "39,0%",
        "feed_title": "ONDE O FIELD <em>JOGA DIFERENTE</em>",
        "feed_spot": "Contra 3-bet (não all-in)",
        "feed_l1": "BTN folda <b>56,9%</b>",
        "feed_l2": "EP folda <b>39,0%</b>",
        "feed_note": "Fold contra 3-bet não all-in",
        "st_quote1": "AA no BB contra open do CO:",
        "st_quote2": "o field só paga",
        "st_v": "13%",
        "st_x": "(84% dão 3-bet não all-in, 3% vão all-in)",
        "st_b1": "Veja a grade, mão a mão.",
        "st_b2": "Conta grátis",
        "s1_t": "COMO O FIELD<br><em>JOGA,</em><br>MÃO A MÃO",
        "s1_s": "Veja o que ele faz de verdade.",
        "s2_t": "UMA GRADE, <em>UM SPOT</em>",
        "s2_b": "13x13: cada célula é uma mão. A cor mostra o que o field faz: paga ou folda.",
        "s2_h": "CO abre, SB dá 3-bet all-in: veja a resposta do CO, mão a mão.",
        "s3_t": "SIGA A <em>MÃO</em>",
        "s3_b": "Open, 3-bet, 4-bet, all-in. Escolha as posições na mesa de 6 lugares e filtre por stack e buy-in.",
        "s3_h": "<b class='n'>90</b> situações com a grade pronta.",
        "s4_t": "ONDE <em>EXPLORAR</em>",
        "s4_b": "Contra 3-bet (não all-in), o BTN folda <b>56,9%</b>. O EP folda <b>39,0%</b>.",
        "s4_h": "BTN larga mais da metade: o seu 3-bet tende a ter mais fold equity. EP: mais critério.",
        "s4_x": "AA no BB contra open do CO: o field só paga <b>13%</b> (<b>84%</b> dão 3-bet não all-in, <b>3%</b> vão all-in).",
        "s4_n": "contra 3-bet não all-in",
        "s5_t": "A <em>BASE</em> POR TRÁS DA GRADE",
        "s5_b": "Leitura do field sobre <b>1,42 bi</b> de decisões pré-flop reais. Stacks de 20bb+, todos os buy&#8209;ins.",
        "s5_btn": "Conta grátis",
        "s5_n1": "1,42 bi", "s5_l1": "decisões pré-flop reais",
        "s6_t": "ABRA O <em>FIELD RANGES</em>",
        "s6_b": "Crie sua conta grátis e veja o seu próximo spot.",
        "s6_btn": "Link na bio",
        "trail": ["Open", "3-bet", "4-bet", "All-in"],
    },
    "en": {
        "sample_hands": "Data: Aura · 96.4M hands with known cards · 20bb+ · 18+",
        "sample_dec": "Data: Aura · 1.42B decisions · 20bb+ · 18+",
        "btn": "BTN", "ep": "EP", "v_btn": "56.9%", "v_ep": "39.0%",
        "feed_title": "WHERE THE FIELD <em>PLAYS DIFFERENTLY</em>",
        "feed_spot": "Facing a non-all-in 3-bet",
        "feed_l1": "BTN folds <b>56.9%</b>",
        "feed_l2": "EP folds <b>39.0%</b>",
        "feed_note": "Fold against non-all-in 3-bets",
        "st_quote1": "AA in the BB vs a CO open:",
        "st_quote2": "the field only calls",
        "st_v": "13%",
        "st_x": "(84% non-all-in 3-bet, 3% all-in)",
        "st_b1": "See the grid, hand by hand.",
        "st_b2": "Free account",
        "s1_t": "HOW THE FIELD<br><em>PLAYS,</em><br>HAND BY HAND",
        "s1_s": "See what it really does.",
        "s2_t": "ONE GRID, <em>ONE SPOT</em>",
        "s2_b": "13x13: each cell is a hand. Color shows what the field does: call or fold.",
        "s2_h": "CO opens, SB 3-bets all-in: see the CO's response, hand by hand.",
        "s3_t": "FOLLOW THE <em>HAND</em>",
        "s3_b": "Open, 3-bet, 4-bet, all-in. Pick positions on the 6-seat table and filter by stack and buy-in.",
        "s3_h": "<b class='n'>90</b> spots with the grid ready.",
        "s4_t": "WHERE TO <em>EXPLOIT</em>",
        "s4_b": "Facing a non-all-in 3-bet, the BTN folds <b>56.9%</b>. EP folds <b>39.0%</b>.",
        "s4_h": "BTN gives up more than half: your 3-bet tends to carry more fold equity. EP: more care.",
        "s4_x": "AA in the BB vs a CO open: the field only calls <b>13%</b> (<b>84%</b> non-all-in 3-bet, <b>3%</b> all-in).",
        "s4_n": "against non-all-in 3-bets",
        "s5_t": "THE <em>DATA</em> BEHIND THE GRID",
        "s5_b": "A read of the field over <b>1.42B</b> real preflop decisions. 20bb+ stacks, all buy&#8209;ins.",
        "s5_btn": "Free account",
        "s5_n1": "1.42B", "s5_l1": "real preflop decisions",
        "s6_t": "OPEN <em>FIELD RANGES</em>",
        "s6_b": "Create your free account and see your next spot.",
        "s6_btn": "Link in bio",
        "trail": ["Open", "3-bet", "4-bet", "All-in"],
    },
}


def bars(t):
    return f"""<div class="fl"><div class="fline">{t['btn']}</div></div>"""


# ---------------------------------------------------------------- FEED
def feed(lang):
    t = T[lang]
    css = """
.page { padding-top: 64px; }
.top { margin-top: 70px; }
.title { font-size: 92px; margin-top: 30px; }
.spot { margin-top: 48px; font-size: 40px; font-weight: 700; color: var(--amber); }
.rows { margin-top: 44px; display: flex; flex-direction: column; gap: 52px; }
.row .q { white-space: nowrap; }
.row .l { font-size: 56px; font-weight: 600; line-height: 1.2; color: var(--ink-soft); }
.row .l b { color: var(--amber); font-weight: 900; font-size: 78px; }
.row .fbar { height: 64px; margin-top: 26px; }
.note { margin-top: 36px; font-size: 28px; font-weight: 600; color: var(--ink-mute); letter-spacing: 0.04em; }
"""
    inner = lockup() + f"""
<div class="top z">{KICK}<h1 class="title">{t['feed_title']}</h1></div>
<div class="spot z">{t['feed_spot']}</div>
<div class="rows z">
  <div class="row"><div class="l">{t['feed_l1']}</div><div class="fbar"><i style="width:56.9%"></i></div></div>
  <div class="row"><div class="l">{t['feed_l2']}</div><div class="fbar"><i style="width:39.0%"></i></div></div>
</div>
{footer(t)}"""
    return page(lang, 1350, inner, css)


# ---------------------------------------------------------------- STORY
def story(lang):
    t = T[lang]
    css = """
.page { padding-top: 250px; padding-bottom: 210px; align-items: center; text-align: center; }
.lockup { justify-content: center; }
.kick { margin-top: 36px; display: flex; align-items: center; gap: 18px; justify-content: center; }
.kick .k { font-size: 27px; font-weight: 800; letter-spacing: 0.22em; color: var(--amber); text-transform: uppercase; }
.q1 { margin-top: 56px; font-size: 44px; font-weight: 700; color: #fff; }
.q2 { margin-top: 10px; font-size: 56px; font-weight: 800; color: var(--ink-soft); }
.q4 { font-size: 30px; font-weight: 600; color: var(--ink-soft); margin-top: -6px; }
.q3 { font-size: 190px; font-weight: 900; line-height: 1.02; letter-spacing: -0.02em; }
.shot { margin-top: 36px; width: 560px; flex: none; }
.b1 { margin-top: 44px; font-size: 42px; font-weight: 700; color: #fff; }
.pill { margin-top: 26px; display: inline-flex; align-items: center; gap: 16px; font-size: 32px; font-weight: 800; color: #0F1526;
  background: linear-gradient(135deg, var(--amber3), var(--amber6)); border-radius: 999px; padding: 18px 40px; box-shadow: 0 10px 34px rgba(245,158,11,.35); }
.sample { margin-top: 30px; text-align: center; font-size: 22px; max-width: 900px; }
.age { margin-top: 22px; }
"""
    inner = f"""
<div class="z">{lockup()}</div>
<div class="kick z"><span class="k">Field Ranges</span></div>
<div class="q1 z">{t['st_quote1']}</div>
<div class="q2 z">{t['st_quote2']}</div>
<div class="q3 z grad">{t['st_v']}</div>
<div class="q4 z">{t['st_x']}</div>
<div class="shot z"><img src="assets/{lang}-card-bbco.png"></div>
<div class="b1 z">{t['st_b1']}</div>
<div class="pill z">{t['st_b2']}
<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#0F1526" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></div>
<div class="sample z">{t['sample_hands']}</div><span class="age z">18+</span>"""
    return page(lang, 1920, inner, css)


# ---------------------------------------------------------------- CARROSSEL
def slide_head(n):
    return lockup(f'<span class="indicator">{n} / 6</span>')


def slide_title(t, key, size=70):
    return f"""<div class="z" style="margin-top:44px">{KICK}<h1 class="title" style="font-size:{size}px;margin-top:24px">{t[key]}</h1></div>"""


def carousel(lang, n):
    t = T[lang]
    css = ""
    if n == 1:
        css = """
.title { font-size: 84px !important; }
.sub { margin-top: 30px; font-size: 36px; font-weight: 500; line-height: 1.4; color: var(--ink-soft); max-width: 860px; }
.duo { margin-top: 36px; display: flex; gap: 28px; }
.duo .shot { flex: 1; border-radius: 22px; }
"""
        inner = slide_head(1) + f"""
<div class="z" style="margin-top:56px">{KICK}<h1 class="title" style="margin-top:26px">{t['s1_t']}</h1>
<p class="sub">{t['s1_s']}</p></div>
<div class="duo z"><div class="shot"><img src="assets/{lang}-c1.png"></div><div class="shot"><img src="assets/{lang}-c2.png"></div></div>
{footer(t)}"""
        return page(lang, 1350, inner, css)

    if n == 2:
        css = """
.shot { width: 540px; margin: 30px auto 0; }
.body { margin-top: 32px; } .hl { margin-top: 26px; }
.body p, .hl { font-size: 32px; }
"""
        inner = slide_head(2) + slide_title(t, "s2_t") + f"""
<div class="shot z"><img src="assets/{lang}-card-allin.png"></div>
<div class="body z"><p>{t['s2_b']}</p></div><div class="hl z">{t['s2_h']}</div>
{footer(t)}"""
        return page(lang, 1350, inner, css)

    if n == 3:
        css = """
.shot { margin-top: 48px; border-radius: 22px; }
.trail { margin-top: 44px; display: flex; align-items: center; gap: 14px; }
.trail span.c { font-size: 28px; font-weight: 800; letter-spacing: 0.08em; text-transform: uppercase; color: var(--amber); border: 2px solid rgba(251,191,36,.5); background: rgba(251,191,36,.08); border-radius: 999px; padding: 12px 24px; }
.trail span.a { color: var(--ink-mute); font-size: 30px; font-weight: 700; }
.body { margin-top: 44px; } .hl { margin-top: 52px; }
.hl .n { font-size: 84px; line-height: 1; vertical-align: -6px; margin-right: 6px; }
"""
        chips = '<span class="a">→</span>'.join(f'<span class="c">{x}</span>' for x in t["trail"])
        inner = slide_head(3) + slide_title(t, "s3_t") + f"""
<div class="shot z"><img src="assets/{lang}-b-trilha.png"></div>
<div class="trail z">{chips}</div>
<div class="body z"><p>{t['s3_b']}</p></div><div class="hl z">{t['s3_h']}</div>
{footer(t)}"""
        return page(lang, 1350, inner, css)

    if n == 4:
        css = """
.mid { flex: 1; display: flex; flex-direction: column; justify-content: center; gap: 64px; padding: 24px 0 36px; }
.body p { font-size: 38px; text-wrap: balance; }
.rows { display: flex; flex-direction: column; gap: 44px; }
.r { display: flex; align-items: center; gap: 24px; }
.r .nm { width: 128px; font-size: 44px; font-weight: 800; color: #fff; }
.r .fbar { flex: 1; margin-top: 0; height: 70px; }
.r .v { width: 230px; text-align: right; font-size: 68px; font-weight: 900; color: var(--amber); font-variant-numeric: tabular-nums; }
.hl { font-size: 38px; }
"""
        inner = slide_head(4) + slide_title(t, "s4_t") + f"""
<div class="mid z">
<div class="body"><p>{t['s4_b']}</p></div>
<div class="rows">
 <div class="r"><span class="nm">BTN</span><div class="fbar"><i style="width:56.9%"></i></div><span class="v">{t['v_btn']}</span></div>
 <div class="r"><span class="nm">EP</span><div class="fbar"><i style="width:39.0%"></i></div><span class="v">{t['v_ep']}</span></div>
</div>
<div class="hl">{t['s4_h']}</div>
</div>
{footer(t)}"""
        return page(lang, 1350, inner, css)

    if n == 5:
        css = """
.body { margin-top: 44px; }
.tile { margin-top: 56px; background: rgba(15,23,42,.85); border: 1.5px solid rgba(251,191,36,.3); border-radius: 28px; padding: 56px 48px; box-shadow: 0 30px 80px rgba(0,0,0,.5); text-align: center; }
.tile .n { font-size: 150px; font-weight: 900; line-height: 1; letter-spacing: -0.01em; }
.tile .l { margin-top: 22px; font-size: 38px; font-weight: 600; color: var(--ink-soft); }
.btnwrap { margin-top: 56px; text-align: center; }
.btn { display: inline-block; font-size: 40px; font-weight: 900; letter-spacing: 0.04em; color: #0F1526; background: linear-gradient(135deg, var(--amber3), var(--amber6)); border-radius: 999px; padding: 26px 66px; box-shadow: 0 16px 50px rgba(245,158,11,.4); }
"""
        inner = slide_head(5) + slide_title(t, "s5_t", 78) + f"""
<div class="body z"><p>{t['s5_b']}</p></div>
<div class="tile z"><div class="n grad">{t['s5_n1']}</div><div class="l">{t['s5_l1']}</div></div>
<div class="btnwrap z"><span class="btn">{t['s5_btn']}</span></div>
{footer(t)}"""
        return page(lang, 1350, inner, css)

    if n == 6:
        css = """
.mid { flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; }
.big { width: 130px; height: 98px; color: var(--gold); filter: drop-shadow(0 0 40px rgba(212,164,24,.45)); }
.big svg { width: 100%; height: 100%; }
.title { font-size: 86px !important; margin-top: 44px; }
.body { margin-top: 30px; max-width: 800px; }
.btn { margin-top: 56px; font-size: 40px; font-weight: 900; letter-spacing: 0.04em; color: #0F1526; background: linear-gradient(135deg, var(--amber3), var(--amber6)); border-radius: 999px; padding: 28px 70px; box-shadow: 0 16px 50px rgba(245,158,11,.4); }
"""
        inner = slide_head(6) + f"""
<div class="mid z"><div style="position:relative;width:130px;height:98px;margin-top:20px"><svg style="position:absolute;left:-45px;top:-61px" width="220" height="220" viewBox="0 0 220 220" fill="none"><circle cx="110" cy="110" r="104" stroke="rgba(212,164,24,0.7)" stroke-width="2.5" stroke-dasharray="460 190" stroke-linecap="round"/><circle cx="110" cy="110" r="88" stroke="rgba(212,164,24,0.2)" stroke-width="1.5"/></svg><div class="big" data-icon></div></div>{KICK.replace('<div','<div style="margin-top:96px"')}
<h1 class="title">{t['s6_t']}</h1><div class="body"><p>{t['s6_b']}</p></div><div class="btn">{t['s6_btn']}</div></div>
{footer(t)}"""
        return page(lang, 1350, inner, css)


# ---------------------------------------------------------------- MOCKUPS
MCSS = """
html, body { width: auto; background: transparent; }
#wrap { display: inline-flex; gap: 56px; padding: 80px; background: transparent; }
.f { border-radius: 30px; overflow: hidden; background: #020617; border: 2px solid rgba(251,191,36,.3);
  box-shadow: 0 34px 90px rgba(0,0,0,.6), 0 0 50px rgba(212,164,24,.12); }
.f img { display: block; }
"""


def mock_html(imgs):
    tags = "".join(f'<div class="f"><img src="assets/{i}"></div>' for i in imgs)
    return f'<!DOCTYPE html><html><head><meta charset="UTF-8"><style>{MCSS}</style></head><body><div id="wrap">{tags}</div></body></html>'


def main():
    ASSETS.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(exist_ok=True)
    MOCK.mkdir(exist_ok=True)
    make_assets()
    make_common_js()
    jobs = []  # (html, png, w, h or None, transparent)
    for lang in ("pt", "en"):
        jobs.append((f"feed-{lang}.html", OUT / f"feed-{lang}.png", 1080, 1350))
        (SRC / f"feed-{lang}.html").write_text(feed(lang), encoding="utf-8")
        jobs.append((f"story-{lang}.html", OUT / f"story-{lang}.png", 1080, 1920))
        (SRC / f"story-{lang}.html").write_text(story(lang), encoding="utf-8")
        for n in range(1, 7):
            (SRC / f"carrossel-{lang}-{n:02d}.html").write_text(carousel(lang, n), encoding="utf-8")
            jobs.append((f"carrossel-{lang}-{n:02d}.html", OUT / f"carrossel-{lang}-{n:02d}.png", 1080, 1350))
        for name, imgs in (("grade-allin", [f"{lang}-a-grade.png"]), ("trilha-mesa", [f"{lang}-b-trilha.png"]),
                           ("contraste", [f"{lang}-c1.png", f"{lang}-c2.png"])):
            (SRC / f"mockup-{name}-{lang}.html").write_text(mock_html(imgs), encoding="utf-8")
            jobs.append((f"mockup-{name}-{lang}.html", MOCK / f"{name}-{lang}.png", None, None))
    with sync_playwright() as p:
        b = p.chromium.launch()
        for html, png, w, h in jobs:
            if w:
                pg = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=1)
                pg.goto((SRC / html).as_uri())
                pg.evaluate("document.fonts.ready")
                pg.wait_for_timeout(250)
                pg.screenshot(path=str(png), clip={"x": 0, "y": 0, "width": w, "height": h})
            else:
                pg = b.new_page(viewport={"width": 2800, "height": 1600}, device_scale_factor=1)
                pg.goto((SRC / html).as_uri())
                pg.evaluate("document.fonts.ready")
                pg.wait_for_timeout(150)
                pg.locator("#wrap").screenshot(path=str(png), omit_background=True)
            pg.close()
            print("ok", png.name)
        b.close()


if __name__ == "__main__":
    main()
