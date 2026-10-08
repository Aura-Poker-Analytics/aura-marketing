"""Modo GTO: numeros, formatacao, estado (DRAFT x final) e o grafico field x GTO (SVG).

Usado por build.py (artes) e build_email.py (e-mail). Nenhum numero mora aqui nem nos HTMLs: tudo vem de numbers.json.
Regra: valor ausente vira o marcador [[N..]] visivel; nunca um numero inventado.
"""
import json
import math
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
POST = ROOT / "content/posts/modo-gto-launch"
SRC = POST / "instagram/src"
ASSETS = SRC / "assets"
OUT = POST / "instagram"
MIRROR = ROOT / "instagram/output/modo-gto-launch"
EMAIL = POST / "email"
TPL = ROOT / "instagram/templates/carrossel-slide.html"
NUMBERS = Path(os.environ.get("AURA_NUMBERS") or (SRC / "numbers.json"))   # AURA_NUMBERS: so para teste de layout
PRINTS = Path(os.environ.get("AURA_PRINTS_DIR") or (ROOT.parent / "_ops/golive-gto-2026-10-04/prints/prod"))
PRINT_NAMES = {            # arquivo esperado em PRINTS (png ou jpg) -> onde entra
    "postflop-en": "carrossel slide 3 (Postflop com o Modo GTO ligado, spot N1)",
    "preflop-en": "carrossel slide 4 (grade do pre-flop, celula N5 destacada, torneio Regular)",
    "postflop-pt": "e-mail PT (mesmo spot N1, em PT)",
}
HANDLE = "@aurapokeranalytics"
LANDING = "https://www.aurapoker.com/?utm_source=email&utm_medium=email&utm_campaign=modo-gto-launch&utm_content={lang}"


def load():
    return json.loads(NUMBERS.read_text(encoding="utf-8"))


def is_num(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def has_text(v):
    return isinstance(v, str) and v.strip() != ""


def find_print(name):
    """Captura de producao em PRINTS (png ou jpg); None se nao existe."""
    for ext in ("png", "jpg", "jpeg"):
        p = PRINTS / f"{name}.{ext}"
        if p.exists():
            return p
    return None


# ---------------------------------------------------------------- formatacao
def dec(n):
    d = n.get("decimals", 1)
    return d if isinstance(d, int) else 1


def fnum(v, lang, n):
    s = f"{v:.{dec(n)}f}"
    return s.replace(".", ",") if lang == "pt" else s


def pct(v, lang, n):
    return fnum(v, lang, n) + "%"


def ph(label):
    """Marcador pendente, bem visivel (HTML)."""
    return f'<span class="ph">[[{label}]]</span>'


def ph_email(label):
    return (f'<span style="background-color:#e11d48; color:#ffffff; font-weight:bold; padding:1px 6px; border-radius:4px;">'
            f'[[{label}]]</span>')


# ---------------------------------------------------------------- campos do exemplo
class Ex:
    """Os campos do exemplo field x GTO ja resolvidos (valor, texto ou marcador)."""

    def __init__(self, n, lang, mark=ph):
        self.n, self.lang, self.mark = n, lang, mark
        n3 = n.get("N3") or {}
        self.n2 = n.get("N2") if is_num(n.get("N2")) else None
        self.c = n3.get("center") if is_num(n3.get("center")) else None
        self.lo = n3.get("from") if is_num(n3.get("from")) else None
        self.hi = n3.get("to") if is_num(n3.get("to")) else None
        n1 = (n.get("N1") or {}).get(lang)
        self.n1 = n1.strip() if has_text(n1) else None
        n4 = n.get("N4")
        if is_num(n4):
            self.n4 = abs(n4)
        elif self.n2 is not None and self.hi is not None and self.n2 > self.hi:
            self.n4 = self.n2 - self.hi          # acima: distancia ao TOPO da faixa (como a tela mostra)
        elif self.n2 is not None and self.lo is not None and self.n2 < self.lo:
            self.n4 = self.lo - self.n2          # abaixo: distancia a BASE da faixa
        elif self.n2 is not None and self.lo is not None and self.hi is not None:
            self.n4 = None                       # dentro da faixa: nao ha distancia a faixa
        else:
            self.n4 = None

    @property
    def chart_ready(self):
        return None not in (self.n2, self.c, self.lo, self.hi)

    @property
    def position(self):
        """above / below / inside, ou None. Usa a faixa GTO (de-a)."""
        if self.n2 is None or self.lo is None or self.hi is None:
            return None
        if self.n2 > self.hi:
            return "above"
        if self.n2 < self.lo:
            return "below"
        return "inside"

    # textos
    def s_n1(self):
        return self.n1 if self.n1 else self.mark("N1")

    def s_n2(self):
        return pct(self.n2, self.lang, self.n) if self.n2 is not None else self.mark("N2")

    def s_n3c(self):
        return pct(self.c, self.lang, self.n) if self.c is not None else self.mark("N3")

    def s_n3(self):
        """GTO central + faixa: '25.2% (19.2-31.2)', como a tela."""
        if self.c is None or self.lo is None or self.hi is None:
            return self.mark("N3")
        return f"{pct(self.c, self.lang, self.n)} ({fnum(self.lo, self.lang, self.n)}–{fnum(self.hi, self.lang, self.n)})"

    def s_n3_words(self):
        """Para texto corrido (e-mail): '25,2% (faixa de 19,2 a 31,2)' / '25.2% (range 19.2-31.2)'."""
        if self.c is None or self.lo is None or self.hi is None:
            return self.mark("N3")
        lo, hi = fnum(self.lo, self.lang, self.n), fnum(self.hi, self.lang, self.n)
        rng = f"faixa de {lo} a {hi}" if self.lang == "pt" else f"range {lo}–{hi}"
        return f"{pct(self.c, self.lang, self.n)} ({rng})"

    def s_n4(self):
        return fnum(self.n4, self.lang, self.n) if self.n4 is not None else self.mark("N4")

    def missing(self, with_n1=False, with_n4=False):
        m = []
        if with_n1 and self.n1 is None:
            m.append("N1")
        if self.n2 is None:
            m.append("N2")
        if None in (self.c, self.lo, self.hi):
            m.append("N3")
        if with_n4 and self.n4 is None:
            m.append("N4")
        return m


def n5_missing(n):
    n5 = n.get("N5") or {}
    return [] if (has_text(n5.get("cell")) and all(is_num(n5.get(k)) for k in ("gto", "field", "deviation"))) else ["N5"]


# ---------------------------------------------------------------- grafico field x GTO (SVG)
AMBER = "#FBBF24"
W = 912
COL_W = 270
FX, GX = 40, 602             # x das colunas: field e GTO
MID = (FX + COL_W + GX) // 2  # centro da zona do gap
HEAD = 212
LEG = {"pt": ("Faixa GTO", "Gap até a faixa"), "en": ("GTO range", "Gap to range")}
TITLE = {"pt": "Fold vs c-bet", "en": "Fold vs c-bet"}
NAMES = ("FIELD", "GTO")


def _topround(x, y, w, h, r):
    r = min(r, w / 2, h)
    return (f"M{x},{y + h} L{x},{y + r} Q{x},{y} {x + r},{y} L{x + w - r},{y} Q{x + w},{y} {x + w},{y + r} L{x + w},{y + h} Z")


def _nice_axis(ex, n):
    if is_num(n.get("scale_max")):
        return float(n["scale_max"])
    top = max(ex.n2, ex.hi, ex.c) * 1.06
    return max(20.0, math.ceil(top / 5.0) * 5.0)


def _ph_text(x, y, label, size):
    wd = len(label) * size * 0.64 + 34
    return (f'<rect x="{x - wd / 2:.0f}" y="{y - size * 0.86:.0f}" width="{wd:.0f}" height="{size * 1.12:.0f}" rx="12" fill="#E11D48"/>'
            f'<text x="{x}" y="{y}" text-anchor="middle" font-size="{size}" font-weight="900" fill="#fff">{label}</text>')


def chart_svg(lang, n, ph_h=470, emphasize=False, caption=None):
    """Barras field x GTO lado a lado, faixa GTO sombreada na barra do GTO, gap em ambar entre as duas.
    Pronto (todos os numeros) -> alturas reais, barras a partir do zero. Senao -> contornos tracejados com [[N..]]."""
    ex = Ex(n, lang)
    ready = ex.chart_ready
    head = HEAD + (30 if caption else 0)
    base = head + ph_h
    H = base + 90
    o = [f'<svg class="chart" width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="Montserrat, Segoe UI, sans-serif">']
    o.append('<defs>'
             '<linearGradient id="fb" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0E8AA3"/><stop offset="1" stop-color="#015A6B"/></linearGradient>'
             f'<filter id="glow" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="{7 if emphasize else 0}"/></filter>'
             '</defs>')
    if caption:
        o.append(f'<text x="0" y="68" font-size="26" font-weight="600" fill="#94A3B8">{caption}</text>')
    o.append(f'<text x="0" y="34" font-size="30" font-weight="700" letter-spacing="2" fill="#A9B6C8">{TITLE[lang].upper()}</text>')
    # nomes das colunas
    for cx, name in ((FX + COL_W / 2, NAMES[0]), (GX + COL_W / 2, NAMES[1])):
        o.append(f'<text x="{cx:.0f}" y="{head - 20}" text-anchor="middle" font-size="32" font-weight="800" letter-spacing="6" fill="#CBD5E1">{name}</text>')

    if ready:
        axis = _nice_axis(ex, n)
        y = lambda v: base - v / axis * ph_h
        yf, yc, yl, yh = y(ex.n2), y(ex.c), y(ex.lo), y(ex.hi)
        # barras
        o.append(f'<path d="{_topround(FX, yf, COL_W, base - yf, 18)}" fill="url(#fb)" stroke="rgba(103,232,249,.4)" stroke-width="2.5"/>')
        o.append(f'<path d="{_topround(GX, yc, COL_W, base - yc, 18)}" fill="rgba(1,90,107,.55)" stroke="#5EC9DB" stroke-width="3.5"/>')
        # faixa GTO sombreada em volta da barra do GTO
        o.append(f'<rect x="{GX - 26}" y="{yh:.1f}" width="{COL_W + 52}" height="{max(yl - yh, 6):.1f}" rx="8" fill="rgba(203,213,225,.20)" '
                 f'stroke="rgba(226,232,240,.85)" stroke-width="2.5" stroke-dasharray="11 8"/>')
        # gap em ambar
        sw = 6 if emphasize else 4
        yg = yh if ex.position == "above" else (yl if ex.position == "below" else yc)   # alvo do gap: topo da faixa (field acima), base (abaixo), centro (dentro)
        top, bot = min(yf, yg), max(yf, yg)
        glow = ""
        if emphasize:
            glow = (f'<g filter="url(#glow)" opacity=".85"><line x1="{MID}" y1="{top:.1f}" x2="{MID}" y2="{bot:.1f}" stroke="{AMBER}" stroke-width="14"/></g>')
        o.append(glow)
        o.append(f'<line x1="{FX + COL_W + 6}" y1="{yf:.1f}" x2="{GX + COL_W + 26}" y2="{yf:.1f}" stroke="{AMBER}" stroke-width="{sw}" stroke-dasharray="14 9"/>')
        o.append(f'<line x1="{FX + COL_W + 6}" y1="{yg:.1f}" x2="{GX - 30}" y2="{yg:.1f}" stroke="{AMBER}" stroke-width="{sw}" stroke-dasharray="14 9"/>')
        o.append(f'<line x1="{MID}" y1="{top:.1f}" x2="{MID}" y2="{bot:.1f}" stroke="{AMBER}" stroke-width="{sw + 2}" stroke-linecap="butt"/>')
        if bot - top > 22:
            a = min(16, (bot - top) / 3.4)
            o.append(f'<polygon points="{MID - a},{top + a * 1.5:.1f} {MID + a},{top + a * 1.5:.1f} {MID},{top:.1f}" fill="{AMBER}"/>')
            o.append(f'<polygon points="{MID - a},{bot - a * 1.5:.1f} {MID + a},{bot - a * 1.5:.1f} {MID},{bot:.1f}" fill="{AMBER}"/>')
        else:
            o.append(f'<line x1="{MID - 18}" y1="{top:.1f}" x2="{MID + 18}" y2="{top:.1f}" stroke="{AMBER}" stroke-width="{sw + 2}"/>')
            o.append(f'<line x1="{MID - 18}" y1="{bot:.1f}" x2="{MID + 18}" y2="{bot:.1f}" stroke="{AMBER}" stroke-width="{sw + 2}"/>')
        # numeros no cabecalho das colunas
        o.append(f'<text x="{FX + COL_W / 2:.0f}" y="{head - 70}" text-anchor="middle" font-size="100" font-weight="900" fill="#fff">{ex.s_n2()}</text>')
        o.append(f'<text x="{GX + COL_W / 2:.0f}" y="{head - 70}" text-anchor="middle" font-size="100" font-weight="900" fill="#fff">{ex.s_n3c()}</text>')
    else:
        # rascunho: alturas ILUSTRATIVAS (nao sao dado), contornos tracejados, marcadores visiveis
        fh, ch_, lo_h, hi_h = 0.86 * ph_h, 0.56 * ph_h, 0.38 * ph_h, 0.74 * ph_h
        yf, yc, yl, yh = base - fh, base - ch_, base - lo_h, base - hi_h
        o.append(f'<path d="{_topround(FX, yf, COL_W, base - yf, 18)}" fill="rgba(1,90,107,.25)" stroke="#5EC9DB" stroke-width="3.5" stroke-dasharray="14 10"/>')
        o.append(f'<path d="{_topround(GX, yc, COL_W, base - yc, 18)}" fill="rgba(1,90,107,.25)" stroke="#5EC9DB" stroke-width="3.5" stroke-dasharray="14 10"/>')
        o.append(f'<rect x="{GX - 26}" y="{yh:.1f}" width="{COL_W + 52}" height="{yl - yh:.1f}" rx="8" fill="rgba(203,213,225,.12)" stroke="rgba(226,232,240,.85)" stroke-width="2.5" stroke-dasharray="11 8"/>')
        o.append(f'<text x="{GX + COL_W / 2:.0f}" y="{yh + 36:.0f}" text-anchor="middle" font-size="26" font-weight="800" fill="#E2E8F0">[[N3 faixa]]</text>')
        o.append(f'<line x1="{FX + COL_W + 6}" y1="{yf:.1f}" x2="{GX + COL_W + 26}" y2="{yf:.1f}" stroke="{AMBER}" stroke-width="3" stroke-dasharray="4 10" opacity=".8"/>')
        o.append(f'<line x1="{FX + COL_W + 6}" y1="{yc:.1f}" x2="{GX - 6}" y2="{yc:.1f}" stroke="{AMBER}" stroke-width="3" stroke-dasharray="4 10" opacity=".8"/>')
        o.append(f'<line x1="{MID}" y1="{yf:.1f}" x2="{MID}" y2="{yc:.1f}" stroke="{AMBER}" stroke-width="4" stroke-dasharray="4 10" opacity=".8"/>')
        o.append(_ph_text(FX + COL_W / 2, head - 70, "[[N2]]" if ex.n2 is None else ex.s_n2(), 68) if ex.n2 is None else
                 f'<text x="{FX + COL_W / 2:.0f}" y="{head - 70}" text-anchor="middle" font-size="100" font-weight="900" fill="#fff">{ex.s_n2()}</text>')
        o.append(_ph_text(GX + COL_W / 2, head - 70, "[[N3]]", 68) if ex.c is None else
                 f'<text x="{GX + COL_W / 2:.0f}" y="{head - 70}" text-anchor="middle" font-size="100" font-weight="900" fill="#fff">{ex.s_n3c()}</text>')
    # linha de base
    o.append(f'<line x1="0" y1="{base}" x2="{W}" y2="{base}" stroke="#475569" stroke-width="3"/>')
    # legenda (conta como parte do grafico): faixa GTO e gap
    ly = base + 56
    lg, gp = LEG[lang]
    if ready:
        lg += f" {fnum(ex.lo, lang, n)}–{fnum(ex.hi, lang, n)}%"
    o.append(f'<rect x="{FX}" y="{ly - 20}" width="44" height="26" rx="5" fill="rgba(203,213,225,.38)" stroke="rgba(226,232,240,.95)" stroke-width="2.5" stroke-dasharray="7 5"/>')
    o.append(f'<text x="{FX + 58}" y="{ly + 1}" font-size="28" font-weight="600" fill="#CBD5E1">{lg}</text>')
    o.append(f'<line x1="{GX - 40}" y1="{ly - 7}" x2="{GX + 4}" y2="{ly - 7}" stroke="{AMBER}" stroke-width="6"/>')
    o.append(f'<text x="{GX + 18}" y="{ly + 1}" font-size="28" font-weight="600" fill="#CBD5E1">{gp}</text>')
    o.append("</svg>")
    return "".join(o), H


def chart_height(ph_h, caption=False):
    return HEAD + (30 if caption else 0) + ph_h + 90
