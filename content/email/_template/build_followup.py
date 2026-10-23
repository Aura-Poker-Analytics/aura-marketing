"""Gera os e-mails de followup do Grátis no template base da Aura (v2, 23/10/2026).

Uso: python -I content/email/_template/build_followup.py
Saída: content/email/followup-*.html

Regras do template (docs/00-strategy/followup-cadastrados-gratis.md §10):
- só tabelas e estilo inline; o <style> do head só ajusta o celular (Gmail e Apple aceitam, Outlook ignora sem quebrar);
- Montserrat quando o cliente carrega webfont (Apple Mail, iOS), Arial nos outros;
- paleta da landing (.theme-a): fundo #0F1526, cartão #13192E, painel #1C2B47, borda #2F435C, dourado #D4A418;
- imagens só de URL pública que responde 200 (www.aurapoker.com/assets/logos para a logo, www.aurapoker.com/email e www.aura.poker/email);
- cabeçalho = a logo oficial em PNG (nunca o ícone com a palavra montada em texto).
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from components import *  # noqa: E402,F403

OUT = pathlib.Path(__file__).resolve().parent.parent

REASON = "Você recebeu este e-mail porque tem uma conta Grátis na Aura Poker Analytics."

a1 = email(
    title="Sua conta na Aura está pronta: comece pelo c-bet do flop",
    preview="Escolha o spot. A Aura mostra o que o field faz ali e onde fica a faixa GTO.",
    headline="Escolha o spot. A Aura mostra o que o field faz ali.",
    sub="E onde fica a faixa GTO. Comece pelo spot aberto no seu Grátis:",
    blocks=[
        row(panel(steps([
            ("Abra o c-bet IP do flop no Postflop", "A reação é livre no Grátis."),
            ("Vá ao BTN vs BB, 30 a 60 big blinds", "Veja o fold do field por size, com a faixa GTO."),
            ("Filtre a textura do flop", "Confira se o número se mantém no seu board."),
        ])), pad="0 40px 24px 40px"),
    ],
    cta="Abrir meu primeiro spot",
    cta_url=LANDING.format(c="ativacao", k="a1"),
    note=para("Qual buy-in você mais joga? Responda com uma linha.", size=15),
    unsub=BATCH_UNSUB,
    reason=REASON,
    draft_note="RASCUNHO A1 v2 · segmento S1 (cadastrado sem uso) · lote semanal até a automação · não enviar sem a frase do Rafael · doc §4.1",
)

u1 = email(
    title="O spot que você abriu continua do outro lado do cadeado",
    preview="Todos os buy-ins, todas as etapas, turn e river e os 8 spots do Field Exploits.",
    headline="O spot que você abriu está no plano Individual.",
    sub="Isto é o que o cadeado esconde:",
    blocks=[
        row(panel(compare([
            ("Buy-ins", "até US$ 22", "todos"),
            ("Torneios", "Vanilla", "Vanilla, KO e Mystery"),
            ("Etapas", "início e meio", "todas"),
            ("Node-by-Node", "flop", "flop, turn e river"),
            ("Field Exploits", "1 spot", "os 8 da semana"),
        ])), pad="0 40px 18px 40px"),
        row(para("R$ 150 ou US$ 29 por mês. Modo GTO incluso no plano Individual por tempo limitado.", size=14, color=INK3, mb=8)),
    ],
    cta="Ver planos",
    cta_url=LANDING.format(c="upgrade", k="u1") + "#planos",
    note=para("Algo te travou? Responda este e-mail.", size=15),
    unsub=BATCH_UNSUB,
    reason=REASON,
    draft_note="RASCUNHO U1 v2 · segmento S3 (Grátis com gate_hit) · até 24 h do gate_hit; lote semanal até a automação · conferir logado no Individual os 8 spots do Field Exploits antes do envio · não enviar sem a frase do Rafael · doc §4.3",
)

r1 = email(
    title="Desde o seu último login, a Aura ganhou o GTO",
    preview="O field e a faixa GTO lado a lado. A amostra já está aberta no seu Grátis.",
    headline="A Aura agora mostra o GTO ao lado do field.",
    sub="Seu login é o mesmo. Um spot do que mudou:",
    blocks=[
        # números: aura-main/_ops/golive-gto-2026-10-04/numeros-verificados.md, exemplo (a), medido em 08/10 e reconferido em 13/10
        row(gto_card(
            spot="CO vs BB, single raised pot, 30 a 60 big blinds",
            context="Flop K-high two-tone. Fold do BB contra c-bet de 33%.",
            field="46,0", gto="38,8", band="faixa GTO de 37,1% a 40,4%",
            verdict="<strong>Overfold:</strong> o field folda 7,2% acima do GTO.",
        ), pad="0 40px 24px 40px"),
    ],
    cta="Ver a nova Aura",
    cta_url=LANDING.format(c="reativacao-gratis", k="r1-a"),
    note="",
    unsub=BROADCAST_UNSUB,
    reason=REASON,
    draft_note="RASCUNHO R1 v2 · variante A do teste A/B (variante B no doc §6) · segmento S4 (Grátis inativo) · broadcast em lote, fora da reconquista · exclui pagantes e ex-pagantes · não enviar sem a frase do Rafael · doc §4.4",
)

# Cupom de ativação (R4 aprovada pelo Rafael em 23/10 e ampliada): [CÓDIGO] e [DATA] são preenchidos por lote,
# com o promotion code criado pelo Rafael no Stripe (spec no doc §12). Quem cai no controle de 20% recebe a versão sem cupom.
OFERTA = "30% no primeiro mês do plano Individual mensal: R$ 105 em vez de R$ 150, ou US$ 20 em vez de US$ 29."

u2 = email(
    title="30% no seu primeiro mês do Individual, até [DATA]",
    preview="O spot que você abriu, com 30% de desconto no primeiro mês. Código válido até [DATA].",
    headline="O spot que você abriu, com 30% no primeiro mês.",
    sub="Use o código no checkout do plano Individual:",
    blocks=[
        row(code_box("[CÓDIGO]", OFERTA, "Válido até [DATA], uma vez por conta."), pad="0 40px 24px 40px"),
    ],
    cta="Usar meu código",
    cta_url=LANDING.format(c="upgrade", k="u2-cupom") + "#planos",
    note=para("Algo te travou? Responda este e-mail.", size=15),
    unsub=BATCH_UNSUB,
    reason=REASON,
    draft_note="RASCUNHO U2 com cupom · segmento S3 (bateu no paywall e não assinou em 72 h) · 80% do lote; os 20% do controle recebem o U2 sem cupom · [CÓDIGO] e [DATA] por lote · não enviar sem o vai da HUB · doc §4.3 e §12",
)

r2 = email(
    title="Volte para a Aura com 30% no primeiro mês, até [DATA]",
    preview="O Modo GTO e o Field Exploits esperam por você. 30% no primeiro mês do Individual, até [DATA].",
    headline="Volte com 30% no primeiro mês.",
    sub="Seu login é o mesmo. O código vale no checkout do plano Individual:",
    blocks=[
        row(code_box("[CÓDIGO]", OFERTA, "Válido até [DATA], uma vez por conta."), pad="0 40px 24px 40px"),
    ],
    cta="Usar meu código",
    cta_url=LANDING.format(c="reativacao-gratis", k="r2-cupom") + "#planos",
    note=para("Parou por algum motivo? Responda com uma linha.", size=15),
    unsub=BROADCAST_UNSUB,
    reason=REASON,
    draft_note="RASCUNHO R2 com cupom · segmento S4 (Grátis, nunca bateu no paywall, sem login 5 dias depois do R1) · 80% do lote; os 20% do controle recebem o R2 sem cupom (spot da semana) · [CÓDIGO] e [DATA] por lote · não enviar sem o vai da HUB · doc §4.4 e §12",
)

for name, html in [("followup-a1-boas-vindas.html", a1), ("followup-u1-paywall.html", u1), ("followup-r1-reativacao.html", r1),
                   ("followup-u2-cupom.html", u2), ("followup-r2-cupom.html", r2)]:
    (OUT / name).write_text(html, encoding="utf-8")
    print(name, len(html))
