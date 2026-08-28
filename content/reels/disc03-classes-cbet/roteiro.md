# disc03-classes-cbet · Reel do eixo "classes de jogador" (PT + EN)

**Campanha:** AURA-DISC03 · **`utm_content`:** `disc03-classes-cbet` · **EN:** `disc03-classes-cbet-en`
**Conceito:** primeiro criativo do eixo. Nada de categoria abstrata — um contraste real entre dois
perfis de reg, com amostra na tela.
**Entrega:** `content/paid/AURA-DISC03/` — `disc03-classes-cbet.mp4` (PT) e `disc03-classes-cbet-en.mp4` (EN), 18,20s cada, + capas 1080×1920

## Dado oficial (validado no banco pelo PO — não alterar)
**Flop CBet IP · SRP · EP contra BB**

| Classe | Flop CBet IP | n |
|---|---|---|
| Reg Aggro | **85,2%** | 2.399.253 |
| Reg Tight | **77,6%** | 804.261 |
| | **gap 7,6 pp** | |

Na tela o `n` aparece arredondado como a UI mostra (**2,4M** / **804k**); os valores exatos ficam
aqui, no roteiro.

## Cenas (corte seco; transições LENTAS)

| # | dur | Conteúdo |
|---|---|---|
| 1 | 3,4s | **GANCHO/CAPA** — logo · kicker `Flop CBet IP · SRP · EP contra BB` · **"O mesmo cbet. Dois regs diferentes."** · os dois números grandes lado a lado com o chip de **7,6 pp** entre eles e o `n` sob cada um |
| 2 | 3,2s | **O spot** — *"Pote single-raised. EP cbeta em posição contra o BB."* |
| 3 | 4,8s | **O coração** — painel da tela CBet IP com Reg Aggro × Reg Tight lado a lado, `n` visível. **Push-in lento** (é a cena mais longa e a única com zoom pronunciado) |
| 4 | 3,2s | **A pergunta** — **"Você defende igual contra os dois?"** |
| 5 | 3,6s | **Fechamento** — *Field intelligence por classe de jogador* · `Grátis pra começar` · Sem cartão · aurapoker.com |

**18,2s** · 9:16 1080×1920 · sem áudio (100% legível mudo) · selo `500M+ mãos auditadas · 7 salas`
no rodapé de **todas** as cenas · 18+ em todo quadro · safe zones conferidas com guias antes do encode.

## ⚠️ O print oficial não chegou — painel recriado como mockup
O brief prevê isso ("se precisar recriar como mockup, fidelidade total à UI"). O painel é
`instagram/templates/mockup-cbet-classes.html` → `shots/mockup-cbet-classes.png`, renderizado a 2×.

A gramática foi copiada da tela real (`aura-total2.png` / `postflop-ref.png`):
cabeçalho de coluna com título âmbar e borda lateral · linha da ação ativa em painel
marrom-avermelhado com chevron, nome em bold, barra âmbar sobre trilho slate, % à direita e
`N hands` abaixo · rail de **Active Context** em âmbar.

**Nada foi inventado.** Em particular: a UI real **não calcula gap** entre colunas de breakdown,
então o **7,6 pp não aparece dentro do painel** — ele vive na nossa data-viz da cena 1. Mantém a
divisão de sempre: *vetor = nossa data-viz · mockup/print = o produto*.

**Labels em inglês** porque a UI do produto é em inglês (é o que os prints reais mostram). Efeito
colateral bom: **o mesmo asset serve aos reels PT e EN**, sem versão traduzida.

> Quando o print oficial chegar, é só trocar `src` na cena `dc-s3` e re-encodar.

## Correção de template feita aqui
No primeiro render as duas porcentagens do gancho saíram **cortadas** — o corpo de 112px do bloco
`vs` tinha sido dimensionado para strings curtas ("50%") e "85,2%" (5 caracteres) vazava do painel.
O `elVs` passou a **ajustar o corpo ao comprimento** do valor (112 / 96 / 82 / 70px), o que resolve
a classe do problema e não só esta cena.

## Compliance conferido
Todo número com amostra na tela · "500M+ mãos" (nunca bilhões) · field/MDF/RFI sem traduzir ·
zero promessa de lucro/winrate · sem "vs GTO"/overlay · sem tom guru · sem dinheiro/fichas ·
grátis = **começar** (preview), nunca "completo grátis" · descrição do comportamento do field,
sem inferência de exploit.

## Versão EN — entregue
`disc03-classes-cbet-en.mp4` (18,20s, idêntico ao PT ao centésimo) + `-en-capa.png`.
Cenas `dc-s1-en`…`dc-cta-en` no deck; PT intocada (diff puramente aditivo).

Decisões de tradução:
- decimais com **ponto** (85.2% · 77.6% · 7.6 pp) · `n = 2.4M` / `n = 804k`
- jargão preservado: **Flop CBet IP · SRP · EP vs BB · cbets in position · BB**
- `classe de jogador` → **player type** (é o rótulo do próprio produto, `BREAKDOWN · PLAYER TYPE`)
- `Reg Aggro` / `Reg Tight` não se traduzem — são rótulos da UI
- `Grátis pra começar` → **Free to start** · `Sem cartão` → **No card**
- **field**, nunca "pool"

**Cena 4 reescrita na EN.** A tradução literal ("Do you defend the same against both?") tem 22
caracteres na primeira linha e quebrava no tier de 76px, deixando um **"SAME" órfão** numa terceira
linha — o PT é um duas-linhas limpo. Em vez de reduzir a fonte (perderia o impacto da pergunta),
reescrevi para **"Do you defend / both the same?"**: mesmo sentido, mesma ênfase no *both*, duas
linhas equilibradas.

**O mockup não tem versão EN e não precisa** — a UI do produto já é em inglês, então
`shots/mockup-cbet-classes.png` serve aos dois reels.

## Como regerar
```
node instagram/build-disc03.mjs            # PT — renderiza + encoda MP4 + capa
node instagram/build-disc03.mjs --en       # EN
node instagram/build-disc03.mjs --guides   # só renderiza, com zonas seguras
```
Cenas: `deck.js` (`dc-s1`…`dc-cta` e `dc-s1-en`…`dc-cta-en`).
