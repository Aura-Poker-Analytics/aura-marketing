/* Gera crops APERTADOS dos prints reais, em resolucao nativa (sem downscale).
 * Regra: a largura da regiao define o upscale no video. Prefiro regioes >=700px
 * de largura pra ficar <=1.3x quando exibidas ~900px no layout. */
import { execFileSync, spawn } from 'child_process';
import path from 'path';
import fs from 'fs';

const TPL = 'C:/Users/Rafael/Documents/GitHub/aura-main/aura-marketing/instagram/templates';
const SHOTS = path.join(TPL, 'shots');
const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 5091;

// [saida, fonte, x, y, w, h]
const CROPS = [
  // Preflop: tabela Reg Aggro (cabecalho + linhas principais)
  ['crop-preflop-table.png', 'auta-total.png', 415, 180, 700, 560],
  // Preflop: rail de filtros (tipo de torneio, estagio, buy-in) — prova de "software"
  ['crop-filters-rail.png', 'auta-total.png', 8, 435, 336, 382],
  // Postflop: distribuicao de sizes (barras + contagem de maos)
  ['crop-sizedist.png', 'aura-total2.png', 320, 258, 520, 320],
  // Postflop: cards de Exploitative Sizes (2 colunas)
  ['crop-exploit-cards.png', 'aura-total2.png', 330, 588, 500, 360],
  // Postflop: duas colunas inteiras — largura ~nativa p/ 1080
  ['crop-postflop-wide.png', 'aura-total2.png', 300, 140, 1070, 860],
  // Postflop: coluna 'Disconnected' INTEIRA — prova real dos numeros de textura do V3
  ['crop-disconnected-col.png', 'aura-total2.png', 862, 140, 514, 812],
];

const srv = spawn('npx.cmd', ['serve', '-l', String(PORT), TPL], { stdio: 'ignore', shell: true });
await new Promise(r => setTimeout(r, 6000));

for (const [out, src, x, y, w, h] of CROPS) {
  const html = `<!DOCTYPE html><meta charset="utf-8"><style>*{margin:0;padding:0}
html,body{background:#0B1120}#c{width:${w}px;height:${h}px;overflow:hidden;position:relative}
#c img{position:absolute;left:${-x}px;top:${-y}px;display:block}</style>
<div id="c"><img src="http://localhost:${PORT}/shots/${src}"></div>`;
  fs.writeFileSync(path.join(TPL, '_crop.html'), html);
  execFileSync(CHROME, ['--headless=new', '--disable-gpu', '--hide-scrollbars',
    `--window-size=${w},${h}`, '--force-device-scale-factor=1', '--virtual-time-budget=3500',
    `--screenshot=${path.join(SHOTS, out)}`, `http://localhost:${PORT}/_crop`], { stdio: 'ignore' });
  const b = fs.readFileSync(path.join(SHOTS, out));
  console.log(out.padEnd(28), b.readUInt32BE(16) + 'x' + b.readUInt32BE(20));
}
fs.unlinkSync(path.join(TPL, '_crop.html'));
srv.kill();
try { execFileSync('taskkill', ['/F', '/T', '/PID', String(srv.pid)], { stdio: 'ignore' }); } catch {}
