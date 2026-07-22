# AURA-PAID01 — 3 criativos de vídeo (anúncio, não post orgânico)

**Entregue por:** thread Fábrica de Posts · **Para:** thread Mídia Paga
**Brief:** [campanha-1-plano-revisado.md §3](../../../docs/02-paid/campanha-1-plano-revisado.md)
**Status:** prontos para subir. **Nenhum anúncio foi criado, subido ou ativado por agente.**

## Arquivos

| Arquivo | Duração | Tamanho | Thumb |
|---|---|---|---|
| `paid01-v1-preflop.mp4` | 17,9s | 3,8 MB | `paid01-v1-preflop-thumb.png` |
| `paid01-v2-field.mp4` | 17,9s | 3,6 MB | `paid01-v2-field-thumb.png` |
| `paid01-v3-leak.mp4` | 17,9s | 3,9 MB | `paid01-v3-leak-thumb.png` |

Todos **1080×1920 (9:16) · 30fps · H.264 · faststart · SEM ÁUDIO**.
Nomes conferem com o brief — eles viram `utm_content`, **não renomear**.
Thumbnail = 1º quadro de cada vídeo (o gancho), que é o que o Gerenciador usa como capa.

## Specs conferidas

- ✅ 9:16 · 1080×1920 · 17,9s (dentro da faixa 15–30s)
- ✅ **Gancho no 1º quadro** — não nos 2 primeiros segundos: no primeiro frame. O número/jargão já está em tela em t=0.
- ✅ **Zonas seguras** — nada crítico nos 269px de cima (14%) nem nos 384px de baixo (20%).
  Renderizado e conferido com as guias ligadas (`?guides=1` no template).
- ✅ **Legenda queimada** — barra de legenda fixa no rodapé da zona segura, em toda cena.
- ✅ **100% PT-BR, inclusive a arte** (inverte a convenção "arte EN" do orgânico — decisão da Mídia Paga).
- ✅ **UI real do produto** — as telas Preflop e Postflop aparecem recriadas em vetor HTML/CSS
  (mesmos números das telas reais). Vetor em vez de print colado porque print reescalado fica borrado.
- ✅ Sem "link na bio" em nenhum roteiro. CTA aponta pro site (botão do anúncio).

## Roteiros (cena a cena)

**`paid01-v1-preflop`** — réplica do vencedor histórico: jargão preflop puro como filtro de público.
1. "RFI de **50%** no BTN" · É o que o reg agressivo do field faz. Medido, não estimado.
2. Reg agressivo 50% **vs** Reg tight 35% (RFI no BTN) — 15 pts de diferença
3. A tela real: tabela Reg Aggro por posição (CO/BTN/SB)
4. Fold vs RFI 73% · 3-Bet 10% · Steal Attempt 42%
5. Recorta por posição, stack, estágio e tipo de vilão
6. CTA

**`paid01-v2-field`** — dados reais vs. teoria (ângulo desocupado na Ads Library).
1. "A matemática diz **64,5%**" · O field defende 57,7%.
2. C-bet de 55% do pote: barra da defesa real contra a marca do MDF (overfold 6,8 pts)
3. A tela real: 33%, 42%, 55% do pote — overfold em todos
4. 10,6M mãos nesse spot · 500M+ auditadas · 7 salas
5. "Solver mostra o equilíbrio" — a Aura mostra o que o field realmente faz
6. CTA

**`paid01-v3-leak`** — leak/variância, tom direto.
1. "Não é **azar**" · É padrão. E padrão dá pra medir.
2. Board conectado 6,9% **vs** desconexo 9,9% (overfold vs MDF, c-bet 55%)
3. No overpot: 2,9% **vs** 8,2% (+5,3 pts)
4. A tela real filtrada por textura de board (3,1M mãos, board desconexo)
5. "O leak é do **field**" — a Aura mostra onde ele está
6. CTA

## Procedência dos números — todos reais, nenhum ilustrativo

| Fonte | Contexto na tela | Usado em |
|---|---|---|
| `assets/screenshots/auta-total.png` | Preflop · breakdown **Player Type** · All Tournaments · Any Stage · Any Buy-in · Last 2 Years | V1 |
| `assets/screenshots/aura-total2.png` | Postflop · breakdown **Flop Connectedness** · SRP · RFI: CO · Caller: BB · Last 2 Years | V2, V3 |

Cada número foi lido do print, não estimado. Se a Mídia Paga precisar defender qualquer
frame, o print está no repo.

## ⚠️ Dois desvios do brief — leia antes de subir

**1. O gancho de V1 mudou.** O brief pedia:
> "RFI do field no BTN: 44%. O solver diz 48%. Essa diferença é EV que o field te entrega."

Não dá pra usar como está, por três motivos:
- **44% e 48% não existem em lugar nenhum.** O RFI real de BTN nas nossas telas é 50% (reg agressivo) / 35% (reg tight).
- **"O solver diz 48%" seria um número inventado atribuído a um solver que não rodamos.** A Aura não é solver e não faz overlay solver×pool — [product-truth-aura.md §0 e §9](../../../docs/00-strategy/product-truth-aura.md) proíbem explicitamente.
- **"Essa diferença é EV"** é claim de EV/resultado — proibido no gabarito e é exatamente o tipo de coisa que a Meta reprova.

O que ficou no lugar preserva o mecanismo que fez o criativo vencer (**jargão preflop denso como
filtro de público**) e ainda ganha um contraste real: **reg agressivo 50% vs reg tight 35% no
mesmo spot**, que é o produto fazendo o que ele de fato faz.

Em V2 a comparação "teoria vs real" ficou contra o **MDF** — que é identidade matemática, não output
de solver. Por isso a copy diz "a matemática diz", nunca "o solver diz". A frase de posicionamento
"solver mostra o equilíbrio" continua (é categoria, não claim de feature) — já aprovada no orgânico.

**2. V3 não fala "seu redline".** O brief sugeria "Seu redline não é azar". Redline é conceito de
tracker e a Aura não vê as suas mãos — a peça prometeria uma análise pessoal que o produto não
entrega. Ficou "Não é azar. É padrão", e a cena 5 fecha explicitando **"o leak é do field"**, que é
a correção que você já tinha feito no orgânico.

## Guard-rails conferidos

- ✅ Nada de "grátis completo" — CTA diz **"preview de cada módulo, sem cartão"**
- ✅ Zero promessa de winrate/lucro/EV
- ✅ Sem dinheiro, luxo, dado de cliente ou concorrente nominal
- ✅ 18+ visível em todos os quadros
- ✅ "500M+ mãos" e "7 salas" — nunca "bilhões", nunca proporção por sala

## Áudio

Saem **sem trilha**, de propósito. Em anúncio a trilha entra no Gerenciador (biblioteca licenciada
para uso comercial) ou vem do editor — não fica queimada no arquivo, senão não dá pra trocar sem
reencodar e sem perder o histórico de aprendizado do anúncio. Os vídeos são legíveis mudos: todo o
conteúdo está em texto na tela.

## Como regerar

```
node instagram/build-paid.mjs            # renderiza as 18 cenas + encoda os 3 MP4
node instagram/build-paid.mjs --guides   # só renderiza, com as zonas seguras desenhadas
```
Template: `instagram/templates/paid-scene.html` · conteúdo das cenas: `instagram/templates/deck.js`
(chaves `p1-s*`, `p2-s*`, `p3-s*`, `p-cta`).
