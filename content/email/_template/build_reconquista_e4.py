"""Gera o e4 da reconquista (ex-pagantes) no template base da Aura (v2), com o VOLTA70 e as novidades dos últimos 60 dias.

Uso: python -I content/email/_template/build_reconquista_e4.py
Saída: content/email/reconquista-2026-11/e4-volta70.html e .txt

Decisão do Rafael em 02/11 ("e3 sai, 70% no e4"): o e4 vira um e-mail novo, com o bloco de novidades do R2 do followup
e o VOLTA70 (cupom I2sJ1r09, promo_1UXLEqIsnKTRWBVci5Ybstmg: R$ 105 a menos por mês nos 3 primeiros meses, só Individual,
40 usos, até 30/11). O VOLTA70 substitui o VOLTA. Data proposta: seg. 09/11, 10h (_ops/email-calendario-2026-11.md).
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from components import *  # noqa: E402,F403

OUT = pathlib.Path(__file__).resolve().parent.parent / "reconquista-2026-11"

CODIGO, DATA = "VOLTA70", "30/11"
OFERTA = "70% nos 3 primeiros meses do plano Individual mensal: R$ 45 por mês em vez de R$ 150."
TITULO = "A Aura mudou muito desde que você saiu"
PREVIEW = f"Modo GTO no turn e no river, Field Exploits, Field Ranges e mais. Volte com 70% por 3 meses até {DATA}."
REASON = "Você recebeu este e-mail porque já assinou a Aura Poker Analytics."
URL = LANDING.format(c="reconquista-2026-11", k="e4-volta70") + "#planos"

e4 = email(
    title=f"{TITULO}. Volte com 70% por 3 meses",
    preview=PREVIEW,
    headline=f"{TITULO}.",
    sub=f"Em 60 dias entraram 8 novidades. E até {DATA} você volta com 70% nos 3 primeiros meses:",
    blocks=[
        row(novidades(note="Tudo isso está no plano Individual."), pad="0 40px 24px 40px"),
        row(code_box(CODIGO, OFERTA, f"Válido até {DATA}, no plano Individual."), pad="0 40px 16px 40px"),
        row(para(f"O {CODIGO} substitui o código VOLTA dos e-mails anteriores: vale mais e por mais tempo.",
                 size=14, color=INK3, mb=24)),
    ],
    cta="Usar meu código",
    cta_url=URL,
    note=para("Se algo te fez sair, responda com uma linha. Eu leio todas.", size=15),
    unsub=BATCH_UNSUB,
    reason=REASON,
    draft_note="RASCUNHO e4 da reconquista com o VOLTA70 · ex-pagantes sem assinatura ativa (Stripe, Woo e NOWPayments conferidos no dia) · seg. 09/11 10h · não enviar sem o sim do Rafael digitado na sessão da reconquista · _ops/email-calendario-2026-11.md",
)

TXT = f"""{TITULO}.

Em 60 dias entraram 8 novidades. E até {DATA} você volta com 70% nos 3 primeiros meses.

O que entrou na Aura nos últimos 60 dias:
""" + "\n".join(f"- {n}: {t}" for n, t in NOVIDADES_60D) + f"""

Tudo isso está no plano Individual.

Código: {CODIGO}
{OFERTA}
Válido até {DATA}, no plano Individual.

O {CODIGO} substitui o código VOLTA dos e-mails anteriores: vale mais e por mais tempo.

Usar meu código: {URL}

Se algo te fez sair, responda com uma linha. Eu leio todas.

Rafael
Fundador da Aura

{REASON}
Descadastrar: {BATCH_UNSUB}
"""

OUT.mkdir(exist_ok=True)
(OUT / "e4-volta70.html").write_text(e4, encoding="utf-8")
(OUT / "e4-volta70.txt").write_text(TXT, encoding="utf-8")
print("e4-volta70.html", len(e4), "| links:", sorted(set(re.findall(r'href="([^"]+)"', e4))))
