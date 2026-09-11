/* BOARD01 v2 — "1,560 boards". Slug/utm_content: board01-1560-boards(-en).
 *
 *   node instagram/build-board1560.mjs --en            # EN: mockups + cenas + MP4 + capa
 *   node instagram/build-board1560.mjs --en --guides   # so renderiza, com zonas seguras
 *   node instagram/build-board1560.mjs --en --nomock   # reaproveita mockups (itera so a copy)
 *
 * Substitui board01-amostra-antes, recusado pelo PO: aquele vendia MECANISMO
 * (classes colapsando), este vende a PROMESSA — escolha o board, receba a
 * analise dele. Arco: acervo -> voce define -> voce recebe.
 *
 * 1.560 = 73 flop + 615 turn + 872 river, contados no extrato da referencia.
 *
 * ⚠️ A cena do resultado NAO afirma "nesse board": os numeros do painel sao
 * reais mas vem do print CO/BB SEM filtro de board. Ver comentario do bloco
 * bd- no deck.js.
 *
 * ⚠️ ZERO CONTAGEM ABSOLUTA DE MAOS vinda do eixo de textura (o "105 milhoes"
 * dos docs e linha IP+OOP no banco local). Os "10.6M hands" do painel de
 * resultado sao output real do produto, transcritos do print.
 *
 * O painel de resultado sai em DUAS cenas (?part=sizes / ?part=expl): inteiro
 * ele tem 1512px e nao cabe na zona segura sem encolher o texto ate borrar.
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
const EN = process.argv.includes('--en');
const GUIDES = process.argv.includes('--guides');
const NO_MOCK = process.argv.includes('--nomock');
const PORT = EN ? 5304 : 5303;
const W = 1080, H = 1920, FPS = 30;

const NAME = 'board01-1560-boards' + (EN ? '-en' : '');   // = utm_content, nao renomear
const SCENES = ['bd-s1', 'bd-s2', 'bd-s3', 'bd-s4', 'bd-s5', 'bd-cta'].map(id => EN ? id + '-en' : id);
// gancho 3,4 · acervo 4,0 · define 4,4 · sizes 4,4 · defesa 4,4 · CTA 3,6 = 24,2s
const DURS = [3.4, 4.0, 4.4, 4.4, 4.4, 3.6];
const PANEL = 3;   // primeira cena do resultado — push-in lento

const OUT_DIR = path.join(ROOT, 'content/paid/AURA-BOARD01');
const SHOTS = path.join(TPL, 'shots');
const FRAMES = path.join(ROOT, 'instagram/output/board1560-frames' + (EN ? '-en' : ''));
const TMP = path.join(ROOT, 'instagram/output/_segs-board1560' + (EN ? '-en' : ''));
[OUT_DIR, SHOTS, FRAMES, TMP].forEach(d => fs.mkdirSync(d, { recursive: true }));

const srv = spawn('npx.cmd', ['serve', '-l', String(PORT), TPL], { stdio: 'ignore', shell: true });
await new Promise(r => setTimeout(r, 6000));

const shot = (out, url, w, h, dpr = 1) => execFileSync(CHROME, ['--headless=new', '--disable-gpu',
  '--hide-scrollbars', `--window-size=${w},${h}`, '--force-device-scale-factor=' + dpr,
  '--virtual-time-budget=4500', `--screenshot=${out}`, url], { stdio: 'ignore' });

/* o canvas e MEDIDO, nao chutado: a pagina publica fit:LxA no <title>.
   Margem sobrando viraria faixa clara dentro do .shotframe. */
const fit = (url) => {
  const dom = execFileSync(CHROME, ['--headless=new', '--disable-gpu', '--window-size=1500,2400',
    '--virtual-time-budget=4000', '--dump-dom', url], { encoding: 'utf8', maxBuffer: 64e6 });
  const m = dom.match(/fit:(\d+)x(\d+)/);
  if (!m) throw new Error('nao consegui medir o mockup: ' + url);
  return [Number(m[1]), Number(m[2])];
};
const render = (file, url) => { const [w, h] = fit(url); shot(path.join(SHOTS, file), url, w, h, 2); };

if (!NO_MOCK) {
  // painel de selecao: estado de abertura e o board definido (3 chips)
  for (const step of [1, 5]) {
    render(`mockup-board-s${step}-en.png`,
      `http://localhost:${PORT}/mockup-board-facets?step=${step}&lang=en&reel=1`);
  }
  // painel de resultado, em duas secoes
  for (const part of ['sizes', 'expl']) {
    render(`mockup-results-${part}.png`,
      `http://localhost:${PORT}/mockup-board-results?reel=1&part=${part}`);
  }
  console.log('4 mockups renderizados');
} else {
  console.log('mockups reaproveitados (--nomock)');
}

for (let i = 0; i < SCENES.length; i++) {
  shot(path.join(FRAMES, `s${i}.png`),
    `http://localhost:${PORT}/paid-scene?p=${SCENES[i]}${GUIDES ? '&guides=1' : ''}`, W, H);
}
console.log(`${SCENES.length} cenas renderizadas`);

srv.kill();
try { execFileSync('taskkill', ['/F', '/T', '/PID', String(srv.pid)], { stdio: 'ignore' }); } catch {}
if (GUIDES) { console.log('modo guias — nada encodado'); process.exit(0); }

const ffmpeg = process.env.FFMPEG_PATH || (await import('ffmpeg-static')).default;

// capa estatica = o gancho (tambem e o thumb do anuncio)
fs.copyFileSync(path.join(FRAMES, 's0.png'), path.join(OUT_DIR, `${NAME}-capa.png`));

/* Ken Burns. Primeira cena do resultado: push-in lento. Gancho: easing sqrt
   pra ter movimento ja nos primeiros frames. Demais: deriva minima. */
const zoomExpr = (i, D) => {
  if (i === PANEL) return `min(1.0+0.09*on/${D},1.09)`;
  if (i === 0) return `min(1.0+0.06*sqrt(on/${D}),1.06)`;
  return (i % 2 === 1) ? `min(1.0+0.03*on/${D},1.03)` : `max(1.03-0.03*on/${D},1.0)`;
};
const run = (a) => execFileSync(ffmpeg, a, { stdio: ['ignore', 'ignore', 'pipe'] });

const segs = [];
SCENES.forEach((_, i) => {
  const D = Math.round(DURS[i] * FPS);
  const seg = path.join(TMP, `s${i}.mp4`);
  run(['-loop', '1', '-framerate', String(FPS), '-t', DURS[i].toFixed(3), '-i', path.join(FRAMES, `s${i}.png`),
    '-filter_complex', `[0:v]scale=${W * 2}:${H * 2},setsar=1,zoompan=z='${zoomExpr(i, D)}':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=${W}x${H}:fps=${FPS},format=yuv420p,setsar=1[v]`,
    '-map', '[v]', '-r', String(FPS), '-frames:v', String(D),
    '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p', '-y', seg]);
  segs.push(seg);
});

const out = path.join(OUT_DIR, `${NAME}.mp4`);
const list = path.join(TMP, 'list.txt');
fs.writeFileSync(list, segs.map(s => `file '${s.replace(/\\/g, '/')}'`).join('\n'));
run(['-f', 'concat', '-safe', '0', '-i', list, '-c', 'copy', '-movflags', '+faststart', '-y', out]);

let dur = '?';
try { run(['-i', out]); } catch (e) { const m = String(e.stderr).match(/Duration:\s*([0-9:.]+)/); if (m) dur = m[1]; }
console.log(`${NAME}.mp4  ${W}x${H}  DURACAO REAL ${dur}  ${(fs.statSync(out).size / 1048576).toFixed(2)} MB  (alvo ${DURS.reduce((a, b) => a + b, 0).toFixed(1)}s)`);
fs.rmSync(TMP, { recursive: true, force: true });
