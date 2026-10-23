"""Field Hotspots: numeros, formatacao, componentes visuais (cartas, spots, barras field x GTO).

Usado por build.py (artes) e build_email.py (e-mail). Nenhum numero estatistico mora aqui nem nos HTMLs:
tudo vem de numbers.json. Valor ausente ou "[NUM]" vira o marcador [NUM] visivel; nunca um numero inventado.
"""
import json
import math
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
POST = ROOT / "content/posts/field-hotspots-launch"
SRC = POST / "instagram/src"
ASSETS = SRC / "assets"
OUT = POST / "instagram"
MIRROR = ROOT / "instagram/output/field-hotspots-launch"
EMAIL = POST / "email"
MOCK = POST / "mockups"
TPL = ROOT / "instagram/templates/carrossel-slide.html"
NUMBERS = Path(os.environ.get("AURA_NUMBERS") or (SRC / "numbers.json"))   # AURA_NUMBERS: so para teste de layout
HANDLE = "@aurapokeranalytics"
LANDING = "https://www.aurapoker.com?utm_source=email&utm_medium=email&utm_campaign=field-hotspots-launch&utm_content={lang}"
EMAIL_IMG_BASE = "https://www.aurapoker.com/email/"        # hospedagem a definir (aura-landing), como o modo-gto
MARK = "[NUM]"
SIZES = ("33", "50", "65")


def load():
    return json.loads(NUMBERS.read_text(encoding="utf-8"))


def is_num(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool)


# ---------------------------------------------------------------- formatacao
def dec(n):
    d = n.get("decimals", 1)
    return d if isinstance(d, int) else 1


def fnum(v, lang, n):
    s = f"{v:.{dec(n)}f}"
    return s.replace(".", ",") if lang == "pt" else s


def pct(v, lang, n):
    return fnum(v, lang, n) + "%"


def ph():
    """Marcador [NUM] visivel (HTML)."""
    return f'<span class="ph">{MARK}</span>'


def ph_email():
    return (f'<span style="background-color:#e11d48; color:#ffffff; font-weight:bold; padding:1px 6px; border-radius:4px;">{MARK}</span>')


def pv(v, lang, n, mark=None):
    """Valor em % ou o marcador."""
    return pct(v, lang, n) if is_num(v) else (mark or ph)()


def below(v, lang, n, mark=None):
    """Diferenca no formato da tela: 'xx,x% abaixo' / 'xx.x% below'."""
    word = "abaixo" if lang == "pt" else "below"
    return f"{pv(v, lang, n, mark)} {word}"


# ---------------------------------------------------------------- estado dos numeros
def missing(n, keys=("N1", "N2", "N3")):
    m = []
    for k in keys:
        if k in ("N4", "N5"):
            d = n.get(k) or {}
            if not all(is_num(d.get(s)) for s in SIZES):
                m.append(k)
        elif not is_num(n.get(k)):
            m.append(k)
    return m


# ---------------------------------------------------------------- cartas (4 cores, face creme)
SUIT = {"s": "♠", "h": "♥", "c": "♣", "d": "♦"}


def card(rank, suit, w=116):
    return f'<div class="pc {suit}" style="--cw:{w}px"><b>{rank}</b><i>{SUIT[suit]}</i></div>'


def board(cards, w=116, label=None):
    inner = "".join(card(r, s, w) for r, s in cards)
    if label:
        return f'<div class="bwrap"><div class="board">{inner}</div><small>{label}</small></div>'
    return f'<div class="board">{inner}</div>'


FLOPS = [  # os 3 boards de exemplo do spot (tela de 22/10)
    [("A", "s"), ("3", "s"), ("6", "h")],
    [("6", "s"), ("A", "c"), ("7", "c")],
    [("7", "c"), ("A", "h"), ("5", "h")],
]


# ---------------------------------------------------------------- icones
LOCK = ('<svg class="lock" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">'
        '<rect x="4" y="10.5" width="16" height="10.5" rx="2.5"/><path d="M8 10.5V7.5a4 4 0 0 1 8 0v3"/></svg>')


# ---------------------------------------------------------------- barras Field x GTO (SVG)
AMBER = "#FBBF24"
W = 912
COL_W = 270
FX, GX = 40, 602
HEAD = 212
TITLE = {"pt": "Fold vs c-bet 50%", "en": "Fold vs 50% c-bet"}
CAPTION = "UTG vs BB · 25bb · A-high two-tone"
CHIP = "OVERDEFEND"
NAMES = ("FIELD", "GTO")


def _topround(x, y, w, h, r):
    r = min(r, w / 2, h)
    return f"M{x},{y + h} L{x},{y + r} Q{x},{y} {x + r},{y} L{x + w - r},{y} Q{x + w},{y} {x + w},{y + r} L{x + w},{y + h} Z"


def _ph_svg(x, y, size, label=MARK):
    wd = len(label) * size * 0.66 + 34
    return (f'<rect x="{x - wd / 2:.0f}" y="{y - size * 0.86:.0f}" width="{wd:.0f}" height="{size * 1.12:.0f}" rx="12" fill="#E11D48"/>'
            f'<text x="{x}" y="{y}" text-anchor="middle" font-size="{size}" font-weight="900" fill="#fff">{label}</text>')


def _axis(n, a, b):
    if is_num(n.get("scale_max")):
        return float(n["scale_max"])
    top = max(a, b) * 1.06
    return max(20.0, math.ceil(top / 5.0) * 5.0)


def chart_svg(lang, n, ph_h=440, emphasize=False, caption=True):
    """Duas barras (fold do field e fold do GTO), a diferenca em ambar entre os topos.
    Com N1 e N2: alturas reais a partir do zero. Sem: contornos tracejados ILUSTRATIVOS (nao sao dado) e [NUM] visivel."""
    f_, g_, d_ = n.get("N1"), n.get("N2"), n.get("N3")
    ready = is_num(f_) and is_num(g_)
    head = HEAD + (30 if caption else 0)
    base = head + ph_h
    H = base + 40
    o = [f'<svg class="chart" width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="Montserrat, Segoe UI, sans-serif">']
    o.append('<defs><linearGradient id="fb" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0E8AA3"/><stop offset="1" stop-color="#015A6B"/></linearGradient>'
             f'<filter id="glow" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="{7 if emphasize else 0}"/></filter></defs>')
    o.append(f'<text x="0" y="34" font-size="30" font-weight="700" letter-spacing="2" fill="#A9B6C8">{TITLE[lang].upper()}</text>')
    chip_w = 236
    o.append(f'<rect x="{W - chip_w}" y="4" width="{chip_w}" height="42" rx="11" fill="rgba(251,146,60,.16)" stroke="rgba(251,146,60,.5)" stroke-width="2"/>'
             f'<text x="{W - chip_w / 2}" y="34" text-anchor="middle" font-size="25" font-weight="800" letter-spacing="1.5" fill="#FDBA74">{CHIP}</text>')
    if caption:
        o.append(f'<text x="0" y="74" font-size="26" font-weight="600" fill="#94A3B8">{CAPTION}</text>')
    for cx, name in ((FX + COL_W / 2, NAMES[0]), (GX + COL_W / 2, NAMES[1])):
        o.append(f'<text x="{cx:.0f}" y="{head - 20}" text-anchor="middle" font-size="32" font-weight="800" letter-spacing="6" fill="#CBD5E1">{name}</text>')
    word = "abaixo" if lang == "pt" else "below"
    if ready:
        axis = _axis(n, f_, g_)
        y = lambda v: base - v / axis * ph_h
        yf, yg = y(f_), y(g_)
        o.append(f'<path d="{_topround(FX, yf, COL_W, base - yf, 18)}" fill="url(#fb)" stroke="rgba(103,232,249,.4)" stroke-width="2.5"/>')
        o.append(f'<path d="{_topround(GX, yg, COL_W, base - yg, 18)}" fill="rgba(1,90,107,.55)" stroke="#5EC9DB" stroke-width="3.5"/>')
        o.append(f'<text x="{FX + COL_W / 2:.0f}" y="{head - 70}" text-anchor="middle" font-size="100" font-weight="900" fill="#fff">{pct(f_, lang, n)}</text>')
        o.append(f'<text x="{GX + COL_W / 2:.0f}" y="{head - 70}" text-anchor="middle" font-size="100" font-weight="900" fill="#fff">{pct(g_, lang, n)}</text>')
    else:
        yf, yg = base - 0.60 * ph_h, base - 0.86 * ph_h
        o.append(f'<path d="{_topround(FX, yf, COL_W, base - yf, 18)}" fill="rgba(1,90,107,.25)" stroke="#5EC9DB" stroke-width="3.5" stroke-dasharray="14 10"/>')
        o.append(f'<path d="{_topround(GX, yg, COL_W, base - yg, 18)}" fill="rgba(1,90,107,.25)" stroke="#5EC9DB" stroke-width="3.5" stroke-dasharray="14 10"/>')
        for cx, v in ((FX + COL_W / 2, f_), (GX + COL_W / 2, g_)):
            if is_num(v):
                o.append(f'<text x="{cx:.0f}" y="{head - 70}" text-anchor="middle" font-size="100" font-weight="900" fill="#fff">{pct(v, lang, n)}</text>')
            else:
                o.append(_ph_svg(cx, head - 70, 72))
    # diferenca em ambar entre os topos
    top, bot = min(yf, yg), max(yf, yg)
    ax = FX + COL_W + 38                      # eixo da seta
    sw = 6 if emphasize else 4
    if emphasize:
        o.append(f'<g filter="url(#glow)" opacity=".85"><line x1="{ax}" y1="{top:.1f}" x2="{ax}" y2="{bot:.1f}" stroke="{AMBER}" stroke-width="14"/></g>')
    o.append(f'<line x1="{FX + COL_W + 6}" y1="{yf:.1f}" x2="{GX - 8}" y2="{yf:.1f}" stroke="{AMBER}" stroke-width="{sw}" stroke-dasharray="14 9"/>')
    o.append(f'<line x1="{FX + COL_W + 6}" y1="{yg:.1f}" x2="{GX + COL_W + 26}" y2="{yg:.1f}" stroke="{AMBER}" stroke-width="{sw}" stroke-dasharray="14 9"/>')
    o.append(f'<line x1="{ax}" y1="{top:.1f}" x2="{ax}" y2="{bot:.1f}" stroke="{AMBER}" stroke-width="{sw + 2}"/>')
    a = min(16, (bot - top) / 3.2)
    o.append(f'<polygon points="{ax - a},{top + a * 1.5:.1f} {ax + a},{top + a * 1.5:.1f} {ax},{top:.1f}" fill="{AMBER}"/>')
    o.append(f'<polygon points="{ax - a},{bot - a * 1.5:.1f} {ax + a},{bot - a * 1.5:.1f} {ax},{bot:.1f}" fill="{AMBER}"/>')
    # rotulo da diferenca: ao lado da seta, sobre fundo escuro para nao brigar com as linhas tracejadas
    midy = (top + bot) / 2
    lx = ax + 24
    if is_num(d_):
        txt = f"{pct(d_, lang, n)} {word}"
        o.append(f'<rect x="{lx - 8}" y="{midy - 24:.1f}" width="{len(txt) * 17.5 + 16:.0f}" height="48" rx="10" fill="#020617"/>')
        o.append(f'<text x="{lx}" y="{midy + 11:.1f}" font-size="31" font-weight="900" fill="{AMBER}">{txt}</text>')
    else:
        o.append(f'<rect x="{lx - 8}" y="{midy - 24:.1f}" width="226" height="48" rx="10" fill="#020617"/>')
        o.append(f'<rect x="{lx}" y="{midy - 20:.1f}" width="88" height="40" rx="9" fill="#E11D48"/>'
                 f'<text x="{lx + 44}" y="{midy + 9:.1f}" text-anchor="middle" font-size="26" font-weight="900" fill="#fff">{MARK}</text>'
                 f'<text x="{lx + 98}" y="{midy + 10:.1f}" font-size="30" font-weight="900" fill="{AMBER}">{word}</text>')
    o.append(f'<line x1="0" y1="{base}" x2="{W}" y2="{base}" stroke="#475569" stroke-width="3"/>')
    o.append("</svg>")
    return "".join(o), H


# ---------------------------------------------------------------- barras por size (HTML), slide 3
SIZE_L = {"pt": ("Fold por size de c-bet", "Field", "GTO"), "en": ("Fold by c-bet size", "Field", "GTO")}


def sizes_html(lang, n, max_pct=None):
    """3 linhas (33/50/65): barra do field e barra do GTO. Sem numero: contornos tracejados + [NUM]."""
    f_, g_ = n.get("N4") or {}, n.get("N5") or {}
    allv = [v for v in list(f_.values()) + list(g_.values()) if is_num(v)]
    top = max_pct or (max(allv) * 1.08 if allv else 100)
    rows = []
    for s in SIZES:
        fv, gv = f_.get(s), g_.get(s)
        cells = []
        for nm, v, cls in ((SIZE_L[lang][1], fv, "bf"), (SIZE_L[lang][2], gv, "bg")):
            if is_num(v):
                w = max(4, min(100, v / top * 100))
                bar = f'<div class="trk"><div class="fil {cls}" style="width:{w:.1f}%"></div></div>'
                val = f'<span class="val">{pct(v, lang, n)}</span>'
            else:
                bar = f'<div class="trk"><div class="fil {cls} dr" style="width:{58 if cls == "bf" else 74}%"></div></div>'
                val = f'<span class="val">{ph()}</span>'
            cells.append(f'<div class="srow"><span class="nm">{nm}</span>{bar}{val}</div>')
        rows.append(f'<div class="sgrp"><div class="slab">c-bet {s}%</div>{"".join(cells)}</div>')
    return "".join(rows)
