"""Field Trends - build das artes de lancamento (mesmo pipeline do Field Ranges).

1. recorta as capturas brutas (mockups/raw) -> src/assets
2. gera os HTMLs-fonte em src/
3. renderiza com Playwright (device_scale_factor=1) -> PNGs finais

Uso: python build.py   (depois: python build_email.py)

Textos: so os de T e C abaixo (regra de texto do Rafael, 08/10). Os numeros vem dos prints do app.
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
BAND_NEW = np.array([46, 60, 82.0])
BAND_STRONG = np.array([70, 88, 118.0])   # slide 3 do carrossel: mesma faixa, mais contraste   # mesma faixa, mesma geometria, so mais clara para ser vista no celular


# DECISAO (coordenacao + design, 07/10): o app pinta a faixa de variacao normal quase invisivel no celular.
# Nas artes e no e-mail a faixa e clareada SO EM COR (19,25,41 -> 46,60,82); geometria, pontos, linhas e numeros
# ficam identicos. Os mockups/ finais usam a captura crua, sem este realce. Para desligar, tire a chamada de lift_band
# em make_assets().
def lift_band(im, y0=340, y1=400, new=None):
    """A faixa de variacao normal do app e quase invisivel (19,25,41 sobre 2,6,22). Aqui so a COR do preenchimento
    sobe para 46,60,82; forma, posicao e pontos da faixa nao mudam. Mockups finais (mockups/) usam a captura crua."""
    a = np.asarray(im.convert("RGB")).astype(float)
    reg = a[y0:y1].copy()
    new = BAND_NEW if new is None else np.asarray(new, float)
    d = BAND_OLD - BG_APP
    rel = reg - BG_APP
    t = (rel @ d) / (d @ d)
    res = np.linalg.norm(rel - t[..., None] * d, axis=-1)
    m1 = (res < 8) & (t > 0.1) & (t < 1.15)
    out = reg.copy()
    out[m1] = BG_APP + t[m1][..., None] * (new - BG_APP)
    # linha Total e pontos (cinza claro) sobre a faixa: o antialias leva a cor da faixa nova
    neutral = (np.abs(reg[..., 0] - reg[..., 2]) < 40) & (reg[..., 2] > 60)
    bandcol = m1 & (t > 0.9)
    near = np.zeros_like(bandcol)
    for s in range(-4, 5):
        near |= np.roll(bandcol, s, axis=0)
    m2 = neutral & near & ~m1
    al = np.clip((reg[..., 2] - 41) / (225 - 41), 0, 1)
    out[m2] = reg[m2] + (new - BAND_OLD) * (1 - al[m2])[..., None]
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
        # slide 3 do carrossel: faixa com mais contraste (so a cor; geometria e pontos iguais) e menos margem lateral
        # (a largura do slide e o limite: so da para ganhar ~3 % de escala sem cortar rotulos do eixo)
        ch3 = lift_band(serie, new=BAND_STRONG).crop((30, 4, 1748, 636))
        px3 = ch3.load()
        for yy in range(0, 30):
            for xx in range(ch3.width - 12, ch3.width):
                px3[xx, yy] = (2, 6, 22)
        ch3.save(ASSETS / f"{lang}-chart3.png")
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

# REGRA DE TEXTO (Rafael, 08/10): por peca, no maximo 1 titulo curto (~6 palavras) + 1 linha de apoio (~10 palavras).
# A imagem (cards / grafico do app) fala. Sem paragrafo, sem diagrama, sem numero digitado (so os que estao nos prints).
# Selo de lancamento ("NOVO MODULO" / "NEW MODULE"): pilula ambar + kicker. Nunca "Beta".
NEWCSS = """
.krow { display: flex; align-items: center; gap: 22px; }
.krow.c { justify-content: center; }
.newpill { flex: none; font-size: 32px; font-weight: 900; letter-spacing: 0.1em; text-transform: uppercase; color: #0F1526;
  background: linear-gradient(135deg, var(--amber3), var(--amber6)); border-radius: 999px; padding: 14px 32px; box-shadow: 0 8px 30px rgba(245,158,11,.35); }
.krow .kicker { font-size: 27px; }
.krow .kicker::before { display: none; }
.cgrid { display: flex; flex-direction: column; width: 100%; }
.crow { display: flex; justify-content: center; }
.cgrid img, .cardone { display: block; height: auto; filter: drop-shadow(0 18px 34px rgba(0,0,0,.55)); }
.btnpill { display: inline-flex; align-items: center; gap: 16px; font-weight: 800; color: #0F1526;
  background: linear-gradient(135deg, var(--amber3), var(--amber6)); border-radius: 999px; box-shadow: 0 12px 40px rgba(245,158,11,.4); }
"""
ARROW = '<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#0F1526" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'


def kickrow(t, center=False):
    c = " c" if center else ""
    return f'<div class="krow{c}"><span class="newpill">{t["new"]}</span>{KICK}</div>'


def footer(t, data=True):
    d = f'<div class="sample">{t["data"]}</div>' if data else ""
    return f"""<footer><div class="f-left"><div class="handle"><span class="icon" data-icon></span><span>@aurapokeranalytics</span></div>{d}</div><span class="age">18+</span></footer>"""


# Textos reais das artes (so isto aparece escrito; o resto e captura do app).
T = {
    "pt": {
        "new": "NOVO MÓDULO",
        "data": "Dados: Aura · 2T26 em curso",
        "feed_title": "O field mudou.<br><em>E o seu exploit?</em>", "feed_size": 88,
        "feed_cta": "Já na Aura · conta grátis, link na bio",
        "st_title": "O field<br><em>mudou?</em>", "st_size": 116,
        "st_sub": "Trimestre a trimestre.",
        "st_btn": "Conta grátis",
    },
    "en": {
        "new": "NEW MODULE",
        "data": "Data: Aura · 2Q26 in progress",
        "feed_title": "The field changed.<br><em>Your exploit?</em>", "feed_size": 80,
        "feed_cta": "Now on Aura · free account, link in bio",
        "st_title": "Did the field<br><em>change?</em>", "st_size": 100,
        "st_sub": "Quarter by quarter.",
        "st_btn": "Free account",
    },
}

# Carrossel: SO EN, 5 slides.
C = {
    "c1_t": "Did the field<br><em>change?</em>", "c1_s": "Quarter by quarter.",
    "c2_t": "What changed<br><em>this year</em>", "c2_s": "Change over 1 year.",
    "c3_t": "Real change or<br><em>normal variation?</em>", "c3_s": "The shaded band is normal variation.",
    "c4_t": "Fold to <em>IP c-bet</em>", "c4_s": "Above its own normal variation band.",
    "c5_t": "Open<br><em>Field Trends</em>", "c5_btn": "Free account · link in bio",
}


def img(lang, name, width=None):
    w = f' width="{width}"' if width else ""
    return f'<img src="assets/{lang}-{name}.png"{w}>'


def cards_grid(lang, rows, width, gap=18):
    """rows = [[ids], [ids]]: cada fila e uma linha flex sem quebra; a largura util da pagina e 912 px."""
    out = "".join(f'<div class="crow" style="gap:{gap}px">' + "".join(img(lang, f"card{i}", width) for i in r) + "</div>" for r in rows)
    return f'<div class="cgrid" style="gap:{gap}px">{out}</div>'


# ---------------------------------------------------------------- FEED
def feed(lang):
    t = T[lang]
    css = NEWCSS + """
.page { padding-top: 64px; }
.title { font-size: %SIZE%px; line-height: 1.06; margin-top: 30px; }
.mid { flex: 1; display: flex; flex-direction: column; justify-content: center; padding: 20px 0 10px; }
.cta { margin: 6px 0 28px; font-size: 38px; font-weight: 800; color: var(--amber); }
""".replace("%SIZE%", str(t["feed_size"]))
    inner = lockup() + f"""
<div class="z" style="margin-top:44px">{kickrow(t)}<h1 class="title">{t['feed_title']}</h1></div>
<div class="mid z">{cards_grid(lang, [[5, 2, 3], [4, 1]], 292, 18)}</div>
<div class="cta z">{t['feed_cta']}</div>
{footer(t)}"""
    return page(lang, 1350, inner, css)


# ---------------------------------------------------------------- STORY (capa em PT-BR / EN)
def story(lang):
    t = T[lang]
    css = NEWCSS + """
.page { padding-top: 250px; padding-bottom: 352px; align-items: center; text-align: center; justify-content: space-between; }
.blk { display: flex; flex-direction: column; align-items: center; }
.lockup { justify-content: center; }
.newpill { font-size: 36px; padding: 16px 36px; }
.krow .kicker { font-size: 30px; }
.title { font-size: %SIZE%px; line-height: 1.02; }
.sub { margin-top: 18px; font-size: 46px; font-weight: 600; color: var(--ink-soft); }
.pill { font-size: 40px; padding: 26px 56px; }
.sample { margin-top: 24px; text-align: center; }
.blk + .blk { margin-top: 26px; }
.age { margin-top: 14px; }
""".replace("%SIZE%", str(t["st_size"]))
    inner = f"""
<div class="blk z">{lockup()}<div style="margin-top:34px">{kickrow(t, True)}</div></div>
<div class="blk z"><h1 class="title">{t['st_title']}</h1><div class="sub">{t['st_sub']}</div></div>
<div class="blk z">{cards_grid(lang, [[5, 2], [4, 3]], 360, 22)}</div>
<div class="blk z"><div class="btnpill pill">{t['st_btn']} {ARROW}</div>
<div class="sample">{t['data']}</div><span class="age">18+</span></div>"""
    return page(lang, 1920, inner, css)


# ---------------------------------------------------------------- CARROSSEL (EN, 5 slides)
def slide_head(n):
    return lockup(f'<span class="indicator">{n} / 5</span>')


BLEED = """
.shot { margin-left: -84px; margin-right: -84px; width: 1080px; border-radius: 0; border-left: 0; border-right: 0; }
"""


def carousel(n):
    lang = "en"
    t = T[lang]
    base = NEWCSS + """
.title { font-size: 84px; line-height: 1.06; margin-top: 24px; }
.sub { margin-top: 22px; font-size: 42px; font-weight: 500; color: var(--ink-soft); }
.mid { flex: 1; display: flex; flex-direction: column; justify-content: center; padding: 10px 0 30px; }
"""
    if n == 1:
        inner = slide_head(1) + f"""
<div class="z" style="margin-top:50px">{kickrow(t)}<h1 class="title" style="font-size:100px;margin-top:30px">{C['c1_t']}</h1>
<p class="sub">{C['c1_s']}</p></div>
<div class="mid z">{cards_grid(lang, [[5, 2]], 440, 32)}</div>
{footer(t)}"""
        return page(lang, 1350, inner, base)

    if n == 2:
        inner = slide_head(2) + f"""
<div class="z" style="margin-top:44px">{KICK}<h1 class="title">{C['c2_t']}</h1><p class="sub">{C['c2_s']}</p></div>
<div class="mid z">{cards_grid(lang, [[1, 2, 3], [4, 5]], 292, 18)}</div>
{footer(t)}"""
        return page(lang, 1350, inner, base)

    if n == 3:
        inner = slide_head(3) + f"""
<div class="z" style="margin-top:44px">{KICK}<h1 class="title" style="font-size:76px">{C['c3_t']}</h1></div>
<div class="mid z"><div class="shot">{img(lang, 'chart3')}</div><p class="sub" style="margin-top:34px">{C['c3_s']}</p></div>
{footer(t)}"""
        return page(lang, 1350, inner, base + BLEED)

    if n == 4:
        inner = slide_head(4) + f"""
<div class="z" style="margin-top:44px">{KICK}<h1 class="title">{C['c4_t']}</h1><p class="sub">{C['c4_s']}</p></div>
<div class="mid z" style="align-items:center">{img(lang, 'card5', 700).replace('<img', '<img class="cardone"')}</div>
{footer(t)}"""
        return page(lang, 1350, inner, base)

    if n == 5:
        css = base + """
.mid { align-items: center; text-align: center; padding-bottom: 20px; }
.big { width: 130px; height: 98px; color: var(--gold); filter: drop-shadow(0 0 40px rgba(212,164,24,.45)); }
.big svg { width: 100%; height: 100%; }
.title { font-size: 104px; margin-top: 44px; }
.btn { margin-top: 52px; font-size: 40px; padding: 28px 60px; }
.krow { margin-top: 70px; }
"""
        inner = slide_head(5) + f"""
<div class="mid z"><div style="position:relative;width:130px;height:98px;margin-top:20px"><svg style="position:absolute;left:-45px;top:-61px" width="220" height="220" viewBox="0 0 220 220" fill="none"><circle cx="110" cy="110" r="104" stroke="rgba(212,164,24,0.7)" stroke-width="2.5" stroke-dasharray="460 190" stroke-linecap="round"/><circle cx="110" cy="110" r="88" stroke="rgba(212,164,24,0.2)" stroke-width="1.5"/></svg><div class="big" data-icon></div></div>
{kickrow(t, True)}
<h1 class="title">{C['c5_t']}</h1><div class="btnpill btn">{C['c5_btn']}</div></div>
{footer(t, data=False)}"""
        return page(lang, 1350, inner, css)


# ---------------------------------------------------------------- MOCKUPS (nao sao regerados por padrao: "ficam como estao")
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
    import sys
    with_mockups = "--mockups" in sys.argv      # mockups/ ficam como estao, a menos que se peca
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
        if with_mockups:
            for name, f in (("cards", f"{lang}-mock-cards.png"), ("serie", f"{lang}-mock-serie.png")):
                (SRC / f"mockup-{name}-{lang}.html").write_text(mock_html([f]), encoding="utf-8")
                jobs.append((f"mockup-{name}-{lang}.html", MOCK / f"{name}-{lang}.png", None, None))
    for n in range(1, 6):
        (SRC / f"carrossel-en-{n:02d}.html").write_text(carousel(n), encoding="utf-8")
        jobs.append((f"carrossel-en-{n:02d}.html", OUT / f"carrossel-en-{n:02d}.png", 1080, 1350))
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
