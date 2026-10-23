"""Gera os e-mails de followup do Grátis no template base da Aura (v2, 23/10/2026).

Uso: python -I content/email/_template/build_followup.py
Saída: content/email/followup-*.html

Regras do template (docs/00-strategy/followup-cadastrados-gratis.md §10):
- só tabelas e estilo inline; o <style> do head só ajusta o celular (Gmail e Apple aceitam, Outlook ignora sem quebrar);
- Montserrat quando o cliente carrega webfont (Apple Mail, iOS), Arial nos outros;
- paleta da landing (.theme-a): fundo #0F1526, cartão #13192E, painel #1C2B47, borda #2F435C, dourado #D4A418;
- imagens só de URL pública que responde 200 (www.aura.poker/email e www.aurapoker.com/email).
"""
import pathlib

OUT = pathlib.Path(__file__).resolve().parent.parent

NIGHT, DECK, FELT, RAIL = "#0F1526", "#13192E", "#1C2B47", "#2F435C"
GOLD, GOLD_TXT, ON_GOLD = "#D4A418", "#E8BC3A", "#0F1526"
INK, INK2, INK3 = "#F5F6F8", "#C3C7D1", "#9AA0AE"
LOCK = "#6B7489"
FONT = "Montserrat,Arial,Helvetica,sans-serif"
LANDING = "https://www.aurapoker.com/?utm_source=email&utm_medium=email&utm_campaign={c}&utm_content={k}"
BATCH_UNSUB = "mailto:manager@aurapoker.com?subject=Descadastrar"  # o batch leva também List-Unsubscribe (P4)
BROADCAST_UNSUB = "{{{RESEND_UNSUBSCRIBE_URL}}}"


def para(text, size=16, color=INK2, mb=16, weight=400):
    return (f'<p style="margin:0 0 {mb}px 0; font-family:{FONT}; font-size:{size}px; '
            f'line-height:1.6; color:{color}; font-weight:{weight};">{text}</p>')


def row(inner, pad="0 40px", cls="px"):
    return f'<tr><td class="{cls}" style="padding:{pad};">{inner}</td></tr>'


def button(text, url):
    return f'''<table role="presentation" cellpadding="0" cellspacing="0" border="0" class="btn-wrap"><tr>
  <td align="center" bgcolor="{GOLD}" style="border-radius:8px; background-color:{GOLD};">
    <a href="{url}" class="btn" style="display:inline-block; padding:15px 30px; font-family:{FONT}; font-size:16px; font-weight:800; line-height:1.2; color:{ON_GOLD}; text-decoration:none; border-radius:8px;">{text}</a>
  </td></tr></table>'''


def panel(inner, title=None):
    head = ""
    if title:
        head = (f'<tr><td style="padding:16px 20px 12px 20px; border-bottom:1px solid {RAIL}; font-family:{FONT}; '
                f'font-size:14px; font-weight:700; color:{INK};">{title}</td></tr>')
    return f'''<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:{FELT}; border:1px solid {RAIL}; border-radius:10px;">
{head}<tr><td style="padding:6px 20px 8px 20px;">{inner}</td></tr></table>'''


def steps(items):
    rows = ""
    for i, (title, text) in enumerate(items, 1):
        border = "" if i == len(items) else f"border-bottom:1px solid {RAIL};"
        rows += f'''<tr>
  <td width="44" valign="top" style="padding:14px 0; {border}">
    <table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" valign="middle" width="30" height="30" style="width:30px; height:30px; border-radius:15px; border:2px solid {GOLD}; font-family:{FONT}; font-size:14px; font-weight:800; color:{GOLD_TXT};">{i}</td></tr></table>
  </td>
  <td valign="top" style="padding:14px 0; {border} font-family:{FONT};">
    <p style="margin:0 0 4px 0; font-size:16px; font-weight:700; line-height:1.4; color:{INK};">{title}</p>
    <p style="margin:0; font-size:14px; line-height:1.55; color:{INK2};">{text}</p>
  </td></tr>'''
    return f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{rows}</table>'


def compare(rows_):
    head = f'''<tr>
  <td style="padding:14px 0 10px 0; font-family:{FONT}; font-size:12px; color:{INK3};">&nbsp;</td>
  <td width="30%" style="padding:14px 8px 10px 8px; font-family:{FONT}; font-size:13px; font-weight:700; color:{INK3};">Grátis</td>
  <td width="34%" style="padding:14px 0 10px 8px; font-family:{FONT}; font-size:13px; font-weight:800; color:{GOLD_TXT};">Individual</td></tr>'''
    body = ""
    for label, free, paid in rows_:
        body += f'''<tr>
  <td valign="top" style="padding:11px 0; border-top:1px solid {RAIL}; font-family:{FONT}; font-size:14px; font-weight:700; line-height:1.4; color:{INK};">{label}</td>
  <td valign="top" style="padding:11px 8px; border-top:1px solid {RAIL}; font-family:{FONT}; font-size:14px; line-height:1.4; color:{LOCK};">{free}</td>
  <td valign="top" style="padding:11px 0 11px 8px; border-top:1px solid {RAIL}; font-family:{FONT}; font-size:14px; font-weight:600; line-height:1.4; color:{INK};">{paid}</td></tr>'''
    return f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{head}{body}</table>'


def bullets(items):
    out = ""
    for i, (b, t) in enumerate(items):
        border = "" if i == len(items) - 1 else f"border-bottom:1px solid {RAIL};"
        out += f'''<tr><td style="padding:13px 0; {border} font-family:{FONT};">
  <p style="margin:0 0 3px 0; font-size:16px; font-weight:700; color:{INK};">{b}</p>
  <p style="margin:0; font-size:14px; line-height:1.55; color:{INK2};">{t}</p></td></tr>'''
    return f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{out}</table>'


def image(src, alt, url, w=520):
    return (f'<a href="{url}" style="text-decoration:none;"><img src="{src}" width="{w}" alt="{alt}" '
            f'style="display:block; width:100%; max-width:{w}px; height:auto; border:0; border-radius:10px;"></a>')


def email(*, title, preview, headline, sub, blocks, cta, cta_url, note, unsub, reason, draft_note):
    body = "\n".join(blocks)
    return f'''<!DOCTYPE html>
<!-- {draft_note} -->
<html lang="pt-BR" xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="color-scheme" content="dark">
<meta name="supported-color-schemes" content="dark">
<meta name="x-apple-disable-message-reformatting">
<title>{title}</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>
  body {{ margin:0; padding:0; }}
  @media only screen and (max-width:620px) {{
    .shell {{ width:100% !important; }}
    .px {{ padding-left:20px !important; padding-right:20px !important; }}
    .h1 {{ font-size:26px !important; line-height:32px !important; }}
    .btn-wrap {{ width:100% !important; }}
    .btn {{ display:block !important; text-align:center !important; }}
  }}
</style>
</head>
<body style="margin:0; padding:0; width:100%; background-color:{NIGHT}; -webkit-text-size-adjust:100%; -ms-text-size-adjust:100%;">
<div style="display:none; max-height:0; overflow:hidden; mso-hide:all; font-size:1px; line-height:1px; color:{NIGHT}; opacity:0;">{preview}&#847;&zwnj;&nbsp;&#847;&zwnj;&nbsp;&#847;&zwnj;&nbsp;&#847;&zwnj;&nbsp;</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{NIGHT}" style="background-color:{NIGHT};">
<tr><td align="center" style="padding:28px 10px 36px 10px;">
<table role="presentation" class="shell" width="600" cellpadding="0" cellspacing="0" border="0" bgcolor="{DECK}" style="width:600px; max-width:600px; background-color:{DECK}; border:1px solid {RAIL}; border-radius:14px;">
{row(f"""<table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr>
<td style="padding-right:10px; vertical-align:middle;"><img src="https://www.aura.poker/email/aura-logo.png" width="35" height="28" alt="Aura" style="display:block; border:0;"></td>
<td style="vertical-align:middle; font-family:{FONT}; font-size:17px; font-weight:800; letter-spacing:5px; color:{INK};">AURA</td>
</tr></table>""", pad="30px 40px 0 40px")}
{row(f"""<h1 class="h1" style="margin:0; font-family:{FONT}; font-size:30px; line-height:36px; font-weight:800; color:{INK};">{headline}</h1>
<p style="margin:12px 0 0 0; font-family:{FONT}; font-size:17px; line-height:1.5; color:{INK2};">{sub}</p>""", pad="30px 40px 26px 40px")}
{body}
{row(button(cta, cta_url), pad="6px 40px 30px 40px")}
{row(note + para(f'Rafael<br><span style="color:{INK3}; font-weight:400;">Fundador da Aura</span>', size=15, color=INK, mb=0, weight=700), pad="24px 40px 32px 40px; border-top:1px solid " + RAIL)}
<tr><td class="px" bgcolor="{NIGHT}" style="padding:22px 40px 26px 40px; background-color:#0C1120; border-radius:0 0 14px 14px;">
{para(reason, size=12, color=INK3, mb=6)}
{para(f'<a href="{unsub}" style="color:{INK3}; text-decoration:underline;">Descadastrar</a> &nbsp;|&nbsp; Dúvidas no <a href="https://discord.gg/wYquSmUtAK" style="color:{INK3}; text-decoration:underline;">Discord</a>', size=12, color=INK3, mb=0)}
</td></tr>
</table>
</td></tr></table>
</body>
</html>
'''


REASON = "Você recebeu este e-mail porque tem uma conta Grátis na Aura Poker Analytics."

a1 = email(
    title="Sua conta na Aura está pronta: comece pelo c-bet do flop",
    preview="Escolha o spot. A Aura mostra o que o field faz ali e onde fica a faixa GTO.",
    headline="Escolha o spot. A Aura mostra o que o field faz ali.",
    sub="E onde fica a faixa GTO, ao lado. Sua conta Grátis abre o field de mais de 400 mil torneios, em buy-ins até US$ 22, torneios Vanilla, nas etapas de início e meio.",
    blocks=[
        row(panel(steps([
            ("Abra o Postflop no c-bet IP do flop", "Essa reação fica aberta no Grátis, no flop, no turn e no river."),
            ("Vá ao spot aberto: BTN vs BB, single raised pot, 30 a 60 big blinds", "Nele você vê quanto o field folda para cada size, com a faixa GTO ao lado."),
            ("Confira no seu board", "Filtre a textura do flop e veja se o número se mantém."),
        ]), title="Seu primeiro spot em três passos"), pad="0 40px 22px 40px"),
        row(para("Depois, passe no <strong style=\"color:#F5F6F8;\">Field Exploits</strong>. Toda semana, um dos 8 spots do plano Individual fica aberto no Grátis, inteiro: o número do field, o do GTO e como explorar.", mb=8)),
    ],
    cta="Abrir meu primeiro spot",
    cta_url=LANDING.format(c="ativacao", k="a1"),
    note=para("Uma pergunta: qual buy-in você mais joga, e o que você estuda hoje? Responda este e-mail com uma linha. Eu leio todas.", size=15),
    unsub=BATCH_UNSUB,
    reason=REASON,
    draft_note="RASCUNHO A1 v2 · segmento S1 (cadastrado sem uso) · lote semanal até a automação · não enviar sem a frase do Rafael · doc §4.1",
)

u1 = email(
    title="O spot que você abriu continua do outro lado do cadeado",
    preview="Todos os buy-ins, todas as etapas, turn e river e os 8 spots do Field Exploits.",
    headline="O spot que você abriu está no plano Individual.",
    sub="O cadeado aparece quando o spot sai do recorte Grátis. Isto é o que muda quando ele abre:",
    blocks=[
        row(panel(compare([
            ("Buy-ins", "até US$ 22", "todos"),
            ("Torneios", "Vanilla", "Vanilla, KO e Mystery"),
            ("Etapas", "início e meio", "todas, da bolha à mesa final"),
            ("Node-by-Node", "flop", "flop, turn e river"),
            ("Field Exploits", "1 spot da semana", "os 8 spots da semana"),
            ("Modo GTO", "amostra no spot aberto", "field e faixa GTO no flop, turn e river"),
            ("Exploit do Painel", "fixo", "um novo por semana"),
        ])), pad="0 40px 20px 40px"),
        row(para("Individual: R$ 150 ou US$ 29 por mês. No anual, R$ 1.295 ou US$ 259, cerca de US$ 21,58 por mês. O Modo GTO está incluso por tempo limitado.", size=15, mb=8)),
    ],
    cta="Ver planos",
    cta_url=LANDING.format(c="upgrade", k="u1") + "#planos",
    note=para("Se o que te travou foi outra coisa, responda este e-mail e me conte.", size=15),
    unsub=BATCH_UNSUB,
    reason=REASON,
    draft_note="RASCUNHO U1 v2 · segmento S3 (Grátis com gate_hit) · até 24 h do gate_hit; lote semanal até a automação · conferir logado no Individual os 8 spots do Field Exploits antes do envio · não enviar sem a frase do Rafael · doc §4.3",
)

r1 = email(
    title="Desde o seu último login, a Aura ganhou o GTO",
    preview="O field e a faixa GTO lado a lado. A amostra já está aberta no seu Grátis.",
    headline="A Aura agora mostra o GTO ao lado do field.",
    sub="Seu login é o mesmo, e a amostra já está aberta no seu Grátis.",
    blocks=[
        row(image("https://www.aurapoker.com/email/modo-gto-pt.png",
                  "Modo GTO: fold contra c-bet, field 46,0% e GTO 38,8%, ao lado da grade Field vs GTO do open do SB",
                  LANDING.format(c="reativacao-gratis", k="r1-a-img")), pad="0 40px 22px 40px"),
        row(panel(bullets([
            ("Modo GTO", "O que o field faz e onde fica a faixa GTO, no flop, turn e river. No Grátis: a amostra no spot aberto do c-bet IP do flop."),
            ("Field Ranges", "O range que o field abre e defende, mão a mão, ao lado do GTO. No Grátis: o open do CO e a reação do BB."),
            ("Field Exploits", "Os spots em que o field se afasta do GTO, com o exploit de cada um. No Grátis: o spot da semana, inteiro."),
        ]), title="Os três módulos novos"), pad="0 40px 24px 40px"),
    ],
    cta="Ver a nova Aura",
    cta_url=LANDING.format(c="reativacao-gratis", k="r1-a"),
    note="",
    unsub=BROADCAST_UNSUB,
    reason=REASON,
    draft_note="RASCUNHO R1 v2 · variante A do teste A/B (variante B no doc §6) · segmento S4 (Grátis inativo) · broadcast em lote, fora da reconquista · exclui pagantes e ex-pagantes · não enviar sem a frase do Rafael · doc §4.4",
)

for name, html in [("followup-a1-boas-vindas.html", a1), ("followup-u1-paywall.html", u1), ("followup-r1-reativacao.html", r1)]:
    (OUT / name).write_text(html, encoding="utf-8")
    print(name, len(html))
