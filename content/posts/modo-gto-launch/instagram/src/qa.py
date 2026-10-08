"""QA das artes e do e-mail do Modo GTO. Uso: python qa.py  (depois de build.py e build_email.py)

Artes: dimensao exata do PNG; nada fora das margens laterais (84 px); blocos sem sobreposicao; nada abaixo do rodape;
linha de apoio de uma linha cabe sem corte; DRAFT x final coerente (final nao tem marcador [[...]]);
palavras proibidas no texto visivel.
E-mail: marcador pendente so em DRAFT, link do botao, descadastro, logo, preheader oculto, largura 600.
Sai com codigo 1 se achar problema.
"""
import re
import sys
from pathlib import Path

from PIL import Image
from playwright.sync_api import sync_playwright

import lib
from build import ART

SRC = Path(__file__).resolve().parent
OUT = lib.OUT
POST = lib.POST
BANNED = ["overlay", "solver", "beta", "wizard", "pool", "campo", "gtowizard", "piosolver", "monkersolver"]
JS = """() => {
  const out = {issues: []};
  const page = document.querySelector('.page');
  out.h = Math.round(page.getBoundingClientRect().height);
  const sel = ['.title', '.sub', '.chart', '.slot', '.slotimg', '.sticker', 'header', 'footer'];
  const boxes = [];
  for (const s of sel) for (const e of document.querySelectorAll(s)) {
    const r = e.getBoundingClientRect();
    if (r.width) boxes.push([s, Math.round(r.left), Math.round(r.top), Math.round(r.right), Math.round(r.bottom), e]);
  }
  for (const [s, l, t, r, b, e] of boxes) {
    if (l < 80 || r > 1000) out.issues.push(`${s} fora da margem lateral (${l}..${r})`);
    if (s !== 'footer' && b > out.h) out.issues.push(`${s} passa do fim da pagina`);
    if (e.scrollWidth > e.clientWidth + 2 && s === '.sub') out.issues.push('linha de apoio cortada');
  }
  const ft = boxes.find(x => x[0] === 'footer');
  for (const bx of boxes) if (bx[0] !== 'footer' && bx[0] !== 'header' && ft && bx[4] > ft[2] - 4) out.issues.push(`${bx[0]} encosta no rodape (${bx[4]} > ${ft[2]})`);
  const body = boxes.filter(x => ['.title', '.sub', '.chart', '.slot', '.slotimg', '.sticker'].includes(x[0]));
  for (let i = 0; i < body.length; i++) for (let j = i + 1; j < body.length; j++) {
    const a = body[i], c = body[j];
    if (a[1] < c[3] && c[1] < a[3] && a[2] < c[4] && c[2] < a[4]) out.issues.push(`${a[0]} sobrepoe ${c[0]}`);
  }
  // svg: texto dentro do viewBox
  for (const svg of document.querySelectorAll('svg.chart')) {
    const vb = svg.viewBox.baseVal, sr = svg.getBoundingClientRect();
    for (const t of svg.querySelectorAll('text')) {
      const r = t.getBoundingClientRect();
      if (r.left < sr.left - 1 || r.right > sr.right + 1 || r.top < sr.top - 1 || r.bottom > sr.bottom + 1) out.issues.push('texto do grafico fora do SVG: ' + t.textContent.slice(0, 20));
    }
  }
  out.text = document.body.innerText;
  out.ph = document.querySelectorAll('.ph').length + (document.body.innerHTML.includes('[[') ? 1 : 0);
  return out;
}"""

problems = []


def bad(msg):
    problems.append(msg)
    print("  PROBLEMA:", msg)


with sync_playwright() as p:
    b = p.chromium.launch()
    for name, a in ART.items():
        w, h = a["size"]
        found = [(s, SRC / f"{name}{s}.html", OUT / f"{name}{s}.png") for s in ("", "-DRAFT") if (OUT / f"{name}{s}.png").exists()]
        if len(found) != 1:
            bad(f"{name}: esperava exatamente 1 PNG (final ou DRAFT), achei {len(found)}")
            continue
        suffix, html, png = found[0]
        im = Image.open(png)
        pg = b.new_page(viewport={"width": 1080, "height": 1920})
        pg.goto(html.as_uri())
        pg.evaluate("document.fonts.ready")
        pg.wait_for_timeout(250)
        r = pg.evaluate(JS)
        pg.close()
        print(png.name, im.size, "page", r["h"], "DRAFT" if suffix else "final")
        if im.size != (w, h):
            bad(f"{png.name}: {im.size} != {(w, h)}")
        if r["h"] != h:
            bad(f"{png.name}: pagina {r['h']} != {h}")
        for i in r["issues"]:
            bad(f"{png.name}: {i}")
        if not suffix and r["ph"]:
            bad(f"{png.name}: arte final com marcador pendente")
        vis = r["text"].lower()
        for w_ in BANNED:
            if re.search(rf"\b{w_}\b", vis):
                bad(f"{png.name}: palavra proibida '{w_}'")
    b.close()

# ---- e-mail
for lang in ("pt", "en"):
    for f in (POST / f"email-{lang}.html", POST / f"email-{lang}.preview.html"):
        t = f.read_text(encoding="utf-8")
        draft = "[[" in t or "[DRAFT]" in t
        print(f.name, "DRAFT" if draft else "final")
        if '<table role="presentation" width="600"' not in t:
            bad(f"{f.name}: sem tabela de 600 px")
        if "{{{RESEND_UNSUBSCRIBE_URL}}}" not in t:
            bad(f"{f.name}: sem placeholder de descadastro")
        if "https://www.aura.poker/email/aura-logo.png" not in t:
            bad(f"{f.name}: sem logo")
        url = lib.LANDING.format(lang=lang)
        if f'href="{url}"' not in t:
            bad(f"{f.name}: botao sem o link da landing esperado")
        if "display:none; max-height:0" not in t:
            bad(f"{f.name}: sem preheader oculto")
        if "18+" not in t:
            bad(f"{f.name}: sem 18+")
        if not draft and ("[DRAFT]" in t or "DRAFT" in t):
            bad(f"{f.name}: e-mail final com marca de DRAFT")
        vis = re.sub(r"<[^>]+>", " ", t).lower()
        for w_ in BANNED:
            if re.search(rf"\b{w_}\b", vis):
                bad(f"{f.name}: palavra proibida '{w_}'")
        m = re.search(r'<img src="([^"]*modo-gto-[^"]+)"', t)
        if not m:
            bad(f"{f.name}: sem imagem do slot")
        else:
            img_ref = m.group(1)
            name = img_ref.rsplit("/", 1)[-1]
            if not (POST / "email" / name).exists():
                bad(f"{f.name}: imagem {name} nao existe em email/")
        if f.name.endswith("preview.html") and "https://www.aurapoker.com/email/modo-gto" in t:
            bad(f"{f.name}: preview deve usar caminho relativo email/")
        if not f.name.endswith("preview.html") and 'src="email/' in t:
            bad(f"{f.name}: html de envio deve usar a URL hospedada")

print("\nOK" if not problems else f"\n{len(problems)} problema(s)")
sys.exit(1 if problems else 0)
