/* AURA-PAID01 — VARIANTE -B (v3, camada de persuasao). PT e EN.
 *
 *   node instagram/build-paid-b.mjs            # renderiza + encoda os 6 MP4 (-b e -b-en)
 *   node instagram/build-paid-b.mjs --guides   # so renderiza, com as zonas seguras
 *   node instagram/build-paid-b.mjs --pt       # so PT   |  --en  # so EN
 *
 * DESAFIANTE do teste A/B. O CONTROLE (paid01-v*.mp4, sem sufixo) NAO e tocado
 * por este script — arquivos, nomes e conteudo ficam intactos, senao o teste
 * nao mede nada. Tudo que a v3 adiciona no template e opt-in (callout/proof/
 * heroLight/anim), entao re-rodar build-paid.mjs continua reproduzindo a v2.
 *
 * O que muda tecnicamente vs build-paid.mjs:
 *  - ANIMACAO REAL: cenas marcadas em ANIM renderizam K frames variando ?a=0..100
 *    (count-up nos numeros, barras crescendo, reveal em beat). O video sai da
 *    sequencia de PNGs + hold do ultimo frame.
 *  - CORTE SECO entre cenas: o crossfade produzia visao dupla (ver DURS abaixo).
 *    Segmentos sao concatenados sem reencode.
 *  - THUMB = estado FINAL do gancho (a=100), nao o frame 0. O frame 0 tem o
 *    reveal ainda escondido; como capa, o estado assentado vende mais.
 *
 * Requisitos: Chrome + ffmpeg (FFMPEG_PATH se o ffmpeg-static nao estiver no repo).
 * GOTCHA: renderize sempre com URL LIMPA (sem `.html`) — o cleanUrls do `serve`
 * derruba a query string e todas as cenas saem identicas.
 */
import { execFileSync, spawn } from 'child_process';
import path from 'path';
import fs from 'fs';
import { fileURLToPath } from 'url';

const ffmpeg = process.env.FFMPEG_PATH || (await import('ffmpeg-static')).default;
const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const TPL = path.join(ROOT, 'instagram/templates');
const CHROME = process.env.CHROME_PATH || 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 5111;
const W = 1080, H = 1920, FPS = 30;

/* CORTE SECO entre todas as cenas (sem crossfade).
   Motivo, medido: amostrei o meio das transicoes da v2 e o crossfade produz
   visao dupla — nao so nos blocos de texto. Como cada cena tem Ken Burns
   proprio, no meio da transicao a cena que sai e a que entra estao em ESCALAS
   diferentes, entao ate os elementos fixos (logo, rodape, selo) aparecem
   duplicados e deslocados. Reduzir pra 0,16s so encurta o problema, nao resolve.
   Corte seco elimina de vez e le como intencional num anuncio informativo.
   (A v2/controle mantem o crossfade — vira mais um eixo que o teste mede.) */
const DURS = [3.8, 4.8, 5.2, 4.8, 4.8, 3.4];        // soma 26,8s — sem transicao consumindo tempo
const K_HOOK = 18;   // frames de animacao do gancho (0,60s) — cabe o beat do reveal
const K_DATA = 10;   // frames de animacao das cenas de dado (0,33s) — count-up rapido

const GUIDES = process.argv.includes('--guides');
const ONLY_PT = process.argv.includes('--pt');
const ONLY_EN = process.argv.includes('--en');
const SKIP_RENDER = process.argv.includes('--skip-render'); // reaproveita PNGs ja renderizados

// indice da cena -> quantos frames de animacao. Cena ausente = estatica (1 frame).
const SETS = [
  { base: 'paid01-v1-preflop-b', ids: ['b1-s1','b1-s2','b1-s3','b1-s4','b1-s5','p-cta-b'], anim: {0:K_HOOK, 1:K_DATA, 3:K_DATA} },
  { base: 'paid01-v2-field-b',   ids: ['b2-s1','b2-s2','b2-s3','b2-s4','b2-s5','p-cta-b'], anim: {0:K_HOOK, 1:K_DATA, 3:K_DATA} },
  { base: 'paid01-v3-leak-b',    ids: ['b3-s1','b3-s2','b3-s3','b3-s4','b3-s5','p-cta-b'], anim: {0:K_HOOK, 1:K_DATA, 2:K_DATA} },
];

const LANGS = [];
if (!ONLY_EN) LANGS.push({ tag: 'pt', suffix: '', outDir: path.join(ROOT, 'content/paid/AURA-PAID01'), idSuffix: '' });
if (!ONLY_PT) LANGS.push({ tag: 'en', suffix: '-en', outDir: path.join(ROOT, 'content/paid/AURA-PAID01/en'), idSuffix: '-en' });

const FRAMES = path.join(ROOT, 'instagram/output/paid-frames-b');
const TMP = path.join(ROOT, 'instagram/output/_segs-b');
[FRAMES, TMP].forEach(d => fs.mkdirSync(d, { recursive: true }));
LANGS.forEach(l => fs.mkdirSync(l.outDir, { recursive: true }));

const srv = SKIP_RENDER ? null : spawn('npx.cmd', ['serve', '-l', String(PORT), TPL], { stdio: 'ignore', shell: true });
if (!SKIP_RENDER) await new Promise(r => setTimeout(r, 6000));

function shot(id, out, a) {
  const q = [`p=${id}`];
  if (a !== undefined) q.push(`a=${a}`);
  if (GUIDES) q.push('guides=1');
  execFileSync(CHROME, ['--headless=new', '--disable-gpu', '--hide-scrollbars',
    `--window-size=${W},${H}`, '--force-device-scale-factor=1',
    '--virtual-time-budget=4000', `--screenshot=${out}`,
    `http://localhost:${PORT}/paid-scene?${q.join('&')}`], { stdio: 'ignore' });
}

// ---------- render ----------
if (!SKIP_RENDER) for (const L of LANGS) {
  for (const S of SETS) {
    const name = S.base + L.suffix;
    const dir = path.join(FRAMES, name);
    fs.mkdirSync(dir, { recursive: true });
    S.ids.forEach((id, i) => {
      const sceneId = id + L.idSuffix;
      const K = S.anim[i];
      if (!K) { shot(sceneId, path.join(dir, `s${i}_000.png`)); return; }
      for (let f = 0; f < K; f++) {
        shot(sceneId, path.join(dir, `s${i}_${String(f).padStart(3, '0')}.png`), Math.round((f / (K - 1)) * 100));
      }
    });
    console.log(`${name}: ${S.ids.length} cenas renderizadas`);
  }
}
if (srv) { srv.kill(); try { execFileSync('taskkill', ['/F', '/T', '/PID', String(srv.pid)], { stdio: 'ignore' }); } catch {} }
if (GUIDES) { console.log('modo guias — nada foi encodado'); process.exit(0); }

/* Ken Burns. Cena 0: push-in com easing sqrt (movimento ja nos primeiros frames).
   d=1 porque aqui o zoompan recebe uma SEQUENCIA (1 frame de saida por entrada). */
const zoomExpr = (i, D) => i === 0
  ? `min(1.0+0.09*sqrt(on/${D}),1.09)`
  : (i % 2 === 1 ? `min(1.0+0.05*on/${D},1.05)` : `max(1.05-0.05*on/${D},1.0)`);

const run = (args) => execFileSync(ffmpeg, args, { stdio: ['ignore', 'ignore', 'pipe'] });

for (const L of LANGS) {
  for (const S of SETS) {
    const name = S.base + L.suffix;
    const dir = path.join(FRAMES, name);
    const segs = [];

    // --- passo 1: cada cena vira um segmento com D frames + Ken Burns ---
    S.ids.forEach((_, i) => {
      const D = Math.round(DURS[i] * FPS);
      const K = S.anim[i] || 1;
      const seg = path.join(TMP, `${name}-s${i}.mp4`);
      const lastFrame = path.join(dir, `s${i}_${String(K - 1).padStart(3, '0')}.png`);
      const holdSec = (D - K) / FPS;
      const zp = `zoompan=z='${zoomExpr(i, D)}':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=${W}x${H}:fps=${FPS}`;
      const args = [];
      let fc;
      if (K > 1) {
        // sequencia animada + hold do ultimo frame, concatenados antes do zoom
        args.push('-framerate', String(FPS), '-i', path.join(dir, `s${i}_%03d.png`));
        args.push('-loop', '1', '-framerate', String(FPS), '-t', holdSec.toFixed(3), '-i', lastFrame);
        fc = `[0:v]scale=${W * 2}:${H * 2},setsar=1[a];[1:v]scale=${W * 2}:${H * 2},setsar=1[b];` +
             `[a][b]concat=n=2:v=1:a=0[c];[c]${zp},format=yuv420p,setsar=1[v]`;
      } else {
        args.push('-loop', '1', '-framerate', String(FPS), '-t', DURS[i].toFixed(3), '-i', lastFrame);
        fc = `[0:v]scale=${W * 2}:${H * 2},setsar=1,${zp},format=yuv420p,setsar=1[v]`;
      }
      args.push('-filter_complex', fc, '-map', '[v]', '-r', String(FPS),
        '-frames:v', String(D), '-c:v', 'libx264', '-preset', 'medium', '-crf', '18',
        '-pix_fmt', 'yuv420p', '-y', seg);
      run(args);
      segs.push(seg);
    });

    // --- passo 2: CORTE SECO — concat dos segmentos, sem reencode ---
    const total = DURS.reduce((a, b) => a + b, 0);
    const out = path.join(L.outDir, `${name}.mp4`);
    const listFile = path.join(TMP, `${name}-list.txt`);
    fs.writeFileSync(listFile, segs.map(s => `file '${s.replace(/\\/g, '/')}'`).join('\n'));
    run(['-f', 'concat', '-safe', '0', '-i', listFile,
      '-c', 'copy', '-movflags', '+faststart', '-y', out]);

    let dur = '?';
    try { run(['-i', out]); } catch (e) {
      const m = String(e.stderr).match(/Duration:\s*([0-9:.]+)/); if (m) dur = m[1];
    }
    const mb = (fs.statSync(out).size / 1024 / 1024).toFixed(2);

    // thumb = gancho no estado FINAL (a=100), nao o frame 0 (reveal ainda oculto)
    const k0 = S.anim[0] || 1;
    fs.copyFileSync(path.join(dir, `s0_${String(k0 - 1).padStart(3, '0')}.png`),
                    path.join(L.outDir, `${name}-thumb.png`));
    console.log(`${name}.mp4  ${W}x${H}  DURACAO REAL ${dur}  ${mb} MB  (alvo ${total.toFixed(2)}s)`);
  }
}
fs.rmSync(TMP, { recursive: true, force: true });
