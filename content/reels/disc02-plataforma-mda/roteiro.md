# disc02-plataforma-mda · Reel de apresentação da plataforma (PT)

**Campanha:** AURA-DISC02 (apresentação) · **`utm_content`:** `disc02-plataforma-mda`
**Substitui:** o criativo "Não é solver. Não é tracker." · **Objetivo do clique:** "quero ver esse produto"
**Entrega:** `content/paid/AURA-DISC02/disc02-plataforma-mda.mp4` (26,2s) + `-capa.png` (1080×1920)

## Cenas (corte seco; tempo = máx(2,5s ; palavras÷4+1s), errando pro lento)

| # | dur | Conteúdo |
|---|---|---|
| 1 | 3,2s | **GANCHO/CAPA** — logo completa · eyebrow `MTT` · **"Você realmente sabe com quem está jogando?"** · abaixo: *A única plataforma de **Field Intelligence (MDA)** do mundo. Stats da população em segundos.* · UI real escurecida atrás · 18+ |
| 2 | 4,6s | **Preflop** — tela real · *"**% RFI, % 3-bet, % 4-bet** e dezenas de outras stats — por **posição, stack e tipo de vilão**."* |
| 3 | 4,0s | **Postflop** — tela real · *"Defesa do field vs MDF — por **street, size e textura de board**."* |
| 4 | 3,4s | **Node-by-Node** — mockup da spec do PO (PT) · *"Navegue a árvore inteira."* |
| 5 | 3,8s | **Filtros** — painel real (6 estágios nomeados + faixas de buy-in) · `20+ filtros empilháveis` · *"Do Early Game à mesa final — e por faixa de buy-in."* |
| 6 | 4,2s | **Grade dos 3 módulos** — **"Você monta o cenário que quer analisar."** · *Grátis pra começar. Sem cartão.* · Preflop *(por posição, stack e vilão)* · Postflop *(por street, size e textura)* · Node-by-Node *(a árvore de decisão inteira)* |
| 7 | 3,0s | **CTA** — `Conheça a plataforma` · 500M+ mãos auditadas · 7 salas · aurapoker.com |

**26,2s** · 9:16 1080×1920 · sem áudio (100% legível mudo) · selo `500M+ mãos auditadas · 7 salas`
no rodapé de todas as cenas · 18+ em todo quadro · safe zones conferidas com guias antes do encode.

---

## v3 (PO, 10/08) — copy revisada
- **Gancho ganhou conceituação e virou pergunta.** Abre com *"Você realmente sabe com quem está
  jogando?"* e o claim MDA responde logo abaixo, com *"Stats da população em segundos."*
  Duração 2,0 → **3,2s** (o PO reportou frame 1 rápido demais; 3,2s também realinha com o playbook,
  que pede 3–4s no gancho — o desvio registrado na v2 deixa de existir).
- **Preflop:** stats com o sinal de porcentagem na frente, e *"e dezenas de outras stats"*. O PO
  optou por **não fixar número** ("30+") — evita claim de contagem que o gabarito não documenta.
- **Node-by-Node:** ficou só *"Navegue a árvore inteira."*
- **Removida toda referência a tamanho de amostra com a letra `n` nos TEXTOS** (linha da cena 4 e
  célula da grade). O `n=` **continua visível dentro do mockup** — é a UI do produto e veio da spec
  do próprio PO; decisão dele em 10/08.
- **"Um recorte seu" e "você monta o recorte" eliminados.** A frase aprovada — *"Você monta o
  cenário que quer analisar"* — fica **só na cena 6**. A cena 5 passou a descrever o painel
  (*"Do Early Game à mesa final — e por faixa de buy-in"*), senão as duas cenas seguidas diriam a
  mesma coisa. Vira uma sequência melhor: cena 5 é o **mecanismo**, cena 6 é a **conclusão**.
- Total 25,2 → **26,2s**.

## v2 (PO, 28/07) — Hotspot fora, eixo vira FILTRO/FATIA
- **Hotspot removido.** Ficam 3 módulos: Preflop, Postflop e Node-by-Node.
- Cada cena de módulo nomeia por quais dimensões ele **desagrega**, e entra uma cena dedicada ao
  painel de filtros real.
- Grade final de 4 → 3 módulos, em coluna única (2+1 ficava desbalanceado no 9:16).

## ⚠️ Claim do gancho — decisão do PO
**"A única plataforma de Field Intelligence (MDA) do mundo"** reativa a versão **(b)** que a matriz
de descoberta havia descartado (§2: risco de reprova da Meta por superlativo não-substanciado,
exposição a report de concorrente, público técnico cético). O doc condiciona rodar (b) à
**verificação de mercado do PO** — de que não existe ferramenta pública de dado populacional de MTT
que invalide o claim. Registrado; a fábrica executou conforme pedido.

Na v3 o claim deixou de ser a manchete e passou a ser a **resposta** da pergunta de abertura, o que
reduz a exposição: quem lê encontra primeiro a tensão, não a afirmação.

## Assets usados
- **Preflop:** `shots/crop-preflop-table.png` (real, auta-total)
- **Postflop:** `shots/postflop-ref.png` (real)
- **Node-by-Node:** `shots/mockup-node-by-node.png` (mockup da spec do PO, PT, números reais)
- **Filtros:** `shots/crop-filters-rail.png` (painel real)
- Cena 6: grade tipográfica (builder `grid` do `paid-scene.html`, modo `cols:1`)

> Saiu na v2: o crop do Hotspot (`mockup-hotspot-cards.png`) e o passo que o gerava no build.
> O asset fica no repo caso o módulo volte a um criativo futuro.

## Compliance conferido
"500M+ mãos" (nunca bilhões) · field intelligence/MDA sem traduzir · jargão EN (RFI, MDF, field,
size, street) · zero promessa de lucro/winrate · sem "vs GTO"/overlay · sem tom guru · sem
dinheiro/fichas · grátis = **começar** (preview), nunca "completo grátis" · Node-by-Node descrito
como navegação da árvore, sem promessa de solver.

## Como regerar
```
node instagram/build-disc02.mjs            # renderiza + encoda MP4 + capa
node instagram/build-disc02.mjs --guides   # só renderiza, com zonas seguras
```
Cenas: `deck.js` (`dm-s1`…`dm-s6`, `dm-cta`).
