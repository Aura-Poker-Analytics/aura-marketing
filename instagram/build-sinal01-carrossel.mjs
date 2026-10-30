/* Estudo de sinal 01, 5o anuncio: carrossel "a Aura inteira" (10 cartoes x PT/EN = 20 PNG, 1080x1350).
 * Versao limpa: titulo curto, no maximo 1 linha de apoio, 1 visual grande, 1 rotulo por cartao, leitura em 2 s.
 *
 *   node instagram/build-sinal01-carrossel.mjs          # gera HTML/CSS-fonte, renderiza com Chrome headless e copia para output
 *   node instagram/build-sinal01-carrossel.mjs --html   # so gera os HTML/CSS
 *
 * Copy: content/ads/sinal01/carrossel/copy-carrossel.md (PT) e en/copy-carrossel.md (EN). Capa = opcao 1.
 * Numeros: so os da copy (BTN vs SB 25bb, flop A-high rainbow, c-bet de 33%, field fold 41,5% x GTO 25,0%, 6,9 mi+, 90 situacoes;
 * spot: docs/02-paid/sinal01-spots-fortes.md linha 1 e content/ads/sinal01/numeros/spots_all.csv).
 * Onde a copy nao tem numero (preflop, reacoes, tendencia, arvore), as telas mostram barras e formas, nunca numero inventado.
 * Regras duras: sem carta, ficha, dinheiro, mesa, roleta. Fundo navy, ambar, indicador de progresso 1..10 no rodape de todo cartao.
 * Fonte: HTML e CSS separados (CSS em .css, <link>, sem <title>, sem numero em style inline), por idioma.
 */
import fs from 'fs';
import path from 'path';
import { execFileSync } from 'child_process';
import { fileURLToPath, pathToFileURL } from 'url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const TPL = path.join(ROOT, 'instagram/templates');
const BASE = path.join(ROOT, 'content/ads/sinal01/carrossel');
const ART = path.join(BASE, 'art');
const SRC = path.join(BASE, 'fonte');
const OUT2 = path.join(ROOT, 'instagram/output/sinal01-carrossel');
const CHROME = process.env.CHROME_PATH || 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const ONLY_HTML = process.argv.includes('--html');
for (const d of [ART, OUT2]) fs.mkdirSync(d, { recursive: true });

/* logos oficiais: extraidos do template existente (nada retipado) */
const tplSrc = fs.readFileSync(path.join(TPL, 'carrossel-capa.html'), 'utf8');
const ICON = /const ICON_PATHS = `([\s\S]*?)`;/.exec(tplSrc)[1];
const LETTERS = /const AURA_LETTERS = `([\s\S]*?)`;/.exec(tplSrc)[1];
const ICON_SVG = `<svg viewBox="0 0 60 45" fill="currentColor" xmlns="http://www.w3.org/2000/svg">${ICON}</svg>`;
const WORD_SVG = `<svg viewBox="1 204 594 129" fill="currentColor" xmlns="http://www.w3.org/2000/svg">${LETTERS}</svg>`;
const CHECK = `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12.5l5 5L20 6.5"/></svg>`;
const ARROW = `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12h15M13 6l6 6-6 6"/></svg>`;

const N = 10;
const T = {
  pt: {
    lang: 'pt-BR', dec: ',', url: 'www.aurapoker.com', ill: 'Exemplo ilustrativo',
    c1: { a: 'O solver mostra o equilíbrio.', b: 'A Aura mostra o field.', s: 'Do preflop ao river, ao lado do GTO.' },
    c2: { chip: 'Novo · Field Exploits', h: 'O SB folda <span class="hl">demais</span> contra c-bet', ctx: 'BTN vs SB · 25bb · flop A-high rainbow · c-bet de 33%', field: 'Field', gto: 'GTO', act: 'C-bet para ter auto-profit!' },
    c3: { chip: 'Modo GTO', h: 'GTO ao lado de <span class="hl">cada spot</span>', big: '6,9 mi+', cap: 'pontos de decisão GTO, do flop ao river' },
    c4: { chip: 'Postflop Analysis', h: 'Ação e <span class="hl">reação</span>', p: 'C-bet, barrel e raise do field, e como reagem.', r: ['Fold', 'Call', 'Raise'] },
    c5: { chip: 'Preflop Analysis', h: 'Preflop, <span class="hl">posição a posição</span>', p: 'RFI, 3-bet e squeeze por buy-in e etapa.' },
    c6: { chip: 'Field Ranges', h: 'Ranges do field, <span class="hl">mão a mão</span>', p: 'Em âmbar: onde o field difere do GTO.', gtoL: 'GTO' },
    c7: { chip: 'Field Trends', h: 'O que <span class="hl">mudou</span> no field', p: 'Trimestre a trimestre: mudou ou oscilou?' },
    c8: { chip: 'Node-by-Node', h: 'A árvore da mão, <span class="hl">nó a nó</span>', p: 'De quem é a vez e a frequência de cada ação.', acts: ['Check', 'Donk', 'C-bet'] },
    c9: { chip: 'Plano Individual', h: 'Todos os módulos, <span class="hl">um login</span>',
      mods: ['Preflop Analysis', 'Postflop Analysis', 'Field Ranges', 'Field Exploits', 'Field Trends', 'Node-by-Node'] },
    c10: { h: 'Comece grátis.<br><span class="hl">Sem cartão.</span>', btn: 'Criar conta grátis', foot: 'Ferramenta de estudo · 18+' },
  },
  en: {
    lang: 'en', dec: '.', url: 'www.aurapoker.com', ill: 'Illustrative example',
    c1: { a: 'The solver shows equilibrium.', b: 'Aura shows the field.', s: 'Preflop to river, next to GTO.' },
    c2: { chip: 'New · Field Exploits', h: 'The SB folds <span class="hl">too much</span> vs c-bet', ctx: 'BTN vs SB · 25bb · A-high rainbow flop · 33% c-bet', field: 'Field', gto: 'GTO', act: 'C-bet for auto-profit!' },
    c3: { chip: 'GTO Mode', h: 'GTO next to <span class="hl">every spot</span>', big: '6.9M+', cap: 'GTO decision points, flop to river' },
    c4: { chip: 'Postflop Analysis', h: 'Action and <span class="hl">reaction</span>', p: 'C-bet, barrel, raise, and how they respond.', r: ['Fold', 'Call', 'Raise'] },
    c5: { chip: 'Preflop Analysis', h: 'Preflop, <span class="hl">position by position</span>', p: 'RFI, 3-bet and squeeze by buy-in and stage.' },
    c6: { chip: 'Field Ranges', h: 'Field ranges, <span class="hl">hand by hand</span>', p: 'In amber: where the field differs from GTO.', gtoL: 'GTO' },
    c7: { chip: 'Field Trends', h: 'What <span class="hl">changed</span> in the field', p: 'Real change or normal variation?' },
    c8: { chip: 'Node-by-Node', h: 'The hand tree, <span class="hl">node by node</span>', p: 'Whose turn it is and how often each action.', acts: ['Check', 'Donk', 'C-bet'] },
    c9: { chip: 'Individual plan', h: 'Every module, <span class="hl">one login</span>',
      mods: ['Preflop Analysis', 'Postflop Analysis', 'Field Ranges', 'Field Exploits', 'Field Trends', 'Node-by-Node'] },
    c10: { h: 'Start free.<br><span class="hl">No credit card.</span>', btn: 'Create free account', foot: 'Study tool · 18+' },
  },
};

/* ---------- CSS (um por idioma; sem numero em style inline, tudo por classe) ---------- */
const FONT = pathToFileURL(path.join(TPL, 'fonts/Montserrat-Variable-latin.woff2')).href;
const CSS = `
@font-face{font-family:"Montserrat";src:url("${FONT}") format("woff2");font-weight:100 900;font-display:block}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px;overflow:hidden}
body{font-family:"Montserrat","Segoe UI",sans-serif;position:relative;display:flex;flex-direction:column;padding:56px 72px 48px;
  color:#fff;-webkit-font-smoothing:antialiased;
  background:radial-gradient(1000px 760px at 100% -6%,rgba(212,164,24,.22),transparent 60%),radial-gradient(900px 700px at -4% 104%,rgba(34,53,89,.6),transparent 62%),#020617}
svg{display:block}
.top{display:flex;align-items:center;justify-content:space-between;height:64px;flex:none}
.brand{display:flex;align-items:center;gap:16px;height:100%;color:#D4A418}
.brand .ic{width:58px;height:44px}.brand .wm{width:132px}.brand svg{width:100%;height:100%}
.chip{font-size:26px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:#FBBF24;border:2px solid rgba(251,191,36,.6);border-radius:12px;padding:10px 20px;background:rgba(251,191,36,.07)}
.ill{font-size:26px;font-weight:700;color:#E2E8F0;border:2px dashed #94A3B8;border-radius:12px;padding:10px 20px;background:rgba(148,163,184,.10)}
h1.hd{font-size:84px;font-weight:900;text-transform:uppercase;line-height:1.04;letter-spacing:-.005em;margin-top:52px;flex:none;text-wrap:balance}
.hl{color:#FBBF24}
p.ln{font-size:40px;font-weight:500;line-height:1.3;color:#E2E8F0;margin-top:24px;flex:none}
p.ctx{font-size:30px;font-weight:700;line-height:1.3;color:#CBD5E1;margin-top:26px;flex:none}
.vis{flex:1;min-height:0;display:flex;flex-direction:column;justify-content:center;margin-top:16px}
.nav{display:flex;align-items:center;justify-content:space-between;height:36px;flex:none;margin-top:26px}
.segs{display:flex;gap:8px}
.segs .s{display:block;width:56px;height:8px;border-radius:4px;background:#1E293B}
.segs .s.past{background:#475569}.segs .s.on{background:#FBBF24}
.cnt{display:flex;align-items:center;gap:12px;font-size:26px;font-weight:800;color:#CBD5E1;letter-spacing:.04em}
.cnt b{color:#FBBF24;font-weight:800}.cnt svg{width:30px;height:30px;color:#FBBF24}

/* 01 capa */
.c01 .cvmain{flex:1;display:flex;flex-direction:column;justify-content:center}
.c01 .t1{font-size:78px;font-weight:900;text-transform:uppercase;line-height:1.06;color:#94A3B8;letter-spacing:.005em}
.c01 .t2{font-size:118px;font-weight:900;text-transform:uppercase;line-height:1.02;color:#FBBF24;margin-top:26px;letter-spacing:-.01em}
.c01 .sub{font-size:44px;font-weight:600;color:#E2E8F0;margin-top:44px;line-height:1.25}

/* 02 field exploits */
.c02 .pair{display:flex;gap:28px}
.c02 .cell{flex:1;display:flex;flex-direction:column;gap:14px;background:#0F172A;border:2px solid rgba(251,191,36,.32);border-radius:36px;padding:40px 34px 44px;box-shadow:0 30px 80px rgba(0,0,0,.45)}
.c02 .k{font-size:34px;font-weight:800;letter-spacing:.14em;text-transform:uppercase}
.c02 .v{font-size:128px;font-weight:800;line-height:1;letter-spacing:-.03em}
.c02 .f .k,.c02 .f .v{color:#34C9E6}.c02 .g .k,.c02 .g .v{color:#5FDB9C}
.c02 .act{font-size:54px;font-weight:800;line-height:1.15;color:#FBBF24;margin-top:60px;text-wrap:balance}

/* 03 modo gto */
.c03 .vis{align-items:flex-start}
.c03 .big{font-size:230px;font-weight:900;line-height:1;color:#FBBF24;letter-spacing:-.04em;white-space:nowrap}
.c03 .cap{font-size:46px;font-weight:600;line-height:1.25;color:#E2E8F0;margin-top:30px;text-wrap:balance}

/* 04 acao e reacao */
.rb{display:flex;align-items:center;gap:30px;margin-top:56px}.rb:first-child{margin-top:0}
.rb .n{width:210px;font-size:52px;font-weight:800;flex:none}
.rb .tr{flex:1;height:100px;border-radius:50px;background:#1E293B;position:relative;overflow:hidden}
.rb .tr i{position:absolute;left:0;top:0;bottom:0;border-radius:50px}
.rb.fo .n{color:#4FC3DA}.rb.fo i{width:48%;background:#0B6B80;border:4px solid #4FC3DA}
.rb.ca .n{color:#5FDB9C}.rb.ca i{width:32%;background:#348A5D;border:4px solid #5FDB9C}
.rb.ra .n{color:#F18A91}.rb.ra i{width:20%;background:#AD2C34;border:4px solid #F18A91}

/* 05 preflop */
.pr{display:flex;align-items:center;gap:30px;margin-top:30px}.pr:first-child{margin-top:0}
.pr .n{width:150px;font-size:48px;font-weight:800;flex:none}
.pr .tr{flex:1;height:64px;border-radius:32px;background:#1E293B;position:relative;overflow:hidden}
.pr .tr i{position:absolute;left:0;top:0;bottom:0;border-radius:32px;background:linear-gradient(90deg,#0C7F99,#34C9E6)}
.pr.w1 i{width:26%}.pr.w2 i{width:38%}.pr.w3 i{width:54%}.pr.w4 i{width:76%}.pr.w5 i{width:64%}.pr.w6 i{width:44%}

/* 06 grade */
.duo{display:flex;gap:20px;margin:16px -34px 0}
.duo .g{flex:1;display:flex;flex-direction:column;gap:18px}
.duo .gl{font-size:52px;font-weight:800;letter-spacing:.06em;text-transform:uppercase}
.duo .g.fld .gl{color:#34C9E6}.duo .g.gt .gl{color:#5FDB9C}
.gridw{display:grid;width:100%;grid-template-columns:repeat(6,1fr);gap:5px}
.gridw i{display:flex;align-items:center;justify-content:center;aspect-ratio:1/1;border-radius:10px;font-style:normal;font-size:30px;font-weight:800;color:#fff;opacity:.28}
.gridw i.d{opacity:1;box-shadow:inset 0 0 0 5px #FBBF24}
.gridw i.d.f{background:#2A6F8F}
.gridw i.r{background:#AD2C34}.gridw i.f{background:#16384A}.gridw i.m{background:linear-gradient(90deg,#AD2C34 0 55%,#16384A 55% 100%)}

/* 07 tendencia e 08 arvore */
svg.fig{width:100%;height:auto}
.fig text{font-family:"Montserrat","Segoe UI",sans-serif;font-weight:800}

/* 09 lista */
html[lang="pt-BR"] .c09 h1.hd{font-size:72px}
.mods{display:flex;flex-direction:column;gap:14px}
.mods .m{display:flex;align-items:center;gap:26px;background:#0F172A;border:2px solid rgba(251,191,36,.28);border-radius:20px;padding:0 30px;height:86px;font-size:42px;font-weight:700}
.mods .m .ck{width:46px;height:46px;border-radius:50%;background:#348A5D;color:#fff;display:flex;align-items:center;justify-content:center;flex:none}
.mods .m .ck svg{width:28px;height:28px}

/* 10 cta */
.c10 .cm{flex:1;display:flex;flex-direction:column;justify-content:center}
.c10 .lgb{display:flex;align-items:center;gap:26px;color:#D4A418}
.c10 .lgb .ic{width:118px;height:88px}.c10 .lgb .wm{width:300px}.c10 .lgb svg{width:100%;height:100%}
.c10 h1.big{font-size:124px;font-weight:900;text-transform:uppercase;line-height:1.02;margin-top:70px;letter-spacing:-.01em}
.c10 .btn{margin-top:80px;display:flex;align-items:center;justify-content:center;gap:18px;height:132px;border-radius:30px;background:linear-gradient(180deg,#FCD34D,#F59E0B);color:#0F1526;font-size:52px;font-weight:900;box-shadow:0 24px 60px rgba(245,158,11,.28)}
.c10 .btn svg{width:50px;height:50px}
.c10 .url{margin-top:36px;text-align:center;font-size:44px;font-weight:800;color:#FBBF24;letter-spacing:.02em}
.c01 .age{flex:none;font-size:26px;font-weight:700;color:#94A3B8;border:2px solid #334155;border-radius:10px;padding:6px 14px;letter-spacing:.04em}
.c10 .small{flex:none;text-align:center;font-size:28px;font-weight:600;color:#94A3B8;letter-spacing:.02em}
`;

/* ---------- pecas ---------- */
const brand = `<div class="brand"><span class="ic">${ICON_SVG}</span><span class="wm">${WORD_SVG}</span></div>`;
const nav = (n) => `<div class="nav"><div class="segs">${Array.from({ length: N }, (_, i) => `<i class="s${i + 1 < n ? ' past' : i + 1 === n ? ' on' : ''}"></i>`).join('')}</div>
  </div>`;
const num = (lang, s) => s.replace('.', T[lang].dec);

/* card: topo (logo + 1 rotulo), titulo, apoio opcional, 1 visual */
function card(lang, n, { right = '', h, p = '', ctx = '', vis }) {
  const t = T[lang];
  return `<!DOCTYPE html>
<html lang="${t.lang}"><head><meta charset="UTF-8">
<link rel="stylesheet" href="carrossel.css"></head>
<body class="c${String(n).padStart(2, '0')}">
<div class="top">${brand}${right}</div>
<h1 class="hd">${h}</h1>
${p ? `<p class="ln">${p}</p>` : ''}${ctx ? `<p class="ctx">${ctx}</p>` : ''}
<div class="vis">${vis}</div>
${nav(n)}
</body></html>`;
}
const chip = (x) => `<span class="chip">${x}</span>`;
const exChip = (lang, x) => chip(`${lang === 'pt' ? 'Exemplo' : 'Example'} · ${x}`);

/* 01 */
function c01(lang) {
  const t = T[lang], c = t.c1;
  return `<!DOCTYPE html>
<html lang="${t.lang}"><head><meta charset="UTF-8">
<link rel="stylesheet" href="carrossel.css"></head>
<body class="c01">
<div class="top">${brand}<div class="age">18+</div></div>
<div class="cvmain">
  <div class="t1">${c.a}</div>
  <div class="t2">${c.b}</div>
  <div class="sub">${c.s}</div>
</div>
${nav(1)}
</body></html>`;
}
/* 02 */
function c02(lang) {
  const t = T[lang], c = t.c2;
  return card(lang, 2, {
    right: chip(c.chip), h: c.h, ctx: c.ctx,
    vis: `<div class="pair"><div class="cell f"><span class="k">${c.field}</span><span class="v">${num(lang, '41.5')}%</span></div>
    <div class="cell g"><span class="k">${c.gto}</span><span class="v">${num(lang, '25.0')}%</span></div></div>
    <div class="act">${c.act}</div>`,
  });
}
/* 03 */
function c03(lang) {
  const c = T[lang].c3;
  return card(lang, 3, { right: chip(c.chip), h: c.h, vis: `<div class="big">${c.big}</div><div class="cap">${c.cap}</div>` });
}
/* 04 */
function c04(lang) {
  const c = T[lang].c4;
  return card(lang, 4, {
    right: exChip(lang, c.chip), h: c.h, p: c.p,
    vis: `<div class="rb fo"><span class="n">${c.r[0]}</span><div class="tr"><i></i></div></div>
      <div class="rb ca"><span class="n">${c.r[1]}</span><div class="tr"><i></i></div></div>
      <div class="rb ra"><span class="n">${c.r[2]}</span><div class="tr"><i></i></div></div>`,
  });
}
/* 05 */
function c05(lang) {
  const c = T[lang].c5;
  const rows = ['UTG', 'HJ', 'CO', 'BTN', 'SB'];
  return card(lang, 5, {
    right: exChip(lang, c.chip), h: c.h, p: c.p,
    vis: rows.map((r, i) => `<div class="pr w${i + 1}"><span class="n">${r}</span><div class="tr"><i></i></div></div>`).join(''),
  });
}
/* 06 */
function c06(lang) {
  const t = T[lang], c = t.c6;
  const kind = (i, j) => {
    if (i === j) return 'r';
    const suited = i < j; const hi = Math.min(i, j), lo = Math.max(i, j);
    if (suited) {
      if (hi === 0) return 'r';
      if (hi === 1) return lo <= 5 ? 'r' : lo <= 9 ? 'm' : 'f';
      if (hi === 2 || hi === 3) return lo <= 5 ? 'r' : lo === 6 ? 'm' : 'f';
      if (hi === 4) return lo <= 6 ? 'r' : lo === 7 ? 'm' : 'f';
      if (hi === 5) return lo <= 7 ? 'r' : 'f';
      if (hi === 6) return lo === 7 ? 'r' : lo === 8 ? 'm' : 'f';
      if (hi === 7) return lo === 8 ? 'r' : 'f';
      if (hi === 8) return lo === 9 ? 'r' : 'f';
      if (hi === 9) return lo === 10 ? 'm' : 'f';
      return 'f';
    }
    if (hi === 0) return lo <= 4 ? 'r' : lo === 5 ? 'm' : 'f';
    if (hi === 1) return lo <= 3 ? 'r' : lo === 4 ? 'm' : 'f';
    if (hi === 2) return lo === 3 ? 'r' : lo === 4 ? 'm' : 'f';
    if (hi === 3) return lo === 4 ? 'm' : 'f';
    return 'f';
  };
  /* recorte A..9 (6x6) com o mesmo bloco nos dois grids; notacao padrao: par na diagonal, suited acima, offsuit abaixo.
     diferencas plausiveis: o field abre mais offsuit fraca e folda suited que o GTO joga (mesmas celulas destacadas nos dois) */
  const N6 = 6, R = 'AKQJT9';
  const fieldRaise = [[5, 0], [5, 1], [4, 1], [5, 2], [4, 2], [5, 3], [4, 3], [5, 4]];
  const fieldFold = [[1, 5], [2, 5], [3, 5], [2, 4]];
  const has = (list, i, j) => list.some(([x, y]) => x === i && y === j);
  const grid = (isField) => {
    let cells = '';
    for (let i = 0; i < N6; i++) for (let j = 0; j < N6; j++) {
      const raise = has(fieldRaise, i, j), fold = has(fieldFold, i, j), d = raise || fold;
      let k = kind(i, j);
      if (isField && raise) k = 'r';
      if (isField && fold) k = 'f';
      const hi = Math.min(i, j), lo = Math.max(i, j);
      const name = R[hi] + R[lo] + (i === j ? '' : i < j ? 's' : 'o');
      cells += `<i class="${k}${d ? ' d' : ''}">${name}</i>`;
    }
    return `<div class="gridw">${cells}</div>`;
  };
  return card(lang, 6, { right: exChip(lang, c.chip), h: c.h, p: c.p,
    vis: `<div class="duo"><div class="g fld"><span class="gl">${t.c2.field}</span>${grid(true)}</div><div class="g gt"><span class="gl">${c.gtoL}</span>${grid(false)}</div></div>` });
}
/* 07 */
function c07(lang) {
  const t = T[lang], c = t.c7;
  const xs = [70, 175, 280, 385, 490, 595, 700, 805];
  const ys = [330, 300, 350, 310, 340, 290, 150, 100];
  const pts = xs.map((x, i) => `${x},${ys[i]}`).join(' ');
  const dots = xs.map((x, i) => {
    const out = i >= 6;
    return `<circle cx="${x}" cy="${ys[i]}" r="${out ? 18 : 14}" fill="${out ? '#FBBF24' : '#0F172A'}" stroke="${out ? '#FBBF24' : '#34C9E6'}" stroke-width="6"/>`;
  }).join('');
  return card(lang, 7, {
    right: exChip(lang, c.chip), h: c.h, p: c.p,
    vis: `<svg class="fig" viewBox="0 0 864 520" xmlns="http://www.w3.org/2000/svg">
      <rect x="20" y="240" width="824" height="150" rx="22" fill="#FBBF24" fill-opacity="0.13" stroke="#FBBF24" stroke-opacity="0.65" stroke-width="3" stroke-dasharray="14 10"/>
      <polyline points="${pts}" fill="none" stroke="#34C9E6" stroke-width="9" stroke-linejoin="round" stroke-linecap="round"/>
      ${dots}
    </svg>`,
  });
}
/* 08 */
function c08(lang) {
  const c = T[lang].c8;
  const pill = (x, y, label, fill, stroke) => `<rect x="${x}" y="${y}" width="340" height="110" rx="28" fill="${fill}" stroke="${stroke}" stroke-width="4"/>
      <text x="${x + 170}" y="${y + 71}" font-size="46" fill="#fff" text-anchor="middle">${label}</text>`;
  const br = (x1, y1, x2, y2, col) => `<path d="M${x1} ${y1} C${x1} ${(y1 + y2) / 2} ${x2} ${(y1 + y2) / 2} ${x2} ${y2}" fill="none" stroke="${col}" stroke-width="7" stroke-linecap="round"/>`;
  return card(lang, 8, {
    right: exChip(lang, c.chip), h: c.h, p: c.p,
    vis: `<svg class="fig" viewBox="0 0 864 700" xmlns="http://www.w3.org/2000/svg">
      ${br(432, 40, 216, 230, '#FBBF24')}${br(432, 40, 648, 230, '#FBBF24')}
      ${br(216, 340, 216, 520, '#64748B')}
      <circle cx="432" cy="40" r="34" fill="#FBBF24"/>
      ${pill(46, 230, c.acts[0], '#334155', '#94A3B8')}
      ${pill(478, 230, c.acts[1], '#7A5A0B', '#FBBF24')}
      ${pill(46, 520, c.acts[2], '#7A5A0B', '#FBBF24')}
    </svg>`,
  });
}
/* 09 */
function c09(lang) {
  const c = T[lang].c9;
  return card(lang, 9, {
    right: chip(c.chip), h: c.h,
    vis: `<div class="mods">${c.mods.map((m) => `<div class="m"><span class="ck">${CHECK}</span>${m}</div>`).join('')}</div>`,
  });
}
/* 10 (sem titulo padrao) */
function c10(lang) {
  const t = T[lang], c = t.c10;
  return `<!DOCTYPE html>
<html lang="${t.lang}"><head><meta charset="UTF-8">
<link rel="stylesheet" href="carrossel.css"></head>
<body class="c10">
<div class="top"></div>
<div class="cm">
  <div class="lgb"><span class="ic">${ICON_SVG}</span><span class="wm">${WORD_SVG}</span></div>
  <h1 class="big">${c.h}</h1>
  <div class="btn">${c.btn}${ARROW}</div>
  <div class="url">${t.url}</div>
</div>
<div class="small">${c.foot}</div>
${nav(10)}
</body></html>`;
}

const BUILD = [c01, c02, c03, c04, c05, c06, c07, c08, c09, c10];
const jobs = [];
for (const lang of ['pt', 'en']) {
  const dir = path.join(SRC, lang);
  fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(path.join(dir, 'carrossel.css'), CSS);
  BUILD.forEach((fn, i) => {
    const nn = String(i + 1).padStart(2, '0');
    const name = `carrossel-${lang}-${nn}`;
    fs.writeFileSync(path.join(dir, `${name}.html`), fn(lang));
    jobs.push({ name, dir });
  });
}
console.log(`${jobs.length} HTML gerados em ${SRC}`);
if (ONLY_HTML) process.exit(0);

for (const j of jobs) {
  const png = path.join(ART, `${j.name}.png`);
  execFileSync(CHROME, ['--headless=new', '--disable-gpu', '--hide-scrollbars', '--allow-file-access-from-files',
    '--window-size=1080,1350', '--force-device-scale-factor=1', '--virtual-time-budget=3000',
    `--screenshot=${png}`, pathToFileURL(path.join(j.dir, `${j.name}.html`)).href], { stdio: 'ignore' });
  fs.copyFileSync(png, path.join(OUT2, `${j.name}.png`));
  console.log('ok', j.name);
}
