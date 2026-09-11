/* BOARD01 — carrossel 4:5 (EN). Slug/utm_content: board01-1560-carrossel-en.
 *
 *   node instagram/build-board1560-carrossel.mjs
 *
 * Versao estatica da mesma promessa do reel board01-1560-boards-en. Existe
 * porque os paineis sao DENSOS: no reel a cena de Size distribution dura 4,4s
 * e ninguem le seis barras com numero em 4,4s. No carrossel cada painel fica
 * parado o tempo que o leitor quiser.
 *
 * 5 cards = os 4 paineis distintos ja renderizados + CTA. Sem repetir painel.
 * Reaproveita os mockups do build-board1560.mjs — rode aquele antes se os
 * shots ainda nao existirem.
 *
 * ⚠️ NAO usa carrossel-capa: o mock de UI dela tem um Exploit Card com
 * "−14 pts · Confianca alta · 480k maos" hardcoded, que e dado fabricado.
 * O card 1 e um carrossel-slide fazendo as vezes de capa.
 *
 * GOTCHA: URL LIMPA sempre (cleanUrls do `serve` derruba a query string).
 */
import { execFileSync, spawn } from 'child_process';
import path from 'path';
import fs from 'fs';
import { fileURLToPath } from 'url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const TPL = path.join(ROOT, 'instagram/templates');
const CHROME = process.env.CHROME_PATH || 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 5306;
const W = 1080, H = 1350;   // 4:5, o formato da biblioteca de content/posts

const NAME = 'board01-1560-carrossel-en';   // = utm_content, nao renomear
// card -> template. O 5 e o CTA; os outros sao slides internos.
const CARDS = [
  ['cb-1-en', 'carrossel-slide'],
  ['cb-2-en', 'carrossel-slide'],
  ['cb-3-en', 'carrossel-slide'],
  ['cb-4-en', 'carrossel-slide'],
  ['cb-5-en', 'carrossel-cta'],
];

const OUT_DIR = path.join(ROOT, 'content/posts/board01-1560-carrossel');
fs.mkdirSync(OUT_DIR, { recursive: true });

const need = ['mockup-board-s1-en', 'mockup-board-s5-en']
  .map(f => path.join(TPL, 'shots', f + '.png')).filter(f => !fs.existsSync(f));
if (need.length) {
  console.error('faltam mockups — rode `node instagram/build-board1560.mjs --en` antes:');
  need.forEach(f => console.error('  ' + path.basename(f)));
  process.exit(1);
}

const srv = spawn('npx.cmd', ['serve', '-l', String(PORT), TPL], { stdio: 'ignore', shell: true });
await new Promise(r => setTimeout(r, 6000));

/* variantes COMPACTAS do painel de resultado (sem rail de contexto e sem
   'Total'): no card 4:5 o painel inteiro nao cabe junto com o titulo, e
   encolher a imagem pra caber devolveria o texto ilegivel. */
for (const part of ['sizes', 'expl']) {
  const url = `http://localhost:${PORT}/mockup-board-results?reel=1&compact=1&part=${part}`;
  const dom = execFileSync(CHROME, ['--headless=new', '--disable-gpu', '--window-size=1500,2400',
    '--virtual-time-budget=4000', '--dump-dom', url], { encoding: 'utf8', maxBuffer: 64e6 });
  const m = dom.match(/fit:(\d+)x(\d+)/);
  if (!m) throw new Error('nao consegui medir: ' + url);
  execFileSync(CHROME, ['--headless=new', '--disable-gpu', '--hide-scrollbars',
    `--window-size=${m[1]},${m[2]}`, '--force-device-scale-factor=2', '--virtual-time-budget=4500',
    `--screenshot=${path.join(TPL, 'shots', 'mockup-results-' + part + '-c.png')}`, url], { stdio: 'ignore' });
}

CARDS.forEach(([id, tpl], i) => {
  const out = path.join(OUT_DIR, `${NAME}-${String(i + 1).padStart(2, '0')}.png`);
  execFileSync(CHROME, ['--headless=new', '--disable-gpu', '--hide-scrollbars',
    `--window-size=${W},${H}`, '--force-device-scale-factor=1', '--virtual-time-budget=4500',
    `--screenshot=${out}`, `http://localhost:${PORT}/${tpl}?p=${id}`], { stdio: 'ignore' });
});

srv.kill();
try { execFileSync('taskkill', ['/F', '/T', '/PID', String(srv.pid)], { stdio: 'ignore' }); } catch {}

const files = fs.readdirSync(OUT_DIR).filter(f => f.endsWith('.png')).sort();
console.log(`${files.length} cards ${W}x${H} em content/posts/board01-1560-carrossel/`);
files.forEach(f => console.log('  ' + f + '  ' + (fs.statSync(path.join(OUT_DIR, f)).size / 1024).toFixed(0) + ' KB'));
