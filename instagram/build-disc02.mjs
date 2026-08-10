/* DISC02 — reel "plataforma inteira" (PT). Slug/utm_content: disc02-plataforma-mda.
 *
 *   node instagram/build-disc02.mjs            # renderiza + encoda MP4 + capa PNG
 *   node instagram/build-disc02.mjs --guides   # so renderiza, com zonas seguras
 *
 * Campanha de APRESENTACAO da plataforma (substitui 'Nao e solver. Nao e
 * tracker.'). Tour v2: gancho -> Preflop -> Postflop -> Node-by-Node -> filtros
 * -> grade dos 3 modulos -> CTA. Eixo: filtros/fatias/desagregacoes. 'Conheca a plataforma'.
 *
 * RITMO (playbook §criativo): tempo por cena = max(2,5s ; palavras/4 + 1s),
 * errando pro LENTO (feedback do PO: transicoes rapidas demais).
 * ⚠️ DESVIO REGISTRADO: o playbook pede gancho de 3-4s; o brief do disc02
 * fixa o gancho em 0-2s (frame 1 tambem vira capa estatica). Prevalece o
 * brief — o gancho e headline unica, sem segunda linha pra ler.
 * Corte seco entre cenas (crossfade duplica logo/rodape/selo — ver
 * build-descoberta.mjs).
 *
 * Requisitos: Chrome + ffmpeg (FFMPEG_PATH se o ffmpeg-static nao estiver no
 * repo). GOTCHA: URL LIMPA sempre (cleanUrls do `serve` derruba query string).
 */
import { execFileSync, spawn } from 'child_process';
import path from 'path';
import fs from 'fs';
import { fileURLToPath } from 'url';

const ffmpeg = process.env.FFMPEG_PATH || (await import('ffmpeg-static')).default;
const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const TPL = path.join(ROOT, 'instagram/templates');
const CHROME = process.env.CHROME_PATH || 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 5171;
const W = 1080, H = 1920, FPS = 30;

const NAME = 'disc02-plataforma-mda';           // = utm_content, nao renomear
const SCENES = ['dm-s1', 'dm-s2', 'dm-s3', 'dm-s4', 'dm-s5', 'dm-s6', 'dm-cta'];
/* v2 — Hotspot fora; 3 modulos + cena de filtros. tempo = max(2,5s ; palavras/4+1s):
   s1 gancho 2,0 (brief) · s2 ~12 palavras -> 4,0 · s3 ~12 -> 4,0 · s4 ~12 -> 4,2
   · s5 ~11 -> 3,8 · s6 grade 3 linhas + 2 frases -> 4,2 · CTA 3,0. Total 25,2s. */
const DURS = [2.0, 4.0, 4.0, 4.2, 3.8, 4.2, 3.0];

const GUIDES = process.argv.includes('--guides');
const OUT_DIR = path.join(ROOT, 'content/paid/AURA-DISC02');
const FRAMES = path.join(ROOT, 'instagram/output/disc02-frames');
const TMP = path.join(ROOT, 'instagram/output/_segs-disc02');
[OUT_DIR, FRAMES, TMP].forEach(d => fs.mkdirSync(d, { recursive: true }));

const srv = spawn('npx.cmd', ['serve', '-l', String(PORT), TPL], { stdio: 'ignore', shell: true });
await new Promise(r => setTimeout(r, 6000));

function shot(url, out, w, h, dpr = 1) {
  execFileSync(CHROME, ['--headless=new', '--disable-gpu', '--hide-scrollbars',
    `--window-size=${w},${h}`, `--force-device-scale-factor=${dpr}`,
    '--virtual-time-budget=4500', `--screenshot=${out}`, url], { stdio: 'ignore' });
}

for (let i = 0; i < SCENES.length; i++) {
  const q = GUIDES ? '&guides=1' : '';
  shot(`http://localhost:${PORT}/paid-scene?p=${SCENES[i]}${q}`, path.join(FRAMES, `s${i}.png`), W, H);
}
console.log(`${SCENES.length} cenas renderizadas`);
srv.kill();
try { execFileSync('taskkill', ['/F', '/T', '/PID', String(srv.pid)], { stdio: 'ignore' }); } catch {}
if (GUIDES) { console.log('modo guias — nada encodado'); process.exit(0); }

// capa estatica = frame 1 (tambem e o thumb do anuncio)
fs.copyFileSync(path.join(FRAMES, 's0.png'), path.join(OUT_DIR, `${NAME}-capa.png`));

const zoomExpr = (i, D) => i === 0
  ? `min(1.0+0.09*sqrt(on/${D}),1.09)`
  : (i % 2 === 1 ? `min(1.0+0.05*on/${D},1.05)` : `max(1.05-0.05*on/${D},1.0)`);
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
