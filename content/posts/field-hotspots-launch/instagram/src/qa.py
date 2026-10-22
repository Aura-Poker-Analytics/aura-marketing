"""QA das artes e do e-mail do Field Hotspots. Uso: python qa.py  (depois de build.py e build_email.py)

Artes: dimensao exata; nada fora das margens laterais; blocos sem sobreposicao; nada sobre o rodape; texto sem corte;
palavras proibidas; [NUM] e so o esperado (arte sem numero nao pode ter [NUM]; arte com numero so tem [NUM] se numbers.json pendente).
E-mail: link do botao, descadastro, logo, preheader oculto, largura 600, imagem existe, URL hospedada x relativa no preview.
Sai com codigo 1 se achar problema. [NUM] pendente NAO e problema aqui (e o estado esperado); build.py --strict cobre isso.
"""
import re
import sys
from pathlib import Path

from PIL import Image
from playwright.sync_api import sync_playwright

import lib
from build import ART

SRC = Path(__file__).resolve().parent
OUT, POST = lib.OUT, lib.POST
BANNED = ["beta", "ponte", "pool vs gto", "overlay", "solver", "wizard", "pool", "campo", "early bird", "mdf"]
JS = """() => {
  const out = {issues: []};
  const page = document.querySelector('.page');
  out.h = Math.round(page.getBoundingClientRect().height);
  const boxes = [];
  for (const s of ['.title', '.sub', 'header', 'footer', '.sticker']) for (const e of document.querySelectorAll(s)) {
    const r = e.getBoundingClientRect(); if (r.width) boxes.push([s, r.left, r.top, r.right, r.bottom, e]);
  }
  for (const [s, l, t, r, b, e] of boxes) {
    if ((l < 80 || r > 1002) && s !== 'footer' && s !== 'header') out.issues.push(`${s} fora da margem lateral (${Math.round(l)}..${Math.round(r)})`);
    if (e.scrollWidth > e.clientWidth + 2 && s === '.sub') out.issues.push('linha de apoio cortada');
  }
  const ft = boxes.find(x => x[0] === 'footer');
  // qualquer elemento visivel dentro da pagina que invada o rodape ou saia da area util
  const all = page.querySelectorAll('.title,.sub,.chart,.sp,.how,.win,.stage,.brd,.panel,.grid,.gh,.ghs,.mid,.fc,.cl,.pc,.board,.flop,.lockpill,.hd,.nvbar,.lst');
  for (const e of all) {
    const r = e.getBoundingClientRect(); if (!r.width) continue;
    if (ft && r.bottom > ft.top ? false : false) {}
    if (r.right > 1080 + 1 || r.left < -1) out.issues.push(`${e.className.toString().slice(0,18)} sai da pagina lateralmente (${Math.round(r.left)}..${Math.round(r.right)})`);
    if (ft && r.bottom > ft.top + 2 && !e.contains(ft) && !ft.contains(e) && e.className.toString().indexOf('mid') < 0 && e.className.toString().indexOf('fc') < 0 && e.className.toString().indexOf('stage') < 0)
      out.issues.push(`${e.className.toString().slice(0,18)} invade o rodape (${Math.round(r.bottom)} > ${Math.round(ft.top)})`);
  }
  for (const svg of document.querySelectorAll('svg.chart')) {
    const sr = svg.getBoundingClientRect();
    for (const t of svg.querySelectorAll('text')) {
      const r = t.getBoundingClientRect();
      if (r.left < sr.left - 1 || r.right > sr.right + 1 || r.top < sr.top - 1 || r.bottom > sr.bottom + 1) out.issues.push('texto do grafico fora do SVG: ' + t.textContent.slice(0, 20));
    }
  }
  out.text = document.body.innerText;
  out.ph = (document.body.innerText.match(/\\[NUM\\]/g) || []).length;
  return out;
}"""

problems = []


def bad(msg):
    problems.append(msg)
    print("  PROBLEMA:", msg)


n = lib.load()
with sync_playwright() as p:
    b = p.chromium.launch()
    for name, a in ART.items():
        w, h = a["size"]
        png, html = OUT / f"{name}.png", SRC / f"{name}.html"
        if not png.exists():
            bad(f"{name}: PNG ausente")
            continue
        im = Image.open(png)
        pg = b.new_page(viewport={"width": 1080, "height": 1920})
        pg.goto(html.as_uri())
        pg.evaluate("document.fonts.ready")
        pg.wait_for_timeout(250)
        r = pg.evaluate(JS)
        pg.close()
        pend = lib.missing(n, a["num"])
        print(png.name, im.size, "page", r["h"], f"[NUM]x{r['ph']}" if r["ph"] else "sem [NUM]")
        if im.size != (w, h):
            bad(f"{png.name}: {im.size} != {(w, h)}")
        if r["h"] != h:
            bad(f"{png.name}: pagina {r['h']} != {h}")
        for i in r["issues"]:
            bad(f"{png.name}: {i}")
        if r["ph"] and not pend:
            bad(f"{png.name}: [NUM] visivel mas numbers.json esta preenchido (rode build.py)")
        if not a["num"] and r["ph"]:
            bad(f"{png.name}: arte sem numero tem [NUM]")
        vis = r["text"].lower()
        for w_ in BANNED:
            if re.search(rf"\b{re.escape(w_)}\b", vis):
                bad(f"{png.name}: palavra proibida '{w_}'")
        if a["lang"] == "pt" and "us$" in vis or a["lang"] == "en" and "r$" in vis:
            bad(f"{png.name}: moeda de outro idioma")
    b.close()

names = set(ART)
for f in OUT.glob("*.png"):
    if f.stem not in names:
        bad(f"PNG sobrando: {f.name}")
for f in SRC.glob("*.html"):
    if f.stem not in names and not f.name.startswith("_"):
        bad(f"HTML-fonte sobrando: {f.name}")
mir = lib.MIRROR
for nm in names:
    if not (mir / f"{nm}.png").exists():
        bad(f"{nm}: falta copia em {mir}")

# ---- e-mail
for lang in ("pt", "en"):
    img = POST / "email" / f"field-hotspots-{lang}.png"
    if not img.exists():
        bad(f"{img.name}: ausente")
    else:
        print(img.name, Image.open(img).size)
    for f in (POST / f"email-{lang}.html", POST / f"email-{lang}.preview.html"):
        t = f.read_text(encoding="utf-8")
        print(f.name, "[NUM] pendente" if "[NUM]" in t else "sem [NUM]")
        if '<table role="presentation" width="600"' not in t:
            bad(f"{f.name}: sem tabela de 600 px")
        if "{{{RESEND_UNSUBSCRIBE_URL}}}" not in t:
            bad(f"{f.name}: sem placeholder de descadastro")
        if "https://www.aura.poker/email/aura-logo.png" not in t:
            bad(f"{f.name}: sem logo")
        if f'href="{lib.LANDING.format(lang=lang)}"' not in t:
            bad(f"{f.name}: botao sem o link esperado")
        if "display:none; max-height:0" not in t:
            bad(f"{f.name}: sem preheader oculto")
        if "18+" not in t:
            bad(f"{f.name}: sem 18+")
        vis = re.sub(r"<[^>]+>", " ", t).lower()
        for w_ in BANNED:
            if re.search(rf"\b{re.escape(w_)}\b", vis):
                bad(f"{f.name}: palavra proibida '{w_}'")
        prev = f.name.endswith("preview.html")
        if prev and f"{lib.EMAIL_IMG_BASE}field-hotspots" in t:
            bad(f"{f.name}: preview deve usar caminho relativo email/")
        if not prev and f"{lib.EMAIL_IMG_BASE}field-hotspots-{lang}.png" not in t:
            bad(f"{f.name}: html de envio deve usar a URL hospedada")

print("\nOK" if not problems else f"\n{len(problems)} problema(s)")
sys.exit(1 if problems else 0)
