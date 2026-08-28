/* DISC03 — reel "classes de jogador" (PT). Slug/utm_content: disc03-classes-cbet.
 *
 *   node instagram/build-disc03.mjs            # renderiza + encoda MP4 + capa PNG
 *   node instagram/build-disc03.mjs --guides   # so renderiza, com zonas seguras
 *   node instagram/build-disc03.mjs --en       # versao inglesa (cenas dc-*-en)
 *
 * Primeiro criativo do eixo "classes de jogador": contraste real entre dois
 * perfis de reg, com amostra na tela.
 *
 * DADO OFICIAL (validado no banco pelo PO — NAO ALTERAR):
 *   Flop CBet IP · SRP · EP contra BB
 *   Reg Aggro 85,2% (n=2.399.253) · Reg Tight 77,6% (n=804.261) · gap 7,6 pp
 *
 * RITMO: brief pede 15-20s com transicoes LENTAS. Soma 18,2s.
 * A cena 3 (o coracao: painel real) e a mais longa E leva um push-in LENTO —
 * as demais ficam quase paradas, pra o zoom da cena 3 se destacar.
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
/* --en: sufixo -en no arquivo = utm_content distinto (anuncios diferentes) */
const EN = process.argv.includes('--en');
const GUIDES = process.argv.includes('--guides');
const PORT = EN ? 5192 : 5191;
const W = 1080, H = 1920, FPS = 30;

const NAME = 'disc03-classes-cbet' + (EN ? '-en' : '');   // = utm_content, nao renomear
const SCENES = ['dc-s1', 'dc-s2', 'dc-s3', 'dc-s4', 'dc-cta'].map(id => EN ? id + '-en' : id);
// gancho 3,4 · setup 3,2 · painel 4,8 (o coracao) · pergunta 3,2 · CTA 3,6 = 18,2s
const DURS = [3.4, 3.2, 4.8, 3.2, 3.6];
const PANEL = 2;   // indice da cena do painel real — leva o push-in lento

const OUT_DIR = path.join(ROOT, 'content/paid/AURA-DISC03');
const FRAMES = path.join(ROOT, 'instagram/output/disc03-frames' + (EN ? '-en' : ''));
const TMP = path.join(ROOT, 'instagram/output/_segs-disc03' + (EN ? '-en' : ''));
[OUT_DIR, FRAMES, TMP].forEach(d => fs.mkdirSync(d, { recursive: true }));

const srv = spawn('npx.cmd', ['serve', '-l', String(PORT), TPL], { stdio: 'ignore', shell: true });
await new Promise(r => setTimeout(r, 6000));

for (let i = 0; i < SCENES.length; i++) {
  const q = GUIDES ? '&guides=1' : '';
  execFileSync(CHROME, ['--headless=new', '--disable-gpu', '--hide-scrollbars',
    `--window-size=${W},${H}`, '--force-device-scale-factor=1', '--virtual-time-budget=4500',
    `--screenshot=${path.join(FRAMES, `s${i}.png`)}`,
    `http://localhost:${PORT}/paid-scene?p=${SCENES[i]}${q}`], { stdio: 'ignore' });
}
console.log(`${SCENES.length} cenas renderizadas`);
srv.kill();
try { execFileSync('taskkill', ['/F', '/T', '/PID', String(srv.pid)], { stdio: 'ignore' }); } catch {}
if (GUIDES) { console.log('modo guias — nada encodado'); process.exit(0); }

// capa estatica = frame 1 (tambem e o thumb do anuncio)
fs.copyFileSync(path.join(FRAMES, 's0.png'), path.join(OUT_DIR, `${NAME}-capa.png`));

/* Ken Burns. Cena do PAINEL: push-in lento e mais longo (o brief pede "zoom
   lento" justamente ali). Gancho: push-in curto com easing sqrt, pra ter
   movimento ja nos primeiros frames. Demais: deriva minima. */
const zoomExpr = (i, D) => {
  if (i === PANEL) return `min(1.0+0.10*on/${D},1.10)`;
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
