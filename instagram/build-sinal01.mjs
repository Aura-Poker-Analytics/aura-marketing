/* Estudo de sinal 01 (anuncios Meta, pos-Andromeda): 4 angulos x PT/EN x feed 1080x1350 + story 1080x1920 = 16 PNG.
 * Versao limpa (mesmas regras do carrossel): titulo curto, no maximo 1 linha de apoio, 1 visual dominante, no maximo 1 rotulo no topo,
 * 18+ discreto (topo direito sem chip; canto inferior direito com chip), sem rodape, sem n de maos, sem Overfold, sem legenda.
 *
 *   node instagram/build-sinal01.mjs          # gera os 16 HTML-fonte, renderiza com Chrome headless e copia para output
 *   node instagram/build-sinal01.mjs --html   # so gera os HTML
 *
 * Copy: content/ads/sinal01/copy-sinal01.md. Numeros aprovados: BTN vs SB, 25bb, flop A-high rainbow, c-bet de 33%, field fold 41,5% x GTO 25,0%.
 * Os 4 angulos mantem cor propria (estudo compara angulos): A navy+ambar, B claro+azul, C verde-escuro+menta, D grafite+coral.
 * Story: ~250 px livres em cima e embaixo (zona da UI do Instagram).
 */
import fs from 'fs';
import path from 'path';
import { execFileSync } from 'child_process';
import { fileURLToPath, pathToFileURL } from 'url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const TPL = path.join(ROOT, 'instagram/templates');
const ART = path.join(ROOT, 'content/ads/sinal01/art');
const OUT2 = path.join(ROOT, 'instagram/output/sinal01');
/* HTML-fonte e CSS por idioma (o casa-lint le en/ como ingles); o CSS fica em .css, fora do lint de texto */
const SRC = path.join(ROOT, 'content/ads/sinal01/fonte');
const CHROME = process.env.CHROME_PATH || 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const ONLY_HTML = process.argv.includes('--html');
fs.mkdirSync(ART, { recursive: true });
fs.mkdirSync(OUT2, { recursive: true });

/* logos oficiais: extraidos do template existente (nada retipado) */
const tplSrc = fs.readFileSync(path.join(TPL, 'carrossel-capa.html'), 'utf8');
const ICON = /const ICON_PATHS = `([\s\S]*?)`;/.exec(tplSrc)[1];
const LETTERS = /const AURA_LETTERS = `([\s\S]*?)`;/.exec(tplSrc)[1];
const ICON_SVG = `<svg viewBox="0 0 60 45" fill="currentColor" xmlns="http://www.w3.org/2000/svg">${ICON}</svg>`;
const WORD_SVG = `<svg viewBox="1 204 594 129" fill="currentColor" xmlns="http://www.w3.org/2000/svg">${LETTERS}</svg>`;

/* ---------- textos (copy-sinal01.md) ---------- */
const T = {
  pt: {
    lang: 'pt-BR', dec: ',', field: 'Field', gto: 'GTO', action: 'C-bet for auto-profit!',
    A: { chip: 'Novo · Field Exploits', h: 'Onde o field <span class="hl">erra</span>', ctx: 'BTN vs SB · 25bb · flop A-high rainbow · c-bet de 33%' },
    B: { h: 'Você não precisa<br>de <s>mais vídeo</s>', s: 'Precisa saber <b>o que estudar primeiro.</b>', l1: 'BTN vs SB', l2: '25bb · flop A-high rainbow', tag: 'Folda demais' },
    C: { h: 'Comece <span class="hl">grátis.</span><br>Sem cartão.', s: 'Veja onde o field erra.', create: 'Criar conta', btn: 'Criar conta grátis' },
    D: { k: 'Seu spot, lido em segundos', title: 'O SB <span class="hl">folda demais</span> contra <span class="nw">c-bet</span>' },
  },
  en: {
    lang: 'en', dec: '.', field: 'Field', gto: 'GTO', action: 'C-bet for auto-profit!',
    A: { chip: 'New · Field Exploits', h: 'Where the field<br>gets it <span class="hl">wrong</span>', ctx: 'BTN vs SB · 25bb · A-high rainbow flop · 33% c-bet' },
    B: { h: 'You don’t need<br><s>more videos</s>', s: 'You need to know <b>what to study first.</b>', l1: 'BTN vs SB', l2: '25bb · A-high rainbow flop', tag: 'Overfolds' },
    C: { h: 'Start <span class="hl">free.</span><br>No credit card.', s: 'See where the field errs.', create: 'Create account', btn: 'Create free account' },
    D: { k: 'Your spot, read in seconds', title: 'The SB <span class="hl">folds too much</span> vs <span class="nw">c-bet</span>' },
  },
};
const num = (lang, s) => s.replace('.', T[lang].dec);

/* ---------- base ---------- */
const FONT = pathToFileURL(path.join(TPL, 'fonts/Montserrat-Variable-latin.woff2')).href;
const baseCss = (fmt) => `
@font-face{font-family:"Montserrat";src:url("${FONT}") format("woff2");font-weight:100 900;font-display:block}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:${fmt === 'story' ? 1920 : 1350}px;overflow:hidden}
body{font-family:"Montserrat","Segoe UI",sans-serif;position:relative;display:flex;flex-direction:column;
  padding:${fmt === 'story' ? '250px 72px 250px' : '60px 72px 56px'};-webkit-font-smoothing:antialiased}
.top{display:flex;align-items:center;justify-content:space-between;height:64px;flex:none}
.brand{display:flex;align-items:center;gap:16px;height:100%}
.brand .ic{width:58px;height:44px}.brand .wm{width:132px}
.brand svg{width:100%;height:100%;display:block}
.age{font-weight:800;font-size:24px;border:2px solid currentColor;border-radius:10px;padding:5px 12px;opacity:.8}
.foot{display:flex;justify-content:flex-end;flex:none;height:44px;margin-top:10px}
.main{flex:1;display:flex;flex-direction:column;justify-content:${fmt === 'story' ? 'space-between' : 'center'};gap:${fmt === 'story' ? 0 : 84}px;padding:${fmt === 'story' ? '48px 0 40px' : '18px 0 14px'}}
h1{font-weight:900;text-transform:uppercase;line-height:1.04;letter-spacing:.005em;text-wrap:balance}
.sup{font-weight:500;line-height:1.3}
`;

/* ---------- A: navy + ambar, dois numeros grandes ---------- */
function pageA(lang, fmt) {
  const t = T[lang], big = fmt === 'story';
  const css = `
body{background:radial-gradient(1100px 800px at 85% -8%,rgba(212,164,24,.20),transparent 60%),radial-gradient(900px 700px at 0% 105%,rgba(34,53,89,.55),transparent 60%),#020617;color:#fff}
.brand{color:#D4A418}
.chip{font-size:26px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:#FBBF24;border:2px solid rgba(251,191,36,.6);border-radius:12px;padding:10px 20px;background:rgba(251,191,36,.07)}
h1{font-size:${big ? 92 : 84}px}.hl{color:#FBBF24}
.ctx{font-size:32px;font-weight:700;line-height:1.3;color:#CBD5E1;margin-top:28px}
.pair{display:flex;gap:28px}
.cell{flex:1;display:flex;flex-direction:column;gap:14px;background:#0F172A;border:2px solid rgba(251,191,36,.32);border-radius:36px;padding:${big ? '56px 34px 60px' : '64px 34px 70px'};box-shadow:0 30px 80px rgba(0,0,0,.45)}
.cell .k{font-size:34px;font-weight:800;letter-spacing:.14em;text-transform:uppercase}
.cell .v{font-size:128px;font-weight:800;line-height:1;letter-spacing:-.03em}
.cell.f .k,.cell.f .v{color:#34C9E6}.cell.g .k,.cell.g .v{color:#5FDB9C}
.act{font-size:${big ? 62 : 64}px;font-weight:800;line-height:1.15;color:#FBBF24}
.age{color:#94A3B8}`;
  return page(lang, fmt, css, `
  <div class="top"><div class="brand"><span class="ic">${ICON_SVG}</span><span class="wm">${WORD_SVG}</span></div><span class="chip">${t.A.chip}</span></div>
  <div class="main"><div><h1>${t.A.h}</h1><p class="ctx">${t.A.ctx}</p></div>
    <div class="pair"><div class="cell f"><span class="k">${t.field}</span><span class="v">${num(lang, '41.5')}%</span></div>
      <div class="cell g"><span class="k">${t.gto}</span><span class="v">${num(lang, '25.0')}%</span></div></div>
    <div class="act">${t.action}</div></div>`, 'bottom');
}

/* ---------- B: claro + azul, um card grande com rótulo ---------- */
function pageB(lang, fmt) {
  const t = T[lang], big = fmt === 'story';
  const css = `
body{background:linear-gradient(180deg,#F4F6FA 0%,#DCE4EF 100%);color:#0F1526}
.brand{color:#0F1526}
h1{font-size:${big ? 92 : 80}px;color:#0F1526}
h1 s{text-decoration:none;position:relative;color:#223559;white-space:nowrap}
h1 s::after{content:"";position:absolute;left:-6px;right:-6px;top:52%;height:${big ? 12 : 10}px;background:#AD2C34;border-radius:6px;transform:rotate(-2deg)}
.sup{font-size:${big ? 44 : 40}px;color:#2F435C;margin-top:22px}.sup b{color:#0F1526;font-weight:800}
.card{display:flex;align-items:center;justify-content:space-between;gap:30px;background:#fff;border:4px solid #223559;border-radius:48px;box-shadow:0 30px 70px rgba(15,21,38,.18);padding:${big ? '110px 60px' : '120px 60px'}}
.card .p{font-size:${big ? 112 : 104}px;font-weight:800;line-height:1.05;color:#0F1526;letter-spacing:-.01em}
.card .q{font-size:46px;font-weight:600;line-height:1.25;color:#475569;margin-top:20px}
.card .tag{display:inline-block;margin-top:34px;padding:16px 34px;border-radius:999px;background:#FBE4E5;color:#8E1F27;font-size:${big ? 50 : 46}px;font-weight:800;letter-spacing:.01em}
.age{color:#475569}`;
  return page(lang, fmt, css, `
  <div class="top"><div class="brand"><span class="ic">${ICON_SVG}</span><span class="wm">${WORD_SVG}</span></div><span class="age">18+</span></div>
  <div class="main"><div><h1>${t.B.h}</h1><p class="sup">${t.B.s}</p></div>
    <div class="card"><div><div class="p">${t.B.l1}</div><div class="q">${t.B.l2}</div><span class="tag">${t.B.tag}</span></div></div></div>`);
}

/* ---------- C: verde-escuro + menta, um celular ---------- */
function pageC(lang, fmt) {
  const t = T[lang], big = fmt === 'story';
  const ph = big ? 1040 : 730, pw = big ? 560 : 452;
  const css = `
body{background:radial-gradient(1000px 760px at 50% 108%,rgba(127,227,174,.22),transparent 62%),linear-gradient(170deg,#04323B 0%,#02171C 100%);color:#fff}
.brand{color:#fff}
h1{font-size:${big ? 88 : 80}px}.hl{color:#7FE3AE}
.sup{font-size:${big ? 44 : 40}px;color:#D5F5E3;margin-top:20px}
.stage{display:flex;justify-content:center;flex:none;margin-top:${big ? 0 : 20}px}
.phone{position:relative;width:${pw}px;height:${ph}px;border-radius:64px;background:#0F172A;border:10px solid #0B1220;box-shadow:0 0 0 2px #2B3A52,0 40px 80px rgba(0,0,0,.55);overflow:hidden;padding:34px 34px}
.notch{position:absolute;top:12px;left:50%;width:120px;height:10px;margin-left:-60px;border-radius:6px;background:#1E293B}
.su{display:flex;flex-direction:column;height:100%;padding-top:34px}
.su .lg{color:#D4A418;width:84px;height:63px}.su .lg svg{width:100%;height:100%}
.su h2{font-size:40px;font-weight:800;margin-top:${big ? 44 : 30}px}
.su .in{height:${big ? 96 : 84}px;border-radius:20px;background:#1E293B;border:2px solid #334155;margin-top:${big ? 28 : 20}px;display:flex;align-items:center;padding:0 26px}
.su .in i{display:block;height:18px;border-radius:9px;background:#64748B}
.su .in.a i{width:46%}.su .in.b i{width:30%}.su .in.c i{width:38%}
.su .btn{margin-top:${big ? 54 : 40}px;height:${big ? 108 : 96}px;border-radius:24px;background:linear-gradient(180deg,#FCD34D,#F59E0B);color:#0F1526;font-size:31px;font-weight:800;display:flex;align-items:center;justify-content:center}
.age{color:#A9D6C2}`;
  return page(lang, fmt, css, `
  <div class="top"><div class="brand"><span class="ic">${ICON_SVG}</span><span class="wm">${WORD_SVG}</span></div><span class="age">18+</span></div>
  <div class="main"><div><h1>${t.C.h}</h1><p class="sup">${t.C.s}</p></div>
    <div class="stage"><div class="phone"><span class="notch"></span><div class="su">
      <span class="lg">${ICON_SVG}</span><h2>${t.C.create}</h2>
      <div class="in a"><i></i></div><div class="in b"><i></i></div><div class="in c"><i></i></div>
      <div class="btn">${t.C.btn}</div></div></div></div></div>`);
}

/* ---------- D: grafite + coral, kicker + titulo unico + acao ---------- */
function pageD(lang, fmt) {
  const t = T[lang], big = fmt === 'story';
  const css = `
body{background:radial-gradient(900px 700px at 0% 100%,rgba(240,98,107,.20),transparent 62%),#090B10;color:#fff}
.brand{color:#fff}
.main{align-items:flex-start}
.kick{font-size:${big ? 40 : 38}px;font-weight:700;letter-spacing:.02em;color:#FF9AA0}
.nw{white-space:nowrap}
.tt{font-size:${big ? 100 : 88}px;font-weight:900;text-transform:uppercase;line-height:1.04;letter-spacing:-.005em;margin-top:-30px}
.tt .hl{color:#F0626B}
.act{border-left:12px solid #F0626B;background:rgba(240,98,107,.10);border-radius:0 20px 20px 0;padding:${big ? '32px 36px' : '30px 36px'};font-size:${big ? 62 : 60}px;font-weight:800;line-height:1.12}
.age{color:#94A3B8}`;
  return page(lang, fmt, css, `
  <div class="top"><div class="brand"><span class="ic">${ICON_SVG}</span><span class="wm">${WORD_SVG}</span></div><span class="age">18+</span></div>
  <div class="main"><div class="kick">${t.D.k}</div><div class="tt">${t.D.title}</div><div class="act">${t.action}</div></div>`);
}

function page(lang, fmt, css, body, foot = '') {
  const t = T[lang];
  return `<!DOCTYPE html>
<html lang="${t.lang}"><head><meta charset="UTF-8">
<style>${baseCss(fmt)}${css}</style></head><body>
${body}
${foot === 'bottom' ? '<div class="foot"><span class="age">18+</span></div>' : ''}
</body></html>`;
}

const PAGES = { A: pageA, B: pageB, C: pageC, D: pageD };
const jobs = [];
for (const ang of Object.keys(PAGES)) for (const lang of ['pt', 'en']) for (const fmt of ['feed', 'story']) {
  const name = `sinal01-${ang}-${lang}-${fmt}`;
  const dir = path.join(SRC, lang);
  fs.mkdirSync(dir, { recursive: true });
  const full = PAGES[ang](lang, fmt);
  const css = /<style>([\s\S]*?)<\/style>/.exec(full)[1];
  fs.writeFileSync(path.join(dir, `${name}.css`), css);
  fs.writeFileSync(path.join(dir, `${name}.html`), full.replace(/<style>[\s\S]*?<\/style>/, `<link rel="stylesheet" href="${name}.css">`));
  jobs.push({ name, fmt, dir });
}
console.log(`${jobs.length} HTML gerados em ${SRC}`);
if (ONLY_HTML) process.exit(0);

for (const j of jobs) {
  const png = path.join(ART, `${j.name}.png`);
  const H = j.fmt === 'story' ? 1920 : 1350;
  execFileSync(CHROME, ['--headless=new', '--disable-gpu', '--hide-scrollbars', '--allow-file-access-from-files',
    `--window-size=1080,${H}`, '--force-device-scale-factor=1', '--virtual-time-budget=3000',
    `--screenshot=${png}`, pathToFileURL(path.join(j.dir, `${j.name}.html`)).href], { stdio: 'ignore' });
  fs.copyFileSync(png, path.join(OUT2, `${j.name}.png`));
  console.log('ok', j.name);
}
