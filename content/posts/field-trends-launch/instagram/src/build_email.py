"""Imagens do e-mail do Field Trends: cards de variacao significativa + grafico com a faixa, empilhados.
1200 px de largura (exibida a 552 px), sem transparencia, fundo #0b1220. Sem titulo de filtro, sem navegacao do app.
Uso: python build_email.py   (depois da build.py, que gera os recortes em assets/)
Tambem grava a altura de exibicao (a 552 px) nos <img> de email-*.html e email-*.preview.html."""
import re
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

import build as B

OUT = B.POST / "email"
OUT.mkdir(exist_ok=True)
BG_APP = np.array([2, 6, 23.0])
BG_MAIL = np.array([11, 18, 32.0])  # #0b1220
W = 1200
M = 14                                        # margem em volta de tudo (nenhuma borda encostada na beirada)
GAP = 24
INNER = W - 2 * M                              # 1172
CARD_W = (INNER - 2 * GAP) // 3                # 374
SC = CARD_W / 334.0
CARD_H = round(244 * SC)
CHART_GAP = 18
CCAP = {
    "pt": "Variação em 1 ano (2T26 em curso)",
    "en": "Change over 1 year (2Q26 in progress)",
}
CCAP_H = 52
CAPTION = {
    "pt": "Gráfico: C-bet no flop (IP) %, com a sua faixa de variação normal",
    "en": "Chart: IP flop c-bet %, with its normal variation band",
}
CAP_H = 64
FONT = "C:/Windows/Fonts/segoeui.ttf"
FRAME = (30, 41, 59)                          # borda cinza do app (slate-800)
def remap(arr):
    """Fundo do app (#020617) -> fundo do e-mail (#0b1220), sem halo: mapa linear por canal que leva 2,6,23 a 11,18,32 e 255 a 255."""
    return BG_MAIL + (arr - BG_APP) * (255 - BG_MAIL) / (255 - BG_APP)


def flat(im_rgba):
    """RGBA (cantos transparentes) -> RGB com fundo do e-mail, cores remapeadas."""
    a = np.asarray(im_rgba).astype(float)
    rgb = remap(a[..., :3])
    al = a[..., 3:4] / 255.0
    out = rgb * al + BG_MAIL * (1 - al)
    return Image.fromarray(out.round().clip(0, 255).astype("uint8"))


def rounded_border(size, r, color, width=2):
    k = 4
    w, h = size
    m = Image.new("L", (w * k, h * k), 0)
    d = ImageDraw.Draw(m)
    d.rounded_rectangle((0, 0, w * k - 1, h * k - 1), radius=r * k, fill=255)
    d.rounded_rectangle((width * k, width * k, w * k - 1 - width * k, h * k - 1 - width * k), radius=(r - width) * k, fill=0)
    return m.resize(size, Image.LANCZOS)


def build(lang):
    cards = [Image.open(B.ASSETS / f"{lang}-card{i}.png").convert("RGBA") for i in range(1, 6)]
    cards = [c.resize((CARD_W, CARD_H), Image.LANCZOS) for c in cards]
    chart = Image.open(B.ASSETS / f"{lang}-chart.png").convert("RGB")
    ch = round(chart.height * INNER / chart.width)
    chart = chart.resize((INNER, ch), Image.LANCZOS)
    cards_h = CARD_H * 2 + GAP
    y_chart = M + cards_h + CCAP_H + CHART_GAP
    H = y_chart + ch + CAP_H + M
    canvas = Image.new("RGB", (W, H), tuple(int(v) for v in BG_MAIL))
    # linha 1: 3 cards; linha 2: 2 cards centralizados
    for i in range(3):
        canvas.paste(flat(cards[i]), (M + i * (CARD_W + GAP), M))
    off = M + (INNER - (2 * CARD_W + GAP)) // 2
    for j in range(2):
        canvas.paste(flat(cards[3 + j]), (off + j * (CARD_W + GAP), M + CARD_H + GAP))
    d = ImageDraw.Draw(canvas)
    f = ImageFont.truetype(FONT, 30)
    # legenda dos cards: a variacao e em 1 ano e o 2T26 esta em curso
    txt = CCAP[lang]
    tw = d.textlength(txt, font=f)
    d.text(((W - tw) / 2, M + cards_h + 10), txt, font=f, fill=(203, 213, 225))
    # grafico em moldura com cantos arredondados
    tile = flat(chart.convert("RGBA"))
    r = 22
    k = 4
    mk = Image.new("L", (INNER * k, ch * k), 0)
    ImageDraw.Draw(mk).rounded_rectangle((0, 0, INNER * k - 1, ch * k - 1), radius=r * k, fill=255)
    mk = mk.resize((INNER, ch), Image.LANCZOS)
    canvas.paste(tile, (M, y_chart), mk)
    bm = rounded_border((INNER, ch), r, FRAME, 2)
    canvas.paste(Image.new("RGB", (INNER, ch), FRAME), (M, y_chart), bm)
    # legenda do grafico: e o do C-bet IP (nao o do Fold); os cards em cima trazem os numeros deles
    txt = CAPTION[lang]
    tw = d.textlength(txt, font=f)
    d.text(((W - tw) / 2, y_chart + ch + 14), txt, font=f, fill=(203, 213, 225))
    return canvas


def set_height(html_path, h_display):
    t = html_path.read_text(encoding="utf-8")
    t2, n = re.subn(r'(<img src="[^"]*field-trends-(?:pt|en)\.png" width="552")(?: height="\d+")?', rf'\1 height="{h_display}"', t)
    if n != 1:
        raise SystemExit(f"{html_path.name}: esperava 1 <img> do Field Trends, achei {n}")
    html_path.write_text(t2, encoding="utf-8")
    print(" ", html_path.name, "height=", h_display)


for lang in ("pt", "en"):
    im = build(lang)
    q = im.quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
    dst = OUT / f"field-trends-{lang}.png"
    q.save(dst, optimize=True)
    chk = Image.open(dst)
    print(dst.name, chk.size, chk.mode, round(dst.stat().st_size / 1024), "KB")
    hd = round(chk.height * 552 / chk.width)
    for name in (f"email-{lang}.html", f"email-{lang}.preview.html"):
        set_height(B.POST / name, hd)
