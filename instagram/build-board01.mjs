/* BOARD01 — lancamento da selecao de board no Postflop Analysis.
 * Slug/utm_content: board01-amostra-antes (+ -en).
 *
 *   node instagram/build-board01.mjs             # PT: mockups + cenas + MP4 + capa
 *   node instagram/build-board01.mjs --en        # EN
 *   node instagram/build-board01.mjs --guides    # so renderiza, com zonas seguras
 *   node instagram/build-board01.mjs --mock      # so re-renderiza os 8 mockups
 *   node instagram/build-board01.mjs --nomock   # reaproveita os mockups (itera so a copy)
 *
 * O painel e RECRIADO (mockup-board-facets.html), nao e captura. As
 * porcentagens saem da distribuicao medida embutida no template e sao
 * recalculadas com a mesma matematica do produto — por isso a fileira
 * Conectividade muda sozinha entre o passo 1 e o passo 2.
 *
 * ⚠️ ZERO CONTAGEM ABSOLUTA DE MAOS em qualquer asset daqui. O "105 milhoes"
 * dos docs internos e linha IP+OOP no banco local, nao mao unica, e nao e
 * numero de producao.
 *
 * RITMO: 19,4s. As cenas 2 e 3 tem layout identico de proposito — o corte
 * seco entre elas LE como o recalculo acontecendo. Corte seco em tudo
 * (crossfade duplica logo/rodape/selo — ver build-descoberta.mjs).
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
const MOCK_ONLY = process.argv.includes('--mock');
// --nomock: pula os mockups (ja renderizados) pra iterar so a copy das cenas
const NO_MOCK = process.argv.includes('--nomock');
const PORT = EN ? 5294 : 5293;
const W = 1080, H = 1920, FPS = 30;

const NAME = 'board01-amostra-antes' + (EN ? '-en' : '');   // = utm_content, nao renomear
const SCENES = ['bf-s1', 'bf-s2', 'bf-s3', 'bf-s4', 'bf-cta'].map(id => EN ? id + '-en' : id);
// gancho 3,2 · passo 1 3,8 · passo 2 (o post inteiro) 4,6 · riscado 4,2 · CTA 3,6 = 19,4s
const DURS = [3.2, 3.8, 4.6, 4.2, 3.6];
const PANEL = 2;   // cena do recalculo — push-in lento

const OUT_DIR = path.join(ROOT, 'content/paid/AURA-BOARD01');
const SHOTS = path.join(TPL, 'shots');
const FRAMES = path.join(ROOT, 'instagram/output/board01-frames' + (EN ? '-en' : ''));
const TMP = path.join(ROOT, 'instagram/output/_segs-board01' + (EN ? '-en' : ''));
[OUT_DIR, SHOTS, FRAMES, TMP].forEach(d => fs.mkdirSync(d, { recursive: true }));

const srv = spawn('npx.cmd', ['serve', '-l', String(PORT), TPL], { stdio: 'ignore', shell: true });
await new Promise(r => setTimeout(r, 6000));

/* dpr explicito: o mockup renderiza a 2x (vai ser reduzido dentro da cena),
   a cena do anuncio renderiza a 1x — ela JA e 1080x1920 */
const shot = (out, url, w, h, dpr = 1) => execFileSync(CHROME, ['--headless=new', '--disable-gpu',
  '--hide-scrollbars', `--window-size=${w},${h}`, '--force-device-scale-factor=' + dpr,
  '--virtual-time-budget=4500', `--screenshot=${out}`, url], { stdio: 'ignore' });

/* 1) os 4 passos do painel. Duas variantes:
     - REEL  (estreita, tipo grande) -> mockup-board-sN.png, usada pelo anuncio
     - WIDE  (larga)                 -> mockup-board-wide-sN.png, imagem solta
   O tamanho do canvas NAO e chutado: a pagina mede a janela e publica
   'fit:LxA' no <title>; lemos isso com --dump-dom e so entao tiramos o
   screenshot no tamanho exato. Margem sobrando viraria faixa clara dentro
   do .shotframe. */
const fit = (url) => {
  const dom = execFileSync(CHROME, ['--headless=new','--disable-gpu','--window-size=1500,1500',
    '--virtual-time-budget=4000','--dump-dom', url], { encoding:'utf8', maxBuffer: 64e6 });
  const m = dom.match(/fit:(\d+)x(\d+)/);
  if (!m) throw new Error('nao consegui medir o mockup: ' + url);
  return [Number(m[1]), Number(m[2])];
};
if (!NO_MOCK) for (const lang of ['pt','en']) {
  for (const step of [1,2,3,4]) {
    const suf = lang === 'en' ? '-en' : '';
    for (const [variant, pre] of [['&reel=1',''], ['','-wide']]) {
      const url = `http://localhost:${PORT}/mockup-board-facets?step=${step}&lang=${lang}${variant}`;
      const [w,h] = fit(url);
      shot(path.join(SHOTS, `mockup-board${pre}-s${step}${suf}.png`), url, w, h, 2);
    }
  }
}
console.log(NO_MOCK ? 'mockups reaproveitados (--nomock)' : '16 mockups renderizados (4 passos x 2 idiomas x reel/wide)');

if (!MOCK_ONLY) {
  /* 2) as cenas do anuncio */
  for (let i = 0; i < SCENES.length; i++) {
    shot(path.join(FRAMES, `s${i}.png`),
      `http://localhost:${PORT}/paid-scene?p=${SCENES[i]}${GUIDES ? '&guides=1' : ''}`, W, H);
  }
  console.log(`${SCENES.length} cenas renderizadas`);
}

srv.kill();
try { execFileSync('taskkill', ['/F', '/T', '/PID', String(srv.pid)], { stdio: 'ignore' }); } catch {}
if (MOCK_ONLY) process.exit(0);
if (GUIDES) { console.log('modo guias — nada encodado'); process.exit(0); }

const ffmpeg = process.env.FFMPEG_PATH || (await import('ffmpeg-static')).default;

// capa estatica = passo 2 do painel dentro da cena (o frame que Midia Paga pediu congelado)
fs.copyFileSync(path.join(FRAMES, 's2.png'), path.join(OUT_DIR, `${NAME}-capa.png`));

/* Ken Burns. Cena do recalculo: push-in lento. Gancho: easing sqrt pra ter
   movimento ja nos primeiros frames. Demais: deriva minima. */
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
