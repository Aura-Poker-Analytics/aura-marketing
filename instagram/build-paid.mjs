/* Gera os 3 videos de anuncio da campanha AURA-PAID01.
 *
 *   node instagram/build-paid.mjs            # renderiza as 18 cenas + encoda os 3 MP4
 *   node instagram/build-paid.mjs --guides   # so renderiza, com as zonas seguras desenhadas
 *
 * Requisitos: Chrome instalado + `npm i ffmpeg-static` (o pacote pode viver fora do repo;
 * ajuste o import se preciso). ffmpeg-static NAO traz ffprobe — a duracao real e lida
 * do stderr do `ffmpeg -i`.
 *
 * GOTCHA: renderize sempre com URL LIMPA (sem `.html`). O cleanUrls do `npx serve`
 * redireciona `/paid-scene.html?p=x` para `/paid-scene` e DERRUBA a query string —
 * o efeito e todas as cenas sairem identicas.
 */
import { execFileSync, spawn } from 'child_process';
import ffmpeg from 'ffmpeg-static';
import path from 'path';
import fs from 'fs';
import { fileURLToPath } from 'url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const TPL = path.join(ROOT, 'instagram/templates');
const OUT_DIR = path.join(ROOT, 'content/paid/AURA-PAID01');
const FRAMES = path.join(ROOT, 'instagram/output/paid-frames');
const CHROME = process.env.CHROME_PATH || 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 5107;
const W = 1080, H = 1920, FPS = 30;
const DUR = 3.4;   // s por cena
const XF = 0.5;    // crossfade
const D = Math.round(DUR * FPS);

const GUIDES = process.argv.includes('--guides');
fs.mkdirSync(FRAMES, { recursive: true });
fs.mkdirSync(OUT_DIR, { recursive: true });

// nomes EXATOS: viram utm_content na atribuicao — nao renomear
const VIDEOS = [
  { name: 'paid01-v1-preflop', scenes: ['p1-s1', 'p1-s2', 'p1-s3', 'p1-s4', 'p1-s5', 'p-cta'] },
  { name: 'paid01-v2-field',   scenes: ['p2-s1', 'p2-s2', 'p2-s3', 'p2-s4', 'p2-s5', 'p-cta'] },
  { name: 'paid01-v3-leak',    scenes: ['p3-s1', 'p3-s2', 'p3-s3', 'p3-s4', 'p3-s5', 'p-cta'] },
];

const srv = spawn('npx.cmd', ['serve', '-l', String(PORT), TPL], { stdio: 'ignore', shell: true });
await new Promise(r => setTimeout(r, 6000));

function shot(id, out) {
  const url = `http://localhost:${PORT}/paid-scene?p=${id}${GUIDES ? '&guides=1' : ''}`;
  execFileSync(CHROME, ['--headless=new', '--disable-gpu', '--hide-scrollbars',
    `--window-size=${W},${H}`, '--force-device-scale-factor=1',
    '--virtual-time-budget=4000', `--screenshot=${out}`, url], { stdio: 'ignore' });
}

for (const v of VIDEOS) {
  const dir = path.join(FRAMES, v.name);
  fs.mkdirSync(dir, { recursive: true });
  v.scenes.forEach((id, i) => shot(id, path.join(dir, `s${i + 1}.png`)));
  console.log(`${v.name}: ${v.scenes.length} cenas renderizadas`);
}
srv.kill();
try { execFileSync('taskkill', ['/F', '/T', '/PID', String(srv.pid)], { stdio: 'ignore' }); } catch {}

if (GUIDES) { console.log('modo guias — nada foi encodado'); process.exit(0); }

for (const v of VIDEOS) {
  const dir = path.join(FRAMES, v.name);
  const N = v.scenes.length;
  const args = [];
  // 1 FRAME por cena (sem -loop): com -loop o zoompan multiplica os frames de entrada
  for (let i = 1; i <= N; i++) args.push('-i', path.join(dir, `s${i}.png`));

  const parts = [];
  for (let i = 0; i < N; i++) {
    const z = (i % 2 === 0) ? `min(1.0+0.045*on/${D},1.045)` : `max(1.045-0.045*on/${D},1.0)`;
    parts.push(`[${i}:v]scale=${W * 2}:${H * 2},setsar=1,` +
      `zoompan=z='${z}':d=${D}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=${W}x${H}:fps=${FPS},` +
      `format=yuv420p,setsar=1[v${i}]`);
  }
  let last = 'v0', acc = DUR;
  for (let i = 1; i < N; i++) {
    const off = (acc - XF).toFixed(3);
    const o = i === N - 1 ? 'vout' : `x${i}`;
    parts.push(`[${last}][v${i}]xfade=transition=fade:duration=${XF}:offset=${off}[${o}]`);
    last = o; acc = acc + DUR - XF;
  }
  const total = N * DUR - (N - 1) * XF;
  const out = path.join(OUT_DIR, `${v.name}.mp4`);
  args.push('-filter_complex', parts.join(';'), '-map', '[vout]', '-r', String(FPS),
    '-c:v', 'libx264', '-preset', 'medium', '-crf', '20',
    '-pix_fmt', 'yuv420p', '-movflags', '+faststart',
    '-t', total.toFixed(3), '-y', out);
  execFileSync(ffmpeg, args, { stdio: ['ignore', 'ignore', 'pipe'] });

  let dur = '?';
  try { execFileSync(ffmpeg, ['-i', out], { stdio: 'pipe' }); }
  catch (e) { const m = String(e.stderr).match(/Duration:\s*([0-9:.]+)/); if (m) dur = m[1]; }
  const mb = (fs.statSync(out).size / 1024 / 1024).toFixed(2);

  // thumbnail = 1o quadro (o gancho) — e o que o Gerenciador usa de capa
  fs.copyFileSync(path.join(dir, 's1.png'), path.join(OUT_DIR, `${v.name}-thumb.png`));
  console.log(`${v.name}.mp4  ${W}x${H}  DURACAO REAL ${dur}  ${mb} MB  (alvo ${total.toFixed(2)}s)`);
}
