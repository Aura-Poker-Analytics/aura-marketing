"""Gera o e-mail do dia seguinte ao cadastro (Grátis D1, Q23 aprovada pelo Rafael em 04/11/2026), em PT e EN.

Uso: python -I content/email/_template/build_gratis_d1.py
Saída: content/email/gratis-d1/{d1-pt,d1-en}.html

Brief: nota da HUB brief-email-dia-seguinte-2026-11-04.md. Público: content/email/gratis-d1/publico.sql.
Uma coisa só: o spot grátis da semana (o card que o Grátis vê em Exploits), com o número lido no dia por
content/email/gratis-d1/spot-da-semana.sql (mesma regra do PoolVsGtoRelease.FreeSpot da aura-api). Sem oferta e sem cupom.
Envio em batch transacional do Resend, com List-Unsubscribe no cabeçalho e mailto no rodapé. Nada é enviado por este script.
"""
import datetime
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from components import *  # noqa: E402,F403

OUT = pathlib.Path(__file__).resolve().parent.parent / "gratis-d1"
OUT.mkdir(exist_ok=True)

# Spot grátis da semana, lido em 04/11/2026 por spot-da-semana.sql: river:31:opening:btn_bb:1311, 60bb,
# release 02/11, snapshot 20261102, referência 20261022, direção underbet. Troca na segunda (próxima: 09/11).
SPOT = {"field": "27,7", "gto": "50,1", "lo": "43,1", "hi": "57,1"}
SPOT_SEMANA = (datetime.date(2026, 11, 2), datetime.date(2026, 11, 9))  # vale de segunda a domingo; fora disso, reler o SQL
# Fonte e conferência: content/email/gratis-d1/numeros-verificados.md

if not (SPOT_SEMANA[0] <= datetime.date.today() < SPOT_SEMANA[1]):
    sys.exit(f"SPOT vencido: vale de {SPOT_SEMANA[0]} a {SPOT_SEMANA[1]}. Rode spot-da-semana.sql, atualize SPOT, "
             "o numeros-verificados.md e passe pelo casa:revisor antes de gerar.")

SEND = "RASCUNHO · não enviar sem o sim do Rafael digitado na sessão · sem automação no Resend sem o sim dele"
UNSUB_EN = "mailto:manager@aurapoker.com?subject=Unsubscribe"

emails = {}

emails["d1-pt"] = email(
    title="O spot grátis da semana: o BTN dá delayed c-bet de menos no river",
    preview=f"Field {SPOT['field']}%, contra pelo menos {SPOT['lo']}% do GTO. Está aberto na sua conta Grátis.",
    headline="O BTN dá delayed c&#8209;bet de menos no river.",  # hífen que não quebra
    sub="Esse é o spot grátis da semana no Field Exploits, aberto na sua conta:",
    blocks=[
        row(gto_card(
            spot="BTN vs BB, single raised pot, 60 big blinds",
            context="Flop 9-high ou menor, two-tone, sem par, com OESD possível, qualquer turn e river. GTO chipEV · field de todos os tipos de torneio (Regular, KO e Mystery).",
            field=SPOT["field"], gto=SPOT["gto"], band=f"faixa GTO de {SPOT['lo']}% a {SPOT['hi']}%",
            verdict=f"<strong>Too passive:</strong> o field dá delayed c-bet em {SPOT['field']}%, contra pelo menos {SPOT['lo']}% do GTO. Quando ele aposta, folde mais as mãos marginais.",
            label="Field Exploits · spot grátis da semana",
        ), pad="0 40px 24px 40px"),
        row(para("O spot grátis troca toda segunda.", size=14, color=INK3, mb=8)),
    ],
    cta="Ver o spot grátis",
    cta_url=LANDING.format(c="gratis_d1", k="d1-pt"),
    note=para("Ficou alguma dúvida? Responda com uma linha.", size=15),
    unsub=BATCH_UNSUB,
    reason="Você recebeu este e-mail porque criou uma conta Grátis na Aura Poker Analytics.",
    draft_note=f"Dia seguinte, em PT · Grátis criado há 20 a 28 h sem 2º login · 1 e-mail por conta, nunca repetido · {SEND} · content/email/gratis-d1/",
)

emails["d1-en"] = email(
    lang="en",
    title="This week's free spot: BTN doesn't fire enough delayed c-bets on the river",
    preview=f"Field {SPOT['field'].replace(',', '.')}%, against at least {SPOT['lo'].replace(',', '.')}% for GTO. It's open on your Free account.",
    headline="BTN doesn't fire enough delayed c&#8209;bets on the river.",
    sub="This is this week's free spot in Field Exploits, open on your account:",
    blocks=[
        row(gto_card(
            spot="BTN vs BB, single raised pot, 60 big blinds",
            context="Flop 9-high or lower, two-tone, unpaired, with an OESD possible, any turn and river. GTO chipEV · field from every tournament type (Regular, KO and Mystery).",
            field=SPOT["field"].replace(",", "."), gto=SPOT["gto"].replace(",", "."),
            band=f"GTO range {SPOT['lo'].replace(',', '.')}% to {SPOT['hi'].replace(',', '.')}%",
            verdict=f"<strong>Too passive:</strong> the field delayed c-bets {SPOT['field'].replace(',', '.')}% of the time, against at least {SPOT['lo'].replace(',', '.')}% for GTO. When it bets, fold more of your bluff-catchers.",
            label="Field Exploits · this week's free spot",
        ), pad="0 40px 24px 40px"),
        row(para("The free spot changes every Monday.", size=14, color=INK3, mb=8)),
    ],
    cta="See the free spot",
    cta_url=LANDING.format(c="gratis_d1", k="d1-en"),
    note=para("Any questions? Reply with one line.", size=15),
    unsub=UNSUB_EN,
    reason="You're receiving this because you created a Free account on Aura Poker Analytics.",
    draft_note=f"Dia seguinte, em EN · Free account created 20 to 28 h ago, no 2nd login · 1 e-mail per account, never repeated · {SEND} · content/email/gratis-d1/",
)

for name, html in emails.items():
    (OUT / f"{name}.html").write_text(html, encoding="utf-8")
    print("ok", name, len(html))
