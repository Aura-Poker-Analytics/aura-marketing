"""QA de layout: nada estoura a area segura nem a largura. Uso: python qa.py"""
from pathlib import Path
from playwright.sync_api import sync_playwright
SRC = Path(__file__).resolve().parent
JS = """() => {
  const out = [];
  const W = 1080;
  const leaves = [...document.querySelectorAll('.page *')].filter(e => e.children.length === 0 && (e.textContent||'').trim().length && !e.closest('svg') || e.tagName==='IMG' || e.tagName==='text');
  let minTop=1e9, maxBot=0;
  for (const e of leaves) {
    const r = e.getBoundingClientRect();
    if (r.width===0) continue;
    if (e.closest('.suits')) continue;
    minTop=Math.min(minTop,r.top); maxBot=Math.max(maxBot,r.bottom);
    if (r.right > W-60 || r.left < 60) { if (!e.closest('.shot') && e.tagName!=='IMG') out.push(['x', e.tagName, (e.textContent||'').trim().slice(0,30), Math.round(r.left), Math.round(r.right)]); }
  }
  const ft = document.querySelector('footer');
  const f = ft ? ft.getBoundingClientRect().top : null;
  // sobreposicao: ultimo bloco antes do rodape
  return {minTop, maxBot, footerTop:f, issues: out, h: document.querySelector('.page').getBoundingClientRect().height};
}"""
with sync_playwright() as p:
    b = p.chromium.launch()
    for f in sorted(SRC.glob("feed-*.html")) + sorted(SRC.glob("story-*.html")) + sorted(SRC.glob("carrossel-*.html")):
        pg = b.new_page(viewport={"width": 1080, "height": 1920})
        pg.goto(f.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(120)
        r = pg.evaluate(JS)
        print(f.name, {k: (round(v) if isinstance(v, float) else v) for k, v in r.items() if k != 'issues'}, r['issues'][:4])
        pg.close()
    b.close()
