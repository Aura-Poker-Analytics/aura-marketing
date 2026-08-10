# disc02-plataforma-mda · Reel de apresentação da plataforma (PT)

**Campanha:** AURA-DISC02 (apresentação) · **`utm_content`:** `disc02-plataforma-mda`
**Substitui:** o criativo "Não é solver. Não é tracker." · **Objetivo do clique:** "quero ver esse produto"
**Entrega:** `content/paid/AURA-DISC02/disc02-plataforma-mda.mp4` (25,2s) + `-capa.png` (1080×1920)

## v2 (PO, 28/07) — Hotspot fora, eixo vira FILTRO/FATIA
- **Hotspot removido.** Ficam **3 módulos**: Preflop, Postflop e Node-by-Node.
- O eixo da mensagem passa a ser **o recorte que o usuário monta**: cada cena de módulo nomeia
  por quais dimensões ele **desagrega**, e entra uma **cena dedicada ao painel de filtros real**.
- Grade final passa de 4 para **3 módulos**, em coluna única (2+1 ficava desbalanceado no 9:16),
  e cada linha carrega a desagregação daquele módulo.
- Duração 23,4s → **25,2s** (menos uma cena, mas as que ficaram têm mais texto pra ler).

## ⚠️ Claim do gancho — decisão do PO
**"A única plataforma de Field Intelligence (MDA) do mundo"** reativa a versão **(b)** que a matriz
de descoberta havia descartado (§2: risco de reprova da Meta por superlativo não-substanciado,
exposição a report de concorrente, público técnico cético). O doc condiciona rodar (b) à
**verificação de mercado do PO** — de que não existe ferramenta pública de dado populacional de MTT
que invalide o claim. Registrado; a fábrica executou conforme pedido.

## Cenas (corte seco; tempo = máx(2,5s ; palavras÷4+1s), errando pro lento)

| # | dur | Conteúdo |
|---|---|---|
| 1 | 2,0s | **GANCHO/CAPA** — logo completa · eyebrow `MTT` · **"A única plataforma de Field Intelligence (MDA) do mundo"** · UI real escurecida atrás · 18+ |
| 2 | 4,0s | **Preflop** — tela real · *"RFI, 3-bet, 4-bet, steal — desagregado por **posição, stack e tipo de vilão**."* |
| 3 | 4,0s | **Postflop** — tela real · *"Defesa do field vs MDF — fatiada por **street, size e textura de board**."* |
| 4 | 4,2s | **Node-by-Node** — mockup da spec do PO (PT) · *"Navegue a árvore inteira — nó por nó, com **n** em cada um."* |
| 5 | 3,8s | **Filtros** — painel real (6 estágios nomeados + faixas de buy-in) · `20+ filtros empilháveis` · *"Estágio, buy-in, tipo de torneio — **você monta o recorte**."* |
| 6 | 4,2s | **Grade dos 3 módulos** — "Três módulos. Um recorte seu." · cada linha com sua desagregação · *"Grátis pra começar. Sem cartão."* |
| 7 | 3,0s | **CTA** — `Conheça a plataforma` · 500M+ mãos auditadas · 7 salas · aurapoker.com |

**25,2s** · 9:16 1080×1920 · sem áudio (100% legível mudo) · selo `500M+ mãos auditadas · 7 salas`
no rodapé de todas as cenas · 18+ em todo quadro · safe zones conferidas com guias antes do encode.

### Desvio registrado vs playbook
O playbook pede gancho de 3–4s; o brief do DISC02 fixa **0–2s** (o frame também vira capa estática).
Prevaleceu o brief — o gancho é headline única, sem segunda linha pra ler.

## Assets usados
- **Preflop:** `shots/crop-preflop-table.png` (real, auta-total)
- **Postflop:** `shots/postflop-ref.png` (real)
- **Node-by-Node:** `shots/mockup-node-by-node.png` (mockup da spec do PO, PT, números reais)
- **Filtros:** `shots/crop-filters-rail.png` (painel real)
- Cena 6: grade tipográfica (builder `grid` do `paid-scene.html`, modo `cols:1`)

> Sai da v1: o crop do Hotspot (`mockup-hotspot-cards.png`) e o passo que o gerava no build.
> O asset fica no repo caso o módulo volte a um criativo futuro.

## Compliance conferido
"500M+ mãos" (nunca bilhões) · field intelligence/MDA sem traduzir · jargão EN (RFI, MDF, field,
size, street) · zero promessa de lucro/winrate · sem "vs GTO"/overlay · sem tom guru · sem
dinheiro/fichas · grátis = **começar** (preview), nunca "completo grátis" · Node-by-Node descrito
como navegação com tamanho de amostra, sem promessa de solver.

## Como regerar
```
node instagram/build-disc02.mjs            # renderiza + encoda MP4 + capa
node instagram/build-disc02.mjs --guides   # só renderiza, com zonas seguras
```
Cenas: `deck.js` (`dm-s1`…`dm-s6`, `dm-cta`).
