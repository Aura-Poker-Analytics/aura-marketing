"""Gera o primeiro e-mail EN da escada do Grátis que não assina (R2 EN), no template v2, com o novidades() do #60 em inglês.

Uso: python -I content/email/_template/build_gratis_pais.py
Saída: content/email/gratis-por-pais/{r2-en-cupom,r2-en-controle}.html
Plano: docs/00-strategy/gratis-por-pais-plano.md (§4 e §8). O VOLTE50 vale em BRL e em USD (currency_options). Nada é enviado por este script.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from components import *  # noqa: E402,F403

OUT = pathlib.Path(__file__).resolve().parent.parent / "gratis-por-pais"
OUT.mkdir(exist_ok=True)

REASON_EN = "You're receiving this because you have a Free account on Aura Poker Analytics."
SEND = "RASCUNHO · não enviar sem o sim do Rafael digitado na sessão · MKT-D4"

# Mesmos 8 itens de NOVIDADES_60D (conferidos como "no ar" em 02/11), na mesma ordem. Se a lista em PT mudar, esta muda junto.
NOVIDADES_60D_EN = [
    ("GTO Mode", "The GTO range next to the field on every action of the flop, turn and river."),
    ("Preflop GTO under 20bb", "Preflop GTO at short stacks, under 20bb, in the spots already covered."),
    ("Field Exploits", "The spots where the field strays furthest from GTO, already ranked, now with turn and river. Every Monday, 2 come in and 2 go out."),
    ("Field Ranges", "The field's range hand by hand against GTO, with Copy Range to take into your study."),
    ("Field Trends", "How the field changed on each stat, now preflop too."),
    ("Showdown hand grid", "The hands the field shows at showdown on each action, on the 13x13 grid."),
    ("Dashboard home", "Aura's entry screen is now a dashboard, with what's new in plain sight."),
    ("Faster Postflop", "The Postflop screens load a lot faster."),
]
assert len(NOVIDADES_60D_EN) == len(NOVIDADES_60D), "a lista EN tem de ter os mesmos itens da PT"

NOTE_FREE = "All of this is in the Individual plan. On Free you see a preview of each screen."
TITLE = "Aura changed a lot in 60 days"
DATA = "Nov 30"
OFERTA = "50% off your first 3 months of the monthly Individual plan: $14.50 per month instead of $29. Enter the code at checkout."


def landing(c, k, anchor=""):
    return LANDING.format(c=c, k=k) + anchor


emails = {}

emails["r2-en-cupom"] = email(
    lang="en",
    title=f"{TITLE}. Come back for 50% off 3 months",
    preview=f"GTO Mode on turn and river, Field Exploits, Field Ranges and more. Code VOLTE50 until {DATA}.",
    headline="8 new things in Aura since you signed up.",
    sub=f"All in the last 60 days. And until {DATA} you can come back for 50% off your first 3 months:",
    blocks=[
        row(novidades(items=NOVIDADES_60D_EN, title="What's new in the last 60 days", note=NOTE_FREE, badge="NEW"), pad="0 40px 24px 40px"),
        row(code_box("VOLTE50", OFERTA, f"Valid until {DATA}, first subscription only."), pad="0 40px 24px 40px"),
    ],
    cta="Use my code",
    cta_url=landing("reativacao-gratis-en", "r2-cupom-en", "#planos"),
    note=para("Did you stop for a reason? Reply with one line.", size=15),
    unsub=BROADCAST_UNSUB,
    reason=REASON_EN,
    draft_note=f"R2 EN com cupom · Grátis que não assina e não é BR/PT · VOLTE50 vale em USD pelo currency_options do cupom R6eSQeTK · 80% do lote; 20% recebem o controle · {SEND} · docs/00-strategy/gratis-por-pais-plano.md",
)

emails["r2-en-controle"] = email(
    lang="en",
    title=TITLE,
    preview="GTO Mode on turn and river, Field Exploits, Field Ranges and more. Your login is the same.",
    headline="8 new things in Aura since you signed up.",
    sub="All in the last 60 days. Same login, nothing to set up:",
    blocks=[
        row(novidades(items=NOVIDADES_60D_EN, title="What's new in the last 60 days", note=NOTE_FREE, badge="NEW"), pad="0 40px 24px 40px"),
    ],
    cta="See the new Aura",
    cta_url=landing("reativacao-gratis-en", "r2-controle-en"),
    note=para("Did you stop for a reason? Reply with one line.", size=15),
    unsub=BROADCAST_UNSUB,
    reason=REASON_EN,
    draft_note=f"R2 EN controle · 20% do lote, o mesmo e-mail sem código · {SEND} · docs/00-strategy/gratis-por-pais-plano.md",
)

for name, html in emails.items():
    (OUT / f"{name}.html").write_text(html, encoding="utf-8")
    print("ok", name, len(html))
