"""Componentes do template de e-mail da Aura (v2). Só constantes e funções: importar não gera nada.

Uso, a partir de outro script em content/email/:
    import sys, pathlib
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent / "_template"))  # ajuste ao caminho do script
    from components import *

Peças: para, row, button, panel, steps, compare, bullets, gto_card (rótulo em `label`, padrão "Modo GTO"), image e email.
Regras do template: ver o docstring de build_followup.py e a §10 de docs/00-strategy/followup-cadastrados-gratis.md.
"""

NIGHT, DECK, FELT, RAIL = "#0F1526", "#13192E", "#1C2B47", "#2F435C"
GOLD, GOLD_TXT, ON_GOLD = "#D4A418", "#E8BC3A", "#0F1526"
INK, INK2, INK3 = "#F5F6F8", "#C3C7D1", "#9AA0AE"
LOCK = "#6B7489"
FONT = "Montserrat,Arial,Helvetica,sans-serif"
LANDING = "https://www.aurapoker.com/?utm_source=email&utm_medium=email&utm_campaign={c}&utm_content={k}"
BATCH_UNSUB = "mailto:manager@aurapoker.com?subject=Descadastrar"  # o batch leva também List-Unsubscribe (P4)
BROADCAST_UNSUB = "{{{RESEND_UNSUBSCRIBE_URL}}}"
# logo oficial (o "A" e a palavra AURA em dourado, igual ao cabeçalho da landing); PNG 1011x209 servido pela landing desde o
# primeiro commit (aura-landing public/assets/logos). Exibida a 160x33, ou seja, com mais de 6x de resolução para tela retina.
LOGO = "https://www.aurapoker.com/assets/logos/Ativo%2078@2x.png"


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


FOLD, FOLD_GTO, TRACK = "#38ACC4", "#7FD3E3", "#0F1526"


def code_box(code, offer, validity):
    """Cupom: o código em destaque, a oferta e a validade. Sem imagem."""
    return f'''<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:{FELT}; border:1px dashed {GOLD}; border-radius:10px;">
<tr><td align="center" style="padding:22px 20px 8px 20px; font-family:{FONT}; font-size:14px; line-height:1.5; color:{INK2};">{offer}</td></tr>
<tr><td align="center" style="padding:4px 20px 6px 20px; font-family:{FONT}; font-size:28px; font-weight:800; letter-spacing:3px; color:{GOLD_TXT};">{code}</td></tr>
<tr><td align="center" style="padding:0 20px 20px 20px; font-family:{FONT}; font-size:13px; color:{INK3};">{validity}</td></tr>
</table>'''


def gto_card(spot, context, field, gto, band, verdict, label="Modo GTO"):
    """Quadro field x GTO de um spot, em tabela (sem imagem hospedada). Números só de numeros-verificados."""
    def bar(label, pct, color, value, sub=""):
        w = max(1, min(99, round(float(pct.replace(",", ".")))))
        subrow = f'<p style="margin:4px 0 0 0; font-family:{FONT}; font-size:12px; color:{INK3};">{sub}</p>' if sub else ""
        return f'''<tr>
  <td width="58" valign="top" style="padding:10px 0; font-family:{FONT}; font-size:13px; font-weight:700; color:{INK2};">{label}</td>
  <td valign="top" style="padding:13px 12px 10px 0;">
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-radius:6px;"><tr>
      <td width="{w}%" height="12" bgcolor="{color}" style="height:12px; line-height:12px; font-size:0; background-color:{color}; border-radius:6px 0 0 6px;">&nbsp;</td>
      <td height="12" bgcolor="{TRACK}" style="height:12px; line-height:12px; font-size:0; background-color:{TRACK}; border-radius:0 6px 6px 0;">&nbsp;</td>
    </tr></table>{subrow}
  </td>
  <td width="76" align="right" valign="top" style="padding:6px 0; font-family:{FONT}; font-size:22px; font-weight:800; color:{INK};">{value}</td></tr>'''
    return f'''<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:{FELT}; border:1px solid {RAIL}; border-radius:10px;">
<tr><td style="padding:18px 20px 6px 20px; font-family:{FONT};">
  <p style="margin:0 0 4px 0; font-size:12px; font-weight:700; color:{GOLD_TXT};">{label}</p>
  <p style="margin:0 0 4px 0; font-size:16px; font-weight:700; line-height:1.4; color:{INK};">{spot}</p>
  <p style="margin:0; font-size:14px; line-height:1.5; color:{INK2};">{context}</p>
</td></tr>
<tr><td style="padding:8px 20px 4px 20px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
{bar("Field", field, FOLD, field + "%")}
{bar("GTO", gto, FOLD_GTO, gto + "%", sub=band)}
</table></td></tr>
<tr><td style="padding:10px 20px 18px 20px; border-top:1px solid {RAIL}; font-family:{FONT}; font-size:14px; line-height:1.5; color:{INK};">{verdict}</td></tr>
</table>'''


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
{row(f'<a href="https://www.aurapoker.com/" style="text-decoration:none;"><img src="{LOGO}" width="160" height="33" alt="Aura" style="display:block; width:160px; height:33px; border:0;"></a>', pad="30px 40px 0 40px")}
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
