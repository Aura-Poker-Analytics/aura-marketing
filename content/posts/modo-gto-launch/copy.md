# Modo GTO: copy de lançamento

Status: rascunho com números fechados; não publicado. Sem commit. Entra no ar em 08/10/2026.
@aurapokeranalytics: a confirmar pelo Rafael. URLs com UTM prontas na tabela abaixo.
Fonte única dos números: `aura-main/_ops/golive-gto-2026-10-04/numeros-verificados.md` (08/10, lido em produção). Os números usados estão mapeados em "Números usados" no fim. **Nenhum marcador `[[N..]]` restou no pacote.**
Peças deste pacote: Discord (também em `discord.md`), Instagram (feed, story, story da capa em PT, carrossel só em EN), landing e e-mail (em `email.md`).

> **Regra de texto das artes (Rafael, 08/10): "muita informação, muito texto; não pode ter tanto texto em nenhum post".** Cada arte tem no máximo UM título curto (~6 palavras) e, se precisar, UMA linha de apoio (~10 palavras). A imagem fala: barras field × GTO lado a lado, com os números. O detalhe vai para a legenda. Em toda arte só ficam o `@aurapokeranalytics` e o `18+`, pequenos. O link é o sticker/link na bio, não texto de arte. A frase do plano Grátis fica na legenda e no e-mail, não nas artes. Nas artes não entram contagem de mãos nem "amostra"; nas legendas e no e-mail também ficam de fora.

## Origem das capturas
As telas dos slides 3 e 4 e do e-mail vêm do front no SHA de produção (aura-novofront `429c093`, build com o Modo GTO ligado) servido localmente e lendo a API local `:7060` com os snapshots do go-live (flop e turn/river 20261008, reação a raise 20261006, pré-flop 20261007), por conta de teste local (sem login em produção). Capturadas em 08/10 com Playwright, em EN e PT. A imagem do e-mail é o recorte do card de 33% do painel de Fold por tamanho de Flop CBet; a célula do CO no slide 4 tem um contorno âmbar desenhado só para destaque. Na tela, o card do 33% mostra +5,6 pp (distância ao topo da faixa).

## Pendências reais
1. **Conferência das capturas no teste logado.** As capturas (slides 3 e 4, recorte do e-mail) vêm do front no SHA de produção + API local com os snapshots do go-live (ver "Origem das capturas"). O teste logado do Rafael (passo 6 do roteiro de go-live) deve conferir, em `www.aura.poker`, os MESMOS valores do exemplo (46,0% / 38,8% / faixa 37,1–40,4% e RFI do CO 31,6% / 37,0%) antes de qualquer post ou envio. Nenhuma peça chama as capturas de "print de produção". A captura do slide 3 não mostra a reação a raise de BB 3-bet vs CO, SB 3-bet vs BTN ou BTN 3-bet vs CO a 40/60bb, que ainda não tem GTO.
2. **Ordem de publicação.** Só postar depois do teste logado do Rafael (passo 6 do roteiro de go-live).
3. **Bug do front a avisar.** O app em PT mistura formatos no mesmo card: "46.0%" (ponto) e "38,8%" (vírgula). Nas peças em PT escrevemos sempre com vírgula; o app não.

## Decisões registradas (revisão de marca, 08/10)
- **Capa com duas linhas (decisão consciente).** A capa (story PT e slide 1 do carrossel) tem o apoio ("Novo: Modo GTO" / "New: GTO Mode") e uma micro-legenda do spot ("CO × BB · K-high two-tone · c-bet de 33%" / "CO × BB · K-high two-tone · 33% c-bet"). É a única exceção à regra de uma linha de apoio.
- **Slide 4 mostra os números arredondados da tela.** A captura traz Field 32% / GTO 37% / −5. A fonte tem 31,6 / 37,0 / −5,4; as legendas e a landing usam os valores da fonte.
- **"Rodapé de amostra".** O brand-kit pede rodapé de amostra em post com número. A instrução do Rafael de 08/10 (sem contagem de mãos nem amostra nas peças) o substitui; nenhuma peça traz amostra.
- **Slide 3.** O apoio é "SRP and 3-bet, flop and turn. Raise response on SRP flop." A reação a raise vale só para o flop do SRP; os 3-bets (CO×BB e os demais citados acima) a 40/60bb não têm.

## Fatos de produto aplicados (referência, já resolvidos)
- **Reação a raise:** dita só como "no flop do SRP". Sem generalizar.
- **Cobertura, sem absolutos:** nenhuma peça diz "cada número" nem "cada célula". PT: "onde há referência" e "nas células cobertas"; EN: "where a reference exists" e "in the covered cells". A fonte só garante 30 situações no flop e 225 decisões de pré-flop.
- **Pré-flop:** "o GTO e o desvio nas células cobertas, inclusive o RFI de CO e BTN a 40bb" (pré-flop `20261007`).
- **Filtro do exemplo nas peças:** "torneios Regular" (EN "Regular tournaments") e "últimos 2 anos" (EN "last 2 years"), sem vanilla nem chipEV.
- **Plano Grátis (lido do código):** conta Grátis (e Individual) não vê número GTO nem faixa; segue com o field e a comparação com o MDF, e o GTO aparece como cadeado. Frase única, PT: "O Modo GTO é um plano pago. A conta grátis segue com o field e a comparação com o MDF; o número GTO e a faixa são do plano Modo GTO." EN: "GTO Mode is a paid plan. The free account keeps the field and the MDF comparison; the GTO number and range are on the GTO Mode plan." Vive na legenda, no Discord, na landing e no e-mail. CTAs: "Conhecer o Modo GTO" / "See GTO Mode"; nenhum diz "grátis". Sem "prévia", sem "borrado", sem preço, sem "Beta".
- **Escopo da referência:** a ressalva de torneios vanilla fica só na Metodologia do app (pedido do Rafael em 06/10). Nenhuma peça a repete; "Regular" aparece só como filtro do spot.
- **"Spot"** é a situação ou a decisão, nunca contagem de linhas.
- **Formato dos números:** vírgula em PT (46,0%), ponto em EN (46.0%).
- **Nome em inglês:** "GTO Mode".
- **Carrossel só em EN;** a capa tem story PT-BR 1080x1920. Não há story EN da capa.

## O exemplo (fonte: `numeros-verificados.md`, exemplo (a))
Filtro da tela: Postflop · SRP · RFI CO, caller BB · stack 30.1–60bb (GTO a 40bb) · torneio Regular (Vanilla) · flop K-high, two-tone, sem par, desconectado · reação do BB ao c-bet de 33%.
- Field folda **46,0%**; GTO folda **38,8%**, faixa **37,1–40,4%**; diferença **+5,6 pp** (a tela mostra a distância ao topo da faixa; contra o centro do GTO são 7,2). Leitura: acima da faixa (o field está acima do topo da faixa).

**Texto final do exemplo, PT:** "CO × BB em pote simples (SRP), 30–60bb (GTO a 40bb), torneios Regular, últimos 2 anos, flop K-high two-tone, sem par, desconectado, contra o c-bet de 33%. O field folda 46,0% contra 38,8% do GTO (faixa 37,1–40,4%): 5,6 pp acima do topo da faixa. Aqui o field folda mais do que o GTO. É um spot, não a média do field. Confira no seu board."

**Final example text, EN:** "CO × BB single-raised pot (SRP), 30–60bb (GTO at 40bb), Regular tournaments, last 2 years, K-high two-tone, unpaired, disconnected flop, facing a 33% c-bet. The field folds 46.0% against GTO's 38.8% (range 37.1–40.4%): 5.6 pp above the top of the range. Here the field folds more than GTO does. This is one spot, not the field average. Check it on your board."

**Exemplo de pré-flop (exemplo (b)):** RFI do CO, torneio Regular, stack 30–50bb (GTO a 40bb). Field abre **31,6%**; GTO abre **37,0%**; diferença **−5,4 pp** (o field abre de menos). PT: "No pré-flop, RFI do CO a 30–50bb (GTO a 40bb), torneios Regular, últimos 2 anos: o field abre 31,6% e o GTO abre 37,0%." EN: "Preflop, CO RFI at 30–50bb (GTO at 40bb), Regular tournaments, last 2 years: the field opens 31.6% and GTO opens 37.0%."

## URLs por peça
Regra: Discord leva ao app (`https://www.aura.poker/`); Instagram e e-mail levam à landing (`https://www.aurapoker.com/`). Parâmetros: `utm_source=<fonte>&utm_medium=<meio>&utm_campaign=modo-gto-launch&utm_content=<peça>`.

| Peça | Idioma | Destino | utm_source | utm_content | URL |
|---|---|---|---|---|---|
| Discord PT | PT | app | discord | discord-pt | https://www.aura.poker/?utm_source=discord&utm_medium=social&utm_campaign=modo-gto-launch&utm_content=discord-pt |
| Discord EN | EN | app | discord | discord-en | https://www.aura.poker/?utm_source=discord&utm_medium=social&utm_campaign=modo-gto-launch&utm_content=discord-en |
| Feed (link na bio) | PT e EN | landing | instagram | feed | https://www.aurapoker.com/?utm_source=instagram&utm_medium=social&utm_campaign=modo-gto-launch&utm_content=feed |
| Story (sticker de link) | PT e EN | landing | instagram | story | https://www.aurapoker.com/?utm_source=instagram&utm_medium=social&utm_campaign=modo-gto-launch&utm_content=story |
| Story da capa do carrossel (sticker de link) | PT | landing | instagram | story-capa-pt | https://www.aurapoker.com/?utm_source=instagram&utm_medium=social&utm_campaign=modo-gto-launch&utm_content=story-capa-pt |
| Carrossel, só EN (link na bio) | EN (legenda PT e EN) | landing | instagram | carrossel-en | https://www.aurapoker.com/?utm_source=instagram&utm_medium=social&utm_campaign=modo-gto-launch&utm_content=carrossel-en |
| Landing (botão de CTA, para o cadastro no app) | PT e EN | app | landing | modo-gto (utm_medium=website) | https://www.aura.poker/Login?tab=signup&utm_source=landing&utm_medium=website&utm_campaign=modo-gto-launch&utm_content=modo-gto |
| E-mail PT | PT | landing | email | pt | https://www.aurapoker.com/?utm_source=email&utm_medium=email&utm_campaign=modo-gto-launch&utm_content=pt |
| E-mail EN | EN | landing | email | en | https://www.aurapoker.com/?utm_source=email&utm_medium=email&utm_campaign=modo-gto-launch&utm_content=en |

Observação: para o botão da landing mantive `utm_source=landing`, como no Field Trends. Ajustar se o Rafael preferir outro valor.

## Rodapé
- **Artes:** só `@aurapokeranalytics · 18+`, pequeno.
- **Legendas, landing e e-mail:** PT "Ferramenta de estudo. 18+." / EN "Study tool. 18+." (na landing, também "A Aura não é site de apostas e não oferece jogo.").

---

# (a) Instagram

## Texto final de cada arte (título + apoio)

Em toda arte: `@aurapokeranalytics · 18+`, pequeno, e mais nada. Nas barras, o % central do GTO no rótulo e a faixa GTO como sombreado, com a faixa escrita pequena.

| Arte | Formato | Idioma | Título | Apoio (uma linha) | O que a imagem mostra |
|---|---|---|---|---|---|
| Feed | 1080x1350 | PT | Mesmo spot, dois números | CO × BB · K-high two-tone · c-bet de 33% | Barras de fold lado a lado: Field 46,0% e GTO 38,8% (faixa 37,1–40,4%) |
| Feed | 1080x1350 | EN | Same spot, two numbers | CO × BB · K-high two-tone · 33% c-bet | Fold bars side by side: Field 46.0% and GTO 38.8% (range 37.1–40.4%) |
| Story | 1080x1920 | PT | O field folda mais que o GTO? | CO × BB · K-high two-tone · c-bet de 33% | Mesmas barras (46,0% e 38,8%); sticker de link "Conhecer o Modo GTO" |
| Story | 1080x1920 | EN | Does the field fold more than GTO? | CO × BB · K-high two-tone · 33% c-bet | Same bars (46.0% and 38.8%); link sticker "See GTO Mode" |
| Story da capa do carrossel | 1080x1920 | PT | Onde o field sai do GTO? | Novo: Modo GTO (+ micro-legenda do spot: CO × BB · K-high two-tone · c-bet de 33%) | Mesmas barras com o gap em âmbar (46,0% e 38,8%); sticker "Conhecer o Modo GTO" |
| Carrossel 1 (capa) | 1080x1350 | EN | Where does the field leave GTO? | New: GTO Mode (+ spot micro-caption: CO × BB · K-high two-tone · 33% c-bet) | Mesma imagem da capa PT (46.0% and 38.8%) |
| Carrossel 2 | 1080x1350 | EN | Same spot, two numbers | (nenhum) | Só as barras e os dois números: Field 46.0%, GTO 38.8% (range 37.1–40.4%) |
| Carrossel 3 | 1080x1350 | EN | Postflop: GTO and range | SRP and 3-bet, flop and turn. Raise response on SRP flop. | Captura do Postflop com o Modo GTO ligado, no spot do exemplo |
| Carrossel 4 | 1080x1350 | EN | Preflop: GTO and deviation | Includes CO and BTN RFI at 40bb. | Captura da grade com a célula do RFI do CO destacada: na tela, Field 32%, GTO 37%, −5 (arredondado; a fonte tem 31,6 / 37,0 / −5,4) |
| Carrossel 5 | 1080x1350 | EN | GTO Mode is a paid plan | (nenhum) | O cadeado "Disponível no Modo GTO" do app |
| Carrossel 6 (CTA) | 1080x1350 | EN | See GTO Mode | Link in bio. | Logo e fundo da marca |

Notas de arte:
- **Cores:** fold em teal `#015A6B`; a distância entre a barra do field e a do GTO em âmbar (o gap). Faixa GTO sombreada em volta da barra do GTO.
- **Slide 4 (carrossel):** o stack da captura é 30–50bb (GTO a 40bb), torneio Regular. O número fica dentro da captura; nenhum texto de arte o repete.
- **Slide 5:** cadeado do app. A frase do plano Grátis fica na legenda.
- **Enquete opcional no story (fora da arte):** "Qual spot você quer ver com o GTO ao lado?" com as opções "SRP" e "3-bet" / "Which spot do you want to see with GTO next to it?" with "SRP" and "3-bet".

## Legendas

### Legenda do feed
PT:
```
O GTO folda 38,8%. O field folda 46,0%. Mesmo spot.

Novo na Aura: Modo GTO. Ao lado do número do field, o número GTO e a faixa GTO, onde há referência.

Exemplo: CO × BB em pote simples (SRP), 30–60bb (GTO a 40bb), torneios Regular, últimos 2 anos, flop K-high two-tone, sem par, desconectado, contra o c-bet de 33%. O field folda 46,0% contra 38,8% do GTO (faixa 37,1–40,4%): 5,6 pp acima do topo da faixa. Aqui o field folda mais do que o GTO. É um spot, não a média do field. Confira no seu board.

Pós-flop: SRP e 3-bet, flop e turn, inclusive a reação a raise no flop do SRP. Pré-flop: o GTO e o desvio nas células cobertas, inclusive o RFI de CO e BTN a 40bb.

O Modo GTO é um plano pago. A conta grátis segue com o field e a comparação com o MDF; o número GTO e a faixa são do plano Modo GTO.

Conhecer o Modo GTO, link na bio. Ferramenta de estudo. 18+.

#poker #pokerMTT #pokerestudo #aurapoker
```
EN:
```
GTO folds 38.8%. The field folds 46.0%. Same spot.

New on Aura: GTO Mode. Next to the field number, the GTO number and the GTO range, where a reference exists.

Example: CO × BB single-raised pot (SRP), 30–60bb (GTO at 40bb), Regular tournaments, last 2 years, K-high two-tone, unpaired, disconnected flop, facing a 33% c-bet. The field folds 46.0% against GTO's 38.8% (range 37.1–40.4%): 5.6 pp above the top of the range. Here the field folds more than GTO does. This is one spot, not the field average. Check it on your board.

Postflop: SRP and 3-bet, flop and turn, including the response to a raise on the SRP flop. Preflop: the GTO and the deviation in the covered cells, including the CO and BTN RFI at 40bb.

GTO Mode is a paid plan. The free account keeps the field and the MDF comparison; the GTO number and range are on the GTO Mode plan.

See GTO Mode, link in bio. Study tool. 18+.

#poker #pokerMTT #pokerestudo #aurapoker
```

### Legenda do carrossel e da capa
PT (usar também com o story da capa, se o Rafael postar legenda):
```
Onde o field sai do GTO?

Novo na Aura: Modo GTO. Ao lado do número do field, o número GTO e a faixa GTO, onde há referência, no pós-flop (SRP e 3-bet, flop e turn, inclusive a reação a raise no flop do SRP) e no pré-flop (o GTO e o desvio nas células cobertas, inclusive o RFI de CO e BTN a 40bb).

Pós-flop: CO × BB em pote simples (SRP), 30–60bb (GTO a 40bb), torneios Regular, últimos 2 anos, flop K-high two-tone, sem par, desconectado, contra o c-bet de 33%. O field folda 46,0% contra 38,8% do GTO (faixa 37,1–40,4%): 5,6 pp acima do topo da faixa. Aqui o field folda mais do que o GTO. É um spot, não a média do field. Confira no seu board.

Pré-flop: RFI do CO a 30–50bb (GTO a 40bb), torneios Regular, últimos 2 anos. O field abre 31,6% e o GTO abre 37,0%.

O Modo GTO é um plano pago. A conta grátis segue com o field e a comparação com o MDF; o número GTO e a faixa são do plano Modo GTO.

Conhecer o Modo GTO, link na bio. Salve para estudar. Ferramenta de estudo. 18+.

#poker #pokerMTT #pokerestudo #aurapoker
```
EN:
```
Where does the field leave GTO?

New on Aura: GTO Mode. Next to the field number, the GTO number and the GTO range, where a reference exists, postflop (SRP and 3-bet, flop and turn, including the response to a raise on the SRP flop) and preflop (the GTO and the deviation in the covered cells, including the CO and BTN RFI at 40bb).

Postflop: CO × BB single-raised pot (SRP), 30–60bb (GTO at 40bb), Regular tournaments, last 2 years, K-high two-tone, unpaired, disconnected flop, facing a 33% c-bet. The field folds 46.0% against GTO's 38.8% (range 37.1–40.4%): 5.6 pp above the top of the range. Here the field folds more than GTO does. This is one spot, not the field average. Check it on your board.

Preflop: CO RFI at 30–50bb (GTO at 40bb), Regular tournaments, last 2 years. The field opens 31.6% and GTO opens 37.0%.

GTO Mode is a paid plan. The free account keeps the field and the MDF comparison; the GTO number and range are on the GTO Mode plan.

See GTO Mode, link in bio. Save it for study. Study tool. 18+.

#poker #pokerMTT #pokerestudo #aurapoker
```

---

# (b) Landing

@aurapokeranalytics: a confirmar pelo Rafael. URL do CTA: ver a linha "Landing" da tabela "URLs por peça".

## Kicker (acima do título, com a pílula de novo)
- PT: Novo na Aura · Modo GTO
- EN: New on Aura · GTO Mode

## Título
- PT: O GTO e o field na mesma tela.
- EN: GTO and the field on the same screen.

## Subtítulo
- PT: Modo GTO: o número GTO e a faixa GTO ao lado do número do field, onde há referência, no pós-flop e no pré-flop. Veja onde o field sai da faixa e estude esse spot.
- EN: GTO Mode: the GTO number and the GTO range next to the field number, where a reference exists, postflop and preflop. See where the field leaves the range and study that spot.

## 3 bullets
PT:
- Pós-flop: SRP e 3-bet, flop e turn, com o número GTO e a faixa GTO ao lado do field, inclusive a reação a raise no flop do SRP.
- Pré-flop: a grade traz o GTO e o desvio nas células cobertas, inclusive o RFI de CO e BTN a 40bb. No RFI do CO a 30–50bb (GTO a 40bb), torneios Regular, últimos 2 anos, o field abre 31,6% e o GTO abre 37,0%.
- Exemplo: CO × BB em pote simples (SRP), 30–60bb (GTO a 40bb), torneios Regular, últimos 2 anos, flop K-high two-tone, sem par, desconectado, contra o c-bet de 33%. O field folda 46,0% contra 38,8% do GTO (faixa 37,1–40,4%): 5,6 pp acima do topo da faixa. Aqui o field folda mais do que o GTO. É um spot, não a média do field. Confira no seu board.

EN:
- Postflop: SRP and 3-bet, flop and turn, with the GTO number and the GTO range next to the field, including the response to a raise on the SRP flop.
- Preflop: the grid carries the GTO and the deviation in the covered cells, including the CO and BTN RFI at 40bb. On the CO RFI at 30–50bb (GTO at 40bb), Regular tournaments, last 2 years, the field opens 31.6% and GTO opens 37.0%.
- Example: CO × BB single-raised pot (SRP), 30–60bb (GTO at 40bb), Regular tournaments, last 2 years, K-high two-tone, unpaired, disconnected flop, facing a 33% c-bet. The field folds 46.0% against GTO's 38.8% (range 37.1–40.4%): 5.6 pp above the top of the range. Here the field folds more than GTO does. This is one spot, not the field average. Check it on your board.

Nota de rodapé da seção (PT): "Um spot, não a média do field. Dados: Aura · 30 situações (10 confrontos de posição a 25, 40 e 60bb) com GTO no flop, mais de 2.300 flops, quase 7 milhões de nós de turn e river e 225 decisões de pré-flop, de 10 a 60bb. Ferramenta de estudo · 18+. A Aura não é site de apostas e não oferece jogo."
Footnote (EN): "One spot, not the field average. Data: Aura · 30 situations (10 position matchups at 25, 40 and 60bb) with GTO on the flop, over 2,300 flops, nearly 7 million turn and river nodes and 225 preflop decisions, from 10 to 60bb. Study tool · 18+. Aura is not a betting site and does not offer gambling."

CTA: PT "Conhecer o Modo GTO" / EN "See GTO Mode".
Frase sob o CTA, PT: "O Modo GTO é um plano pago. A conta grátis segue com o field e a comparação com o MDF; o número GTO e a faixa são do plano Modo GTO." / EN: "GTO Mode is a paid plan. The free account keeps the field and the MDF comparison; the GTO number and range are on the GTO Mode plan."

## Alt text das imagens (2)
### Imagem 1: o exemplo lado a lado
- PT: "Duas barras de fold no mesmo spot do pós-flop: o field em 46,0% e o GTO em 38,8%, com a faixa GTO de 37,1 a 40,4% em volta da barra do GTO e a diferença em destaque."
- EN: "Two fold bars for the same postflop spot: the field at 46.0% and GTO at 38.8%, with the 37.1–40.4% GTO range around the GTO bar and the gap highlighted."
### Imagem 2: a grade do pré-flop
- PT: "Grade de mãos do Preflop Analysis em que as células cobertas mostram o GTO e o desvio do field, com a célula do RFI do CO em destaque."
- EN: "Preflop Analysis hand grid where the covered cells show the GTO and the field deviation, with the CO RFI cell highlighted."

Nota para o designer: as imagens só mostram os números de "Números usados". Não mostrar preço nem "prévia".

---

# (c) Discord

Texto completo, com URLs, em `discord.md` (mesma pasta). PT e EN, abaixo de 1.200 caracteres cada. Tamanho real (len do texto exato, URL inclusa): **PT 1.038, EN 1.078**. 3 emojis funcionais (📊 título, 🔎 convite, 👉 CTA). **Só postar depois do passo 6 do roteiro.**

**PT**
```
📊 **Novo na Aura: Modo GTO**

Ao lado do número do field, o número GTO e a faixa GTO, onde há referência. Onde o field sai da faixa, está o spot para estudar.

**Exemplo de spot**
CO × BB em pote simples, 30–60bb (GTO a 40bb), torneios Regular, últimos 2 anos, flop K-high two-tone, sem par, desconectado. Contra o c-bet de 33%, o field folda 46,0% e o GTO folda 38,8% (faixa 37,1–40,4%): 5,6 pp acima do topo da faixa.
Aqui o field folda mais do que o GTO. É um spot, não a média do field. Confira no seu board.

**O que você vê**
- Pós-flop: SRP e 3-bet, flop e turn, inclusive a reação a raise no flop do SRP
- Pré-flop: o GTO e o desvio nas células cobertas, inclusive o RFI de CO e BTN a 40bb

🔎 Abra um spot que você joga e olhe o gap.

O Modo GTO é um plano pago. A conta grátis segue com o field e a comparação com o MDF; o número GTO e a faixa são do plano Modo GTO.
Ferramenta de estudo. 18+.
👉 Conhecer o Modo GTO: https://www.aura.poker/?utm_source=discord&utm_medium=social&utm_campaign=modo-gto-launch&utm_content=discord-pt
```

**EN**
```
📊 **New on Aura: GTO Mode**

Next to the field number, the GTO number and the GTO range, where a reference exists. Where the field leaves the range, that is the spot to study.

**Example spot**
CO × BB single-raised pot, 30–60bb (GTO at 40bb), Regular tournaments, last 2 years, K-high two-tone, unpaired, disconnected flop. Facing a 33% c-bet, the field folds 46.0% and GTO folds 38.8% (range 37.1–40.4%): 5.6 pp above the top of the range.
Here the field folds more than GTO does. This is one spot, not the field average. Check it on your board.

**What you see**
- Postflop: SRP and 3-bet, flop and turn, including the response to a raise on the SRP flop
- Preflop: the GTO and the deviation in the covered cells, including the CO and BTN RFI at 40bb

🔎 Open a spot you play and look at the gap.

GTO Mode is a paid plan. The free account keeps the field and the MDF comparison; the GTO number and range are on the GTO Mode plan.
Study tool. 18+.
👉 See GTO Mode: https://www.aura.poker/?utm_source=discord&utm_medium=social&utm_campaign=modo-gto-launch&utm_content=discord-en
```

---

# (d) E-mail

Texto, assuntos, preheader e notas técnicas em `email.md`. Assunto recomendado: a 1 ("Novo na Aura: Modo GTO" / "New on Aura: GTO Mode"). Botão "Conhecer o Modo GTO" / "See GTO Mode". O HTML existe (`email-pt.html` e `email-en.html`; para abrir do disco, `email-pt.preview.html` e `email-en.preview.html`). A imagem do e-mail (`email/modo-gto-pt.png` e `-en.png`) é a captura recortada do card de 33% do app, com os mesmos números do texto (46,0% e 38,8%, faixa 37,1–40,4%, 5,6 pp acima do topo da faixa); não são duas barras renderizadas.

---

## Números usados (todos de `numeros-verificados.md`, 08/10; leitura de produção)

| Número no texto | Valor | Seção da fonte | Onde aparece |
|---|---|---|---|
| Spot do exemplo (antigo N1) | CO × BB · SRP · 30–60bb (GTO a 40bb) · Regular (Vanilla) · flop K-high, two-tone, sem par, desconectado · c-bet de 33% | Exemplo (a) | Linha de apoio do feed; legendas, Discord, landing, e-mail |
| Field folda (N2) | 46,0% (EN 46.0%) | Exemplo (a), `potPercentage` do `actionSize` 2 | Barras (feed, stories, carrossel 1 e 2); legendas, Discord, landing, e-mail |
| GTO folda e faixa (N3) | 38,8% (38,78 na API); faixa 37,1–40,4% (37,13–40,43) | Exemplo (a), `gtoFold` e `gtoBand.fold` | Barras com a faixa como sombreado; legendas, Discord, landing, e-mail |
| Diferença (N4) | +5,6 pp (acima do topo da faixa, como a tela mostra; 7,2 é contra o centro) | Exemplo (a) | Só texto: legendas, Discord, landing, e-mail |
| Pré-flop (N5) | RFI do CO, Regular, 30–50bb (GTO a 40bb): field abre 31,6%, GTO abre 37,0%, −5,4 pp | Exemplo (b) e "Pré-flop" (37 %) | Captura do slide 4 do carrossel; legenda do carrossel e landing (bullet 2). O −5,4 pp não é citado no texto |
| Escala (N6) | 30 situações (10 confrontos de posição a 25, 40 e 60bb) com GTO no flop; mais de 2.300 flops (2.330); quase 7 milhões de nós de turn e river (6.980.568); 225 decisões de pré-flop, de 10 a 60bb | "Pós-flop" e "Pré-flop" | Só a nota da landing. Fora das artes |

Não usados, por instrução da fonte e da HUB: as 10.216 mãos e as 23,8 milhões de oportunidades; contagens de linhas; o candidato SB × BB 3-bet (amostra pequena); RFI do BTN a 40bb (51%), que fica disponível para peças de sustentação.
