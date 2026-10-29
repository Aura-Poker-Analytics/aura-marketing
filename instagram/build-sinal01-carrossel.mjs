/* Estudo de sinal 01, 5o anuncio: carrossel "a Aura inteira" (10 cartoes x PT/EN = 20 PNG, 1080x1350).
 *
 *   node instagram/build-sinal01-carrossel.mjs          # gera HTML/CSS-fonte, renderiza com Chrome headless e copia para output
 *   node instagram/build-sinal01-carrossel.mjs --html   # so gera os HTML/CSS
 *
 * Copy: content/ads/sinal01/carrossel/copy-carrossel.md (PT) e en/copy-carrossel.md (EN). Capa = opcao 1.
 * Numeros: so os da copy (BTN vs SB 25bb, flop A-high rainbow, c-bet de 33%, field fold 41,5% x GTO 25,0% faixa 19,0-31,0, n = 9.937 maos, 6,9 mi+, 90 situacoes;
 * spot: docs/02-paid/sinal01-spots-fortes.md linha 1 e content/ads/sinal01/numeros/spots_all.csv).
 * Mockups reconstruidos com a paleta do brand-kit; onde a copy nao tem numero (preflop, reacoes, tendencia, arvore),
 * as telas mostram barras e formas, nunca numero inventado.
 * Regras duras: sem carta, ficha, dinheiro, mesa, roleta. Estilo coeso: fundo navy, ambar, painel do app,
 * indicador de progresso 1..10 no rodape de todo cartao.
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
const CHEV = `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9l6 6 6-6"/></svg>`;

const N = 10;
const T = {
  pt: {
    lang: 'pt-BR', dec: ',', foot: 'Ferramenta de estudo', url: 'www.aurapoker.com',
    c1: { a: 'O solver mostra o equilíbrio.', b: 'A Aura mostra o field.', s: 'Do preflop ao river, ao lado do GTO.' },
    field: 'Field', gto: 'GTO',
    c2: { badge: 'NOVO MÓDULO', h: 'Onde o field <span class="hl">erra</span>', p: 'BTN vs SB, 25bb, flop A-high rainbow: o SB folda 41,5% contra o c-bet de 33%. O GTO, 25,0%.',
      ctx: 'BTN vs SB · 25bb', cls: 'flop A-high rainbow', n: '9.937 mãos', lbl: 'Fold contra c-bet de 33%', over: 'OVERFOLD', band: 'Faixa do GTO', how: 'Como explorar', howTxt: 'C-bet mais vezes, inclusive sem mão.' },
    c3: { chip: 'Postflop Analysis', h: 'GTO no <span class="hl">mesmo spot</span>', p: '6,9 mi+ pontos de decisão GTO (flop, turn e river) ao lado do field.',
      mode: 'Modo GTO', plan: 'Plano Individual', ctx: 'BTN vs SB · 25bb · flop A-high rainbow', n: '9.937 mãos', cbet: 'c-bet de 33%', fold: 'Fold', rest: 'Call · Raise' },
    c4: { chip: 'Postflop Analysis', h: 'Postflop: <span class="hl">ação e reação</span>', p: 'C-bet, barrel, raise e check-raise do field, e como o adversário reage. IP e OOP.',
      acts: 'Ações do agressor', react: 'Reação do adversário', a: ['C-bet', 'Barrel', 'Raise', 'Check-raise'], r: ['Fold', 'Call', 'Raise'] },
    c5: { chip: 'Preflop Analysis', h: 'Preflop, <span class="hl">posição a posição</span>', p: 'RFI, 3-bet, squeeze e fold vs 3-bet do field, por posição, buy-in e etapa.',
      pos: 'Posição', cols: ['RFI', '3-bet', 'Squeeze', 'Fold vs<br>3-bet'], f1: 'Buy-in', f2: 'Etapa' },
    c6: { chip: 'Field Ranges', h: 'Ranges do field, <span class="hl">mão a mão</span>', p: '90 situações preflop, do open ao 4-bet, na grade.',
      ill: 'Exemplo ilustrativo', ctx: 'Open do CO', fold: 'Fold', raise: 'Raise', mix: 'Misto' },
    c7: { chip: 'Field Trends', h: 'Field Trends: <span class="hl">o que mudou</span>', p: 'Stats do field trimestre a trimestre, com a variação normal marcada. Mudou de verdade ou oscilou?',
      stat: 'Stat do field', ill: 'Exemplo ilustrativo', sub: 'Trimestre a trimestre', band: 'Variação normal', drift: 'Oscilou', real: 'Mudou de verdade' },
    c8: { chip: 'Node-by-Node', h: 'Node-by-Node: <span class="hl">a árvore</span>', p: 'Navegue a árvore da mão: de quem é a vez e a frequência de cada ação, nó a nó.',
      tex: 'Textura do flop', turn: 'Vez do', st: 'Flop', acts: ['Check', 'Donk 33%'], cbet: 'C-bet' },
    c9: { chip: 'Plano Individual', h: 'Tudo num <span class="hl">login só</span>', p: 'O plano Individual abre todos os módulos.',
      mods: ['Preflop Analysis', 'Postflop Analysis', 'Modo GTO', 'Field Exploits', 'Field Ranges', 'Field Trends', 'Node-by-Node'],
      free: 'Grátis: Preflop, Postflop, prévias de Field Ranges e Field Trends.' },
    c10: { h: 'Comece grátis.<br><span class="hl">Sem cartão.</span>', p: 'Crie sua conta e veja onde o field erra.', btn: 'Criar conta grátis' },
  },
  en: {
    lang: 'en', dec: '.', foot: 'Study tool', url: 'www.aurapoker.com',
    c1: { a: 'The solver shows equilibrium.', b: 'Aura shows the field.', s: 'Preflop to river, next to GTO.' },
    field: 'Field', gto: 'GTO',
    c2: { badge: 'NEW MODULE', h: 'Where the field <span class="hl">errs</span>', p: 'BTN vs SB, 25bb, A-high rainbow flop: the SB folds 41.5% vs a 33% c-bet. GTO folds 25.0%.',
      ctx: 'BTN vs SB · 25bb', cls: 'A-high rainbow flop', n: '9,937 hands', lbl: 'Fold vs 33% c-bet', over: 'OVERFOLD', band: 'GTO range', how: 'How to exploit', howTxt: 'C-bet more often, even with air.' },
    c3: { chip: 'Postflop Analysis', h: 'GTO in the <span class="hl">same spot</span>', p: '6.9M+ GTO decision points (flop, turn and river) next to the field.',
      mode: 'GTO Mode', plan: 'Individual plan', ctx: 'BTN vs SB · 25bb · A-high rainbow flop', n: '9,937 hands', cbet: '33% c-bet', fold: 'Fold', rest: 'Call · Raise' },
    c4: { chip: 'Postflop Analysis', h: 'Postflop: <span class="hl">action and reaction</span>', p: 'Field c-bet, barrel, raise and check-raise, and how the opponent reacts. IP and OOP.',
      acts: 'Aggressor actions', react: 'Opponent reaction', a: ['C-bet', 'Barrel', 'Raise', 'Check-raise'], r: ['Fold', 'Call', 'Raise'] },
    c5: { chip: 'Preflop Analysis', h: 'Preflop, <span class="hl">position by position</span>', p: 'Field RFI, 3-bet, squeeze and fold vs 3-bet, by position, buy-in and stage.',
      pos: 'Position', cols: ['RFI', '3-bet', 'Squeeze', 'Fold vs<br>3-bet'], f1: 'Buy-in', f2: 'Stage' },
    c6: { chip: 'Field Ranges', h: 'Field ranges, <span class="hl">hand by hand</span>', p: '90 preflop situations, from open to 4-bet, on the grid.',
      ill: 'Illustrative example', ctx: 'CO open', fold: 'Fold', raise: 'Raise', mix: 'Mixed' },
    c7: { chip: 'Field Trends', h: 'Field Trends: <span class="hl">what changed</span>', p: 'Field stats quarter by quarter, with the normal variation marked. Real change or drift?',
      stat: 'Field stat', ill: 'Illustrative example', sub: 'Quarter by quarter', band: 'Normal variation', drift: 'Drift', real: 'Real change' },
    c8: { chip: 'Node-by-Node', h: 'Node-by-Node: <span class="hl">the tree</span>', p: 'Walk the hand tree: whose turn it is and the frequency of each action, node by node.',
      tex: 'Flop texture', turn: '', after: ' to act', st: 'Flop', acts: ['Check', 'Donk 33%'], cbet: 'C-bet' },
    c9: { chip: 'Individual plan', h: 'Every module, <span class="hl">one login</span>', p: 'The Individual plan opens all of them.',
      mods: ['Preflop Analysis', 'Postflop Analysis', 'GTO Mode', 'Field Exploits', 'Field Ranges', 'Field Trends', 'Node-by-Node'],
      free: 'Free: Preflop, Postflop, previews of Field Ranges and Field Trends.' },
    c10: { h: 'Start free.<br><span class="hl">No card.</span>', p: 'Create your account and see where the field errs.', btn: 'Create free account' },
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
.chip{font-size:24px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:#FBBF24;border:2px solid rgba(251,191,36,.6);border-radius:12px;padding:10px 20px;background:rgba(251,191,36,.07)}
.badge{font-size:26px;font-weight:900;letter-spacing:.14em;color:#0F1526;background:linear-gradient(180deg,#FCD34D,#F59E0B);border-radius:12px;padding:12px 22px}
h1.hd{font-size:70px;font-weight:900;text-transform:uppercase;line-height:1.05;letter-spacing:.005em;margin-top:30px;flex:none}
.hl{color:#FBBF24}
p.ln{font-size:36px;font-weight:500;line-height:1.3;color:#E2E8F0;margin-top:16px;flex:none}
.panel{margin-top:30px;flex:1;min-height:0;background:#0F172A;border:2px solid rgba(251,191,36,.38);border-radius:36px;padding:32px 36px;display:flex;flex-direction:column;box-shadow:0 30px 80px rgba(0,0,0,.45);overflow:hidden}
.ph{display:flex;align-items:center;justify-content:space-between;margin-bottom:22px;flex:none}
.mod{display:flex;align-items:center;gap:14px;font-size:26px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:#FBBF24}
.mod i{width:40px;height:30px;display:block}.mod i svg{width:100%;height:100%}
.tag{font-size:23px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:#FBBF24;border:2px solid rgba(251,191,36,.6);border-radius:10px;padding:6px 14px;background:rgba(251,191,36,.08)}
.nav{display:flex;align-items:center;justify-content:space-between;height:36px;flex:none;margin-top:26px}
.segs{display:flex;gap:8px}
.segs .s{display:block;width:56px;height:8px;border-radius:4px;background:#1E293B}
.segs .s.past{background:#475569}.segs .s.on{background:#FBBF24}
.cnt{display:flex;align-items:center;gap:12px;font-size:26px;font-weight:800;color:#CBD5E1;letter-spacing:.04em}
.cnt b{color:#FBBF24;font-weight:800}.cnt svg{width:30px;height:30px;color:#FBBF24}
.foot{display:flex;align-items:center;justify-content:space-between;flex:none;margin-top:22px;font-size:26px;font-weight:600;letter-spacing:.02em;color:#94A3B8}
.age{font-weight:800;font-size:26px;border:3px solid currentColor;border-radius:11px;padding:4px 12px}
.ctx{font-size:30px;font-weight:700;color:#CBD5E1}
.ctx2{font-size:30px;font-weight:700;color:#FBBF24;margin-top:4px}
.rt{display:flex;align-items:center;gap:12px}
.ill{font-size:22px;font-weight:700;color:#E2E8F0;border:2px dashed #94A3B8;border-radius:10px;padding:5px 14px;background:rgba(148,163,184,.10)}
.cw{position:relative}
.ill.ab{position:absolute;left:0;top:0;z-index:1}

/* regua field x GTO (cobertura e cartao 2) */
.track{position:relative;height:58px;border-radius:29px;background:#1E293B}
.track .fill{position:absolute;left:0;top:0;bottom:0;width:41.5%;border-radius:29px 0 0 29px;background:linear-gradient(90deg,#0C7F99,#34C9E6)}
.track .gap{position:absolute;top:8px;bottom:8px;left:31%;width:10.5%;background:repeating-linear-gradient(135deg,rgba(251,191,36,.95) 0 8px,rgba(251,191,36,.25) 8px 16px)}
.track .band{position:absolute;top:-9px;bottom:-9px;left:19%;width:12%;border:3px solid #5FDB9C;border-radius:10px;background:rgba(95,219,156,.22)}
.track .tick{position:absolute;top:-16px;bottom:-16px;left:25%;width:7px;margin-left:-3px;border-radius:4px;background:#5FDB9C}
.legend{display:flex;gap:30px;margin-top:28px;font-size:27px;font-weight:700;color:#CBD5E1}
.legend span{display:flex;align-items:center;gap:12px}
.legend i{display:block;width:26px;height:26px;border-radius:7px}
.lg-f{background:#34C9E6}.lg-g{background:#5FDB9C}.lg-x{background:#FBBF24}.lg-r{background:#AD2C34}.lg-fo{background:#0B6B80}.lg-m{background:linear-gradient(90deg,#AD2C34 0 55%,#0B6B80 55% 100%)}

/* 01 capa */
.c01 .cvmain{flex:1;display:flex;flex-direction:column;justify-content:center;gap:0}
.c01 .t1{font-size:74px;font-weight:900;text-transform:uppercase;line-height:1.06;color:#94A3B8;letter-spacing:.005em}
.c01 .t2{font-size:112px;font-weight:900;text-transform:uppercase;line-height:1.02;color:#FBBF24;margin-top:22px;letter-spacing:-.01em}
.c01 .sub{font-size:42px;font-weight:600;color:#E2E8F0;margin-top:34px;line-height:1.25}
.c01 .rl{margin-top:70px}
.c01 .rl .track{height:64px;border-radius:32px}
.c01 .rl .track .fill{border-radius:32px 0 0 32px}
.c01 .rls{position:relative;height:40px;margin-top:26px;font-size:30px;font-weight:800;letter-spacing:.14em;text-transform:uppercase}
.c01 .rls span{position:absolute;top:0;transform:translateX(-50%);white-space:nowrap}
.c01 .rls .a{left:41.5%;color:#34C9E6}.c01 .rls .b{left:25%;color:#5FDB9C}

/* 02 field exploits */
.c02 .panel{justify-content:space-between}
.c02 .ttl{display:flex;align-items:baseline;gap:22px;flex-wrap:wrap}
.c02 .ttl b{font-size:62px;font-weight:800}.c02 .ttl span{font-size:34px;font-weight:600;color:#CBD5E1}
.nn{font-size:.85em;font-weight:600;color:#94A3B8}
.c02 .cls{font-size:32px;font-weight:700;color:#FBBF24;margin-top:8px}
.c02 .lbl{font-size:32px;font-weight:600;color:#CBD5E1;margin-top:6px}
.c02 .nums{display:flex;justify-content:space-between;align-items:flex-end;margin-top:14px}
.c02 .nums div{display:flex;flex-direction:column}
.c02 .nums .k{font-size:28px;font-weight:700;letter-spacing:.14em;text-transform:uppercase}
.c02 .nums .v{font-size:112px;font-weight:800;line-height:1;letter-spacing:-.02em}
.c02 .nums .f .k,.c02 .nums .f .v{color:#34C9E6}
.c02 .nums .g{align-items:flex-end}.c02 .nums .g .k,.c02 .nums .g .v{color:#5FDB9C}
.c02 .rulerbox{margin-top:30px}
.c02 .how{margin-top:34px;border-top:2px solid rgba(148,163,184,.25);padding-top:22px}
.c02 .how .k{font-size:26px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:#FBBF24}
.c02 .how .t{font-size:46px;font-weight:700;margin-top:8px;line-height:1.15;text-wrap:balance}
.over{display:inline-flex;font-size:24px;font-weight:800;letter-spacing:.1em;color:#FCA5A5;border:2px solid rgba(252,165,165,.5);background:rgba(173,44,52,.28);border-radius:10px;padding:6px 14px}

/* 03 modo gto */
.sw{display:flex;align-items:center;gap:14px;font-size:28px;font-weight:800;color:#5FDB9C;letter-spacing:.06em;text-transform:uppercase}
.sw i{display:block;position:relative;width:76px;height:42px;border-radius:21px;background:#348A5D}
.sw i::after{content:"";position:absolute;right:5px;top:5px;width:32px;height:32px;border-radius:50%;background:#fff}
.tabs{display:flex;gap:12px;margin-bottom:26px}
.tabs span{font-size:27px;font-weight:700;color:#94A3B8;border:2px solid #334155;border-radius:14px;padding:10px 24px}
.tabs span.on{color:#0F1526;background:#FBBF24;border-color:#FBBF24;font-weight:800}
.c03 .stack{position:relative;height:190px;border-radius:24px;background:#1E293B;margin-top:100px;border:2px solid #334155}
.c03 .stack .fo{position:absolute;left:0;top:0;bottom:0;width:41.5%;border-radius:22px 0 0 22px;background:#0B6B80;display:flex;align-items:center;padding-left:26px;font-size:34px;font-weight:800}
.c03 .stack .re{position:absolute;left:41.5%;right:0;top:0;bottom:0;display:flex;align-items:center;justify-content:center;font-size:30px;font-weight:700;color:#CBD5E1;background:repeating-linear-gradient(135deg,rgba(148,163,184,.14) 0 10px,transparent 10px 20px)}
.c03 .rl2{position:absolute;right:0;top:216px;font-size:30px;font-weight:700;color:#CBD5E1}
.c03 .mk{position:absolute;left:25%;top:-34px;bottom:-34px;width:9px;margin-left:-4px;border-radius:5px;background:#5FDB9C}
.c03 .mkl{position:absolute;left:25%;top:-96px;transform:translateX(-50%);font-size:30px;font-weight:800;color:#5FDB9C;white-space:nowrap}
.c03 .fl{position:absolute;left:0;top:216px;font-size:30px;font-weight:800;color:#34C9E6}
.c03 .nums{display:flex;gap:56px;margin-top:130px;border-top:2px solid rgba(148,163,184,.25);padding-top:30px}
.c03 .nums div{display:flex;flex-direction:column}
.c03 .nums .k{font-size:27px;font-weight:700;letter-spacing:.14em;text-transform:uppercase}
.c03 .nums .v{font-size:104px;font-weight:800;line-height:1.05;letter-spacing:-.02em}
.c03 .nums .f .k,.c03 .nums .f .v{color:#34C9E6}.c03 .nums .g .k,.c03 .nums .g .v{color:#5FDB9C}

/* 04 acao e reacao */
.seg2{display:flex;border:2px solid #334155;border-radius:14px;overflow:hidden}
.seg2 span{font-size:27px;font-weight:800;padding:8px 26px;color:#94A3B8}.seg2 span.on{background:#FBBF24;color:#0F1526}
.h3{font-size:26px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:#94A3B8;margin-bottom:16px}
.acts{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.acts span{font-size:38px;font-weight:800;border:2px solid #334155;border-radius:18px;padding:32px 30px;background:#1E293B}
.acts span.on{border-color:#FBBF24;color:#FBBF24;background:rgba(251,191,36,.1)}
.c04 .react{margin-top:40px;border-top:2px solid rgba(148,163,184,.25);padding-top:36px}
.rrow{display:flex;align-items:center;gap:22px;margin-top:28px}
.rrow .n{width:140px;font-size:38px;font-weight:800}
.rrow .tr{flex:1;height:60px;border-radius:30px;background:#1E293B;position:relative;overflow:hidden}
.rrow .tr i{position:absolute;left:0;top:0;bottom:0;border-radius:30px}
.rrow.fo .n{color:#4FC3DA}.rrow.fo i{width:46%;background:#0B6B80;border:3px solid #4FC3DA}
.rrow.ca .n{color:#5FDB9C}.rrow.ca i{width:34%;background:#348A5D;border:3px solid #5FDB9C}
.rrow.ra .n{color:#F18A91}.rrow.ra i{width:18%;background:#AD2C34;border:3px solid #F18A91}

/* 05 tabela preflop */
.filters{display:flex;gap:14px}
.fchip{display:flex;align-items:center;gap:10px;font-size:26px;font-weight:700;color:#E2E8F0;border:2px solid #475569;border-radius:14px;padding:8px 16px;background:#1E293B}
.fchip svg{width:24px;height:24px;color:#FBBF24}
.tbl{display:grid;grid-template-columns:178px repeat(4,1fr);column-gap:12px;row-gap:14px;align-items:center}
.tbl .th{font-size:25px;font-weight:800;color:#FBBF24;letter-spacing:.04em;line-height:1.15;padding-bottom:6px}
.tbl .pos{font-size:34px;font-weight:800}
.tbl .cl{height:84px;border-radius:14px;background:#1E293B;position:relative;overflow:hidden}
.tbl .cl i{position:absolute;left:14px;top:27px;height:30px;border-radius:15px;background:linear-gradient(90deg,#0C7F99,#34C9E6)}
.tbl .cl.x{background:transparent;border:2px dashed #334155}
.tbl .cl.x::after{content:"";position:absolute;left:50%;top:50%;width:24px;height:4px;margin:-2px 0 0 -12px;background:#475569;border-radius:2px}
.v1 i{width:30%}.v2 i{width:48%}.v3 i{width:62%}.v4 i{width:76%}.v5 i{width:38%}

/* 06 grade */
.c06 .gw{display:flex;gap:28px;align-items:flex-start}
.c06 .gw .legend{flex-direction:column;gap:20px;margin-top:44px}
.gridw{display:grid;width:650px;flex:none;grid-template-columns:34px repeat(13,1fr);gap:4px;align-items:center}
.gridw .ax{font-size:23px;font-weight:800;color:#94A3B8;text-align:center}
.gridw i{display:block;aspect-ratio:1/1;border-radius:6px}
.gridw i.r{background:#AD2C34}.gridw i.f{background:#16384A}.gridw i.m{background:linear-gradient(90deg,#AD2C34 0 55%,#16384A 55% 100%)}
.gridw i.pr{box-shadow:inset 0 0 0 3px rgba(255,255,255,.55)}

/* 07 tendencia */
.c07 svg.ch{width:100%;height:auto}
.c07 .ch text{font-family:"Montserrat","Segoe UI",sans-serif;font-weight:800}

/* 08 arvore */
.c08 svg.tr{width:100%;height:auto}
.c08 .tr text{font-family:"Montserrat","Segoe UI",sans-serif;font-weight:800}

/* 09 lista */
.mods{display:flex;flex-direction:column;gap:12px}
.mods .m{display:flex;align-items:center;gap:22px;background:#1E293B;border-radius:18px;padding:0 26px;height:80px;font-size:38px;font-weight:700}
.mods .m .ck{width:42px;height:42px;border-radius:50%;background:#348A5D;color:#fff;display:flex;align-items:center;justify-content:center;flex:none}
.mods .m .ck svg{width:26px;height:26px}
.mods .m.nw{border:2px solid rgba(251,191,36,.7)}
.mods .m .nb{margin-left:auto;font-size:21px;font-weight:900;letter-spacing:.12em;color:#0F1526;background:#FBBF24;border-radius:8px;padding:5px 12px}
.freebox{margin-top:22px;border-left:10px solid #5FDB9C;background:rgba(95,219,156,.1);border-radius:0 18px 18px 0;padding:18px 26px;font-size:28px;font-weight:600;line-height:1.3;color:#E2E8F0}

/* 10 cta */
.c10 .cm{flex:1;display:flex;flex-direction:column;justify-content:center}
.c10 .lgb{display:flex;align-items:center;gap:26px;color:#D4A418}
.c10 .lgb .ic{width:118px;height:88px}.c10 .lgb .wm{width:300px}.c10 .lgb svg{width:100%;height:100%}
.c10 h1.big{font-size:104px;font-weight:900;text-transform:uppercase;line-height:1.03;margin-top:60px;letter-spacing:-.005em}
.c10 p.ln{font-size:44px;margin-top:30px}
.c10 .btn{margin-top:60px;display:flex;align-items:center;justify-content:center;gap:18px;height:128px;border-radius:30px;background:linear-gradient(180deg,#FCD34D,#F59E0B);color:#0F1526;font-size:50px;font-weight:900;box-shadow:0 24px 60px rgba(245,158,11,.28)}
.c10 .btn svg{width:48px;height:48px}
.c10 .url{margin-top:34px;text-align:center;font-size:42px;font-weight:800;color:#FBBF24;letter-spacing:.02em}
`;

/* ---------- pecas ---------- */
const brand = `<div class="brand"><span class="ic">${ICON_SVG}</span><span class="wm">${WORD_SVG}</span></div>`;
const nav = (n) => `<div class="nav"><div class="segs">${Array.from({ length: N }, (_, i) => `<i class="s${i + 1 < n ? ' past' : i + 1 === n ? ' on' : ''}"></i>`).join('')}</div>
  <div class="cnt"><span><b>${String(n).padStart(2, '0')}</b> / ${N}</span>${n < N ? ARROW : ''}</div></div>`;
const footer = (t) => `<div class="foot"><span>${t.foot} · 18+</span><span class="age">18+</span></div>`;
const modHd = (name, right = '') => `<div class="ph"><span class="mod"><i>${ICON_SVG}</i>${name}</span>${right}</div>`;
const num = (lang, s) => s.replace('.', T[lang].dec);

function card(lang, n, { chip, h, p, panel, extra = '' }) {
  const t = T[lang];
  const topRight = chip ? (chip.badge ? `<span class="badge">${chip.text}</span>` : `<span class="chip">${chip.text}</span>`) : '';
  return `<!DOCTYPE html>
<html lang="${t.lang}"><head><meta charset="UTF-8">
<link rel="stylesheet" href="carrossel.css"></head>
<body class="c${String(n).padStart(2, '0')}">
<div class="top">${brand}${topRight}</div>
<h1 class="hd">${h}</h1>
<p class="ln">${p}</p>
<div class="panel">${panel}</div>
${extra}${nav(n)}
</body></html>`;
}

const ruler = `<div class="track"><div class="fill"></div><div class="gap"></div><div class="band"></div><div class="tick"></div></div>`;

/* 02 */
function c02(lang) {
  const t = T[lang], c = t.c2;
  return card(lang, 2, {
    chip: { badge: true, text: c.badge }, h: c.h, p: c.p,
    panel: `${modHd('Field Exploits', `<span class="over">${c.over}</span>`)}
    <div class="ttl"><b>BTN vs SB</b><span>25bb</span></div>
    <div class="cls">${c.cls}<span class="nn"> · ${c.n}</span></div>
    <div class="lbl">${c.lbl}</div>
    <div class="nums"><div class="f"><span class="k">${t.field}</span><span class="v">${num(lang, '41.5')}%</span></div>
      <div class="g"><span class="k">${t.gto}</span><span class="v">${num(lang, '25.0')}%</span></div></div>
    <div class="rulerbox">${ruler}</div>
    <div class="legend"><span><i class="lg-f"></i>${t.field}</span><span><i class="lg-g"></i>${c.band}</span></div>
    <div class="how"><div class="k">${c.how}</div><div class="t">${c.howTxt}</div></div>`,
  });
}
/* 03 */
function c03(lang) {
  const t = T[lang], c = t.c3;
  return card(lang, 3, {
    chip: { text: c.chip }, h: c.h, p: c.p,
    panel: `<div class="ph"><span class="sw"><i></i>${c.mode}</span><span class="tag">${c.plan}</span></div>
    <div class="tabs"><span class="on">Flop</span><span>Turn</span><span>River</span></div>
    <div class="ctx">${c.ctx}</div><div class="ctx2">${c.cbet}<span class="nn"> · ${c.n}</span></div>
    <div class="stack"><div class="fo">${c.fold}</div><div class="re"></div><div class="mk"></div><div class="mkl">${t.gto} ${num(lang, '25.0')}%</div><div class="fl">${c.fold} · ${t.field} ${num(lang, '41.5')}%</div><div class="rl2">${c.rest}</div></div>
    <div class="nums"><div class="f"><span class="k">${t.field}</span><span class="v">${num(lang, '41.5')}%</span></div>
      <div class="g"><span class="k">${t.gto}</span><span class="v">${num(lang, '25.0')}%</span></div></div>`,
  });
}
/* 04 */
function c04(lang) {
  const t = T[lang], c = t.c4;
  return card(lang, 4, {
    chip: { text: c.chip }, h: c.h, p: c.p,
    panel: `<div class="ph"><div class="seg2"><span class="on">IP</span><span>OOP</span></div><span class="tag">Flop</span></div>
    <div class="h3">${c.acts}</div>
    <div class="acts">${c.a.map((a, i) => `<span${i === 0 ? ' class="on"' : ''}>${a}</span>`).join('')}</div>
    <div class="react"><div class="h3">${c.react}</div>
      <div class="rrow fo"><span class="n">${c.r[0]}</span><div class="tr"><i></i></div></div>
      <div class="rrow ca"><span class="n">${c.r[1]}</span><div class="tr"><i></i></div></div>
      <div class="rrow ra"><span class="n">${c.r[2]}</span><div class="tr"><i></i></div></div></div>`,
  });
}
/* 05 */
function c05(lang) {
  const t = T[lang], c = t.c5;
  const rows = ['UTG', 'HJ', 'CO', 'BTN', 'SB', 'BB'];
  const cells = rows.map((r, ri) => `<div class="pos">${r}</div>` + [0, 1, 2, 3].map((ci) => {
    const none = (r === 'UTG' && ci === 2) || (r === 'BB' && ci === 0) || (r === 'UTG' && ci === 1 && false);
    return none ? `<div class="cl x"></div>` : `<div class="cl v${((ri * 3 + ci * 2) % 5) + 1}"><i></i></div>`;
  }).join('')).join('');
  return card(lang, 5, {
    chip: { text: c.chip }, h: c.h, p: c.p,
    panel: `<div class="ph"><span class="mod"><i>${ICON_SVG}</i>Preflop</span><div class="filters"><span class="fchip">${c.f1}${CHEV}</span><span class="fchip">${c.f2}${CHEV}</span></div></div>
    <div class="tbl"><div class="th">${c.pos}</div>${c.cols.map((x) => `<div class="th">${x}</div>`).join('')}${cells}</div>`,
  });
}
/* 06 */
function c06(lang) {
  const t = T[lang], c = t.c6;
  const L = 'AKQJT98765432';
  const kind = (i, j) => {
    if (i === j) return 'r pr';
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
  let cells = '<span></span>' + [...L].map((x) => `<span class="ax">${x}</span>`).join('');
  for (let i = 0; i < 13; i++) {
    cells += `<span class="ax">${L[i]}</span>`;
    for (let j = 0; j < 13; j++) cells += `<i class="${kind(i, j)}"></i>`;
  }
  return card(lang, 6, {
    chip: { text: c.chip }, h: c.h, p: c.p,
    panel: `${modHd(c.ctx, `<span class="rt"><span class="ill">${c.ill}</span><span class="tag">13x13</span></span>`)}
    <div class="gw"><div class="gridw">${cells}</div>
    <div class="legend"><span><i class="lg-r"></i>${c.raise}</span><span><i class="lg-m"></i>${c.mix}</span><span><i class="lg-fo"></i>${c.fold}</span></div></div>`,
  });
}
/* 07 */
function c07(lang) {
  const t = T[lang], c = t.c7;
  const xs = [70, 175, 280, 385, 490, 595, 700, 805];
  const ys = [390, 362, 412, 372, 402, 352, 240, 196];
  const pts = xs.map((x, i) => `${x},${ys[i]}`).join(' ');
  const dots = xs.map((x, i) => {
    const out = i >= 6;
    return `<circle cx="${x}" cy="${ys[i]}" r="${out ? 16 : 13}" fill="${out ? '#FBBF24' : '#0F172A'}" stroke="${out ? '#FBBF24' : '#34C9E6'}" stroke-width="5"/>`;
  }).join('');
  return card(lang, 7, {
    chip: { text: c.chip }, h: c.h, p: c.p,
    panel: `<div class="ph"><span class="mod"><i>${ICON_SVG}</i>${c.stat}</span><span class="tag">${c.sub}</span></div>
    <div class="cw"><span class="ill ab">${c.ill}</span>
    <svg class="ch" viewBox="0 0 864 640" xmlns="http://www.w3.org/2000/svg">
      <rect x="20" y="318" width="824" height="130" rx="20" fill="#FBBF24" fill-opacity="0.13" stroke="#FBBF24" stroke-opacity="0.65" stroke-width="3" stroke-dasharray="14 10"/>
      <text x="40" y="504" font-size="30" fill="#FBBF24">${c.band}</text>
      <line x1="20" y1="590" x2="844" y2="590" stroke="#475569" stroke-width="3"/>
      ${xs.map((x) => `<line x1="${x}" y1="582" x2="${x}" y2="598" stroke="#64748B" stroke-width="3"/>`).join('')}
      <polyline points="${pts}" fill="none" stroke="#34C9E6" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>
      ${dots}
      <text x="280" y="296" font-size="32" fill="#34C9E6" text-anchor="middle">${c.drift}</text>
      <text x="844" y="96" font-size="34" fill="#FBBF24" text-anchor="end">${c.real}</text>
      <path d="M805 124 L805 166" stroke="#FBBF24" stroke-width="5" stroke-linecap="round"/>
    </svg></div>`,
  });
}
/* 08 */
function c08(lang) {
  const t = T[lang], c = t.c8;
  const pill = (x, y, w, label, fill, stroke, bar) => `<rect x="${x}" y="${y}" width="${w}" height="68" rx="16" fill="${fill}" stroke="${stroke}" stroke-width="3"/>
      <text x="${x + w / 2}" y="${y + 45}" font-size="30" fill="#fff" text-anchor="middle">${label}</text>
      <rect x="${x}" y="${y + 86}" width="${w}" height="14" rx="7" fill="#1E293B"/><rect x="${x}" y="${y + 86}" width="${bar}" height="14" rx="7" fill="${stroke}"/>`;
  const node = (x, y, who) => `<rect x="${x}" y="${y}" width="270" height="104" rx="24" fill="#1E293B" stroke="#FBBF24" stroke-width="3.5"/>
      <text x="${x + 135}" y="${y + 48}" font-size="33" fill="#fff" text-anchor="middle">${c.turn} ${who}${c.after || ''}</text>
      <text x="${x + 135}" y="${y + 84}" font-size="26" fill="#94A3B8" text-anchor="middle">${c.st}</text>`;
  const br = (x1, y1, x2, y2, col) => `<path d="M${x1} ${y1} C${x1} ${(y1 + y2) / 2} ${x2} ${(y1 + y2) / 2} ${x2} ${y2}" fill="none" stroke="${col}" stroke-width="5" stroke-linecap="round"/>`;
  const A = '#FBBF24', G = '#64748B';
  return card(lang, 8, {
    chip: { text: c.chip }, h: c.h, p: c.p,
    panel: `<div class="ph"><span class="mod"><i>${ICON_SVG}</i>Node-by-Node</span><span class="fchip">${c.tex}${CHEV}</span></div>
    <svg class="tr" viewBox="0 0 864 660" xmlns="http://www.w3.org/2000/svg">
      ${node(297, 6, 'BB')}
      ${br(380, 110, 215, 270, A)}${br(484, 110, 649, 270, A)}
      <text x="214" y="196" font-size="30" fill="${A}" text-anchor="end">${c.acts[0]}</text>
      <text x="650" y="196" font-size="30" fill="${A}">${c.acts[1]}</text>
      ${node(80, 270, 'BTN')}
      ${node(514, 270, 'BTN')}
      ${br(215, 374, 110, 480, G)}${br(215, 374, 318, 480, G)}
      ${br(649, 374, 510, 480, G)}${br(649, 374, 648, 480, G)}${br(649, 374, 786, 480, G)}
      ${pill(20, 480, 180, c.acts[0], '#334155', '#94A3B8', 112)}
      ${pill(228, 480, 180, c.cbet, '#7A5A0B', '#FBBF24', 70)}
      ${pill(448, 480, 124, 'Fold', '#0B6B80', '#4FC3DA', 62)}
      ${pill(586, 480, 124, 'Call', '#348A5D', '#5FDB9C', 84)}
      ${pill(724, 480, 124, 'Raise', '#AD2C34', '#F18A91', 38)}
    </svg>`,
  });
}
/* 09 */
function c09(lang) {
  const t = T[lang], c = t.c9;
  return card(lang, 9, {
    chip: { text: c.chip }, h: c.h, p: c.p,
    panel: `<div class="mods">${c.mods.map((m, i) => `<div class="m${i === 3 ? ' nw' : ''}"><span class="ck">${CHECK}</span>${m}${i === 3 ? `<span class="nb">${t.c2.badge}</span>` : ''}</div>`).join('')}</div>
    <div class="freebox">${c.free}</div>`,
  });
}
/* 01 e 10 (sem painel padrao) */
function c01(lang) {
  const t = T[lang], c = t.c1;
  return `<!DOCTYPE html>
<html lang="${t.lang}"><head><meta charset="UTF-8">
<link rel="stylesheet" href="carrossel.css"></head>
<body class="c01">
<div class="top">${brand}</div>
<div class="cvmain">
  <div class="t1">${c.a}</div>
  <div class="t2">${c.b}</div>
  <div class="sub">${c.s}</div>
  <div class="rl">${ruler}<div class="rls"><span class="b">${t.gto}</span><span class="a">${t.field}</span></div></div>
</div>
${footer(t)}
${nav(1)}
</body></html>`;
}
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
  <p class="ln">${c.p}</p>
  <div class="btn">${c.btn}${ARROW}</div>
  <div class="url">${t.url}</div>
</div>
${footer(t)}
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
