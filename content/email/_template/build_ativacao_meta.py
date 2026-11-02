"""Gera a escada de ativação dos cadastrados da Meta (SINAL01), PT e EN, no template v2.

Uso: python -I content/email/_template/build_ativacao_meta.py
Saída: content/email/ativacao-meta/{a2,a3,u2}-{pt,en}.html, a1-en.html e u1-en.html.
O A1 PT e o U1 PT continuam em content/email/followup-a1-boas-vindas.html e followup-u1-paywall.html.
Plano: docs/00-strategy/ativacao-meta-escada.md. Nada é enviado por este script.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from components import *  # noqa: E402,F403

OUT = pathlib.Path(__file__).resolve().parent.parent / "ativacao-meta"
OUT.mkdir(exist_ok=True)

REASON = {
    "pt": "Você recebeu este e-mail porque tem uma conta Grátis na Aura Poker Analytics.",
    "en": "You're receiving this because you have a Free account on Aura Poker Analytics.",
}
UNSUB = {"pt": BATCH_UNSUB, "en": BATCH_UNSUB.replace("Descadastrar", "Unsubscribe")}
SEND = "RASCUNHO · não enviar sem o sim do Rafael digitado na sessão · MKT-D4: sem automação antes da ficha de LGPD"


def landing(c, k, anchor=""):
    return LANDING.format(c=c, k=k) + anchor


emails = {}

# ---------------------------------------------------------------- A1 PT (D0/D1): mesmo corpo do followup-a1, com a campanha da Meta
emails["a1-pt"] = email(
    title="Sua conta na Aura está pronta: comece pelo c-bet do flop",
    preview="Escolha o spot. A Aura mostra o que o field faz ali e onde fica a faixa GTO.",
    headline="Escolha o spot. A Aura mostra o que o field faz ali.",
    sub="E onde fica a faixa GTO. Comece pelo spot aberto no seu Grátis:",
    blocks=[row(panel(steps([
        ("Abra o c-bet IP do flop no Postflop", "A reação é livre no Grátis."),
        ("Vá ao BTN vs BB, 30 a 60 big blinds", "Veja o fold do field por size, com a faixa GTO."),
        ("Filtre a textura do flop", "Confira se o número se mantém no seu board."),
    ])), pad="0 40px 24px 40px")],
    cta="Abrir meu primeiro spot",
    cta_url=landing("ativacao-meta", "a1"),
    note=para("Qual buy-in você mais joga? Responda com uma linha.", size=15),
    unsub=UNSUB["pt"], reason=REASON["pt"],
    draft_note=f"A1 em português · D0/D1 · cadastrados da Meta em português · {SEND}",
)

# ---------------------------------------------------------------- A1 EN (D0/D1)
emails["a1-en"] = email(
    lang="en",
    title="Your Aura account is ready: start with the flop c-bet",
    preview="Pick a spot. Aura shows what the field does there and where the GTO range sits.",
    headline="Pick a spot. Aura shows what the field does there.",
    sub="And where the GTO range sits. Start with the spot open on your Free plan:",
    blocks=[row(panel(steps([
        ("Open the IP c-bet on the flop in Postflop", "The reaction is free on the Free plan."),
        ("Go to BTN vs BB, 30 to 60 big blinds", "See the field's fold by size, with the GTO range."),
        ("Filter the flop texture", "Check the number holds on your board."),
    ])), pad="0 40px 24px 40px")],
    cta="Open my first spot",
    cta_url=landing("ativacao-meta", "a1-en"),
    note=para("Which buy-in do you play most? Reply with one line.", size=15),
    unsub=UNSUB["en"], reason=REASON["en"],
    draft_note=f"A1 EN · D0/D1 · cadastrados da Meta em inglês · {SEND}",
)

# ---------------------------------------------------------------- A2 (D2, só sem primeira análise)
emails["a2-pt"] = email(
    title="O spot da semana no Field Exploits, aberto no seu Grátis",
    preview="Um spot real do plano Individual, inteiro: o número do field, o do GTO e como explorar.",
    headline="Um spot do plano Individual, aberto no seu Grátis.",
    sub="Toda semana, um dos 8 spots do Field Exploits fica aberto, inteiro. Nesta semana: <strong>[SPOT: posições e stack]</strong>.",
    blocks=[row(panel(bullets([
        ("O número do field", "O que a mesa realmente faz nesse spot."),
        ("O número do GTO e a faixa", "Onde o field se afasta do GTO."),
        ("Como explorar", "O ajuste, em uma linha."),
    ])), pad="0 40px 24px 40px")],
    cta="Ver o spot da semana",
    cta_url=landing("ativacao-meta", "a2"),
    note=para("Abriu e travou em algum ponto? Responda este e-mail.", size=15),
    unsub=UNSUB["pt"], reason=REASON["pt"],
    draft_note=f"A2 em português · D2, só quem não fez a primeira análise · preencher [SPOT] com o free_week da semana, conferido logado (G2), antes do envio · {SEND}",
)
emails["a2-en"] = email(
    lang="en",
    title="This week's Field Exploits spot, open on your Free plan",
    preview="A real Individual-plan spot, in full: the field number, the GTO number and how to exploit it.",
    headline="An Individual-plan spot, open on your Free plan.",
    sub="Every week, one of the 8 Field Exploits spots is open in full. This week: <strong>[SPOT: positions and stack]</strong>.",
    blocks=[row(panel(bullets([
        ("The field number", "What the table actually does in this spot."),
        ("The GTO number and the range", "Where the field drifts from GTO."),
        ("How to exploit it", "The adjustment, in one line."),
    ])), pad="0 40px 24px 40px")],
    cta="See this week's spot",
    cta_url=landing("ativacao-meta", "a2-en"),
    note=para("Opened it and got stuck somewhere? Reply to this email.", size=15),
    unsub=UNSUB["en"], reason=REASON["en"],
    draft_note=f"A2 EN · D2, only if no first analysis · fill [SPOT] with the week's free_week spot, checked logged in (G2), before sending · {SEND}",
)

# ---------------------------------------------------------------- A3 (D5, "travou?", sem botão grande)
emails["a3-pt"] = email(
    title="Travou em algum passo?",
    preview="Duas coisas costumam travar no começo. Se for outra, me conta.",
    headline="Travou em algum passo?",
    sub="Sem pressão. Duas coisas costumam travar no começo:",
    blocks=[row(panel(bullets([
        ("Filtro fora do recorte Grátis", "O Grátis cobre buy-ins até US$ 22, Vanilla, início e meio. Fora disso aparece o cadeado."),
        ("Não achou o spot", "Comece pelo c-bet IP do flop, no Postflop. Ele fica aberto."),
    ])), pad="0 40px 24px 40px")],
    cta=None, cta_url="",
    note=para(f'Me conta numa linha o que travou. Eu leio e respondo. <a href="{landing("ativacao-meta", "a3")}" style="color:{GOLD_TXT};">Abrir a Aura</a>', size=15),
    unsub=UNSUB["pt"], reason=REASON["pt"],
    draft_note=f"A3 em português · D5, só quem não fez a primeira análise · link simples, sem botão grande · {SEND}",
)
emails["a3-en"] = email(
    lang="en",
    title="Stuck on a step?",
    preview="Two things usually get in the way early on. If it is something else, tell me.",
    headline="Stuck on a step?",
    sub="No pressure. Two things usually get in the way early on:",
    blocks=[row(panel(bullets([
        ("A filter outside the Free scope", "Free covers buy-ins up to US$ 22, Vanilla, early and middle stages. Outside that you will see the lock."),
        ("Could not find the spot", "Start with the IP c-bet on the flop, in Postflop. It is open."),
    ])), pad="0 40px 24px 40px")],
    cta=None, cta_url="",
    note=para(f'Tell me in one line what got in the way. I read and reply. <a href="{landing("ativacao-meta", "a3-en")}" style="color:{GOLD_TXT};">Open Aura</a>', size=15),
    unsub=UNSUB["en"], reason=REASON["en"],
    draft_note=f"A3 EN · D5, only if no first analysis · plain link, no big button · {SEND}",
)

# ---------------------------------------------------------------- U1 EN (o PT já existe em followup-u1-paywall.html)
emails["u1-en"] = email(
    lang="en",
    title="The spot you opened is still behind the lock",
    preview="Every buy-in, every stage, turn and river, and all 8 Field Exploits spots.",
    headline="The spot you opened is in the Individual plan.",
    sub="Here's what the lock hides:",
    blocks=[
        row(panel(compare([
            ("Buy-ins", "up to US$ 22", "all"),
            ("Tournaments", "Vanilla", "Vanilla, KO and Mystery"),
            ("Stages", "early and middle", "all"),
            ("Node-by-Node", "flop", "flop, turn and river"),
            ("Field Exploits", "1 spot", "all 8 of the week"),
        ], lang="en")), pad="0 40px 18px 40px"),
        row(para("US$ 29 per month. GTO Mode included in the Individual plan for a limited time.", size=14, color=INK3, mb=8)),
    ],
    cta="See plans",
    cta_url=landing("upgrade-meta", "u1-en", "#planos"),
    note=para("Did something get in the way? Reply to this email.", size=15),
    unsub=UNSUB["en"], reason=REASON["en"],
    draft_note=f"U1 EN · só quem bateu no paywall (gate_hit) · conferir logado os 8 spots do Field Exploits (G1) · {SEND}",
)

# ---------------------------------------------------------------- U2 (cupom de ativação; só gate_hit sem assinatura em 72 h)
OFERTA_PT = "30% no primeiro mês do plano Individual mensal: R$ 105 em vez de R$ 150."
OFERTA_EN = "30% off your first month of the monthly Individual plan: US$ 20 instead of US$ 29."
emails["u2-pt"] = email(
    title="30% no seu primeiro mês do Individual, até [DATA]",
    preview="O spot que você abriu, com 30% de desconto no primeiro mês. Código válido até [DATA].",
    headline="O spot que você abriu, com 30% no primeiro mês.",
    sub="Use o código no checkout do plano Individual:",
    blocks=[row(code_box("[CÓDIGO]", OFERTA_PT, "Válido até [DATA], uma vez por conta."), pad="0 40px 24px 40px")],
    cta="Usar meu código",
    cta_url=landing("upgrade-meta", "u2-cupom", "#planos"),
    note=para("Algo te travou? Responda este e-mail.", size=15),
    unsub=UNSUB["pt"], reason=REASON["pt"],
    draft_note=f"U2 em português · só quem bateu no paywall e não assinou em 72 h (80% cupom, 20% controle sem cupom) · cupom Ph7y2HU9, promotion code ATIVAddmm criado pelo Rafael · {SEND}",
)
emails["u2-en"] = email(
    lang="en",
    title="30% off your first month of Individual, until [DATE]",
    preview="The spot you opened, with 30% off your first month. Code valid until [DATE].",
    headline="The spot you opened, 30% off your first month.",
    sub="Use the code at checkout on the Individual plan:",
    blocks=[row(code_box("[CODE]", OFERTA_EN, "Valid until [DATE], once per account."), pad="0 40px 24px 40px")],
    cta="Use my code",
    cta_url=landing("upgrade-meta", "u2-cupom-en", "#planos"),
    note=para("Did something get in the way? Reply to this email.", size=15),
    unsub=UNSUB["en"], reason=REASON["en"],
    draft_note=f"U2 EN · only gate_hit users with no subscription after 72 h (80% coupon, 20% control without) · coupon Ph7y2HU9, promotion code ATIVAddmm created by Rafael · {SEND}",
)

for k, html in emails.items():
    (OUT / f"{k}.html").write_text(html, encoding="utf-8")
    print(k, len(html))
