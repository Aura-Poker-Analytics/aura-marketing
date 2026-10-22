"""Field Hotspots - e-mail (PT e EN): imagem do spot + email-pt.html, email-en.html e os .preview.html.

Texto: email.md (assunto recomendado = opcao 2). Numeros: numbers.json; "[NUM]" vira marcador vermelho no texto e na imagem.
Imagem: email/field-hotspots-<lang>.png (1200 px, card do spot: par, stack, Overdefend, barras Field x GTO, Como explorar).
Hospedagem PENDENTE: antes do envio, subir os PNGs em https://www.aurapoker.com/email/ (aura-landing), como o modo-gto.
O HTML de envio aponta para essa URL; o .preview.html usa o caminho relativo email/.
Uso: python build_email.py   (nao envia nada, nao toca no Resend)
"""
import html as H

from PIL import Image
from playwright.sync_api import sync_playwright

import lib
from lib import ASSETS, EMAIL, EMAIL_IMG_BASE, POST, SRC, is_num, pct, ph_email, pv

CP = {
    "pt": dict(
        lang_attr="pt-BR", subject="UTG vs BB, 25bb: o field defende demais", h1="Field Hotspots no ar",
        tagline="8 spots de desvio forte do field, spot a spot.",
        pre="Field Hotspots no ar. Dois spots novos toda segunda.", btn="Abrir o Field Hotspots",
        under="Primeira troca de spots: segunda, 02/11. Poker é jogo de habilidade e estudo. 18+.",
        f1="Você recebe este e-mail porque tem uma conta ou lista de espera da Aura.",
        f2='Não quer mais e-mails como este? <a href="{{{RESEND_UNSUBSCRIBE_URL}}}" style="color:#aab6c8; text-decoration:underline;">Cancelar inscrição</a>. Ferramenta de estudo. 18+.',
        f3="Fale com a gente:",
        alt="Card do Field Hotspots para o spot UTG vs BB a 25bb em SRP, flop A-high two-tone: fold do field contra o do GTO, rótulo Overdefend e a caixa Como explorar: blefe menos e aposte mais por value.",
    ),
    "en": dict(
        lang_attr="en", subject="UTG vs BB, 25bb: the field overdefends", h1="Field Hotspots is live",
        tagline="8 strong field deviations from GTO, spot by spot.",
        pre="Field Hotspots is live. Two new spots every Monday.", btn="Open Field Hotspots",
        under="First spot swap: Monday, Nov 2. Poker is a game of skill and study. 18+.",
        f1="You are receiving this email because you have an Aura account or waitlist spot.",
        f2='Don\'t want emails like this anymore? <a href="{{{RESEND_UNSUBSCRIBE_URL}}}" style="color:#aab6c8; text-decoration:underline;">Unsubscribe</a>. Study tool. 18+.',
        f3="Reach us:",
        alt="Field Hotspots card for the UTG vs BB spot at 25bb in an SRP, A-high two-tone flop: field fold against GTO fold, an Overdefend label and the How to exploit box: bluff less and bet more for value.",
    ),
}


def body_paras(lang, n):
    f, g, d = (pv(n.get(k), lang, n, ph_email) for k in ("N1", "N2", "N3"))
    word = "abaixo" if lang == "pt" else "below"
    if lang == "pt":
        return [
            "Os spots pós-flop de MTT em que o field tem desvio forte do GTO, já discriminados: posições, stack, flop, size de c-bet e a ação para explorar.",
            f"UTG vs BB, 25bb, SRP, flop A♠ 3♠ 6♥ (A-high two-tone, OESD possível). Contra o c-bet de 50%, o field folda {f} e o GTO folda {g}: {d} {word}. O BB defende demais contra c-bet. Blefe menos e aposte mais por value.",
            "O Modo GTO libera 8 spots. O Grátis vê 1. Toda segunda, 2 saem e 2 entram, e o que sai não volta igual. O reg do lado pode estar vendo.",
        ]
    return [
        "The postflop MTT spots where the field leaks most, already itemized: positions, stack, flop, c-bet size and the action to exploit it.",
        f"UTG vs BB, 25bb, SRP, A♠ 3♠ 6♥ flop (A-high two-tone, possible OESD). Facing a 50% c-bet, the field folds {f} and GTO folds {g}: {d} {word}. The BB defends too much against the c-bet. Bluff less and bet more for value.",
        "GTO Mode unlocks 8 spots. Free sees 1. Every Monday, 2 leave and 2 come in, and what leaves doesn't come back the same. The reg next to you might be looking.",
    ]


def card_html(lang, n):
    f, g = n.get("N1"), n.get("N2")
    ready = is_num(f) and is_num(g)
    top = (max(f, g) * 1.1) if ready else 100
    pt = lang == "pt"
    lab = "Fold contra c-bet 50% · Field × GTO" if pt else "Fold vs 50% c-bet · Field × GTO"
    how_l = "COMO EXPLORAR" if pt else "HOW TO EXPLOIT"
    how_t = "O BB defende demais contra c-bet. Blefe menos e aposte mais por value." if pt else "The BB defends too much against the c-bet. Bluff less and bet more for value."
    word = "abaixo" if pt else "below"

    def row(name, v, cls, dflt):
        if is_num(v):
            return (f'<div class="row"><span class="n">{name}</span><div class="track"><div class="fill {cls}" style="width:{v / top * 100:.1f}%"></div></div>'
                    f'<span class="v">{pct(v, lang, n)}</span></div>')
        return (f'<div class="row"><span class="n">{name}</span><div class="track"><div class="fill {cls} dr" style="width:{dflt}%"></div></div>'
                f'<span class="v"><span class="ph">[NUM]</span></span></div>')
    d = n.get("N3")
    dtxt = f"{pct(d, lang, n)} {word}" if is_num(d) else f'<span class="ph">[NUM]</span> {word}'
    boards = "".join(lib.board(b, 70, label="FLOP") for b in lib.FLOPS)
    return f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><link rel="stylesheet" href="base.css"><style>
html, body {{ width: 1200px; background: #0b1220; }}
#m {{ position: relative; width: 1200px; padding: 40px 44px 44px; background: radial-gradient(700px 420px at 30% 20%, rgba(251,191,36,.16), transparent), #0b1220; font-family: Montserrat, sans-serif; }}
.card {{ background: #0F172A; border: 2px solid rgba(148,163,184,.3); border-radius: 30px; padding: 32px 38px 34px; box-shadow: 0 30px 80px rgba(0,0,0,.6); }}
.hd {{ display: flex; align-items: baseline; gap: 18px; }} .hd .pair {{ font-size: 44px; font-weight: 800; }} .hd .st {{ font-size: 32px; font-weight: 600; color: #94A3B8; }}
.hd .od {{ margin-left: auto; font-size: 26px; }}
.brd {{ margin-top: 22px; display: flex; gap: 14px; }} .brd .bwrap {{ padding: 12px 14px 8px; }} .brd .bwrap small {{ font-size: 16px; }}
.t {{ margin-top: 26px; font-size: 28px; font-weight: 700; color: #A9B6C8; }}
.row {{ display: flex; align-items: center; gap: 22px; margin-top: 18px; }} .row .n {{ width: 120px; font-size: 28px; font-weight: 800; letter-spacing: .08em; color: #CBD5E1; text-transform: uppercase; }}
.track {{ position: relative; flex: 1; height: 40px; background: rgba(30,41,59,.9); border-radius: 999px; }} .fill {{ position: absolute; left: 0; top: 0; bottom: 0; border-radius: 999px; }}
.ff {{ background: linear-gradient(90deg,#015A6B,#0E8AA3); box-shadow: inset 0 0 0 2px rgba(103,232,249,.35); }} .fg {{ background: rgba(1,90,107,.55); box-shadow: inset 0 0 0 3px #5EC9DB; }}
.dr {{ background: rgba(1,90,107,.18); box-shadow: none; border: 3px dashed #5EC9DB; }}
.row .v {{ width: 150px; text-align: right; font-size: 44px; font-weight: 900; color: #fff; white-space: nowrap; }}
.gap {{ margin-top: 16px; font-size: 32px; font-weight: 900; color: #FBBF24; text-align: right; }}
.how {{ margin-top: 26px; padding: 24px 30px 26px; }} .how .tx {{ font-size: 38px; }}
</style></head><body><div id="m"><div class="card">
<div class="hd"><span class="pair">UTG vs BB</span><span class="st">25bb · SRP</span><span class="od">OVERDEFEND</span></div>
<div class="brd">{boards}</div>
<div class="t">{lab}</div>
{row("Field", f, "ff", 58)}{row("GTO", g, "fg", 76)}
<div class="gap">{dtxt}</div>
<div class="how"><div class="lab">{how_l}</div><div class="tx">{how_t}</div></div>
</div></div></body></html>"""


def render(lang, n, img_name, img_h, preview, pend):
    c = CP[lang]
    url = lib.LANDING.format(lang=lang)
    src = f"email/{img_name}" if preview else f"{EMAIL_IMG_BASE}{img_name}"
    p_html = "".join(f'<p style="margin:0 0 14px 0;">{p}</p>' for p in body_paras(lang, n))
    banner = ""
    if pend:
        txt = ("RASCUNHO · NÃO ENVIAR · [NUM] pendente: " if lang == "pt" else "DRAFT · DO NOT SEND · [NUM] pending: ") + ", ".join(pend)
        banner = (f'<tr><td bgcolor="#e11d48" align="center" style="background-color:#e11d48; padding:10px 14px; font-family:Arial,Helvetica,sans-serif; '
                  f'font-size:13px; font-weight:bold; color:#ffffff; letter-spacing:1px;">{txt}</td></tr>')
    title = ("[DRAFT] " if pend else "") + c["subject"]
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
              {p_html}
            </td>
          </tr>
          <tr>
            <td style="padding-top:12px; padding-right:34px; padding-bottom:4px; padding-left:34px;" align="center">
              <img src="{src}" width="530" height="{img_h}" alt="{H.escape(c['alt'])}" style="display:block; width:100%; max-width:530px; height:auto; border:0; outline:none; text-decoration:none;">
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
"""


def main():
    n = lib.load()
    pend = lib.missing(n, ("N1", "N2", "N3"))
    EMAIL.mkdir(exist_ok=True)
    ASSETS.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        for lang in ("pt", "en"):
            f = SRC / f"_email-card-{lang}.html"
            f.write_text(card_html(lang, n), encoding="utf-8")
            pg = b.new_page(viewport={"width": 1200, "height": 1000}, device_scale_factor=1)
            pg.goto(f.as_uri())
            pg.evaluate("document.fonts.ready")
            pg.wait_for_timeout(300)
            dst = EMAIL / f"field-hotspots-{lang}.png"
            pg.locator("#m").screenshot(path=str(dst))
            pg.close()
            im = Image.open(dst)
            hd = round(im.height * 530 / im.width)
            print(dst.name, im.size, round(dst.stat().st_size / 1024), "KB")
            for preview in (False, True):
                out = POST / (f"email-{lang}.preview.html" if preview else f"email-{lang}.html")
                out.write_text(render(lang, n, dst.name, hd, preview, pend), encoding="utf-8")
            print("  email-%s.html ->" % lang, ("[NUM] pendente: " + ", ".join(pend)) if pend else "final")
        b.close()


if __name__ == "__main__":
    main()
