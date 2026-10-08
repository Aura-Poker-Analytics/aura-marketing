"""Field Trends - build das artes de lancamento (mesmo pipeline do Field Ranges).

1. recorta as capturas brutas (mockups/raw) -> src/assets
2. gera os HTMLs-fonte em src/
3. renderiza com Playwright (device_scale_factor=1) -> PNGs finais

Uso: python build.py   (depois: python build_email.py)

Textos: exatamente os de content/posts/field-trends-launch/copy.md. Numeros: aura-main/_ops/field-trends-launch/numeros-verificados.md.
"""
import re
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[5]
POST = ROOT / "content/posts/field-trends-launch"
SRC = POST / "instagram/src"
ASSETS = SRC / "assets"
OUT = POST / "instagram"
MOCK = POST / "mockups"
RAW = MOCK / "raw"
TPL = ROOT / "instagram/templates/carrossel-slide.html"

# ---------------------------------------------------------------- capturas
# Cards: 5 cartoes de 334x244 px dentro de ft-*-cards.png (1800x700), borda de 2 px, raio ~24 px.
CARD_X = [(16, 350), (374, 708), (732, 1068), (1092, 1426), (1450, 1784)]
CARD_H0 = 244                      # altura do card; o topo e detectado por idioma (PT 454, EN 482 na captura de 07/10)
CARD_R = 24
# A serie: ft-*-serie.png (1772x748). Dentro da moldura do app (2 px de borda); sem a linha "Ver a reacao".
CHART_BOX = (4, 4, 1766, 636)   # no quadro alinhado (linha Total em y=372)

BG_APP = np.array([2, 6, 22.0])
BAND_OLD = np.array([19, 25, 41.0])   # faixa de variacao normal como o app a pinta (1,1:1 contra o fundo)
BAND_NEW = np.array([46, 60, 82.0])   # mesma faixa, mesma geometria, so mais clara para ser vista no celular


# DECISAO (coordenacao + design, 07/10): o app pinta a faixa de variacao normal quase invisivel no celular.
# Nas artes e no e-mail a faixa e clareada SO EM COR (19,25,41 -> 46,60,82); geometria, pontos, linhas e numeros
# ficam identicos. Os mockups/ finais usam a captura crua, sem este realce. Para desligar, tire a chamada de lift_band
# em make_assets().
def lift_band(im, y0=340, y1=400):
    """A faixa de variacao normal do app e quase invisivel (19,25,41 sobre 2,6,22). Aqui so a COR do preenchimento
    sobe para 46,60,82; forma, posicao e pontos da faixa nao mudam. Mockups finais (mockups/) usam a captura crua."""
    a = np.asarray(im.convert("RGB")).astype(float)
    reg = a[y0:y1].copy()
    d = BAND_OLD - BG_APP
    rel = reg - BG_APP
    t = (rel @ d) / (d @ d)
    res = np.linalg.norm(rel - t[..., None] * d, axis=-1)
    m1 = (res < 8) & (t > 0.1) & (t < 1.15)
    out = reg.copy()
    out[m1] = BG_APP + t[m1][..., None] * (BAND_NEW - BG_APP)
    # linha Total e pontos (cinza claro) sobre a faixa: o antialias leva a cor da faixa nova
    neutral = (np.abs(reg[..., 0] - reg[..., 2]) < 40) & (reg[..., 2] > 60)
    bandcol = m1 & (t > 0.9)
    near = np.zeros_like(bandcol)
    for s in range(-4, 5):
        near |= np.roll(bandcol, s, axis=0)
    m2 = neutral & near & ~m1
    al = np.clip((reg[..., 2] - 41) / (225 - 41), 0, 1)
    out[m2] = reg[m2] + (BAND_NEW - BAND_OLD) * (1 - al[m2])[..., None]
    a[y0:y1] = out
    return Image.fromarray(a.round().clip(0, 255).astype("uint8"))


def card_top(cards_im):
    """Topo (borda cinza 30,41,59) do primeiro card, por idioma: as capturas de PT e EN nao tem o mesmo deslocamento vertical."""
    a = np.asarray(cards_im.convert("RGB"))
    for y in range(380, 560):
        if tuple(a[y, 100]) == (30, 41, 59):
            return y
    raise SystemExit("topo dos cards nao encontrado")


def align_serie(im, ref=372):
    """Leva a linha Total (203,213,225) para y=ref, preenchendo com o fundo do app: a captura PT veio rolada para cima."""
    a = np.asarray(im.convert("RGB"))
    ty = next(y for y in range(a.shape[0]) if tuple(a[y, 600]) == (203, 213, 225))
    dy = ref - ty
    out = Image.new("RGB", im.size, (2, 6, 22))
    out.paste(im, (0, dy))
    return out


def rounded_rgba(im, r):
    """Cartao com cantos transparentes (mascara com antialias a 4x)."""
    im = im.convert("RGBA")
    k = 4
    m = Image.new("L", (im.width * k, im.height * k), 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, im.width * k - 1, im.height * k - 1), radius=r * k, fill=255)
    im.putalpha(m.resize(im.size, Image.LANCZOS))
    return im


def make_assets():
    for lang in ("pt", "en"):
        cards = Image.open(RAW / f"ft-{lang}-cards.png").convert("RGB")
        serie = align_serie(Image.open(RAW / f"ft-{lang}-serie.png").convert("RGB"))
        y0 = card_top(cards)
        for i, (x0, x1) in enumerate(CARD_X, 1):
            rounded_rgba(cards.crop((x0, y0, x1, y0 + CARD_H0)), CARD_R).save(ASSETS / f"{lang}-card{i}.png")
        ch = lift_band(serie).crop(CHART_BOX)
        px = ch.load()
        for cx in (0, ch.width - 30):          # sobras da curva da moldura do app nos cantos de cima: nada do conteudo mora ali
            for yy in range(0, 30):
                for xx in range(cx, cx + 30):
                    px[xx, yy] = (2, 6, 22)
        ch.save(ASSETS / f"{lang}-chart.png")
        # mockups finais: capturas cruas (so enquadradas e, na serie, alinhadas)
        cards.crop((0, y0 - 100, 1800, y0 + 252)).save(ASSETS / f"{lang}-mock-cards.png")
        serie.crop((2, 2, 1770, 728)).save(ASSETS / f"{lang}-mock-serie.png")


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


def ring():
    return """<div class="arc" style="top:-110px;left:50%;transform:translateX(-50%)"><svg width="1000" height="1000" viewBox="0 0 1000 1000" fill="none">
<circle cx="500" cy="500" r="470" stroke="url(#g)" stroke-width="3" stroke-linecap="round" stroke-dasharray="2200 750"/>
<circle cx="500" cy="500" r="436" stroke="rgba(212,164,24,0.16)" stroke-width="1.5"/>
<defs><linearGradient id="g" x1="0" y1="0" x2="1000" y2="1000"><stop offset="0" stop-color="#FCD34D"/><stop offset="0.5" stop-color="#D4A418"/><stop offset="1" stop-color="#7A5E0E"/></linearGradient></defs></svg></div>"""


def page(lang, h, inner, css="", bg_arc=False):
    return f"""<!DOCTYPE html>
<html lang="{lang}"><head><meta charset="UTF-8"><title>Aura Field Trends</title>
<link rel="stylesheet" href="base.css"><style>{css}</style></head>
<body><div class="page h{h}">
<div class="suits" id="suits"></div>
{ring() if bg_arc else ""}
<div class="vignette"></div>
{inner}
</div><script src="common.js"></script></body></html>"""


def lockup(right=""):
    return f"""<header><div class="lockup"><span class="icon" data-icon></span><span class="wm" data-wordmark></span></div>{right}</header>"""


def footer(T):
    return f"""<footer><div class="f-left"><div class="handle"><span class="icon" data-icon></span><span>@aurapokeranalytics</span></div>
<div class="sample">{T['sample']}</div></div><span class="age">18+</span></footer>"""


KICK = '<div class="kicker">Field Trends</div>'


# Selo de lancamento ("NOVO MODULO" / "NEW MODULE"): pilula ambar + kicker. Nunca "Beta".
NEWCSS = """
.krow { display: flex; align-items: center; gap: 22px; }
.krow.c { justify-content: center; }
.newpill { flex: none; font-size: 31px; font-weight: 900; letter-spacing: 0.1em; text-transform: uppercase; color: #0F1526;
  background: linear-gradient(135deg, var(--amber3), var(--amber6)); border-radius: 999px; padding: 13px 30px; box-shadow: 0 8px 30px rgba(245,158,11,.35); }
.krow .kicker { font-size: 27px; }
.krow .kicker::before { display: none; }
"""


def kickrow(t, center=False):
    c = " c" if center else ""
    return f'<div class="krow{c}"><span class="newpill">{t["new"]}</span>{KICK}</div>'

T = {
    "pt": {
        "new": "NOVO MÓDULO",
        "feed_cta": "Já na Aura · conta grátis, link na bio",
        "sample": "Dados: Aura · 11 trimestres, até o 2T26 (em curso) · 18+",
        "period": "2T25 → 2T26 (em curso)",
        "ccap": "Variação em 1 ano <span class=\"nw\">(2T26 em curso)</span>",
        "band": "faixa de variação normal",
        "cap": "Gráfico: C-bet no flop (IP) %, com a sua faixa de variação normal",
        # feed
        "feed_title": "O FIELD MUDOU.<br><em>O SEU EXPLOIT<br>AINDA VALE?</em>",
        "feed_size": 82,
        "feed_spot": "Field contra c-bet IP no flop",
        "feed_l1": "Fold to c-bet IP:",
        "feed_v1": "43,62%", "feed_v2": "44,99%",
        "d_delta": "+1,36 pp", "d_band": "± 0,77 pp",
        # story
        "st_q1": "Fold to c-bet IP no flop:",
        "st_q2": "Mudança real ou variação normal?",
        "st_period": "(2T25 → 2T26, em curso)",
        "st_b1": "<b>+1,36 pp</b>, acima da faixa de <span class=\"nw\"><b>± 0,77 pp</b></span>: é mudança real.",
        "st_b2": "Veja uma stat de graça.",
        "st_btn": "Conta grátis",
        # carrossel
        "s1_t": "O FIELD MUDOU.<br><em>E O SEU EXPLOIT?</em>",
        "s1_size": 88,
        "s1_s": "Acompanhe o field, trimestre a trimestre.",
        "s2_t": "STAT <em>POR STAT</em>",
        "s2_b": "<b>114</b> stats do pós-flop: c-bet, fold to c-bet, donk, probe e mais, trimestre a trimestre.",
        "s2_h": "Só o c-bet IP no flop soma <b>75,7 milhões</b> de mãos <small>(a soma inclui o 2T26, em curso)</small>.",
        "s3_t": "SÓ O QUE MUDOU<br><em>DE VERDADE</em>",
        "s3_b": "No último ano, <b>23</b> das <b>114</b> stats tiveram variação significativa.",
        "s3_h": "Menos stat para olhar, mais tempo de estudo.",
        "s4_t": "REAL OU<br><em>VARIAÇÃO NORMAL?</em>",
        "s4_b": "Cada stat traz a faixa de variação normal do próprio field. Dentro da faixa, é oscilação. Fora, o field mudou.",
        "s4_h": "Fold to c-bet IP: <b>+1,36 pp</b>. Faixa: <b>± 0,77 pp</b>. Mudança real.",
        "s5_t": "O QUE FAZER <em>COM ISSO</em>",
        "s5_b": "O fold to c-bet IP foi de <b>43,62%</b> para <b>44,99%</b> <small>(2T26 em curso)</small>, e o call caiu de <b>42,99%</b> para <b>41,84%</b> <small>(2T26 em curso)</small>. O field folda um pouco mais e paga um pouco menos.",
        "s5_h": "Em média, o c-bet de bluff IP tem um pouco mais de fold equity. Confira no seu spot.",
        "s5_m": "Filtre por buy-in e stack <span class=\"nw\">(planos pagos)</span> e confira no field do seu jogo.",
        "s6_t": "ABRA O<br><em>FIELD TRENDS</em>",
        "s6_b": "Crie sua conta grátis e abra o Field Trends.",
        "s6_btn": "Link na bio",
    },
    "en": {
        "new": "NEW MODULE",
        "feed_cta": "Now on Aura · free account, link in bio",
        "sample": "Data: Aura · 11 quarters, through 2Q26 (in progress) · 18+",
        "period": "2Q25 → 2Q26 (in progress)",
        "ccap": "Change over 1 year <span class=\"nw\">(2Q26 in progress)</span>",
        "band": "normal variation band",
        "cap": "Chart: IP flop c-bet %, with its normal variation band",
        "feed_title": "THE FIELD CHANGED.<br><em>DOES YOUR EXPLOIT STILL HOLD?</em>",
        "feed_size": 76,
        "feed_spot": "Field vs IP flop c-bet",
        "feed_l1": "Fold to c-bet IP:",
        "feed_v1": "43.62%", "feed_v2": "44.99%",
        "d_delta": "+1.36 pp", "d_band": "± 0.77 pp",
        "st_q1": "IP flop fold to c-bet:",
        "st_q2": "Real change or normal variation?",
        "st_period": "(2Q25 → 2Q26, in progress)",
        "st_b1": "<b>+1.36 pp</b>, above the <span class=\"nw\"><b>± 0.77 pp</b></span> band: it is a real change.",
        "st_b2": "See one stat for free.",
        "st_btn": "Free account",
        "s1_t": "THE FIELD CHANGED.<br><em>WHAT ABOUT YOUR EXPLOIT?</em>",
        "s1_size": 76,
        "s1_s": "Follow the field, quarter by quarter.",
        "s2_t": "STAT <em>BY STAT</em>",
        "s2_b": "<b>114</b> postflop stats: c-bet, fold to c-bet, donk, probe and more, quarter by quarter.",
        "s2_h": "The IP flop c-bet alone adds up to <b>75.7 million</b> hands <small>(the sum includes 2Q26, in progress)</small>.",
        "s3_t": "ONLY WHAT<br><em>REALLY CHANGED</em>",
        "s3_b": "Over the past year, <b>23</b> of the <b>114</b> stats had a significant change.",
        "s3_h": "Fewer stats to scan, more time to study.",
        "s4_t": "REAL OR<br><em>NORMAL VARIATION?</em>",
        "s4_b": "Every stat carries the normal variation band of its own field. Inside the band, it is drift. Outside, the field changed.",
        "s4_h": "IP fold to c-bet: <b>+1.36 pp</b>. Band: <b>± 0.77 pp</b>. A real change.",
        "s5_t": "WHAT TO DO <em>WITH IT</em>",
        "s5_b": "IP fold to c-bet went from <b>43.62%</b> to <b>44.99%</b> <small>(2Q26 in progress)</small>, and the call dropped from <b>42.99%</b> to <b>41.84%</b> <small>(2Q26 in progress)</small>. The field folds a little more and calls a little less.",
        "s5_h": "On average, the IP bluff c-bet has a little more fold equity. Check it in your own spot.",
        "s5_m": "Filter by buy-in and stack <span class=\"nw\">(paid plans)</span> and check the field you actually play.",
        "s6_t": "OPEN<br><em>FIELD TRENDS</em>",
        "s6_b": "Create your free account and open Field Trends.",
        "s6_btn": "Link in bio",
    },
}


def diagram(t, width=912, height=222):
    """Variacao x faixa. So usa os dois numeros do copy: faixa de +/-0,77 pp e variacao de +1,36 pp, em escala (px por pp)."""
    k = 410.0           # px por pp
    x0 = 20 + 0.77 * k  # origem da variacao = centro da faixa
    xb0, xb1 = x0 - 0.77 * k, x0 + 0.77 * k
    xe = x0 + 1.36 * k
    cy = 108
    return f"""<svg class="diag" width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none">
<rect x="{xb0:.1f}" y="{cy - 46}" width="{xb1 - xb0:.1f}" height="92" rx="16" fill="rgba(148,163,184,.28)" stroke="rgba(203,213,225,.6)" stroke-width="2.5" stroke-dasharray="9 7"/>
<line x1="{x0:.1f}" y1="{cy - 62}" x2="{x0:.1f}" y2="{cy + 62}" stroke="#94A3B8" stroke-width="3"/>
<line x1="{x0:.1f}" y1="{cy}" x2="{xe - 30:.1f}" y2="{cy}" stroke="#FBBF24" stroke-width="13" stroke-linecap="round"/>
<path d="M{xe - 44:.1f} {cy - 30} L{xe:.1f} {cy} L{xe - 44:.1f} {cy + 30} Z" fill="#FBBF24"/>
<text x="{(xb0 + xb1) / 2:.1f}" y="{cy + 104}" text-anchor="middle" font-family="Montserrat" font-weight="700" font-size="40" fill="#CBD5E1">{t['d_band']}</text>
<text x="{xe:.1f}" y="{cy - 56}" text-anchor="end" font-family="Montserrat" font-weight="900" font-size="46" fill="#FBBF24">{t['d_delta']}</text>
</svg>"""


def img(lang, name):
    return f'<img src="assets/{lang}-{name}.png">'


# ---------------------------------------------------------------- FEED
def feed(lang):
    t = T[lang]
    css = f"""
.page {{ padding-top: 64px; }}
.title {{ font-size: {t['feed_size']}px; margin-top: 22px; line-height: 1.06; }}
.mid {{ flex: 1; display: flex; flex-direction: column; justify-content: center; gap: 0; padding: 20px 0 34px; }}
.spot {{ font-size: 40px; font-weight: 700; color: var(--amber); }}
.l1 {{ margin-top: 30px; font-size: 44px; font-weight: 600; color: var(--ink-soft); }}
.nums {{ display: flex; align-items: baseline; gap: 20px; margin-top: 2px; }}
.nums .v {{ font-size: 106px; font-weight: 900; line-height: 1.05; letter-spacing: -0.02em; color: #fff; }}
.nums .v.b {{ background: linear-gradient(180deg, var(--amber3) 0%, var(--amber) 45%, var(--amber6) 100%); -webkit-background-clip: text; background-clip: text; color: transparent; }}
.nums .ar {{ font-size: 62px; font-weight: 700; color: var(--ink-mute); }}
.period {{ font-size: 32px; font-weight: 600; color: var(--ink-mute); margin-top: 2px; }}
.diag {{ display: block; margin-top: 30px; }}
.cta {{ margin-bottom: 26px; font-size: 38px; font-weight: 800; color: var(--amber); }}
"""
    css += NEWCSS
    inner = lockup() + f"""
<div class="z" style="margin-top:34px">{kickrow(t)}<h1 class="title">{t['feed_title']}</h1></div>
<div class="mid z">
<div class="spot">{t['feed_spot']}</div>
<div class="l1">{t['feed_l1']}</div>
<div class="nums"><span class="v">{t['feed_v1']}</span><span class="ar">→</span><span class="v b">{t['feed_v2']}</span></div>
<div class="period">{t['period']}</div>
{diagram(t)}
</div>
<div class="cta z">{t['feed_cta']}</div>
{footer(t)}"""
    return page(lang, 1350, inner, css)


# ---------------------------------------------------------------- STORY
def story(lang):
    t = T[lang]
    css = """
.page { padding-top: 250px; padding-bottom: 340px; align-items: center; text-align: center; justify-content: space-between; }
.blk { display: flex; flex-direction: column; align-items: center; }
.lockup { justify-content: center; }
.kick { margin-top: 30px; font-size: 30px; font-weight: 800; letter-spacing: 0.22em; color: var(--amber); text-transform: uppercase; }
.q1 { font-size: 48px; font-weight: 700; color: #fff; }
.nums { display: flex; align-items: baseline; justify-content: center; gap: 20px; margin-top: 6px; }
.nums .v { font-size: 106px; font-weight: 900; line-height: 1.05; letter-spacing: -0.02em; color: #fff; }
.nums .v.b { background: linear-gradient(180deg, var(--amber3) 0%, var(--amber) 45%, var(--amber6) 100%); -webkit-background-clip: text; background-clip: text; color: transparent; }
.nums .ar { font-size: 60px; font-weight: 700; color: var(--ink-mute); }
.q2 { margin-top: 34px; font-size: 58px; font-weight: 800; line-height: 1.2; color: var(--ink-soft); max-width: 880px; text-wrap: balance; }
.per { margin-top: 18px; font-size: 34px; font-weight: 600; color: var(--ink-mute); }
.diag { display: block; }
.b2 { margin-top: 26px; font-size: 40px; font-weight: 700; color: #fff; }
.pill { display: inline-flex; align-items: center; gap: 16px; font-size: 38px; font-weight: 800; color: #0F1526;
  background: linear-gradient(135deg, var(--amber3), var(--amber6)); border-radius: 999px; padding: 24px 52px; box-shadow: 0 10px 34px rgba(245,158,11,.35); }
.sample { margin-top: 26px; text-align: center; max-width: 900px; }
.age { margin-top: 14px; }
""" + NEWCSS + """
.newpill { font-size: 36px; padding: 16px 36px; }
.krow .kicker { font-size: 30px; }
"""
    inner = f"""
<div class="blk z">{lockup()}<div style="margin-top:34px">{kickrow(t, True)}</div></div>
<div class="blk z"><div class="q1">{t['st_q1']}</div>
<div class="nums"><span class="v">{t['feed_v1']}</span><span class="ar">→</span><span class="v b">{t['feed_v2']}</span></div>
<div class="q2">{t['st_q2']}</div><div class="per">{t['st_period']}</div></div>
<div class="blk z">{diagram(t)}<div class="b2">{t['st_b2']}</div></div>
<div class="blk z"><div class="pill">{t['st_btn']}
<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#0F1526" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></div>
<div class="sample">{t['sample']}</div><span class="age">18+</span></div>"""
    return page(lang, 1920, inner, css)


# ---------------------------------------------------------------- CARROSSEL
def slide_head(n):
    return lockup(f'<span class="indicator">{n} / 6</span>')


def slide_title(t, key, size=70):
    return f"""<div class="z" style="margin-top:40px">{KICK}<h1 class="title" style="font-size:{size}px;margin-top:22px">{t[key]}</h1></div>"""


CARDCSS = """
.cards { display: flex; flex-wrap: wrap; gap: 24px; justify-content: center; }
.cards img { display: block; width: 288px; height: auto; filter: drop-shadow(0 18px 34px rgba(0,0,0,.55)); }
"""


BLEED = """
.shot { margin-left: -84px; margin-right: -84px; width: 1080px; border-radius: 0; border-left: 0; border-right: 0; }
"""


def carousel(lang, n):
    t = T[lang]
    css = ""
    if n == 1:
        css = CARDCSS + """
.mid { flex: 1; display: flex; flex-direction: column; justify-content: center; padding-bottom: 30px; }
.sub { margin-top: 30px; font-size: 40px; font-weight: 500; line-height: 1.4; color: var(--ink-soft); max-width: 860px; }
.cards { margin-top: 56px; gap: 32px; flex-wrap: nowrap; }
.cards img { width: 440px; }
.ccap { margin-top: 18px; text-align: center; font-size: 28px; font-weight: 600; color: var(--ink-soft); }
""" + NEWCSS + """
.newpill { font-size: 34px; padding: 15px 34px; }
"""
        inner = slide_head(1) + f"""
<div class="mid z"><div>{kickrow(t)}<h1 class="title" style="margin-top:30px;font-size:{t['s1_size']}px;line-height:1.08">{t['s1_t']}</h1>
<p class="sub">{t['s1_s']}</p></div>
<div class="cards">{img(lang, 'card1')}{img(lang, 'card3')}</div>
<div class="ccap">{t['ccap']}</div></div>
{footer(t)}"""
        return page(lang, 1350, inner, css)

    if n == 2:
        css = BLEED + """
.mid { flex: 1; display: flex; flex-direction: column; justify-content: center; padding: 24px 0 40px; }
.body { margin-top: 40px; } .hl { margin-top: 32px; }
.body p { font-size: 38px; } .hl { font-size: 40px; }
"""
        inner = slide_head(2) + slide_title(t, "s2_t") + f"""
<div class="mid z"><div class="shot">{img(lang, 'chart')}</div>
<div class="body"><p>{t['s2_b']}</p></div><div class="hl">{t['s2_h']}</div></div>
{footer(t)}"""
        return page(lang, 1350, inner, css)

    if n == 3:
        css = CARDCSS + """
.cards { margin-top: 40px; width: 912px; }
.cards img { width: 280px; }
.ccap { margin-top: 18px; text-align: center; font-size: 28px; font-weight: 600; color: var(--ink-soft); }
.body { margin-top: 30px; } .hl { margin-top: 28px; }
.body p, .hl { font-size: 34px; }
"""
        inner = slide_head(3) + slide_title(t, "s3_t", 66) + f"""
<div class="cards z">{''.join(img(lang, f'card{i}') for i in range(1, 6))}</div>
<div class="ccap z">{t['ccap']}</div>
<div class="body z"><p>{t['s3_b']}</p></div><div class="hl z">{t['s3_h']}</div>
{footer(t)}"""
        return page(lang, 1350, inner, css)

    if n == 4:
        css = BLEED + """
.mid { flex: 1; display: flex; flex-direction: column; justify-content: center; padding: 22px 0 26px; }
.legend { margin-top: 12px; display: flex; align-items: center; font-size: 25px; font-weight: 600; color: var(--ink-soft); }
.legend .sw { flex: none; display: inline-block; width: 44px; height: 20px; border-radius: 6px; background: rgb(46,60,82); border: 1.5px solid rgba(203,213,225,.45); margin-right: 14px; }
.body { margin-top: 20px; } .body p { font-size: 30px; line-height: 1.4; }
.row { margin-top: 18px; display: flex; align-items: center; gap: 28px; }
.row .cardcol { flex: none; width: 280px; }
.row .cardcol img { display: block; width: 280px; height: auto; filter: drop-shadow(0 14px 28px rgba(0,0,0,.55)); }
.row .per { margin-top: 16px; font-size: 27px; font-weight: 600; color: var(--ink-soft); }
.row .hl { font-size: 32px; }
.row .txt { flex: 1; }
.title { font-size: 60px !important; }
"""
        inner = slide_head(4) + slide_title(t, "s4_t", 60) + f"""
<div class="mid z"><div class="shot">{img(lang, 'chart')}</div>
<div class="legend"><i class="sw"></i><span>{t['cap']}</span></div>
<div class="body"><p>{t['s4_b']}</p></div>
<div class="row"><div class="cardcol">{img(lang, 'card5')}</div><div class="txt"><div class="hl">{t['s4_h']}</div><div class="per">{t['period']}</div></div></div></div>
{footer(t)}"""
        return page(lang, 1350, inner, css)

    if n == 5:
        css = CARDCSS + """
.cards { margin-top: 34px; gap: 32px; flex-wrap: nowrap; }
.cards img { width: 440px; }
.ccap { margin-top: 16px; text-align: center; font-size: 28px; font-weight: 600; color: var(--ink-soft); }
.body { margin-top: 26px; } .hl { margin-top: 26px; }
.body p { font-size: 32px; } .hl { font-size: 34px; }
.micro { text-wrap: balance; margin-top: 22px; font-size: 27px; font-weight: 600; line-height: 1.4; color: var(--ink-soft); }
.nw { white-space: nowrap; }
"""
        inner = slide_head(5) + slide_title(t, "s5_t", 66) + f"""
<div class="cards z">{img(lang, 'card5')}{img(lang, 'card2')}</div>
<div class="ccap z">{t['ccap']}</div>
<div class="body z"><p>{t['s5_b']}</p></div><div class="hl z">{t['s5_h']}</div>
<div class="micro z">{t['s5_m']}</div>
{footer(t)}"""
        return page(lang, 1350, inner, css)

    if n == 6:
        css = """
.mid { flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; }
.big { width: 130px; height: 98px; color: var(--gold); filter: drop-shadow(0 0 40px rgba(212,164,24,.45)); }
.big svg { width: 100%; height: 100%; }
.title { font-size: 86px !important; margin-top: 44px; }
.body { margin-top: 30px; max-width: 800px; }
.body p { font-size: 36px; text-wrap: balance; }
.btn { margin-top: 56px; font-size: 40px; font-weight: 900; letter-spacing: 0.04em; color: #0F1526; background: linear-gradient(135deg, var(--amber3), var(--amber6)); border-radius: 999px; padding: 28px 70px; box-shadow: 0 16px 50px rgba(245,158,11,.4); }
""" + NEWCSS + """
.newpill { font-size: 34px; padding: 15px 34px; }
"""
        inner = slide_head(6) + f"""
<div class="mid z"><div style="position:relative;width:130px;height:98px;margin-top:20px"><svg style="position:absolute;left:-45px;top:-61px" width="220" height="220" viewBox="0 0 220 220" fill="none"><circle cx="110" cy="110" r="104" stroke="rgba(212,164,24,0.7)" stroke-width="2.5" stroke-dasharray="460 190" stroke-linecap="round"/><circle cx="110" cy="110" r="88" stroke="rgba(212,164,24,0.2)" stroke-width="1.5"/></svg><div class="big" data-icon></div></div><div style="margin-top:84px">{kickrow(t, True)}</div>
<h1 class="title">{t['s6_t']}</h1><div class="body"><p>{t['s6_b']}</p></div><div class="btn">{t['s6_btn']}</div></div>
{footer(t)}"""
        return page(lang, 1350, inner, css)


# ---------------------------------------------------------------- MOCKUPS (capturas cruas, so enquadradas)
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
    jobs = []  # (html, png, w, h)
    for lang in ("pt", "en"):
        jobs.append((f"feed-{lang}.html", OUT / f"feed-{lang}.png", 1080, 1350))
        (SRC / f"feed-{lang}.html").write_text(feed(lang), encoding="utf-8")
        jobs.append((f"story-{lang}.html", OUT / f"story-{lang}.png", 1080, 1920))
        (SRC / f"story-{lang}.html").write_text(story(lang), encoding="utf-8")
        for n in range(1, 7):
            (SRC / f"carrossel-{lang}-{n:02d}.html").write_text(carousel(lang, n), encoding="utf-8")
            jobs.append((f"carrossel-{lang}-{n:02d}.html", OUT / f"carrossel-{lang}-{n:02d}.png", 1080, 1350))
        for name, f in (("cards", f"{lang}-mock-cards.png"), ("serie", f"{lang}-mock-serie.png")):
            (SRC / f"mockup-{name}-{lang}.html").write_text(mock_html([f]), encoding="utf-8")
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
                pg = b.new_page(viewport={"width": 2300, "height": 1200}, device_scale_factor=1)
                pg.goto((SRC / html).as_uri())
                pg.evaluate("document.fonts.ready")
                pg.wait_for_timeout(150)
                pg.locator("#wrap").screenshot(path=str(png), omit_background=True)
            pg.close()
            print("ok", png.name)
        b.close()


if __name__ == "__main__":
    main()
