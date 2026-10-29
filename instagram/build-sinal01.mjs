/* Estudo de sinal 01 (anuncios Meta, pos-Andromeda): 4 angulos x PT/EN x feed 1080x1350 + story 1080x1920 = 16 PNG.
 *
 *   node instagram/build-sinal01.mjs          # gera os 16 HTML-fonte, renderiza com Chrome headless e copia para output
 *   node instagram/build-sinal01.mjs --html   # so gera os HTML
 *
 * Copy: content/ads/sinal01/copy-sinal01.md. Numeros: numeros-verificados.md do field-exploits-launch
 * (BTN vs SB 25bb, flop A-high rainbow, c-bet 33%, field fold 41,5% x GTO 25,0% faixa 19,0-31,0, 10,5% acima da faixa, n = 9.937 maos;
 * fonte: docs/02-paid/sinal01-spots-fortes.md linha 1 e content/ads/sinal01/numeros/spots_all.csv).
 * Regras duras: sem carta, ficha, dinheiro, mesa, dados; visual = tela do app reconstruida + tipografia.
 * Os 4 angulos mudam de proposito cor, composicao e mockup (Andromeda agrupa criativos parecidos):
 *   A dark navy + amber, card do spot com regua   B claro + azul, lista ranqueada com palavra riscada
 *   C teal + menta, dois celulares (cadastro + spot de exemplo)   D quase preto + coral, close tipografico
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
const LOCK_SVG = `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="11" width="14" height="10" rx="2.5"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>`;
const ARROW_UP = `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20V5M5 12l7-7 7 7"/></svg>`;
const CHECK = `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12.5l5 5L20 6.5"/></svg>`;

/* ---------- textos (copy-sinal01.md) ---------- */
const T = {
  pt: {
    lang: 'pt-BR', dec: ',', foot: 'Ferramenta de estudo',
    badge: 'NOVO MÓDULO', strong: 'DESVIO FORTE', over: 'OVERFOLD',
    foldVs: 'Fold contra c-bet de 33%', field: 'Field', gto: 'GTO',
    below: 'acima da faixa do GTO', how: 'Como explorar', howTxt: 'C-bet mais vezes, inclusive sem mão.',
    rangeLbl: 'faixa do GTO', sub25: '25bb · SRP', cls: 'flop A-high rainbow', n: '9.937 mãos',
    A: { h: '<span class="hl">Field Exploits:</span><br>onde o field erra', s: 'Spot a spot. E como explorar.' },
    B: { h: 'Você não precisa<br>de <s>mais vídeo</s>', s: 'Precisa saber <b>o que estudar primeiro.</b>', list: 'Spots do field', row: '25bb · flop A-high rainbow<br>c-bet de 33%' },
    C: { h: 'Comece <span class="hl">grátis.</span><br>Sem cartão.', s: 'Veja onde o field erra.', create: 'Criar conta', btn: 'Criar conta grátis', nocard: 'Sem cartão', week: 'Exemplo de spot' },
    D: { h: 'Spot lido<br>em segundos', s: 'Sem horas de solver. Com ajuste pronto.', ctx: 'BTN vs SB · 25bb · c-bet de 33%', title: 'O SB <span class="hl">folda demais</span> <span class="nw">contra c-bet</span> <span class="nw">de 33%</span>' },
  },
  en: {
    lang: 'en', dec: '.', foot: 'Study tool',
    badge: 'NEW MODULE', strong: 'STRONG DEVIATION', over: 'OVERFOLD',
    foldVs: 'Fold vs 33% c-bet', field: 'Field', gto: 'GTO',
    below: 'above the GTO range', how: 'How to exploit', howTxt: 'C-bet more often, even with air.',
    rangeLbl: 'GTO range', sub25: '25bb · SRP', cls: 'A-high rainbow flop', n: '9,937 hands',
    A: { h: 'Where the <span class="hl">field</span><br>gets it wrong', s: 'Spot by spot, and how to exploit it.' },
    B: { h: 'You don\u2019t need<br><s>more videos</s>', s: 'You need to know <b>what to study first.</b>', list: 'Field spots', row: '25bb · A-high rainbow flop<br>33% c-bet' },
    C: { h: 'Start <span class="hl">free.</span><br>No card needed.', s: 'See where the field errs.', create: 'Create account', btn: 'Create free account', nocard: 'No card needed', week: 'Example spot' },
    D: { h: 'Your spot,<br>read in seconds', s: 'Not hours in a solver.', ctx: 'BTN vs SB · 25bb · 33% c-bet', title: 'The SB <span class="hl">folds too much</span> vs the <span class="nw">33% c-bet</span>' },
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
.foot{display:flex;align-items:center;justify-content:space-between;flex:none;height:56px;font-size:26px;font-weight:600;letter-spacing:.02em}
.age{font-weight:800;font-size:26px;border:3px solid currentColor;border-radius:11px;padding:4px 12px}
.main{flex:1;display:flex;flex-direction:column;justify-content:${fmt === 'story' ? 'space-between' : 'space-evenly'};padding:${fmt === 'story' ? '48px 0 40px' : '18px 0 14px'}}
h1{font-weight:900;text-transform:uppercase;line-height:1.04;letter-spacing:.005em}
.sup{font-weight:500;line-height:1.3}
`;

/* ---------- card do spot (reconstrucao da tela do Field Exploits) ---------- */
const spotCss = `
.spot{background:#0F172A;border:2px solid rgba(251,191,36,.55);border-radius:2.8em;padding:3.6em 3.8em 3.4em;color:#fff;box-shadow:0 30px 80px rgba(0,0,0,.45)}
.spot .hd{display:flex;align-items:center;justify-content:space-between;margin-bottom:2.2em}
.spot .mod{display:flex;align-items:center;gap:.9em;font-size:2.4em;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:#FBBF24}
.spot .mod i{width:1.5em;height:1.15em;display:block}.spot .mod i svg{width:100%;height:100%}
.spot .chip{font-size:2.2em;font-weight:800;letter-spacing:.08em;color:#FBBF24;border:2px solid rgba(251,191,36,.6);border-radius:.5em;padding:.3em .7em;background:rgba(251,191,36,.08)}
.spot .ttl{display:flex;align-items:baseline;gap:1.3em;flex-wrap:wrap}
.spot .ttl b{font-size:6.2em;font-weight:800;letter-spacing:-.01em}
.spot .ttl span{font-size:3em;font-weight:600;color:#CBD5E1}
.spot .cls{font-size:3em;font-weight:700;color:#FBBF24;margin-top:.4em}
.spot .nn{font-size:.82em;font-weight:600;color:#94A3B8}
.spot .lbl{font-size:3em;font-weight:600;color:#CBD5E1;margin-top:.3em}
.spot .nums{display:flex;justify-content:space-between;align-items:flex-end;margin-top:1em}
.spot .nums div{display:flex;flex-direction:column}
.spot .nums .k{font-size:2.8em;font-weight:700;letter-spacing:.12em;text-transform:uppercase}
.spot .nums .v{font-size:9.6em;font-weight:800;line-height:1;letter-spacing:-.02em;font-variant-numeric:tabular-nums}
.spot .nums .f .k,.spot .nums .f .v{color:#34C9E6}
.spot .nums .g{align-items:flex-end}
.spot .nums .g .k,.spot .nums .g .v{color:#5FDB9C}
.spot .track{position:relative;height:3.4em;border-radius:1.7em;background:#1E293B;margin-top:.7em}
.spot .fill{position:absolute;left:0;top:0;bottom:0;border-radius:1.7em 0 0 1.7em;background:linear-gradient(90deg,#0C7F99,#34C9E6)}
.spot .gap{position:absolute;top:.45em;bottom:.45em;background:repeating-linear-gradient(135deg,rgba(251,191,36,.95) 0 .5em,rgba(251,191,36,.25) .5em 1em)}
.spot .band{position:absolute;top:-.5em;bottom:-.5em;border:.18em solid #5FDB9C;border-radius:.6em;background:rgba(95,219,156,.22)}
.spot .tick{position:absolute;top:-.9em;bottom:-.9em;width:.4em;margin-left:-.2em;border-radius:.2em;background:#5FDB9C}
.spot .rl{display:flex;justify-content:space-between;margin-top:1.1em;font-size:2.8em;font-weight:700}
.spot .rl .a{color:#FBBF24}.spot .rl .b{color:#5FDB9C}
.spot .over{display:inline-flex;align-items:center;gap:.5em;font-size:2.4em;font-weight:800;letter-spacing:.1em;color:#FCA5A5;border:2px solid rgba(252,165,165,.5);background:rgba(173,44,52,.28);border-radius:.5em;padding:.3em .7em;margin-top:1em;align-self:flex-start}
.spot .how{margin-top:1.6em;border-top:2px solid rgba(148,163,184,.25);padding-top:1.3em}
.spot .how .k{font-size:2.4em;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:#FBBF24}
.spot .how .t{font-size:3.9em;font-weight:700;margin-top:.25em;line-height:1.15}
.track .fill{width:41.5%}.track .gap{left:31%;width:10.5%}.track .band{left:19%;width:12%}.track .tick{left:25%}
`;
function rulerHtml(lang, withLabels = true) {
  const t = T[lang];
  return `<div class="track">
    <div class="fill"></div>
    <div class="gap"></div>
    <div class="band"></div>
    <div class="tick"></div>
  </div>
  ${withLabels ? `<div class="rl"><span class="a">${num(lang, '10.5')}% ${t.below}</span></div>` : ''}`;
}
function spotCard(lang, { base = 10, withN = false } = {}) {
  const t = T[lang];
  return `<div class="spot" style="font-size:${base}px">
    <div class="hd"><div class="mod"><i>${ICON_SVG}</i>Field Exploits</div><span class="chip">${t.strong}</span></div>
    <div class="ttl"><b>BTN vs SB</b><span>${t.sub25}</span></div>
    <div class="cls">${t.cls}${withN ? `<span class="nn"><span class="sp"> · </span>${t.n}</span>` : ''}</div>
    <div class="lbl">${t.foldVs}</div>
    <div class="nums"><div class="f"><span class="k">${t.field}</span><span class="v">${num(lang, '41.5')}%</span></div>
      <div class="g"><span class="k">${t.gto}</span><span class="v">${num(lang, '25.0')}%</span></div></div>
    ${rulerHtml(lang)}
    <span class="over">${t.over}</span>
    <div class="how"><div class="k">${t.how}</div><div class="t">${t.howTxt}</div></div>
  </div>`;
}

/* ---------- A: dark navy + amber, card do spot ---------- */
function pageA(lang, fmt) {
  const t = T[lang], big = fmt === 'story';
  const css = `
body{background:radial-gradient(1100px 800px at 85% -8%,rgba(212,164,24,.20),transparent 60%),radial-gradient(900px 700px at 0% 105%,rgba(34,53,89,.55),transparent 60%),#020617;color:#fff}
.brand{color:#D4A418}
.badge{font-size:26px;font-weight:900;letter-spacing:.14em;color:#0F1526;background:linear-gradient(180deg,#FCD34D,#F59E0B);border-radius:12px;padding:12px 22px}
h1{font-size:${big ? 84 : 70}px}.hl{color:#FBBF24}
.sup{font-size:${big ? 42 : 40}px;color:#E2E8F0;margin-top:20px}
.foot{color:#94A3B8}
${spotCss}`;
  return page(lang, fmt, css, `
  <div class="top"><div class="brand"><span class="ic">${ICON_SVG}</span><span class="wm">${WORD_SVG}</span></div><span class="badge">${t.badge}</span></div>
  <div class="main">${spotCard(lang, { base: big ? 10.2 : 9.2, withN: true })}
    <div><h1>${t.A.h}</h1><p class="sup">${t.A.s}</p></div></div>`);
}

/* ---------- B: claro + azul, lista ranqueada, palavra riscada ---------- */
function pageB(lang, fmt) {
  const t = T[lang], big = fmt === 'story';
  const rows = [0, 1, 2, 3].map((i) => `<div class="row ghost" style="opacity:${[0.85, 0.62, 0.42, 0.26][i]}">
      <div class="gb"><i style="width:${[330, 280, 360, 300][i]}px"></i><i class="s" style="width:${[230, 200, 250, 210][i]}px"></i></div><i class="gr"></i></div>`).join('');
  const css = `
body{background:linear-gradient(180deg,#F4F6FA 0%,#DCE4EF 100%);color:#0F1526}
.brand{color:#0F1526}
.badge{font-size:24px;font-weight:800;letter-spacing:.12em;color:#fff;background:#223559;border-radius:12px;padding:10px 20px}
h1{font-size:${big ? 92 : 78}px;color:#0F1526}
h1 s{text-decoration:none;position:relative;color:#223559;white-space:nowrap}
h1 s::after{content:"";position:absolute;left:-6px;right:-6px;top:52%;height:${big ? 12 : 10}px;background:#AD2C34;border-radius:6px;transform:rotate(-2deg)}
.sup{font-size:${big ? 44 : 40}px;color:#2F435C;margin-top:22px}.sup b{color:#0F1526;font-weight:800}
.foot{color:#475569}
.list{background:#fff;border-radius:34px;box-shadow:0 30px 70px rgba(15,21,38,.18),0 2px 0 rgba(15,21,38,.06);padding:34px 36px 30px;width:100%}
.list .lh{display:flex;align-items:center;justify-content:space-between;margin-bottom:22px}
.list .lh .m{display:flex;align-items:center;gap:14px;font-size:26px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:#223559}
.list .lh .m i{width:38px;height:29px;display:block;color:#223559}.list .lh .m i svg{width:100%;height:100%}
.list .lh .c{font-size:24px;font-weight:700;color:#475569}
.row{display:flex;align-items:center;justify-content:space-between;border-radius:22px;padding:22px 26px;margin-top:12px}
.row.top1{background:#EEF3FA;border:3px solid #223559;padding:30px 30px;margin-top:0}
.row.top1 .p{font-size:58px;font-weight:800;line-height:1.05;color:#0F1526}
.row.top1 .q{font-size:30px;font-weight:600;color:#475569;margin-top:8px}
.row.top1 .tag{display:flex;align-items:center;gap:10px;font-size:28px;font-weight:800;letter-spacing:.06em;color:#8E1F27;background:#FBE4E5;border-radius:14px;padding:14px 20px}
.row.top1 .tag i{width:30px;height:30px;display:block}
.row.ghost{border:2px dashed #CBD5E1;filter:blur(4.5px)}
.row.ghost .gb{display:flex;flex-direction:column;gap:12px}
.row.ghost .gb i{display:block;height:26px;border-radius:13px;background:#475569}.row.ghost .gb i.s{height:18px;background:#94A3B8}
.row.ghost .gr{display:block;width:180px;height:34px;border-radius:17px;background:#C9768B}`;
  return page(lang, fmt, css, `
  <div class="top"><div class="brand"><span class="ic">${ICON_SVG}</span><span class="wm">${WORD_SVG}</span></div><span class="badge">${T[lang].badge}</span></div>
  <div class="main"><div><h1>${t.B.h}</h1><p class="sup">${t.B.s}</p></div>
    <div class="list"><div class="lh"><span class="m"><i>${ICON_SVG}</i>Field Exploits</span><span class="c">${t.B.list}</span></div>
      <div class="row top1"><div><div class="p">BTN vs SB</div><div class="q">${t.B.row}</div></div>
        <div class="tag"><i>${ARROW_UP}</i>${t.over}</div></div>
      ${rows}</div></div>`);
}

/* ---------- C: teal + menta, dois celulares ---------- */
function pageC(lang, fmt) {
  const t = T[lang], big = fmt === 'story';
  const ph = big ? 870 : 770, pw = big ? 430 : 410;
  const css = `
${spotCss}
body{background:radial-gradient(1000px 760px at 50% 108%,rgba(127,227,174,.22),transparent 62%),linear-gradient(170deg,#04323B 0%,#02171C 100%);color:#fff}
.brand{color:#fff}
h1{font-size:${big ? 84 : 78}px}.hl{color:#7FE3AE}
.sup{font-size:${big ? 44 : 40}px;color:#D5F5E3;margin-top:20px}
.foot{color:#A9D6C2}
.stage{position:relative;height:${ph + 40}px;flex:none}
.phone{position:absolute;top:20px;width:${pw}px;height:${ph}px;border-radius:58px;background:#0F172A;border:10px solid #0B1220;box-shadow:0 0 0 2px #2B3A52,0 40px 80px rgba(0,0,0,.55);overflow:hidden;padding:30px 26px}
.phone.l{left:6px;transform:rotate(-3deg)}
.phone.r{right:6px;top:${big ? 62 : 56}px;transform:rotate(2.5deg)}
.notch{position:absolute;top:12px;left:50%;width:110px;height:10px;margin-left:-55px;border-radius:6px;background:#1E293B}
.su{display:flex;flex-direction:column;height:100%;padding-top:26px}
.su .lg{color:#D4A418;width:70px;height:52px}.su .lg svg{width:100%;height:100%}
.su h2{font-size:40px;font-weight:800;margin-top:28px}
.su .in{height:76px;border-radius:18px;background:#1E293B;border:2px solid #334155;margin-top:18px;display:flex;align-items:center;padding:0 22px}
.su .in i{display:block;height:16px;border-radius:8px;background:#64748B}
.su .btn{margin-top:30px;height:84px;border-radius:20px;background:linear-gradient(180deg,#FCD34D,#F59E0B);color:#0F1526;font-size:28px;font-weight:800;display:flex;align-items:center;justify-content:center}
.su .nc{display:flex;align-items:center;justify-content:center;gap:12px;margin-top:26px;font-size:27px;font-weight:700;color:#7FE3AE}
.su .nc i{width:30px;height:30px;display:block}
.fs{display:flex;flex-direction:column;height:100%;padding-top:26px}
.fs .h{display:flex;align-items:center;justify-content:space-between}
.fs .h .m{display:flex;align-items:center;gap:10px;font-size:24px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:#FBBF24}
.fs .h .m i{width:36px;height:27px;display:block}.fs .h .m i svg{width:100%;height:100%}
.fs .wk{font-size:26px;font-weight:700;color:#CBD5E1;margin:22px 0 14px}
.fs .spot{font-size:8px;padding:2.6em 2.4em 2.4em;border-radius:2.4em;box-shadow:none}
.fs .spot .hd{display:none}
.fs .spot .how{display:none}
.fs .spot .nn .sp{display:none}
.fs .spot .nn{display:block;font-size:.8em;margin-top:.1em}
.fs .spot .lbl{font-size:2.6em}
.fs .spot .ttl b{font-size:5.4em}
.fs .spot .nums{flex-direction:column;align-items:stretch;gap:.3em}
.fs .spot .nums div{flex-direction:row;justify-content:space-between;align-items:baseline;gap:.8em}
.fs .spot .nums .v{font-size:7.4em}
.fs .spot .track{margin-top:1.5em}
.fs .spot .rl{font-size:2.5em}
.fs .spot .over{margin-top:.9em}
.fs .lockrow{display:flex;align-items:center;justify-content:space-between;border:2px dashed #475569;border-radius:20px;padding:20px 22px;margin-top:14px}
.fs .lockrow i.b{display:block;height:20px;border-radius:10px;background:#64748B;filter:blur(3px)}
.fs .lockrow i.k{display:block;width:34px;height:34px;color:#FBBF24}`;
  return page(lang, fmt, css, `
  <div class="top"><div class="brand"><span class="ic">${ICON_SVG}</span><span class="wm">${WORD_SVG}</span></div></div>
  <div class="main"><div><h1>${t.C.h}</h1><p class="sup">${t.C.s}</p></div>
    <div class="stage">
      <div class="phone l"><span class="notch"></span><div class="su">
        <span class="lg">${ICON_SVG}</span><h2>${t.C.create}</h2>
        <div class="in"><i style="width:46%"></i></div><div class="in"><i style="width:30%"></i></div><div class="in"><i style="width:38%"></i></div>
        <div class="btn">${t.C.btn}</div>
        <div class="nc"><i>${CHECK}</i>${t.C.nocard}</div></div></div>
      <div class="phone r"><span class="notch"></span><div class="fs">
        <div class="h"><span class="m"><i>${ICON_SVG}</i>Field Exploits</span></div>
        <div class="wk">${t.C.week}</div>
        ${spotCard(lang, { base: 8, withN: true })}
        ${big ? `<div class="lockrow"><i class="b" style="width:200px"></i><i class="k">${LOCK_SVG}</i></div>` : ''}</div></div>
    </div></div>`);
}

/* ---------- D: quase preto + coral, close tipografico ---------- */
function pageD(lang, fmt) {
  const t = T[lang], big = fmt === 'story';
  const css = `
body{background:radial-gradient(900px 700px at 0% 100%,rgba(240,98,107,.20),transparent 62%),#090B10;color:#fff}
.brand{color:#fff}
h1{font-size:${big ? 96 : 86}px;letter-spacing:-.005em}
.sup{font-size:${big ? 44 : 40}px;color:#CBD5E1;margin-top:20px}
.foot{color:#94A3B8}
.zoom{margin:0 -72px;background:#10151F;border-top:2px solid #2A2F3C;border-bottom:2px solid #2A2F3C;padding:${big ? '56px 72px 60px' : '44px 72px 46px'}}
.zoom .ctx{display:flex;align-items:center;gap:18px;flex-wrap:wrap;font-size:30px;font-weight:700;color:#CBD5E1}
.zoom .ctx .tg{display:inline-flex;align-items:center;gap:10px;font-size:26px;font-weight:800;letter-spacing:.08em;color:#FF9AA0;border:2px solid rgba(255,154,160,.5);background:rgba(173,44,52,.25);border-radius:12px;padding:8px 16px}
.zoom .ctx .tg i{width:26px;height:26px;display:block}
.zoom .cl{font-size:30px;font-weight:700;color:#FBBF24;margin-top:14px}
.zoom .tt{font-size:${big ? 90 : 80}px;font-weight:900;text-transform:uppercase;line-height:1.04;margin-top:${big ? 34 : 26}px}
.zoom .tt .hl{color:#F0626B}
.nw{white-space:nowrap}
.zoom .how{margin-top:${big ? 40 : 30}px;border-left:12px solid #F0626B;background:rgba(240,98,107,.10);border-radius:0 20px 20px 0;padding:${big ? '28px 34px' : '22px 30px'}}
.zoom .how .k{font-size:26px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:#FF9AA0}
.zoom .how .tx{font-size:${big ? 58 : 52}px;font-weight:800;line-height:1.12;margin-top:8px}`;
  return page(lang, fmt, css, `
  <div class="top"><div class="brand"><span class="ic">${ICON_SVG}</span><span class="wm">${WORD_SVG}</span></div></div>
  <div class="main"><div><h1>${t.D.h}</h1><p class="sup">${t.D.s}</p></div>
    <div class="zoom"><div class="ctx"><span>${t.D.ctx}</span><span class="tg"><i>${ARROW_UP}</i>${t.over}</span></div>
      <div class="cl">${t.cls}</div>
      <div class="tt">${t.D.title}</div>
      <div class="how"><div class="k">${t.how}</div><div class="tx">${t.howTxt}</div></div></div></div>`);
}

function page(lang, fmt, css, body) {
  const t = T[lang];
  return `<!DOCTYPE html>
<html lang="${t.lang}"><head><meta charset="UTF-8">
<style>${baseCss(fmt)}${css}</style></head><body>
${body}
<div class="foot"><span>${t.foot}</span><span class="age">18+</span></div>
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
