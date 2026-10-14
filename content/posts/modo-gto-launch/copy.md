# Modo GTO: copy de lançamento (GTO no flop, turn e river)

Status: rascunho sem marcadores abertos; não publicado. Sem commit. Entra no ar em 13/10/2026 (antes: 08/10); números fechados em 14/10.
@aurapokeranalytics: a confirmar pelo Rafael. URLs com UTM prontas na tabela abaixo.
Fonte dos números: `aura-main/_ops/golive-gto-2026-10-14/numeros-verificados-lancamento.md` (origin/main `e17fc8e`, 14/10), para a cobertura, o pré-flop e o exemplo de abertura; o exemplo CO × BB e o pré-flop seguem iguais aos de `aura-main/_ops/golive-gto-2026-10-04/numeros-verificados.md` (08/10). Os números usados estão mapeados em "Números usados" no fim. **Nenhum marcador `[[...]]` resta no pacote.**
Peças deste pacote: Discord (também em `discord.md`), Instagram (feed, story, story da capa em PT, carrossel de 7 slides só em EN), landing e e-mail (em `email.md`).

> **Regra de texto das artes (Rafael, 08/10): "muita informação, muito texto; não pode ter tanto texto em nenhum post".** Cada arte tem no máximo UM título curto (~6 palavras) e, se precisar, UMA linha de apoio (~10 palavras). A imagem fala: barras field × GTO lado a lado, com os números. O detalhe vai para a legenda. Em toda arte só ficam o `@aurapokeranalytics` e o `18+`, pequenos. O link é o sticker/link na bio, não texto de arte. A frase do plano (Individual com preço e conta grátis) fica na legenda, no Discord, na landing e no e-mail; nas artes, só o slide 6 (título e apoio, com o preço em EN). Nas artes não entram contagem de mãos nem "amostra"; nas legendas e no e-mail também ficam de fora.

## Origem das capturas e artes a refazer (por outro agente)
- **Slide 3 (postflop):** captura nova do aura-novofront `35d7005` (prévia local, API de prévia, 14/10), que mostra Second Barrel e Turn Delayed CBet com o GTO ao lado do field. O Second Barrel só aparece nessa captura; não é o exemplo do slide 5.
- **Slide 4 (pré-flop) e imagem EN do e-mail:** capturas de 08/10 do aura-novofront `429c093` (front no SHA de produção daquele dia, lendo a API local `:7060` com os snapshots do go-live, por conta de teste local, sem login em produção). Os mesmos números foram confirmados em produção em 14/10. A imagem do e-mail EN é o recorte do card de 33% do painel de Fold por tamanho de Flop CBet; a célula do CO no slide 4 tem um contorno âmbar desenhado só para destaque.
- **Slides 2 e a imagem do e-mail PT:** barras renderizadas pela build (46,0% / 38,8% / faixa 37,1–40,4%), não são captura.
- **Slide 5 (abertura):** captura ou barras do Turn Delayed CBet do exemplo de abertura (CO × BB, 30–60bb, GTO a 40bb).
- **Carrossel de 7 slides:** o plano passa a ser o slide 6 e o CTA o 7; indicador "n / 7"; renomear `carrossel-en-05` para 06 e `-06` para 07.
- Nenhuma peça chama as capturas de "print de produção".

## Pendências reais
1. **P-61 no ar e ordem de publicação.** Só postar ou enviar depois do P-61 no ar (Modo GTO aberto ao Individual) e depois que a versão de 13/10 estiver em produção.
2. **Preço (Rafael confere no Stripe).** Decisão do Rafael via HUB, 13/10: "vamos anunciar como fazendo parte do plano de 29 por tempo limitado". A frase do plano cita o preço do Individual: PT "O Modo GTO faz parte do plano Individual (R$ 150/mês) por tempo limitado. A conta grátis segue com o field e a comparação com o MDF." EN "GTO Mode is part of the Individual plan (US$ 29/month) for a limited time. The free account keeps the field and the MDF comparison." Fonte do valor (HUB): `aura-landing` `src/content/pricing.ts` e `aura-novofront` `billingPlans.ts` (US$ 29/mês no checkout em EN, R$ 150/mês no checkout em PT). **Pendente: o Rafael confere no Stripe que o checkout cobra 29 / 150 hoje.** Regras: PT sempre "plano Individual" e "R$ 150/mês" (nunca "US$ 29" nem "R$ 29" em peça PT); EN sempre "Individual plan" e "US$ 29/month". Urgência só por "por tempo limitado" / "for a limited time": sem data de fim, sem "últimas horas", sem "só hoje". Nenhuma peça cita o plano Modo GTO à parte, o plano Top, desconto semestral/anual ou promoção.
3. **Teste logado do Rafael.** Conferir em `www.aura.poker` os mesmos valores do exemplo CO × BB (46,0% / 38,8% / faixa 37,1–40,4%), do RFI do CO (31,6% / 37,0%) e do exemplo de abertura (51,7% / 44,1% / faixa 37,8–50,3%), antes de qualquer post ou envio.
4. **Hospedagem das imagens do e-mail (aura-landing#17).** `email/modo-gto-pt.png` e `-en.png` precisam estar em `https://www.aurapoker.com/email/` antes do envio.
5. **Cobertura: nunca vira "todas".** A tela não cobre todas as ações (por exemplo, o c-bet do flop como abertura, o donk do flop e o probe do river não são feature). Nenhuma peça usa "todas / every / all" para cobertura, nem cita o c-bet do flop, o donk ou o probe do river como feature. O texto fica nas formas abaixo.
6. **"Por tempo limitado" sem data (recomendação do revisor, CONAR/CDC).** Expressão de urgência sem data de fim pode ser questionada. Recomendação: combinar uma data de fim e honrá-la, ou tirar a expressão. Decisão do Rafael. Enquanto não decidir, as peças mantêm "por tempo limitado" / "for a limited time", sem data.
7. **Dependências de produção.** (a) aura-api#84: o turn e o river de co_btn, utg_bb@25 e outros pares ficam fora hoje até o deploy; o texto de cobertura só vale com esse deploy feito. (b) A landing de produção não pode mostrar o GTO como plano à parte (nem preço próprio); só como parte do Individual.

## Decisões registradas
- **Cobertura (texto final, HUB 14/10).** PT: "GTO no flop, no turn e no river. No flop, a reação ao c-bet e ao raise. No turn e no river, também a frequência de aposta do agressor (second barrel, delayed c-bet, probe no turn, third barrel)." EN: "GTO on the flop, turn and river. On the flop, the response to the c-bet and to the raise. On the turn and river, also the aggressor's betting frequency (second barrel, delayed c-bet, turn probe, third barrel)." Nas legendas curtas e no e-mail, versão curta: "no flop, turn e river" e "inclusive as aberturas do agressor no turn e no river", com a lista só "second barrel, delayed c-bet e third barrel" quando houver lista (EN "on the flop, turn and river" e "including the aggressor's openings on the turn and river"; "second barrel, delayed c-bet and third barrel").
- **Capa com duas linhas (decisão consciente, revisão de marca de 08/10).** A capa (story PT e slide 1 do carrossel) tem o apoio ("Novo: Modo GTO" / "New: GTO Mode") e uma micro-legenda do spot ("CO × BB · K-high two-tone · c-bet de 33%" / "CO × BB · K-high two-tone · 33% c-bet"). É a única exceção à regra de uma linha de apoio.
- **Slide 3.** Título "Postflop: GTO with the range", apoio "Turn openings, with the range." (5 palavras; a captura mostra Second Barrel e Turn Delayed CBet). A arte é do outro agente.
- **Slide 4 mostra os números arredondados da tela.** A captura traz Field 32% / GTO 37% / −5. A fonte tem 31,6 / 37,0 / −5,4; as legendas e a landing usam os valores da fonte.
- **Slide 5 novo: abertura do agressor.** Entra como slide 5 para manter o slide 4 do pré-flop como está. Exemplo: Turn Delayed CBet (o CO aposta o turn depois do flop passado), recorte largo. Não se usa o Probe nem o Second Barrel como exemplo (o Second Barrel, dentro da faixa, só aparece na captura do slide 3). Se o Rafael preferir a abertura colada ao pós-flop (slide 4), basta inverter com o pré-flop e renomear os arquivos.
- **Stories e feed** seguem com o exemplo CO × BB (c-bet de 33%). O exemplo de abertura só vive no carrossel (slide 5 e legenda); Discord, landing e e-mail ficam com um exemplo só.
- **Sem contagem de mãos nem amostra.** O brand-kit pede rodapé de amostra em post com número; a instrução do Rafael de 08/10 o substitui. Ficam fora a contagem de mãos do exemplo de abertura (80 mil), as 10.216 mãos do exemplo CO × BB e o número de oportunidades do pré-flop (23,8 milhões).
- **Bug do front a lembrar.** O app em PT mistura formatos no mesmo card ("46.0%" e "38,8%"). Nas peças em PT escrevemos sempre com vírgula.

## Fatos de produto aplicados
- **Dois números ao lado do field:** o número GTO e a faixa GTO. Rótulos de resultado do app que podem aparecer em legenda: "dentro da faixa GTO" e "acima da faixa GTO" (EN "inside the GTO range", "above the GTO range").
- **Fluxo:** "escolha o spot, clique em Apply e veja o field e o GTO juntos" e "a faixa de status do app guia cada clique até ter GTO" (EN "the app's status bar guides you, click by click, until GTO is there"). Sem citar as frases em inglês da tela. Nada de "GTO em breve" nem "ainda sem GTO" como feature.
- **Pré-flop:** "o GTO e o desvio nas células cobertas, inclusive o RFI de CO e BTN a 40bb" (pré-flop `20261007`).
- **Filtro do exemplo nas peças:** "torneios Regular" (EN "Regular tournaments") e "últimos 2 anos" (EN "last 2 years"), sem a palavra vanilla.
- **Plano e conta Grátis:** frase única da Pendência 2. Vive na legenda, no Discord, na landing (sob o CTA) e no e-mail (sob o botão); na arte, só o slide 6. CTAs: "Conhecer o Modo GTO" / "See GTO Mode"; nenhum diz "grátis". O único preço citado é o do plano Individual, dentro da frase do plano, com a moeda nunca trocada.
- **Escopo da referência:** a ressalva de torneios vanilla fica só na Metodologia do app (pedido do Rafael em 06/10). Nenhuma peça a repete; "Regular" aparece só como filtro do spot.
- **"Spot"** é a situação ou a decisão, nunca contagem de linhas.
- **Formato dos números:** vírgula em PT (46,0%), ponto em EN (46.0%).
- **Nome em inglês:** "GTO Mode".
- **Carrossel só em EN;** a capa tem story PT-BR 1080x1920. Não há story EN da capa.

## O exemplo (reação ao c-bet; exemplo (a))
Filtro da tela: Postflop · SRP · RFI CO, caller BB · stack 30.1–60bb (GTO a 40bb) · torneio Regular · flop K-high, two-tone, sem par, desconectado · reação do BB ao c-bet de 33%.
- Field folda **46,0%**; GTO folda **38,8%** (38,78 na API), faixa **37,1–40,4%** (37,13–40,43); diferença **+5,6 pp** (a tela mostra a distância ao topo da faixa; contra o centro do GTO são 7,2). Leitura: acima da faixa.

**Texto final do exemplo, PT:** "CO × BB em pote simples (SRP), 30–60bb (GTO a 40bb), torneios Regular, últimos 2 anos, flop K-high two-tone, sem par, desconectado, contra o c-bet de 33%. O field folda 46,0% contra 38,8% do GTO (faixa 37,1–40,4%): 5,6 pp acima do topo da faixa. Aqui o field folda mais do que o GTO. É um spot, não a média do field. Confira no seu board."

**Final example text, EN:** "CO × BB single-raised pot (SRP), 30–60bb (GTO at 40bb), Regular tournaments, last 2 years, K-high two-tone, unpaired, disconnected flop, facing a 33% c-bet. The field folds 46.0% against GTO's 38.8% (range 37.1–40.4%): 5.6 pp above the top of the range. Here the field folds more than GTO does. This is one spot, not the field average. Check it on your board."

**Exemplo de pré-flop (exemplo (b)):** RFI do CO, torneio Regular, stack 30–50bb (GTO a 40bb). Field abre **31,6%**; GTO abre **37,0%**; diferença **−5,4 pp** (o field abre de menos). PT: "No pré-flop, RFI do CO a 30–50bb (GTO a 40bb), torneios Regular, últimos 2 anos: o field abre 31,6% e o GTO abre 37,0%." EN: "Preflop, CO RFI at 30–50bb (GTO at 40bb), Regular tournaments, last 2 years: the field opens 31.6% and GTO opens 37.0%."

## O exemplo de abertura do agressor (Turn Delayed CBet)
Spot (recorte largo): CO × BB · 30–60bb (GTO a 40bb) · SRP · flop two-tone · turn qualquer · torneios Regular · últimos 2 anos. Ação: Turn Delayed CBet (o CO aposta o turn depois do flop passado). Métrica: frequência da aposta do CO, field contra GTO. Field aposta **51,7%**; GTO aposta **44,1%**, faixa **37,8–50,3%**; **1,4 pp acima do topo da faixa**. Leitura: acima da faixa (o field aposta mais do que o GTO). Resumo para o apoio da arte: "CO × BB · two-tone · turn".

**Texto final, PT:** "CO × BB em pote simples (SRP), 30–60bb (GTO a 40bb), torneios Regular, últimos 2 anos, flop two-tone, qualquer turn. No turn, depois do flop passado, o CO aposta (delayed c-bet): o field aposta 51,7% e o GTO aposta 44,1% (faixa 37,8–50,3%): 1,4 pp acima do topo da faixa. Aqui o field aposta mais do que o GTO. É um spot, não a média do field. Confira no seu board."

**Final text, EN:** "CO × BB single-raised pot (SRP), 30–60bb (GTO at 40bb), Regular tournaments, last 2 years, two-tone flop, any turn. On the turn, after the flop checks through, the CO bets (delayed c-bet): the field bets 51.7% and GTO bets 44.1% (range 37.8–50.3%): 1.4 pp above the top of the range. Here the field bets more than GTO does. This is one spot, not the field average. Check it on your board."

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

Em toda arte, além do título e da linha de apoio: logo AURA, `@aurapokeranalytics · 18+` pequeno e, nos slides, o indicador "n / 7". Nas barras, o % central do GTO no rótulo e a faixa GTO como sombreado, com a faixa escrita pequena.

| Arte | Formato | Idioma | Título | Apoio (uma linha) | O que a imagem mostra |
|---|---|---|---|---|---|
| Feed | 1080x1350 | PT | Mesmo spot, dois números | CO × BB · K-high two-tone · c-bet de 33% | Barras de fold lado a lado: Field 46,0% e GTO 38,8% (faixa 37,1–40,4%) |
| Feed | 1080x1350 | EN | Same spot, two numbers | CO × BB · K-high two-tone · 33% c-bet | Fold bars side by side: Field 46.0% and GTO 38.8% (range 37.1–40.4%) |
| Story | 1080x1920 | PT | O field folda mais que o GTO? | CO × BB · K-high two-tone · c-bet de 33% | Mesmas barras (46,0% e 38,8%); sticker de link "Conhecer o Modo GTO" |
| Story | 1080x1920 | EN | Does the field fold more than GTO? | CO × BB · K-high two-tone · 33% c-bet | Same bars (46.0% and 38.8%); link sticker "See GTO Mode" |
| Story da capa do carrossel | 1080x1920 | PT | Onde o field sai do GTO? | Novo: Modo GTO (+ micro-legenda do spot: CO × BB · K-high two-tone · c-bet de 33%) | Mesmas barras com o gap em âmbar (46,0% e 38,8%); sticker "Conhecer o Modo GTO" |
| Carrossel 1 (capa) | 1080x1350 | EN | Where does the field leave GTO? | New: GTO Mode (+ spot micro-caption: CO × BB · K-high two-tone · 33% c-bet) | Mesma imagem da capa PT (46.0% and 38.8%) |
| Carrossel 2 | 1080x1350 | EN | Same spot, two numbers | CO × BB · K-high two-tone · 33% c-bet | As barras e os dois números: Field 46.0%, GTO 38.8% (range 37.1–40.4%) |
| Carrossel 3 | 1080x1350 | EN | Postflop: GTO with the range | Turn openings, with the range. | Captura nova do Postflop com o Modo GTO ligado (aura-novofront `35d7005`), mostrando Second Barrel e Turn Delayed CBet com o GTO ao lado do field |
| Carrossel 4 | 1080x1350 | EN | Preflop: GTO and deviation | Includes CO and BTN RFI at 40bb. | Captura da grade com a célula do RFI do CO destacada: na tela, Field 32%, GTO 37%, −5 (arredondado; a fonte tem 31,6 / 37,0 / −5,4) |
| Carrossel 5 (novo) | 1080x1350 | EN | Delayed c-bet: field vs GTO | CO × BB · two-tone · turn | Barras de aposta lado a lado: Field 51.7% e GTO 44.1% com a faixa 37.8–50.3% sombreada; gap em âmbar (1.4 pp acima do topo da faixa) |
| Carrossel 6 | 1080x1350 | EN | GTO Mode, now in Individual | Part of the US$ 29/month plan, for a limited time. | Um cadeado desenhado (sem texto do app) |
| Carrossel 7 (CTA) | 1080x1350 | EN | See GTO Mode | Link in bio. | Logo e fundo da marca |

Contagem de palavras (regra do Rafael): títulos de 4 a 7 palavras; apoios de 3 a 10 palavras (slide 3: 5; slide 5: 5; slide 6: 10).

Notas de arte:
- **Cores:** fold em teal `#015A6B`; a distância entre a barra do field e a do GTO em âmbar (o gap). Faixa GTO sombreada em volta da barra do GTO. No slide 5, a barra é de aposta (frequência de bet), não de fold: usar a cor semântica do raise (`#AD2C34`) para a aposta, mantendo o gap em âmbar e a faixa sombreada.
- **Slide 3:** o número fica dentro da captura; nenhum texto de arte o repete. Não mostrar estado de carregamento nem aviso de "sem GTO".
- **Slide 4:** o stack da captura é 30–50bb (GTO a 40bb), torneio Regular. O número fica dentro da captura.
- **Slide 5:** sem contagem de mãos. O 51.7% e o 44.1% ficam nas barras; a faixa pequena, escrita 37.8–50.3%.
- **Slide 6:** título "GTO Mode, now in Individual", apoio "Part of the US$ 29/month plan, for a limited time." (10 palavras; sem data, sem "últimas horas"). O cadeado desenhado continua. A frase completa sobre o plano Individual e a conta grátis fica na legenda.
- **Enquete opcional no story (fora da arte):** "Qual spot você quer ver com o GTO ao lado?" com as opções "Flop" e "Turn/river" / "Which spot do you want to see with GTO next to it?" with "Flop" and "Turn/river".

## Legendas

### Legenda do feed
PT:
```
O GTO folda 38,8%. O field folda 46,0%. Mesmo spot.

Novo na Aura: Modo GTO. Ao lado da frequência do field, o número GTO e a faixa GTO.

Exemplo: CO × BB em pote simples (SRP), 30–60bb (GTO a 40bb), torneios Regular, últimos 2 anos, flop K-high two-tone, sem par, desconectado, contra o c-bet de 33%. O field folda 46,0% contra 38,8% do GTO (faixa 37,1–40,4%): 5,6 pp acima do topo da faixa. Aqui o field folda mais do que o GTO. É um spot, não a média do field. Confira no seu board.

Pós-flop: o GTO no flop, turn e river, inclusive as aberturas do agressor no turn e no river. Escolha o spot, clique em Apply e veja o field e o GTO juntos. A faixa de status do app guia cada clique até ter GTO.

Pré-flop: o GTO e o desvio nas células cobertas, inclusive o RFI de CO e BTN a 40bb.

O Modo GTO faz parte do plano Individual (R$ 150/mês) por tempo limitado. A conta grátis segue com o field e a comparação com o MDF.

Conhecer o Modo GTO, link na bio. Ferramenta de estudo. 18+.

#poker #pokerMTT #pokerestudo #aurapoker
```
EN:
```
GTO folds 38.8%. The field folds 46.0%. Same spot.

New on Aura: GTO Mode. Next to the field frequency, the GTO number and the GTO range.

Example: CO × BB single-raised pot (SRP), 30–60bb (GTO at 40bb), Regular tournaments, last 2 years, K-high two-tone, unpaired, disconnected flop, facing a 33% c-bet. The field folds 46.0% against GTO's 38.8% (range 37.1–40.4%): 5.6 pp above the top of the range. Here the field folds more than GTO does. This is one spot, not the field average. Check it on your board.

Postflop: GTO on the flop, turn and river, including the aggressor's openings on the turn and river. Pick the spot, hit Apply and see the field and GTO together. The app's status bar guides you, click by click, until GTO is there.

Preflop: the GTO and the deviation in the covered cells, including the CO and BTN RFI at 40bb.

GTO Mode is part of the Individual plan (US$ 29/month) for a limited time. The free account keeps the field and the MDF comparison.

See GTO Mode, link in bio. Study tool. 18+.

#poker #pokerMTT #pokerestudo #aurapoker
```

### Legenda do carrossel e da capa
PT (usar também com o story da capa, se o Rafael postar legenda):
```
Onde o field sai do GTO?

Novo na Aura: Modo GTO. Ao lado da frequência do field, o número GTO e a faixa GTO.

Pós-flop: GTO no flop, no turn e no river. No flop, a reação ao c-bet e ao raise. No turn e no river, também a frequência de aposta do agressor (second barrel, delayed c-bet, probe no turn, third barrel). Escolha o spot, clique em Apply e veja o field e o GTO juntos. A faixa de status do app guia cada clique até ter GTO.

Reação: CO × BB em pote simples (SRP), 30–60bb (GTO a 40bb), torneios Regular, últimos 2 anos, flop K-high two-tone, sem par, desconectado, contra o c-bet de 33%. O field folda 46,0% contra 38,8% do GTO (faixa 37,1–40,4%): 5,6 pp acima do topo da faixa. Aqui o field folda mais do que o GTO. É um spot, não a média do field. Confira no seu board.

Abertura: CO × BB em pote simples (SRP), 30–60bb (GTO a 40bb), torneios Regular, últimos 2 anos, flop two-tone, qualquer turn. No turn, depois do flop passado, o CO aposta (delayed c-bet): o field aposta 51,7% e o GTO aposta 44,1% (faixa 37,8–50,3%): 1,4 pp acima do topo da faixa. Aqui o field aposta mais do que o GTO. É um spot, não a média do field.

Pré-flop: o GTO e o desvio nas células cobertas, inclusive o RFI de CO e BTN a 40bb. RFI do CO a 30–50bb (GTO a 40bb), torneios Regular, últimos 2 anos: o field abre 31,6% e o GTO abre 37,0%.

O Modo GTO faz parte do plano Individual (R$ 150/mês) por tempo limitado. A conta grátis segue com o field e a comparação com o MDF.

Conhecer o Modo GTO, link na bio. Salve para estudar. Ferramenta de estudo. 18+.

#poker #pokerMTT #pokerestudo #aurapoker
```
EN:
```
Where does the field leave GTO?

New on Aura: GTO Mode. Next to the field frequency, the GTO number and the GTO range.

Postflop: GTO on the flop, turn and river. On the flop, the response to the c-bet and to the raise. On the turn and river, also the aggressor's betting frequency (second barrel, delayed c-bet, turn probe, third barrel). Pick the spot, hit Apply and see the field and GTO together. The app's status bar guides you, click by click, until GTO is there.

Response: CO × BB single-raised pot (SRP), 30–60bb (GTO at 40bb), Regular tournaments, last 2 years, K-high two-tone, unpaired, disconnected flop, facing a 33% c-bet. The field folds 46.0% against GTO's 38.8% (range 37.1–40.4%): 5.6 pp above the top of the range. Here the field folds more than GTO does. This is one spot, not the field average. Check it on your board.

Opening: CO × BB single-raised pot (SRP), 30–60bb (GTO at 40bb), Regular tournaments, last 2 years, two-tone flop, any turn. On the turn, after the flop checks through, the CO bets (delayed c-bet): the field bets 51.7% and GTO bets 44.1% (range 37.8–50.3%): 1.4 pp above the top of the range. Here the field bets more than GTO does. This is one spot, not the field average.

Preflop: the GTO and the deviation in the covered cells, including the CO and BTN RFI at 40bb. CO RFI at 30–50bb (GTO at 40bb), Regular tournaments, last 2 years: the field opens 31.6% and GTO opens 37.0%.

GTO Mode is part of the Individual plan (US$ 29/month) for a limited time. The free account keeps the field and the MDF comparison.

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
- PT: Modo GTO: no flop, turn e river, o número GTO e a faixa GTO ao lado da frequência do field. Veja onde o field sai da faixa e estude esse spot.
- EN: GTO Mode: on the flop, turn and river, the GTO number and the GTO range next to the field frequency. See where the field leaves the range and study that spot.

## 3 bullets
PT:
- Pós-flop: GTO no flop, no turn e no river. No flop, a reação ao c-bet e ao raise. No turn e no river, também a frequência de aposta do agressor (second barrel, delayed c-bet, probe no turn, third barrel). Escolha o spot, clique em Apply e veja o field e o GTO juntos; a faixa de status do app guia cada clique até ter GTO.
- Pré-flop: a grade traz o GTO e o desvio nas células cobertas, inclusive o RFI de CO e BTN a 40bb. No RFI do CO a 30–50bb (GTO a 40bb), torneios Regular, últimos 2 anos, o field abre 31,6% e o GTO abre 37,0%.
- Exemplo: CO × BB em pote simples (SRP), 30–60bb (GTO a 40bb), torneios Regular, últimos 2 anos, flop K-high two-tone, sem par, desconectado, contra o c-bet de 33%. O field folda 46,0% contra 38,8% do GTO (faixa 37,1–40,4%): 5,6 pp acima do topo da faixa. Aqui o field folda mais do que o GTO. É um spot, não a média do field. Confira no seu board.

EN:
- Postflop: GTO on the flop, turn and river. On the flop, the response to the c-bet and to the raise. On the turn and river, also the aggressor's betting frequency (second barrel, delayed c-bet, turn probe, third barrel). Pick the spot, hit Apply and see the field and GTO together; the app's status bar guides you, click by click, until GTO is there.
- Preflop: the grid carries the GTO and the deviation in the covered cells, including the CO and BTN RFI at 40bb. On the CO RFI at 30–50bb (GTO at 40bb), Regular tournaments, last 2 years, the field opens 31.6% and GTO opens 37.0%.
- Example: CO × BB single-raised pot (SRP), 30–60bb (GTO at 40bb), Regular tournaments, last 2 years, K-high two-tone, unpaired, disconnected flop, facing a 33% c-bet. The field folds 46.0% against GTO's 38.8% (range 37.1–40.4%): 5.6 pp above the top of the range. Here the field folds more than GTO does. This is one spot, not the field average. Check it on your board.

Nota de rodapé da seção (PT): "Um spot, não a média do field. Ferramenta de estudo · 18+. A Aura não é site de apostas e não oferece jogo."
Footnote (EN): "One spot, not the field average. Study tool · 18+. Aura is not a betting site and does not offer gambling."
(Sem números de escala no rodapé: a escala de 08/10 descrevia a cobertura antiga e não foi atualizada.)

CTA: PT "Conhecer o Modo GTO" / EN "See GTO Mode".
Frase sob o CTA, PT: "O Modo GTO faz parte do plano Individual (R$ 150/mês) por tempo limitado. A conta grátis segue com o field e a comparação com o MDF." / EN: "GTO Mode is part of the Individual plan (US$ 29/month) for a limited time. The free account keeps the field and the MDF comparison."

## Alt text das imagens (2)
### Imagem 1: o exemplo lado a lado
- PT: "Duas barras de fold no mesmo spot do pós-flop: o field em 46,0% e o GTO em 38,8%, com a faixa GTO de 37,1 a 40,4% em volta da barra do GTO e a diferença em destaque."
- EN: "Two fold bars for the same postflop spot: the field at 46.0% and GTO at 38.8%, with the 37.1–40.4% GTO range around the GTO bar and the gap highlighted."
### Imagem 2: a grade do pré-flop
- PT: "Grade de mãos do Preflop Analysis em que as células cobertas mostram o GTO e o desvio do field, com a célula do RFI do CO em destaque."
- EN: "Preflop Analysis hand grid where the covered cells show the GTO and the field deviation, with the CO RFI cell highlighted."

Nota para o designer: as imagens só mostram os números de "Números usados". Não mostrar preço nas imagens (o preço fica só na frase do plano, sob o CTA). Não mostrar estado de carregamento nem aviso de "sem GTO".

---

# (c) Discord

Texto completo, com URLs, em `discord.md` (mesma pasta). PT e EN, abaixo de 1.200 caracteres cada. Tamanho real e emojis: ver `discord.md`. **Só postar depois do teste logado e do P-61 no ar.**

---

# (d) E-mail

Texto, assuntos, preheader e notas técnicas em `email.md`. Corpo curto, um exemplo (CO × BB) e a comparação field × GTO dele. Botão "Conhecer o Modo GTO" / "See GTO Mode". A imagem do e-mail (`email/modo-gto-pt.png` e `-en.png`) tem os mesmos números do exemplo (46,0% e 38,8%, faixa 37,1–40,4%).

---

## Números usados

| Número no texto | Valor | Fonte | Onde aparece |
|---|---|---|---|
| Spot do exemplo CO × BB | CO × BB · SRP · 30–60bb (GTO a 40bb) · Regular · flop K-high, two-tone, sem par, desconectado · c-bet de 33% | Exemplo (a), 08/10 | Apoio do feed; legendas, Discord, landing, e-mail |
| Field folda | 46,0% (EN 46.0%) | Exemplo (a), `potPercentage` do `actionSize` 2 | Barras (feed, stories, carrossel 1 e 2); legendas, Discord, landing, e-mail |
| GTO folda e faixa | 38,8% (38,78 na API); faixa 37,1–40,4% (37,13–40,43) | Exemplo (a), `gtoFold` e `gtoBand.fold` | Barras com a faixa como sombreado; legendas, Discord, landing, e-mail |
| Diferença | +5,6 pp (acima do topo da faixa, como a tela mostra; 7,2 é contra o centro) | Exemplo (a) | Só texto: legendas, Discord, landing (o e-mail não a cita) |
| Pré-flop | RFI do CO, Regular, 30–50bb (GTO a 40bb): field abre 31,6%, GTO abre 37,0%, −5,4 pp | Exemplo (b) | Captura do slide 4; legenda do carrossel e landing (bullet 2). O −5,4 pp não é citado no texto |
| Ação da abertura | Turn Delayed CBet (o CO aposta o turn depois do flop passado) | `numeros-verificados-lancamento.md` (14/10) | Título do slide 5; legenda do carrossel |
| Spot da abertura | CO × BB · 30–60bb (GTO a 40bb) · SRP · flop two-tone · turn qualquer · Regular · últimos 2 anos (apoio da arte: "CO × BB · two-tone · turn") | idem | Slide 5 (apoio); legenda do carrossel |
| Field aposta | 51,7% (EN 51.7%) | idem | Slide 5 (barra); legenda do carrossel |
| GTO aposta e faixa | 44,1%, faixa 37,8–50,3% (EN 44.1%, 37.8–50.3%) | idem | Slide 5 (barra e faixa); legenda do carrossel |
| Diferença da abertura | 1,4 pp acima do topo da faixa (EN 1.4 pp above the top of the range) | idem | Slide 5 (gap); legenda do carrossel |
| Cobertura | Texto da seção "Decisões registradas" | idem | Legendas, landing, Discord, e-mail, slide 3 |

Não usados, por instrução da fonte e da HUB: a contagem de mãos do exemplo de abertura (80 mil), as 10.216 mãos e as 23,8 milhões de oportunidades; contagens de linhas e a escala de 08/10 (30 situações, 2.330 flops, 6.980.568 nós, 225 decisões); o Probe e o Second Barrel como exemplo; o candidato SB × BB 3-bet (amostra pequena); RFI do BTN a 40bb (51%), disponível para peças de sustentação.
