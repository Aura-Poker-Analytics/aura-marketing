"""Gera o HTML dos e-mails da reconquista 2026-11 no template base da Aura (v2, content/email/_template/).

Uso: python -I content/email/reconquista-2026-11/build_html.py  (escreve e1.html a e4.html nesta pasta)
Os componentes vêm de _template/components.py (importar não gera nada).
O e-mail 2 só sai depois da conferência logada do Rafael (gate R4 em sequencia.md).
Envio em batch transacional do Resend: descadastro por List-Unsubscribe no cabeçalho e mailto no rodapé (BATCH_UNSUB).
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "_template"))
from components import BATCH_UNSUB, GOLD_TXT, INK3, LANDING, bullets, email, gto_card, panel, para, row  # noqa: E402

CAMPAIGN = "reconquista-2026-11"
REASON = "Você recebeu este e-mail porque já foi assinante da Aura Poker Analytics."
OFFER = (f'Para quem já assinou, o primeiro mês do plano Individual mensal sai com <strong>80% de desconto</strong>, '
         f'de R$ 150 por R$ 30, com o código <strong style="color:{GOLD_TXT};">VOLTA</strong> no checkout. Vale até 16/11.')
FINE = para("O código VOLTA vale uma vez, no primeiro mês do plano Individual, até 16/11. "
            "Modo GTO incluso no plano Individual por tempo limitado.", size=14, color=INK3, mb=8)
DRAFT = "RASCUNHO {k} · reconquista dos ex-pagantes · batch transacional · não enviar sem a frase do Rafael · content/email/reconquista-2026-11/sequencia.md"


def mail(k, **kw):
    return email(cta_url=LANDING.format(c=CAMPAIGN, k=k), unsub=BATCH_UNSUB, reason=REASON,
                 draft_note=DRAFT.format(k=k.upper()), **kw)


e1 = mail(
    "e1",
    title="Desde que você saiu, a Aura ganhou o GTO",
    preview="O Field Exploits mostra spots em que o field se afasta forte do GTO. Para quem já assinou, 80% de desconto no primeiro mês até 16/11.",
    headline="Desde que você saiu, a Aura ganhou o GTO.",
    sub="O produto que você conheceu mudou bastante. Hoje a Aura mostra o GTO ao lado do field:",
    blocks=[
        row(panel(bullets([
            ("Modo GTO", "O número e a faixa GTO ao lado do que o field faz, no flop, turn e river."),
            ("Field Ranges", "O range que o field abre e defende, mão a mão, comparado ao GTO."),
            ("Field Exploits", "8 spots em que o field se afasta forte do GTO, em pares e stacks diferentes, cada um com o exploit pronto para usar. Toda segunda entram 2 novos."),
        ])), pad="0 40px 18px 40px"),
        row(para(OFFER)),
        row(FINE),
    ],
    cta="Ver a nova Aura",
    note="",
)

e2 = mail(
    "e2",
    title="Um spot em que o field erra contra o GTO esta semana",
    preview="Um dos 8 spots do Field Exploits, com o número do field, o do GTO e o exploit.",
    headline="Um spot desta semana no Field Exploits.",
    sub="É um spot, não a média do field. Os outros 7 estão no app.",
    blocks=[
        # números: content/posts/field-exploits-launch/numeros-verificados.md (main), linhas 32 e 86–92; snapshot 20261015
        row(gto_card(
            spot="UTG vs BB, single raised pot, 25 big blinds",
            context="Flop A-high two-tone, sem par, com OESD possível. Fold do BB contra c-bet de 50%.",
            field="53,8", gto="73,5", band="faixa GTO de 67,5% a 79,5%",
            verdict="<strong>Como explorar:</strong> o BB defende demais contra c-bet. Blefe menos e aposte mais por value.",
            label="Field Exploits",
        ), pad="0 40px 24px 40px"),
        row(para(f'O código <strong style="color:{GOLD_TXT};">VOLTA</strong> vale até 16/11: o primeiro mês do Individual mensal sai por R$ 30.')),
        row(FINE),
    ],
    cta="Ver os 8 spots",
    note="",
)

e3 = mail(
    "e3",
    title="2 spots novos hoje, e uma pergunta rápida",
    preview="O Field Exploits ganhou spots novos. E eu queria saber o que te fez sair.",
    headline="Hoje entraram 2 spots novos no Field Exploits.",
    sub="E uma pergunta rápida.",
    blocks=[
        row(para("O que te fez cancelar a Aura? Pode ser uma linha só, respondendo este e-mail. Eu leio todas, e isso decide o que a gente constrói a seguir.")),
        row(para(f'Se quiser voltar, o código <strong style="color:{GOLD_TXT};">VOLTA</strong> vale até domingo, 16/11.')),
        row(FINE),
    ],
    cta="Ver os spots novos",
    note="",
)

e4 = mail(
    "e4",
    title="O código VOLTA vence hoje",
    preview="80% de desconto no primeiro mês do Individual, até 23:59 de hoje.",
    headline="O código VOLTA vence hoje às 23:59.",
    sub="Com ele, o primeiro mês do plano Individual mensal sai por R$ 30 em vez de R$ 150.",
    blocks=[
        row(para("Desde 26/10, o Field Exploits recebeu 6 spots novos, cada um com o exploit.")),
        row(para("Depois disto, não mando mais nada sobre essa oferta.")),
        row(FINE),
    ],
    cta="Voltar para a Aura",
    note="",
)

for name, html in [("e1.html", e1), ("e2.html", e2), ("e3.html", e3), ("e4.html", e4)]:
    (HERE / name).write_text(html, encoding="utf-8")
    print(name, len(html))
