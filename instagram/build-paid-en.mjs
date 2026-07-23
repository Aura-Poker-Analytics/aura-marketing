/* Versao EN dos videos de anuncio AURA-PAID01 (mercado global).
 *
 *   node instagram/build-paid-en.mjs            # renderiza 18 cenas EN + encoda 3 MP4
 *   node instagram/build-paid-en.mjs --guides   # so renderiza, com zonas seguras
 *
 * Identico ao build-paid.mjs, mas com as cenas -en (lang:"en" troca os rotulos
 * fixos da UI no paid-scene.html) e saida em content/paid/AURA-PAID01/en/ com
 * sufixo -en (utm_content distinto — sao anuncios novos, nao renomear).
 * Mesmo GOTCHA da URL LIMPA (sem .html) por causa do cleanUrls do `serve`.
 */
import { execFileSync, spawn } from 'child_process';
import ffmpeg from 'ffmpeg-static';
import path from 'path';
import fs from 'fs';
import { fileURLToPath } from 'url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const TPL = path.join(ROOT, 'instagram/templates');
const OUT_DIR = path.join(ROOT, 'content/paid/AURA-PAID01/en');
const FRAMES = path.join(ROOT, 'instagram/output/paid-frames-en');
const CHROME = process.env.CHROME_PATH || 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 5104;
const W = 1080, H = 1920, FPS = 30, DUR = 3.4, XF = 0.5;
const D = Math.round(DUR * FPS);
const GUIDES = process.argv.includes('--guides');
[FRAMES, OUT_DIR].forEach(d => fs.mkdirSync(d, { recursive: true }));

const VIDEOS = [
  { name: 'paid01-v1-preflop-en', scenes: ['p1-s1-en', 'p1-s2-en', 'p1-s3-en', 'p1-s4-en', 'p1-s5-en', 'p-cta-en'] },
  { name: 'paid01-v2-field-en',   scenes: ['p2-s1-en', 'p2-s2-en', 'p2-s3-en', 'p2-s4-en', 'p2-s5-en', 'p-cta-en'] },
  { name: 'paid01-v3-leak-en',    scenes: ['p3-s1-en', 'p3-s2-en', 'p3-s3-en', 'p3-s4-en', 'p3-s5-en', 'p-cta-en'] },
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
  console.log(`${v.name}: ${v.scenes.length} cenas`);
}
srv.kill();
try { execFileSync('taskkill', ['/F', '/T', '/PID', String(srv.pid)], { stdio: 'ignore' }); } catch {}
if (GUIDES) { console.log('modo guias — nada encodado'); process.exit(0); }

for (const v of VIDEOS) {
  const dir = path.join(FRAMES, v.name);
  const N = v.scenes.length;
  const args = [];
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
    '-pix_fmt', 'yuv420p', '-movflags', '+faststart', '-t', total.toFixed(3), '-y', out);
  execFileSync(ffmpeg, args, { stdio: ['ignore', 'ignore', 'pipe'] });
  let dur = '?';
  try { execFileSync(ffmpeg, ['-i', out], { stdio: 'pipe' }); }
  catch (e) { const m = String(e.stderr).match(/Duration:\s*([0-9:.]+)/); if (m) dur = m[1]; }
  const mb = (fs.statSync(out).size / 1024 / 1024).toFixed(2);
  fs.copyFileSync(path.join(dir, 's1.png'), path.join(OUT_DIR, `${v.name}-thumb.png`));
  console.log(`${v.name}.mp4  DURACAO REAL ${dur}  ${mb} MB`);
}
