# AURA-PAID01 — 3 criativos de vídeo (anúncio, não post orgânico)

**Entregue por:** thread Fábrica de Posts · **Para:** thread Mídia Paga
**Brief:** [campanha-1-plano-revisado.md §3](../../../docs/02-paid/campanha-1-plano-revisado.md)
**Status:** ✅ **v2 (revisão do Rafael) — prontos para subir.** **Nenhum anúncio foi criado, subido ou ativado por agente.**

---

## 🔄 O que mudou na v2

Revisão apontou 3 problemas de execução visual pra **tráfego frio** (gente que nunca ouviu falar da Aura).

### 1. Transições rápidas demais → **17,9s ⇒ 26,0s**, tempo proporcional à densidade
Era 6 cenas × 3,4s fixos. Em tráfego frio ninguém volta pra reler: se não deu tempo, já scrollou.
Agora a duração é **por cena**, proporcional ao que precisa ser lido:

| cena | v1 | v2 | por quê |
|---|---|---|---|
| 1 · gancho | 3,4s | **4,0s** | número + kicker + sub |
| 2 · dado | 3,4s | **5,0s** | comparação com 2 painéis |
| 3 · tela real | 3,4s | **5,4s** | print denso, mais coisa pra varrer |
| 4 · dado | 3,4s | **5,0s** | 3 linhas de número |
| 5 · dado | 3,4s | **5,0s** | idem |
| 6 · CTA | 3,4s | **3,6s** | curto de propósito |

Crossfade de 0,5s → **0,4s** (mais suave em relação ao tempo de cena, não mais seco).

### 2. Primeiro frame pouco chamativo → **produto no frame 1 + movimento imediato**
- O gancho agora tem **print real da plataforma full-bleed no fundo** (escurecido, com vinheta de foco
  atrás do texto). O cara vê tabela, números e barras de overfold **antes de ler qualquer palavra**.
- **Movimento nos primeiros frames:** o push-in da cena 1 usa easing `sqrt` em vez de linear. Anda
  ~2,5% em 0,3s (linear andaria 0,2% e leria como frame parado = scroll).
  Medido no MP4 encodado: **PSNR 19,7 dB entre t=0 e t=0,10** — diferença grande, movimento real.
- Como o thumb é o frame 1, **a capa do anúncio também passou a ter produto**.

### 3. Faltavam prints da plataforma → **crops nativos do print real**
A preocupação com borrão era legítima, então a solução não foi voltar a espremer a tela inteira:
**crops apertados em resolução nativa**, exibidos em tamanho próximo do original (upscale 1,0–1,3x).

| crop | origem | px | usado em |
|---|---|---|---|
| `crop-preflop-table.png` | auta-total.png | 700×560 | V1 fundo do gancho + cena 3 |
| `crop-filters-rail.png` | auta-total.png | 336×382 | V1 cena 5 |
| `crop-exploit-cards.png` | aura-total2.png | 500×360 | V2 fundo do gancho + cena 3 |
| `crop-sizedist.png` | aura-total2.png | 520×320 | V3 fundo do gancho |
| `crop-disconnected-col.png` | aura-total2.png | 514×812 | V3 cena 4 |

Os prints emoldurados ganharam **chrome de janela** (bolinhas + título) — lê como *software*, não como gráfico.
E o `crop-disconnected-col` é a **prova literal** dos números que o V3 afirma: mostra "Disconnected",
XR Flop CBet 11,5%, 3,1M mãos e os overfolds 11,0 / 11,2 / 9,9 / 8,2.

**O vetor não foi abandonado** — continua nas visualizações *derivadas* (comparações, barras, stats),
que não existem como tela no produto. A divisão virou: **vetor = nossa data-viz · print = o produto**.

---

## Arquivos

| Arquivo | Duração | Tamanho | Thumb |
|---|---|---|---|
| `paid01-v1-preflop.mp4` | 26,0s | 5,8 MB | `paid01-v1-preflop-thumb.png` |
| `paid01-v2-field.mp4` | 26,0s | 4,9 MB | `paid01-v2-field-thumb.png` |
| `paid01-v3-leak.mp4` | 26,0s | 5,3 MB | `paid01-v3-leak-thumb.png` |

Versões EN em [`en/`](en/) (mesmas mudanças, mesmos tempos). Ver [`en/README.md`](en/README.md).

Todos **1080×1920 (9:16) · 30fps · H.264 · faststart · SEM ÁUDIO**.
Nomes conferem com o brief — eles viram `utm_content`, **não renomear**.
Thumbnail = 1º quadro de cada vídeo (o gancho), que é o que o Gerenciador usa como capa.

## Specs conferidas

- ✅ 9:16 · 1080×1920 · **26,0s** (dentro da faixa 15–30s; teto confortável de anúncio)
- ✅ **Gancho no 1º quadro** — não nos 2 primeiros segundos: no primeiro frame, já com produto atrás.
- ✅ **Zonas seguras** — nada crítico nos 269px de cima (14%) nem nos 384px de baixo (20%).
  Renderizado e conferido com as guias ligadas (`?guides=1` no template) **antes** de encodar.
  O template agora tem trava de altura (`min-height:0` + `max-height:100%`): print alto demais
  encolhe em vez de vazar pra zona segura.
- ✅ **Legenda queimada** — barra de legenda fixa no rodapé da zona segura, em toda cena.
- ✅ **100% PT-BR, inclusive a arte** (inverte a convenção "arte EN" do orgânico — decisão da Mídia Paga).
- ✅ **Produto real em tela** — crops nativos do print + chrome de janela; vetor só nas viz derivadas.
- ✅ Sem "link na bio" em nenhum roteiro. CTA aponta pro site (botão do anúncio).
- ✅ Verificado **nos MP4 encodados** (não só no render do HTML): duração real, frame 0, movimento
  inicial, cena de print e CTA final.

## Roteiros (cena a cena)

Legenda: 🖼️ = print real da plataforma · 📊 = data-viz vetorial nossa

**`paid01-v1-preflop`** — réplica do vencedor histórico: jargão preflop puro como filtro de público.
1. 🖼️ "RFI de **50%** no BTN" · É o que o reg agressivo do field faz. *(tabela real ao fundo)*
2. 📊 Reg agressivo 50% **vs** Reg tight 35% (RFI no BTN) — 15 pts de diferença
3. 🖼️ **A tela real** — tabela Reg Aggro em janela, "produto real, não mockup"
4. 📊 Fold vs RFI 73% · 3-Bet 10% · Steal Attempt 42%
5. 🖼️ **Painel de filtros real** — estágio (early → mesa final) e buy-in
6. CTA

**`paid01-v2-field`** — dados reais vs. teoria (ângulo desocupado na Ads Library).
1. 🖼️ "A matemática diz **64,5%**" · O field defende 57,7%. *(exploit cards reais ao fundo)*
2. 📊 C-bet de 55% do pote: barra da defesa real contra a marca do MDF (overfold 6,8 pts)
3. 🖼️ **A tela real** — 33%, 42%, 55% do pote, os 6 sizings em janela
4. 📊 10,6M mãos nesse spot · 500M+ auditadas · 7 salas
5. "Solver mostra o equilíbrio" — a Aura mostra o que o field realmente faz
6. CTA

**`paid01-v3-leak`** — leak/variância, tom direto.
1. 🖼️ "Não é **azar**" · É padrão. E padrão dá pra medir. *(distribuição de sizes real ao fundo)*
2. 📊 Board conectado 6,9% **vs** desconexo 9,9% (overfold vs MDF, c-bet 55%)
3. 📊 No overpot: 2,9% **vs** 8,2% (+5,3 pts)
4. 🖼️ **A tela real filtrada por textura** — coluna "Disconnected" inteira: 11,5%, 3,1M mãos
   e os overfolds 11,0 / 11,2 / 9,9 / 8,2. É a prova literal do que as cenas 2 e 3 afirmam.
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
node instagram/build-paid.mjs            # renderiza as 18 cenas + encoda os 3 MP4 (PT)
node instagram/build-paid.mjs --guides   # só renderiza, com as zonas seguras desenhadas
node instagram/build-paid-en.mjs         # idem para as versões EN
```
Se o `ffmpeg-static` não estiver instalado no repo, aponte o binário:
`FFMPEG_PATH=/caminho/ffmpeg.exe node instagram/build-paid.mjs`

- Template: `instagram/templates/paid-scene.html`
- Cenas: `instagram/templates/deck.js` (`p1-s*`, `p2-s*`, `p3-s*`, `p-cta` · sufixo `-en` para EN)
- Ritmo: constante `DURS` no topo do build (duração por cena) e `XF` (crossfade)
- Crops: `instagram/crops.mjs` regenera os `shots/crop-*.png` a partir dos prints originais

⚠️ **Sempre rode com `--guides` e olhe os frames antes de encodar.** Foi assim que apareceram duas
cenas estourando a zona segura nesta v2 (o kicker do V1-s5 subiu pra faixa de cima e o print ficou
cortado embaixo) — no vídeo pronto isso passaria batido.
