"""Modo GTO - e-mail (PT e EN): imagem do slot + email-pt.html, email-en.html e os .preview.html.

Tudo vem de numbers.json (lib.py). Faltando N1..N4, ou a imagem do slot, o e-mail sai em DRAFT:
 - marcadores [[N..]] vermelhos no texto, faixa "RASCUNHO - NAO ENVIAR" no topo, <title> com [DRAFT];
 - imagem do slot com o rotulo [PRINT DE PRODUCAO PENDENTE], nomeada email/modo-gto-<lang>-DRAFT.png.
Pronto: imagem email/modo-gto-<lang>.png (o -DRAFT some) e HTML sem faixa nem marcador.

Imagem do slot (numbers.json "email_image"):
  "print": captura de producao prints/prod/postflop-<lang>.png|jpg, enquadrada (padrao).
  "bars":  as duas barras field x GTO renderizadas aqui com N2/N3 (alternativa do email.md).

Uso: python build_email.py   (depois ou antes de build.py; nao depende dele)
Nao envia nada e nao toca no Resend. Antes do envio, hospedar email/modo-gto-<lang>.png em https://www.aurapoker.com/email/.
"""
import html as H
import re
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont
from playwright.sync_api import sync_playwright

import lib
from lib import ASSETS, EMAIL, POST, SRC, Ex, chart_svg, find_print, fnum, has_text, pct, ph_email

BG_MAIL = (11, 18, 32)  # #0b1220
W = 1200
M = 14
INNER = W - 2 * M
FRAME = (30, 41, 59)
FONT = "C:/Windows/Fonts/segoeui.ttf"
FONTB = "C:/Windows/Fonts/segoeuib.ttf"

CP = {
    "pt": dict(
        lang_attr="pt-BR", subject="Novo na Aura: Modo GTO", h1="Novo na Aura: Modo GTO",
        tagline="O GTO e o field na mesma tela.",
        pre="Novo na Aura: Modo GTO. O número GTO e a faixa GTO ao lado de cada número do field.",
        btn="Conhecer o Modo GTO",
        under="O Modo GTO é um plano pago. A conta grátis segue com o field e a comparação com o MDF; o número GTO e a faixa são do plano Modo GTO. Poker é jogo de habilidade e estudo. 18+.",
        alt="Modo GTO no Postflop Analysis: o número do field e o número GTO com a faixa GTO, lado a lado, no mesmo spot.",
        f1="Você recebeu este e-mail porque criou uma conta na Aura Poker Analytics.",
        f2='Não quer mais e-mails como este? <a href="{{{RESEND_UNSUBSCRIBE_URL}}}" style="color:#aab6c8; text-decoration:underline;">Descadastrar</a> · Dúvidas no <a href="https://discord.gg/wYquSmUtAK" style="color:#aab6c8; text-decoration:underline;">Discord</a>.',
        f3="Fale com a gente:",
        draft="RASCUNHO · NÃO ENVIAR · falta: ",
    ),
    "en": dict(
        lang_attr="en", subject="New on Aura: GTO Mode", h1="New on Aura: GTO Mode",
        tagline="GTO and the field on the same screen.",
        pre="New on Aura: GTO Mode. The GTO number and the GTO range next to every field number.",
        btn="See GTO Mode",
        under="GTO Mode is a paid plan. The free account keeps the field and the MDF comparison; the GTO number and range are on the GTO Mode plan. Poker is a game of skill and study. 18+.",
        alt="GTO Mode in Postflop Analysis: the field number and the GTO number with the GTO range, side by side, in the same spot.",
        f1="You received this email because you created an account on Aura Poker Analytics.",
        f2='Don\'t want emails like this anymore? <a href="{{{RESEND_UNSUBSCRIBE_URL}}}" style="color:#aab6c8; text-decoration:underline;">Unsubscribe</a> · Questions? Find us on <a href="https://discord.gg/wYquSmUtAK" style="color:#aab6c8; text-decoration:underline;">Discord</a>.',
        f3="Reach us:",
        draft="DRAFT · DO NOT SEND · missing: ",
    ),
}


# ---------------------------------------------------------------- texto do exemplo (email.md)
def example_html(lang, n):
    """Paragrafo do exemplo, na redacao de email.md. Retorna (html, faltando)."""
    ex = Ex(n, lang, mark=ph_email)
    pos = ex.position
    miss = ex.missing(with_n1=True, with_n4=(pos != "inside"))
    long_n1 = ((n.get("N1") or {}).get(f"email_{lang}") or "").strip()      # contexto completo do spot (email.md)
    if has_text(long_n1):
        n1 = H.escape(long_n1.rstrip("."))
    elif ex.n1:
        n1 = H.escape(ex.n1.rstrip("."))
        miss.append("N1.email")
    else:
        n1 = ex.s_n1()
    lo = fnum(ex.lo, lang, n) if ex.lo is not None else None
    hi = fnum(ex.hi, lang, n) if ex.hi is not None else None
    rng = f"{lo}–{hi}%" if lo and hi else ph_email("N3")
    if lang == "pt":
        head = f"Exemplo: {n1}. O field folda {ex.s_n2()} contra {pct(ex.c, lang, n) if ex.c is not None else ph_email('N3')} do GTO (faixa {rng}): "
        above = f"{ex.s_n4()} pp acima do topo da faixa. Aqui o field folda mais do que o GTO. "
        below = f"{ex.s_n4()} pp abaixo da base da faixa. Aqui o field folda menos do que o GTO. "
        inside = ph_email("LEITURA: field dentro da faixa GTO, copy a definir") + " "
        tail = "É um spot, não a média do field. Confira no seu board."
    else:
        head = f"Example: {n1}. The field folds {ex.s_n2()} against GTO's {pct(ex.c, lang, n) if ex.c is not None else ph_email('N3')} (range {rng}): "
        above = f"{ex.s_n4()} pp above the top of the range. Here the field folds more than GTO does. "
        below = f"{ex.s_n4()} pp below the bottom of the range. Here the field folds less than GTO does. "
        inside = ph_email("LEITURA: field inside the GTO range, copy to be defined") + " "
        tail = "This is one spot, not the field average. Check it on your board."
    if pos == "inside":
        read = inside
        miss.append("LEITURA")
    elif pos == "below":
        read = below
    else:                       # acima, ou ainda indefinido (rascunho: usa o texto de "acima" do email.md)
        read = above
    return head + read + tail, miss


# ---------------------------------------------------------------- imagem do slot
def _font(path, size):
    return ImageFont.truetype(path, size)


def _dashed_rect(d, box, color, width=4, dash=22, gap=14):
    x0, y0, x1, y1 = box
    for x in range(x0, x1, dash + gap):
        d.line([(x, y0), (min(x + dash, x1), y0)], fill=color, width=width)
        d.line([(x, y1), (min(x + dash, x1), y1)], fill=color, width=width)
    for y in range(y0, y1, dash + gap):
        d.line([(x0, y), (x0, min(y + dash, y1))], fill=color, width=width)
        d.line([(x1, y), (x1, min(y + dash, y1))], fill=color, width=width)


def placeholder_image(lang):
    h = 700
    im = Image.new("RGB", (W, h), BG_MAIL)
    d = ImageDraw.Draw(im)
    _dashed_rect(d, (M + 6, M + 6, W - M - 6, h - M - 6), (251, 191, 36))
    f1, f2 = _font(FONTB, 54), _font(FONT, 30)
    t1 = "[PRINT DE PRODUÇÃO PENDENTE]"
    d.text(((W - d.textlength(t1, font=f1)) / 2, h / 2 - 70), t1, font=f1, fill=(251, 191, 36))
    t2 = f"esperado: prints\\prod\\postflop-{lang}.png (spot N1, field N2, GTO + faixa N3)"
    d.text(((W - d.textlength(t2, font=f2)) / 2, h / 2 + 20), t2, font=f2, fill=(148, 163, 184))
    return im


def framed_print(src):
    """Captura de producao -> imagem do e-mail: 1200 px, fundo #0b1220, cantos arredondados e borda do app."""
    im = Image.open(src).convert("RGB")
    ch = round(im.height * INNER / im.width)
    im = im.resize((INNER, ch), Image.LANCZOS)
    canvas = Image.new("RGB", (W, ch + 2 * M), BG_MAIL)
    k, r = 4, 22
    mk = Image.new("L", (INNER * k, ch * k), 0)
    ImageDraw.Draw(mk).rounded_rectangle((0, 0, INNER * k - 1, ch * k - 1), radius=r * k, fill=255)
    mk = mk.resize((INNER, ch), Image.LANCZOS)
    canvas.paste(im, (M, M), mk)
    bm = Image.new("L", (INNER * k, ch * k), 0)
    bd = ImageDraw.Draw(bm)
    bd.rounded_rectangle((0, 0, INNER * k - 1, ch * k - 1), radius=r * k, fill=255)
    bd.rounded_rectangle((2 * k, 2 * k, INNER * k - 1 - 2 * k, ch * k - 1 - 2 * k), radius=(r - 2) * k, fill=0)
    canvas.paste(Image.new("RGB", (INNER, ch), FRAME), (M, M), bm.resize((INNER, ch), Image.LANCZOS))
    return canvas


def bars_image(lang, n, pw):
    """As duas barras (mesmo grafico das artes) sobre #0b1220, 1200 px. Renderizado pelo Chromium."""
    svg, hh = chart_svg(lang, n, ph_h=360)
    svg = svg.replace(f'width="{lib.W}" height="{hh}"', f'style="width:{INNER - 60}px;height:auto"', 1)
    page = f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><link rel="stylesheet" href="base.css">
<style>html,body{{width:auto;background:#0b1220}}#wrap{{width:{W}px;padding:{M + 20}px 30px {M + 20}px;background:#0b1220;display:flex;justify-content:center}}</style></head>
<body><div id="wrap">{svg}</div></body></html>"""
    f = SRC / f"_email-bars-{lang}.html"
    f.write_text(page, encoding="utf-8")
    pw_page = pw.new_page(viewport={"width": W, "height": 1200}, device_scale_factor=1)
    pw_page.goto(f.as_uri())
    pw_page.evaluate("document.fonts.ready")
    pw_page.wait_for_timeout(250)
    tmp = ASSETS / f"_email-bars-{lang}.png"
    pw_page.locator("#wrap").screenshot(path=str(tmp))
    pw_page.close()
    return Image.open(tmp).convert("RGB")


def slot_image(lang, n, pw):
    """Retorna (imagem PIL, pendente: bool, motivos)."""
    mode = n.get("email_image", "print")
    if mode == "bars":
        ex = Ex(n, lang)
        miss = ex.missing()
        return bars_image(lang, n, pw), bool(miss), [f"imagem:{m}" for m in miss]
    p = find_print(f"postflop-{lang}")
    if p:
        return framed_print(p), False, []
    return placeholder_image(lang), True, [f"print:postflop-{lang}"]


# ---------------------------------------------------------------- HTML
def render(lang, n, img_name, img_h, draft_miss, preview):
    c = CP[lang]
    body, ex_miss = example_html(lang, n)
    miss = list(dict.fromkeys(ex_miss + draft_miss))
    txt = n.get("textos_com_numero") or {}
    corpo = txt.get(f"email_corpo_{lang}")
    if not has_text(corpo):
        corpo = ph_email(f"email_corpo_{lang}")
        miss.append(f"email_corpo_{lang}")
    draft = bool(miss)
    url = lib.LANDING.format(lang=lang)
    src = f"email/{img_name}" if preview else f"https://www.aurapoker.com/email/{img_name}"
    banner = ""
    if draft:
        note = " · leitura acima/abaixo da faixa ainda não definida (texto de 'acima')" if "N2" in miss or "N3" in miss else ""
        banner = (f'<tr><td bgcolor="#e11d48" align="center" style="background-color:#e11d48; padding:10px 14px; font-family:Arial,Helvetica,sans-serif; '
                  f'font-size:13px; font-weight:bold; color:#ffffff; letter-spacing:1px;">{c["draft"]}{H.escape(", ".join(miss))}{H.escape(note)}</td></tr>')
    title = ("[DRAFT] " if draft else "") + c["subject"]
    desc = (f'<!-- {"DRAFT: nao enviar. Gerado por instagram/src/build_email.py a partir de numbers.json; preencha o JSON e rode de novo." if draft else "Gerado por instagram/src/build_email.py a partir de numbers.json. Nao editar a mao."} -->')
    return f"""<!DOCTYPE html>
<html lang="{c['lang_attr']}" xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="color-scheme" content="dark light">
  <meta name="supported-color-schemes" content="dark light">
  <meta name="x-apple-disable-message-reformatting">
  <title>{H.escape(title)}</title>
</head>
<body style="margin:0; padding:0; width:100%; background-color:#070a12; -webkit-text-size-adjust:100%; -ms-text-size-adjust:100%;">
  {desc}
  <div style="display:none; max-height:0; overflow:hidden; mso-hide:all; font-size:1px; line-height:1px; color:#070a12; opacity:0;">{c['pre']}</div>
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#070a12;">
    <tr>
      <td align="center" style="padding:24px 12px;">
        <table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0" style="width:600px; max-width:600px; background-color:#0b1220; border:1px solid #1e293b; border-radius:14px; overflow:hidden;">
          {banner}
          <tr><td bgcolor="#D4A418" style="height:3px; line-height:3px; font-size:0; background-color:#D4A418;">&nbsp;</td></tr>
          <tr>
            <td style="padding-top:26px; padding-right:34px; padding-bottom:6px; padding-left:34px;">
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
                <td style="padding-right:10px; vertical-align:middle; width:50px;"><img src="https://www.aura.poker/email/aura-logo.png" width="40" height="32" border="0" alt="Aura" style="display:block; border:0; outline:none; text-decoration:none;"></td>
                <td style="vertical-align:middle;"><span style="font-family:Arial,Helvetica,sans-serif; font-weight:bold; font-size:20px; letter-spacing:6px; color:#e6ebf2;">AURA</span></td>
              </tr></table>
            </td>
          </tr>
          <tr>
            <td style="padding-top:14px; padding-right:34px; padding-bottom:0; padding-left:34px; font-family:Arial,Helvetica,sans-serif;">
              <h1 style="margin:0; font-size:28px; line-height:1.25; color:#e6ebf2; font-weight:bold;">{c['h1']}</h1>
              <p style="margin:10px 0 0 0; font-size:17px; line-height:1.5; color:#D4A418; font-weight:bold;">{c['tagline']}</p>
            </td>
          </tr>
          <tr>
            <td style="padding-top:16px; padding-right:34px; padding-bottom:4px; padding-left:34px; font-family:Arial,Helvetica,sans-serif; color:#c3ccd9; font-size:15px; line-height:1.65;">
              <p style="margin:0 0 14px 0;">{corpo}</p>
              <p style="margin:0 0 4px 0;">{body}</p>
            </td>
          </tr>
          <tr>
            <td style="padding-top:18px; padding-right:34px; padding-bottom:4px; padding-left:34px;" align="center">
              <img src="{src}" width="552" height="{img_h}" alt="{H.escape(c['alt'])}" style="display:block; width:100%; max-width:552px; height:auto; border:0; outline:none; text-decoration:none;">
            </td>
          </tr>
          <tr>
            <td style="padding-top:22px; padding-right:34px; padding-bottom:6px; padding-left:34px;" align="center">
              <table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr>
                <td align="center" bgcolor="#D4A418" style="border-radius:10px; background-color:#D4A418;">
                  <a href="{url}" style="display:inline-block; padding-top:14px; padding-bottom:14px; padding-left:34px; padding-right:34px; font-family:Arial,Helvetica,sans-serif; font-size:16px; font-weight:bold; color:#0b1220; text-decoration:none; border-radius:10px;">{c['btn']}</a>
                </td>
              </tr></table>
              <p style="margin:12px 0 0 0; font-family:Arial,Helvetica,sans-serif; font-size:13px; line-height:1.5; color:#9aa7ba;">{c['under']}</p>
            </td>
          </tr>
          <tr>
            <td style="padding-top:24px; padding-right:34px; padding-bottom:30px; padding-left:34px; border-top:1px solid #1e293b; background-color:#040711;">
              <p style="margin:0 0 6px 0; font-family:Arial,Helvetica,sans-serif; font-size:12px; line-height:1.6; color:#8a97ab;">{c['f1']}</p>
              <p style="margin:0 0 6px 0; font-family:Arial,Helvetica,sans-serif; font-size:12px; line-height:1.6; color:#8a97ab;">{c['f2']}</p>
              <p style="margin:0 0 6px 0; font-family:Arial,Helvetica,sans-serif; font-size:12px; line-height:1.6; color:#8a97ab;">{c['f3']} <a href="https://discord.gg/wYquSmUtAK" style="color:#aab6c8; text-decoration:underline;">Discord</a> · <a href="https://wa.me/554188083135" style="color:#aab6c8; text-decoration:underline;">WhatsApp</a> · <a href="https://www.youtube.com/@aurapokeranalytics" style="color:#aab6c8; text-decoration:underline;">YouTube</a></p>
              <p style="margin:12px 0 0 0; font-family:Arial,Helvetica,sans-serif; font-size:11px; letter-spacing:1px; color:#8a97ab;">AURA POKER ANALYTICS — © 2026 · 18+</p>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>
""", miss


def main():
    n = lib.load()
    EMAIL.mkdir(exist_ok=True)
    ASSETS.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        for lang in ("pt", "en"):
            im, pending, why = slot_image(lang, n, b)
            # sufixo -DRAFT enquanto a imagem for provisoria (print pendente, ou barras sem numero)
            stem = f"modo-gto-{lang}" + ("-DRAFT" if pending else "")
            dst = EMAIL / f"{stem}.png"
            other = EMAIL / (f"modo-gto-{lang}.png" if pending else f"modo-gto-{lang}-DRAFT.png")
            other.unlink(missing_ok=True)
            q = im.quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.FLOYDSTEINBERG)
            q.save(dst, optimize=True)
            chk = Image.open(dst)
            hd = round(chk.height * 552 / chk.width)
            print(dst.name, chk.size, chk.mode, round(dst.stat().st_size / 1024), "KB", "(provisoria)" if pending else "")
            for preview in (False, True):
                html, miss = render(lang, n, dst.name, hd, why, preview)
                out = POST / (f"email-{lang}.preview.html" if preview else f"email-{lang}.html")
                out.write_text(html, encoding="utf-8")
                if not preview:
                    print(" ", out.name, "->", ("DRAFT: falta " + ", ".join(miss)) if miss else "final")
        b.close()


if __name__ == "__main__":
    main()
