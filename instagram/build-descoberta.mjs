/* CAMPANHA DE DESCOBERTA — 4 celulas, PT. (EN so depois da PT aprovada.)
 *
 *   node instagram/build-descoberta.mjs              # renderiza + encoda os 4 MP4
 *   node instagram/build-descoberta.mjs --frames-only # so estado final de cada cena (PNG p/ PO)
 *   node instagram/build-descoberta.mjs --guides     # so renderiza, com as zonas seguras
 *   node instagram/build-descoberta.mjs --skip-render  # reaproveita os PNGs
 *
 * Design validado pelo PO 25/07 — docs/02-paid/matriz-descoberta-4-celulas.md.
 *
 * ISTO NAO E CAMPANHA DE CONVERSAO. E instrumento de medicao de topo de funil:
 * cada reel isola uma hipotese de persona, os 4 juntos formam o experimento.
 * Consequencia pratica pra producao: tudo que NAO e a variavel testada precisa
 * ser IDENTICO nos 4 (duracao, ritmo, CTA, selo, transicao). Diferenca acidental
 * entre celulas vira viés e contamina a leitura do teste.
 *
 * 🔴 Os 4 primeiros frames sao LITERAIS (doc §2) — o conteudo vive no deck.js
 * com marcacao "LITERAL". Nao editar sem passar pela Midia Paga.
 *
 * ⚠️ DESVIO REGISTRADO vs doc §3.5 (crossfade 0,4s): uso CORTE SECO nos 4.
 * Motivo medido na v3 do AURA-PAID01: como cada cena tem Ken Burns proprio, no
 * meio do crossfade a cena que sai e a que entra estao em ESCALAS diferentes —
 * entao os elementos fixos (logo, rodape e o SELO de prova) aparecem duplicados
 * e deslocados. Com o selo persistente do §3.2 em todas as cenas, o defeito
 * passa a atingir TODAS as transicoes, nao so as de texto denso. Corte seco
 * aplicado igualmente nos 4 preserva a comparabilidade.
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
const PORT = 5121;
const W = 1080, H = 1920, FPS = 30;

// soma 26,0s exatos (doc §3.5) QUANDO a celula tem as 6 cenas padrao. Sem
// transicao consumindo tempo (corte seco).
const DURS = [3.8, 4.7, 5.0, 4.7, 4.6, 3.2];
const K_HOOK = 18;   // frames de animacao do gancho (0,60s) — cabe o beat
const K_DATA = 10;   // frames das cenas de dado (0,33s) — count-up rapido

const GUIDES = process.argv.includes('--guides');
const SKIP_RENDER = process.argv.includes('--skip-render');
const FRAMES_ONLY = process.argv.includes('--frames-only');

/* nome do arquivo = nome do anuncio = utm_content (doc §4). NAO RENOMEAR:
   quebra a serie do relatorio.
   v2.1 (PO 26/07): anim e durs por ID de cena (nao por indice posicional) —
   disc-01 perdeu a cena "d1-s3" (deletada a pedido do PO) e ficou com 5 cenas
   em vez de 6; indexar por id evita off-by-one quando a contagem difere entre
   celulas. disc-01 soma 21,0s (nao 26,0s) — DESVIO REGISTRADO e documentado
   no roteiro.
   v2.2 (PO 26/07, 3a rodada): disc-04 perdeu a cena "d4-s3" ("A tela real")
   pelo mesmo motivo/padrao — tambem cai pra 5 cenas e 21,0s. disc-02 e
   disc-03 seguem com as 6 cenas originais, em 26,0s.
   v2.3 (PO 26/07, 4a rodada): 4 celulas EN adicionadas (mesmos ids + "-en"),
   mesmas durs/estrutura das PT correspondentes — so o vocabulario muda. */
const CELLS = [
  { name: 'disc-01-solver',    ids: ['d1-s1','d1-s2','d1-s4','d1-s5','d-cta'],
    durs: [3.8, 4.7, 4.7, 4.6, 3.2], anim: { 'd1-s1':K_HOOK, 'd1-s4':K_DATA } },
  { name: 'disc-02-exploit',   ids: ['d2-s1','d2-s2','d2-s4','d2-s3','d2-s5','d-cta'],
    durs: DURS, anim: { 'd2-s1':K_HOOK, 'd2-s2':K_DATA, 'd2-s4':K_DATA } },
  { name: 'disc-03-categoria', ids: ['d3-s1','d3-s2','d3-s3','d3-s4','d3-s5','d-cta'],
    durs: DURS, anim: { 'd3-s1':K_HOOK, 'd3-s4':K_DATA } },
  { name: 'disc-04-pioneiro',  ids: ['d4-s1','d4-s2','d4-s4','d4-s5','d-cta'],
    durs: [3.8, 4.7, 4.7, 4.6, 3.2], anim: { 'd4-s1':K_HOOK, 'd4-s2':K_DATA, 'd4-s4':K_DATA } },
  { name: 'disc-01-solver-en',    ids: ['d1-s1-en','d1-s2-en','d1-s4-en','d1-s5-en','d-cta-en'],
    durs: [3.8, 4.7, 4.7, 4.6, 3.2], anim: { 'd1-s1-en':K_HOOK, 'd1-s4-en':K_DATA } },
  { name: 'disc-02-exploit-en',   ids: ['d2-s1-en','d2-s2-en','d2-s4-en','d2-s3-en','d2-s5-en','d-cta-en'],
    durs: DURS, anim: { 'd2-s1-en':K_HOOK, 'd2-s2-en':K_DATA, 'd2-s4-en':K_DATA } },
  { name: 'disc-03-categoria-en', ids: ['d3-s1-en','d3-s2-en','d3-s3-en','d3-s4-en','d3-s5-en','d-cta-en'],
    durs: DURS, anim: { 'd3-s1-en':K_HOOK, 'd3-s4-en':K_DATA } },
  { name: 'disc-04-pioneiro-en',  ids: ['d4-s1-en','d4-s2-en','d4-s4-en','d4-s5-en','d-cta-en'],
    durs: [3.8, 4.7, 4.7, 4.6, 3.2], anim: { 'd4-s1-en':K_HOOK, 'd4-s2-en':K_DATA, 'd4-s4-en':K_DATA } },
];

const OUT_DIR = path.join(ROOT, 'content/paid/AURA-DESCOBERTA');
const FRAMES = path.join(ROOT, 'instagram/output/desc-frames');
const PREVIEW = path.join(ROOT, 'instagram/output/desc-preview');
const TMP = path.join(ROOT, 'instagram/output/_segs-desc');
[OUT_DIR, FRAMES, PREVIEW, TMP].forEach(d => fs.mkdirSync(d, { recursive: true }));

const srv = (SKIP_RENDER && !FRAMES_ONLY) ? null : spawn('npx.cmd', ['serve', '-l', String(PORT), TPL], { stdio: 'ignore', shell: true });
if (srv) await new Promise(r => setTimeout(r, 6000));

function shot(id, out, a) {
  const q = [`p=${id}`];
  if (a !== undefined) q.push(`a=${a}`);
  if (GUIDES) q.push('guides=1');
  execFileSync(CHROME, ['--headless=new', '--disable-gpu', '--hide-scrollbars',
    `--window-size=${W},${H}`, '--force-device-scale-factor=1',
    '--virtual-time-budget=4000', `--screenshot=${out}`,
    `http://localhost:${PORT}/paid-scene?${q.join('&')}`], { stdio: 'ignore' });
}

/* --frames-only: 1 PNG por cena no estado final (a=100), sem guias, sem encode.
   Saida: instagram/output/desc-preview/<reel>/s<N>.png — PO valida antes do MP4. */
if (FRAMES_ONLY) {
  for (const C of CELLS) {
    const dir = path.join(PREVIEW, C.name);
    fs.mkdirSync(dir, { recursive: true });
    C.ids.forEach((id, i) => {
      const out = path.join(dir, `s${i + 1}.png`);
      // estado final: anim=100 (beat revelado, count-up completo)
      shot(id, out, 100);
    });
    console.log(`${C.name}: ${C.ids.length} PNGs de preview → ${dir}`);
  }
  if (srv) { srv.kill(); try { execFileSync('taskkill', ['/F', '/T', '/PID', String(srv.pid)], { stdio: 'ignore' }); } catch {} }
  console.log(`preview pronto: ${PREVIEW} (${CELLS.length * 6} PNGs). Encode so depois do OK do PO.`);
  process.exit(0);
}

if (!SKIP_RENDER) for (const C of CELLS) {
  const dir = path.join(FRAMES, C.name);
  fs.mkdirSync(dir, { recursive: true });
  C.ids.forEach((id, i) => {
    const K = C.anim[id];
    if (!K) { shot(id, path.join(dir, `s${i}_000.png`)); return; }
    for (let f = 0; f < K; f++) {
      shot(id, path.join(dir, `s${i}_${String(f).padStart(3, '0')}.png`), Math.round((f / (K - 1)) * 100));
    }
  });
  console.log(`${C.name}: ${C.ids.length} cenas renderizadas`);
}
if (srv) { srv.kill(); try { execFileSync('taskkill', ['/F', '/T', '/PID', String(srv.pid)], { stdio: 'ignore' }); } catch {} }
if (GUIDES) { console.log('modo guias — nada foi encodado'); process.exit(0); }

const zoomExpr = (i, D) => i === 0
  ? `min(1.0+0.09*sqrt(on/${D}),1.09)`
  : (i % 2 === 1 ? `min(1.0+0.05*on/${D},1.05)` : `max(1.05-0.05*on/${D},1.0)`);

const run = (args) => execFileSync(ffmpeg, args, { stdio: ['ignore', 'ignore', 'pipe'] });

for (const C of CELLS) {
  const dir = path.join(FRAMES, C.name);
  const segs = [];

  // passo 1: cada cena vira um segmento (animacao + hold) com Ken Burns
  C.ids.forEach((id, i) => {
    const D = Math.round(C.durs[i] * FPS);
    const K = C.anim[id] || 1;
    const seg = path.join(TMP, `${C.name}-s${i}.mp4`);
    const lastFrame = path.join(dir, `s${i}_${String(K - 1).padStart(3, '0')}.png`);
    const zp = `zoompan=z='${zoomExpr(i, D)}':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=${W}x${H}:fps=${FPS}`;
    const args = [];
    let fc;
    if (K > 1) {
      args.push('-framerate', String(FPS), '-i', path.join(dir, `s${i}_%03d.png`));
      args.push('-loop', '1', '-framerate', String(FPS), '-t', ((D - K) / FPS).toFixed(3), '-i', lastFrame);
      fc = `[0:v]scale=${W * 2}:${H * 2},setsar=1[a];[1:v]scale=${W * 2}:${H * 2},setsar=1[b];` +
           `[a][b]concat=n=2:v=1:a=0[c];[c]${zp},format=yuv420p,setsar=1[v]`;
    } else {
      args.push('-loop', '1', '-framerate', String(FPS), '-t', C.durs[i].toFixed(3), '-i', lastFrame);
      fc = `[0:v]scale=${W * 2}:${H * 2},setsar=1,${zp},format=yuv420p,setsar=1[v]`;
    }
    args.push('-filter_complex', fc, '-map', '[v]', '-r', String(FPS),
      '-frames:v', String(D), '-c:v', 'libx264', '-preset', 'medium', '-crf', '18',
      '-pix_fmt', 'yuv420p', '-y', seg);
    run(args);
    segs.push(seg);
  });

  // passo 2: corte seco — concat sem reencode
  const out = path.join(OUT_DIR, `${C.name}.mp4`);
  const listFile = path.join(TMP, `${C.name}-list.txt`);
  fs.writeFileSync(listFile, segs.map(s => `file '${s.replace(/\\/g, '/')}'`).join('\n'));
  run(['-f', 'concat', '-safe', '0', '-i', listFile, '-c', 'copy', '-movflags', '+faststart', '-y', out]);

  let dur = '?';
  try { run(['-i', out]); } catch (e) {
    const m = String(e.stderr).match(/Duration:\s*([0-9:.]+)/); if (m) dur = m[1];
  }
  const mb = (fs.statSync(out).size / 1024 / 1024).toFixed(2);

  // thumb = gancho no estado final (frame 0 tem o beat ainda oculto)
  const k0 = C.anim[C.ids[0]] || 1;
  fs.copyFileSync(path.join(dir, `s0_${String(k0 - 1).padStart(3, '0')}.png`),
                  path.join(OUT_DIR, `${C.name}-thumb.png`));
  console.log(`${C.name}.mp4  ${W}x${H}  DURACAO REAL ${dur}  ${mb} MB  (alvo ${C.durs.reduce((a,b)=>a+b,0).toFixed(2)}s)`);
}
fs.rmSync(TMP, { recursive: true, force: true });
