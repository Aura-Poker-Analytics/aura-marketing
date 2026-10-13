# Modo GTO: copy de lançamento ("GTO em todas as ações")

Status: rascunho com marcadores pendentes; não publicado. Sem commit. Versão "GTO em todas as ações do pós-flop", entra no ar em 13/10/2026 (antes: 08/10).
@aurapokeranalytics: a confirmar pelo Rafael. URLs com UTM prontas na tabela abaixo.
Fonte dos números: `aura-main/_ops/golive-gto-2026-10-04/numeros-verificados.md` (08/10, lido em produção). **Ainda não existe `numeros-verificados.md` para a versão de 13/10**: os números do exemplo CO × BB e do pré-flop são os de 08/10 e precisam ser reconfirmados pela HUB (ver Pendências). Os números usados estão mapeados em "Números usados" no fim.
Peças deste pacote: Discord (também em `discord.md`), Instagram (feed, story, story da capa em PT, carrossel de 7 slides só em EN), landing e e-mail (em `email.md`).

> **Marcadores abertos neste pacote (todos devem sumir antes de publicar):**
> - `[[CONFIRMAR-COBERTURA]]`: início de todo trecho que diz "em todas as ações do pós-flop". Tirar quando a HUB confirmar a cobertura no `numeros-verificados.md` novo.
> - `[[CONFIRMAR-PREFLOP]]`: início de todo trecho do pré-flop ("o GTO e o desvio nas células cobertas, inclusive o RFI de CO e BTN a 40bb"). Tirar quando a HUB confirmar que o pré-flop não mudou (ou trocar o texto, se mudou).
> - `[[N7: spot]]`, `[[N8: % do field]]`, `[[N9: % GTO e faixa]]`, `[[N10: diferença em pp]]`: exemplo de abertura do agressor (second barrel ou probe). Sem número até a HUB fornecer.
> - Em `[mais|menos]` (exemplo de abertura): escolher a palavra pelo sinal de N10.

> **Regra de texto das artes (Rafael, 08/10): "muita informação, muito texto; não pode ter tanto texto em nenhum post".** Cada arte tem no máximo UM título curto (~6 palavras) e, se precisar, UMA linha de apoio (~10 palavras). A imagem fala: barras field × GTO lado a lado, com os números. O detalhe vai para a legenda. Em toda arte só ficam o `@aurapokeranalytics` e o `18+`, pequenos. O link é o sticker/link na bio, não texto de arte. A frase do plano (Individual com preço e conta grátis) fica na legenda, no Discord, na landing e no e-mail; nas artes, só o slide 6 (título e apoio, com o preço em EN). Nas artes não entram contagem de mãos nem "amostra"; nas legendas e no e-mail também ficam de fora.

## Origem das capturas
- **Slides 2, 4 (pré-flop) e imagem do e-mail:** as capturas de 08/10 seguem valendo até a reconferência. Vêm do front no SHA de produção daquele dia (aura-novofront `429c093`), lendo a API local `:7060` com os snapshots do go-live (flop e turn/river 20261008, pré-flop 20261007), por conta de teste local (sem login em produção). A imagem do e-mail EN é o recorte do card de 33% do painel de Fold por tamanho de Flop CBet; a célula do CO no slide 4 tem um contorno âmbar desenhado só para destaque.
- **Slide 3 (postflop) e slide 5 (abertura):** precisam de captura nova da versão de 13/10 (tela com GTO nas ações, inclusive a abertura do agressor), a ser feita por quem cuida das artes. O slide 5 depende de N7 a N10.
- Nenhuma peça chama as capturas de "print de produção".

## Pendências reais
1. **Reconfirmar os números do exemplo no snapshot de produção novo.** Os valores do exemplo CO × BB (field 46,0%, GTO 38,8%, faixa 37,1–40,4%, 5,6 pp acima do topo da faixa) e do pré-flop (RFI do CO: field 31,6%, GTO 37,0%) são de 08/10 e estão no texto como estavam. A HUB deve reconfirmá-los no snapshot de produção de 13/10 e entregar o `numeros-verificados.md` novo. Se algum mudar, atualizar todas as peças e as artes (tabela "Números usados" lista onde cada um aparece).
2. **Cobertura "em todas as ações do pós-flop".** Texto-alvo marcado com `[[CONFIRMAR-COBERTURA]]`. Só sai sem marcador se o `numeros-verificados.md` novo confirmar. Enquanto não, nenhuma peça vai ao ar.
3. **Pré-flop.** `[[CONFIRMAR-PREFLOP]]` em todo trecho do pré-flop, incluindo o RFI de CO e BTN a 40bb.
4. **Exemplo de abertura do agressor (N7 a N10).** A HUB fornece: o spot (second barrel ou probe, com posições, stack, filtro e board), a frequência do field, o GTO com a faixa e a diferença em pp. O texto-modelo PT/EN está na seção "O exemplo de abertura" e vale também para o slide 5 do carrossel. Se o número vier de outro tipo de abertura (probe, delayed c-bet), trocar o nome da ação no título do slide 5.
5. **Conferência das capturas no teste logado.** O teste logado do Rafael deve conferir, em `www.aura.poker`, os mesmos valores do exemplo (46,0% / 38,8% / faixa 37,1–40,4% e RFI do CO 31,6% / 37,0%) e os de N7 a N10, antes de qualquer post ou envio.
6. **Ordem de publicação.** Só postar depois do teste logado do Rafael e depois do P-61 no ar (Modo GTO aberto ao Individual), e depois que a versão "GTO em todas as ações" estiver em produção (13/10).
7. **Plano e preço (decisão do Rafael via HUB, 13/10: "vamos anunciar como fazendo parte do plano de 29 por tempo limitado!! pra gerar urgência").** A frase do plano agora cita o preço do Individual: PT "O Modo GTO faz parte do plano Individual (R$ 150/mês) por tempo limitado. A conta grátis segue com o field e a comparação com o MDF." EN "GTO Mode is part of the Individual plan (US$ 29/month) for a limited time. The free account keeps the field and the MDF comparison." Fonte do valor (conferida pela HUB): `aura-landing` `src/content/pricing.ts` e `aura-novofront` `billingPlans.ts` (`SELLABLE_PLAN_IDS` = individual; GTO incluso no Individual desde 09/10): US$ 29/mês no checkout em EN, R$ 150/mês no checkout em PT. **Pendente: a HUB ainda confirma que o checkout cobra 29 / 150 hoje.** Só publicar depois dessa confirmação e do P-61 no ar. Regras: PT sempre "plano Individual" e "R$ 150/mês" (nunca "US$ 29" nem "R$ 29" em peça PT); EN sempre "Individual plan" e "US$ 29/month". Urgência só por "por tempo limitado" / "for a limited time": sem data de fim, sem "últimas horas", sem "só hoje", sem prazo. Nenhuma peça cita o plano Modo GTO à parte, o plano Top, desconto semestral/anual ou promoção.
8. **Landing: nota de rodapé sem números de escala.** Os números de escala de 08/10 (30 situações com GTO no flop, 2.330 flops, 6.980.568 nós de turn e river, 225 decisões de pré-flop) descreviam a cobertura antiga e saíram do rodapé da landing. Voltam só se o `numeros-verificados.md` novo trouxer a escala de 13/10.
9. **Artes a refazer por outro agente (fora deste escopo):** slide 3 (novo título e apoio), slide 5 novo (abertura), renumeração do carrossel de 6 para 7 slides (o plano passa a ser o 6 e o CTA o 7), indicador "n / 7", e o texto do e-mail em `email-pt.html` e `email-en.html` conforme `email.md`.
10. **Bug do front a avisar.** O app em PT mistura formatos no mesmo card: "46.0%" (ponto) e "38,8%" (vírgula). Nas peças em PT escrevemos sempre com vírgula; o app não. Reconferir se segue assim na versão de 13/10.

## Decisões registradas
- **Capa com duas linhas (decisão consciente, revisão de marca de 08/10).** A capa (story PT e slide 1 do carrossel) tem o apoio ("Novo: Modo GTO" / "New: GTO Mode") e uma micro-legenda do spot ("CO × BB · K-high two-tone · c-bet de 33%" / "CO × BB · K-high two-tone · 33% c-bet"). É a única exceção à regra de uma linha de apoio.
- **Slide 4 mostra os números arredondados da tela.** A captura traz Field 32% / GTO 37% / −5. A fonte tem 31,6 / 37,0 / −5,4; as legendas e a landing usam os valores da fonte.
- **"Rodapé de amostra".** O brand-kit pede rodapé de amostra em post com número. A instrução do Rafael de 08/10 (sem contagem de mãos nem amostra nas peças) o substitui; nenhuma peça traz amostra.
- **Slide 3 (13/10).** Passa a mostrar o GTO em todas as ações do pós-flop (flop, turn e river). O apoio antigo ("SRP and 3-bet, flop and turn. Raise response on SRP flop.") sai: nenhuma peça limita a cobertura por street, por tipo de pote ou por ação.
- **Slide 5 novo (13/10): abertura do agressor.** Entra como slide 5 (e não como 4) para manter o slide 4 do pré-flop como está; o plano vira o slide 6 e o CTA o slide 7 (por último). Se o Rafael preferir a abertura colada ao pós-flop (slide 4), basta inverter com o pré-flop e renomear os arquivos.
- **Stories e feed** seguem com o exemplo CO × BB.
- **Exemplo de abertura só no carrossel (slide 5 e legenda).** Feed, stories, Discord, landing e e-mail ficam com um exemplo só (CO × BB), para não poluir.

## Fatos de produto aplicados
- **Cobertura:** "em todas as ações do pós-flop: flop, turn e river, inclusive as aberturas do agressor (c-bet, second barrel, probe)". Sempre com `[[CONFIRMAR-COBERTURA]]` no começo do trecho. Removidas as frases que limitavam a cobertura ("SRP e 3-bet", "flop e turn", "reação a raise só no flop do SRP", "onde há referência" no pós-flop).
- **Cada ação com dois números:** o número GTO e a faixa GTO ao lado da frequência do field.
- **Fluxo:** "escolha o spot, clique em Apply e veja o field e o GTO juntos" e "a cada clique, o app mostra o que falta para ver o GTO". Nada de "GTO em breve" nem "ainda sem GTO" como feature.
- **Pré-flop:** "o GTO e o desvio nas células cobertas, inclusive o RFI de CO e BTN a 40bb" (pré-flop `20261007`), sempre com `[[CONFIRMAR-PREFLOP]]`.
- **Filtro do exemplo nas peças:** "torneios Regular" (EN "Regular tournaments") e "últimos 2 anos" (EN "last 2 years"), sem a palavra vanilla.
- **Plano e conta Grátis (HUB, 08/10, P-61; preço do Individual por decisão do Rafael, 13/10):** PT "O Modo GTO faz parte do plano Individual (R$ 150/mês) por tempo limitado. A conta grátis segue com o field e a comparação com o MDF." EN "GTO Mode is part of the Individual plan (US$ 29/month) for a limited time. The free account keeps the field and the MDF comparison." Vive na legenda, no Discord, na landing (sob o CTA) e no e-mail (sob o botão); na arte, só o slide 6 (título e apoio). CTAs: "Conhecer o Modo GTO" / "See GTO Mode"; nenhum diz "grátis". O único preço citado é o do plano Individual dentro da frase do plano (PT "R$ 150/mês", EN "US$ 29/month", moeda nunca trocada). Nenhuma peça diz "plano pago" do GTO, cita o plano Modo GTO como produto à venda, desconto semestral/anual, promoção, data de fim, nem menciona o plano Top.
- **Escopo da referência:** a ressalva de torneios vanilla fica só na Metodologia do app (pedido do Rafael em 06/10). Nenhuma peça a repete; "Regular" aparece só como filtro do spot.
- **"Spot"** é a situação ou a decisão, nunca contagem de linhas.
- **Formato dos números:** vírgula em PT (46,0%), ponto em EN (46.0%).
- **Nome em inglês:** "GTO Mode".
- **Carrossel só em EN;** a capa tem story PT-BR 1080x1920. Não há story EN da capa.

## O exemplo (fonte: `numeros-verificados.md` de 08/10, exemplo (a); a reconfirmar, pendência 1)
Filtro da tela: Postflop · SRP · RFI CO, caller BB · stack 30.1–60bb (GTO a 40bb) · torneio Regular (Vanilla) · flop K-high, two-tone, sem par, desconectado · reação do BB ao c-bet de 33%.
- Field folda **46,0%**; GTO folda **38,8%**, faixa **37,1–40,4%**; diferença **+5,6 pp** (a tela mostra a distância ao topo da faixa; contra o centro do GTO são 7,2). Leitura: acima da faixa (o field está acima do topo da faixa).

**Texto final do exemplo, PT:** "CO × BB em pote simples (SRP), 30–60bb (GTO a 40bb), torneios Regular, últimos 2 anos, flop K-high two-tone, sem par, desconectado, contra o c-bet de 33%. O field folda 46,0% contra 38,8% do GTO (faixa 37,1–40,4%): 5,6 pp acima do topo da faixa. Aqui o field folda mais do que o GTO. É um spot, não a média do field. Confira no seu board."

**Final example text, EN:** "CO × BB single-raised pot (SRP), 30–60bb (GTO at 40bb), Regular tournaments, last 2 years, K-high two-tone, unpaired, disconnected flop, facing a 33% c-bet. The field folds 46.0% against GTO's 38.8% (range 37.1–40.4%): 5.6 pp above the top of the range. Here the field folds more than GTO does. This is one spot, not the field average. Check it on your board."

**Exemplo de pré-flop (exemplo (b)):** RFI do CO, torneio Regular, stack 30–50bb (GTO a 40bb). Field abre **31,6%**; GTO abre **37,0%**; diferença **−5,4 pp** (o field abre de menos). PT: "No pré-flop, RFI do CO a 30–50bb (GTO a 40bb), torneios Regular, últimos 2 anos: o field abre 31,6% e o GTO abre 37,0%." EN: "Preflop, CO RFI at 30–50bb (GTO at 40bb), Regular tournaments, last 2 years: the field opens 31.6% and GTO opens 37.0%."

## O exemplo de abertura do agressor (novo; números pendentes da HUB)
Ação da abertura: second barrel (ou probe, conforme o spot que a HUB entregar). Métrica: frequência da aposta do agressor, field contra GTO, com a faixa GTO. Marcadores: **N7** spot (posições, pote, stack, filtro, board, rua), **N8** % do field, **N9** % GTO e faixa, **N10** diferença em pp. **Não inventar nenhum valor.**

**Texto-modelo, PT:** "[[N7: spot]]. O field aposta [[N8: % do field]] e o GTO aposta [[N9: % GTO e faixa]]: [[N10: diferença em pp]] pp de diferença. Aqui o field aposta [mais|menos] do que o GTO. É um spot, não a média do field. Confira no seu board."

**Model text, EN:** "[[N7: spot]]. The field bets [[N8: % do field]] and GTO bets [[N9: % GTO e faixa]]: a gap of [[N10: diferença em pp]] pp. Here the field bets [more|less] than GTO does. This is one spot, not the field average. Check it on your board."

Leitura de `[mais|menos]` / `[more|less]`: se o field está acima do topo da faixa, "mais" / "more"; se abaixo da base, "menos" / "less"; se dentro da faixa, trocar a frase por "O field está dentro da faixa GTO" / "The field is inside the GTO range" (e a diferença deixa de ser destaque).

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

Em toda arte, além do título e da linha de apoio: logo AURA, `@aurapokeranalytics · 18+` pequeno e, nos slides, o indicador "n / 7". Nas barras, o % central do GTO no rótulo e a faixa GTO como sombreado, com a faixa escrita pequena. Marcadores `[[...]]` nesta tabela são instrução para o designer: não renderizar o marcador, só o texto depois dele, e só depois de a HUB confirmar.

| Arte | Formato | Idioma | Título | Apoio (uma linha) | O que a imagem mostra |
|---|---|---|---|---|---|
| Feed | 1080x1350 | PT | Mesmo spot, dois números | CO × BB · K-high two-tone · c-bet de 33% | Barras de fold lado a lado: Field 46,0% e GTO 38,8% (faixa 37,1–40,4%) |
| Feed | 1080x1350 | EN | Same spot, two numbers | CO × BB · K-high two-tone · 33% c-bet | Fold bars side by side: Field 46.0% and GTO 38.8% (range 37.1–40.4%) |
| Story | 1080x1920 | PT | O field folda mais que o GTO? | CO × BB · K-high two-tone · c-bet de 33% | Mesmas barras (46,0% e 38,8%); sticker de link "Conhecer o Modo GTO" |
| Story | 1080x1920 | EN | Does the field fold more than GTO? | CO × BB · K-high two-tone · 33% c-bet | Same bars (46.0% and 38.8%); link sticker "See GTO Mode" |
| Story da capa do carrossel | 1080x1920 | PT | Onde o field sai do GTO? | Novo: Modo GTO (+ micro-legenda do spot: CO × BB · K-high two-tone · c-bet de 33%) | Mesmas barras com o gap em âmbar (46,0% e 38,8%); sticker "Conhecer o Modo GTO" |
| Carrossel 1 (capa) | 1080x1350 | EN | Where does the field leave GTO? | New: GTO Mode (+ spot micro-caption: CO × BB · K-high two-tone · 33% c-bet) | Mesma imagem da capa PT (46.0% and 38.8%) |
| Carrossel 2 | 1080x1350 | EN | Same spot, two numbers | CO × BB · K-high two-tone · 33% c-bet | As barras e os dois números: Field 46.0%, GTO 38.8% (range 37.1–40.4%) |
| Carrossel 3 | 1080x1350 | EN | [[CONFIRMAR-COBERTURA]] Postflop: GTO in every action | Flop, turn and river, with the GTO range. | Captura nova do Postflop com o Modo GTO ligado e o GTO nas ações (inclusive a abertura), no spot do exemplo |
| Carrossel 4 | 1080x1350 | EN | Preflop: GTO and deviation | [[CONFIRMAR-PREFLOP]] Includes CO and BTN RFI at 40bb. | Captura da grade com a célula do RFI do CO destacada: na tela, Field 32%, GTO 37%, −5 (arredondado; a fonte tem 31,6 / 37,0 / −5,4) |
| Carrossel 5 (novo) | 1080x1350 | EN | Second barrel: field vs GTO | [[N7: spot]] | Barras da abertura lado a lado: Field [[N8: % do field]] e GTO [[N9: % GTO e faixa]] com a faixa sombreada; gap em âmbar com [[N10: diferença em pp]] pp |
| Carrossel 6 | 1080x1350 | EN | GTO Mode, now in Individual | Part of the US$ 29/month plan, for a limited time. | Um cadeado desenhado (sem texto do app) |
| Carrossel 7 (CTA) | 1080x1350 | EN | See GTO Mode | Link in bio. | Logo e fundo da marca |

Contagem de palavras (regra do Rafael): títulos de 4 a 7 palavras; apoios de 3 a 10 palavras (o apoio do slide 3 tem 8; o do slide 6 tem 10; o do 5 é só a micro-legenda do spot, mesmo formato da capa).

Notas de arte:
- **Cores:** fold em teal `#015A6B`; a distância entre a barra do field e a do GTO em âmbar (o gap). Faixa GTO sombreada em volta da barra do GTO. No slide 5, a barra é de aposta (frequência de bet), não de fold: usar a cor semântica do raise (`#AD2C34`) para a aposta, mantendo o gap em âmbar e a faixa sombreada.
- **Slide 3:** a captura nova deve mostrar o GTO ao lado do field em mais de uma ação (a abertura e a reação). O número fica dentro da captura; nenhum texto de arte o repete. Não mostrar estado de carregamento nem aviso de "sem GTO".
- **Slide 4:** o stack da captura é 30–50bb (GTO a 40bb), torneio Regular. O número fica dentro da captura.
- **Slide 5 (novo):** só entra depois de N7 a N10. Se o spot for probe ou delayed c-bet em vez de second barrel, trocar o nome da ação no título ("Probe: field vs GTO").
- **Slide 6:** título "GTO Mode, now in Individual", apoio "Part of the US$ 29/month plan, for a limited time." (10 palavras; sem data, sem "últimas horas"). O cadeado desenhado continua. A frase completa sobre o plano Individual e a conta grátis fica na legenda. Pendente: a HUB confirma que o checkout cobra US$ 29 hoje. (Era o slide 5; renomear `carrossel-en-05` para 06.)
- **Slide 7:** CTA (era o slide 6; renomear `carrossel-en-06` para 07).
- **Enquete opcional no story (fora da arte):** "Qual spot você quer ver com o GTO ao lado?" com as opções "Flop" e "Turn/river" / "Which spot do you want to see with GTO next to it?" with "Flop" and "Turn/river".

## Legendas

### Legenda do feed
PT:
```
O GTO folda 38,8%. O field folda 46,0%. Mesmo spot.

Novo na Aura: Modo GTO. Ao lado da frequência do field, o número GTO e a faixa GTO.

Exemplo: CO × BB em pote simples (SRP), 30–60bb (GTO a 40bb), torneios Regular, últimos 2 anos, flop K-high two-tone, sem par, desconectado, contra o c-bet de 33%. O field folda 46,0% contra 38,8% do GTO (faixa 37,1–40,4%): 5,6 pp acima do topo da faixa. Aqui o field folda mais do que o GTO. É um spot, não a média do field. Confira no seu board.

[[CONFIRMAR-COBERTURA]] Pós-flop: o GTO em todas as ações, em flop, turn e river, inclusive as aberturas do agressor (c-bet, second barrel, probe). Escolha o spot, clique em Apply e veja o field e o GTO juntos. A cada clique, o app mostra o que falta para ver o GTO.

[[CONFIRMAR-PREFLOP]] Pré-flop: o GTO e o desvio nas células cobertas, inclusive o RFI de CO e BTN a 40bb.

O Modo GTO faz parte do plano Individual (R$ 150/mês) por tempo limitado. A conta grátis segue com o field e a comparação com o MDF.

Conhecer o Modo GTO, link na bio. Ferramenta de estudo. 18+.

#poker #pokerMTT #pokerestudo #aurapoker
```
EN:
```
GTO folds 38.8%. The field folds 46.0%. Same spot.

New on Aura: GTO Mode. Next to the field frequency, the GTO number and the GTO range.

Example: CO × BB single-raised pot (SRP), 30–60bb (GTO at 40bb), Regular tournaments, last 2 years, K-high two-tone, unpaired, disconnected flop, facing a 33% c-bet. The field folds 46.0% against GTO's 38.8% (range 37.1–40.4%): 5.6 pp above the top of the range. Here the field folds more than GTO does. This is one spot, not the field average. Check it on your board.

[[CONFIRMAR-COBERTURA]] Postflop: GTO in every action, on the flop, turn and river, including the aggressor's openings (c-bet, second barrel, probe). Pick the spot, hit Apply and see the field and GTO together. At every click, the app shows what is missing to see GTO.

[[CONFIRMAR-PREFLOP]] Preflop: the GTO and the deviation in the covered cells, including the CO and BTN RFI at 40bb.

GTO Mode is part of the Individual plan (US$ 29/month) for a limited time. The free account keeps the field and the MDF comparison.

See GTO Mode, link in bio. Study tool. 18+.

#poker #pokerMTT #pokerestudo #aurapoker
```

### Legenda do carrossel e da capa
PT (usar também com o story da capa, se o Rafael postar legenda):
```
Onde o field sai do GTO?

Novo na Aura: Modo GTO. Ao lado da frequência do field, o número GTO e a faixa GTO.

[[CONFIRMAR-COBERTURA]] Pós-flop: o GTO em todas as ações, em flop, turn e river, inclusive as aberturas do agressor. Escolha o spot, clique em Apply e veja o field e o GTO juntos. A cada clique, o app mostra o que falta para ver o GTO.

Reação: CO × BB em pote simples (SRP), 30–60bb (GTO a 40bb), torneios Regular, últimos 2 anos, flop K-high two-tone, sem par, desconectado, contra o c-bet de 33%. O field folda 46,0% contra 38,8% do GTO (faixa 37,1–40,4%): 5,6 pp acima do topo da faixa. Aqui o field folda mais do que o GTO. É um spot, não a média do field. Confira no seu board.

Abertura: [[N7: spot]]. O field aposta [[N8: % do field]] e o GTO aposta [[N9: % GTO e faixa]]: [[N10: diferença em pp]] pp de diferença. Aqui o field aposta [mais|menos] do que o GTO. É um spot, não a média do field.

[[CONFIRMAR-PREFLOP]] Pré-flop: o GTO e o desvio nas células cobertas, inclusive o RFI de CO e BTN a 40bb. RFI do CO a 30–50bb (GTO a 40bb), torneios Regular, últimos 2 anos: o field abre 31,6% e o GTO abre 37,0%.

O Modo GTO faz parte do plano Individual (R$ 150/mês) por tempo limitado. A conta grátis segue com o field e a comparação com o MDF.

Conhecer o Modo GTO, link na bio. Salve para estudar. Ferramenta de estudo. 18+.

#poker #pokerMTT #pokerestudo #aurapoker
```
EN:
```
Where does the field leave GTO?

New on Aura: GTO Mode. Next to the field frequency, the GTO number and the GTO range.

[[CONFIRMAR-COBERTURA]] Postflop: GTO in every action, on the flop, turn and river, including the aggressor's openings. Pick the spot, hit Apply and see the field and GTO together. At every click, the app shows what is missing to see GTO.

Response: CO × BB single-raised pot (SRP), 30–60bb (GTO at 40bb), Regular tournaments, last 2 years, K-high two-tone, unpaired, disconnected flop, facing a 33% c-bet. The field folds 46.0% against GTO's 38.8% (range 37.1–40.4%): 5.6 pp above the top of the range. Here the field folds more than GTO does. This is one spot, not the field average. Check it on your board.

Opening: [[N7: spot]]. The field bets [[N8: % do field]] and GTO bets [[N9: % GTO e faixa]]: a gap of [[N10: diferença em pp]] pp. Here the field bets [more|less] than GTO does. This is one spot, not the field average.

[[CONFIRMAR-PREFLOP]] Preflop: the GTO and the deviation in the covered cells, including the CO and BTN RFI at 40bb. CO RFI at 30–50bb (GTO at 40bb), Regular tournaments, last 2 years: the field opens 31.6% and GTO opens 37.0%.

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
- PT: [[CONFIRMAR-COBERTURA]] Modo GTO: em todas as ações do pós-flop, o número GTO e a faixa GTO ao lado da frequência do field. Veja onde o field sai da faixa e estude esse spot.
- EN: [[CONFIRMAR-COBERTURA]] GTO Mode: in every postflop action, the GTO number and the GTO range next to the field frequency. See where the field leaves the range and study that spot.

## 3 bullets
PT:
- [[CONFIRMAR-COBERTURA]] Pós-flop: flop, turn e river, inclusive as aberturas do agressor (c-bet, second barrel, probe), cada ação com o número GTO e a faixa GTO ao lado do field. Escolha o spot, clique em Apply e veja os dois juntos; a cada clique, o app mostra o que falta para ver o GTO.
- [[CONFIRMAR-PREFLOP]] Pré-flop: a grade traz o GTO e o desvio nas células cobertas, inclusive o RFI de CO e BTN a 40bb. No RFI do CO a 30–50bb (GTO a 40bb), torneios Regular, últimos 2 anos, o field abre 31,6% e o GTO abre 37,0%.
- Exemplo: CO × BB em pote simples (SRP), 30–60bb (GTO a 40bb), torneios Regular, últimos 2 anos, flop K-high two-tone, sem par, desconectado, contra o c-bet de 33%. O field folda 46,0% contra 38,8% do GTO (faixa 37,1–40,4%): 5,6 pp acima do topo da faixa. Aqui o field folda mais do que o GTO. É um spot, não a média do field. Confira no seu board.

EN:
- [[CONFIRMAR-COBERTURA]] Postflop: flop, turn and river, including the aggressor's openings (c-bet, second barrel, probe), each action with the GTO number and the GTO range next to the field. Pick the spot, hit Apply and see both together; at every click, the app shows what is missing to see GTO.
- [[CONFIRMAR-PREFLOP]] Preflop: the grid carries the GTO and the deviation in the covered cells, including the CO and BTN RFI at 40bb. On the CO RFI at 30–50bb (GTO at 40bb), Regular tournaments, last 2 years, the field opens 31.6% and GTO opens 37.0%.
- Example: CO × BB single-raised pot (SRP), 30–60bb (GTO at 40bb), Regular tournaments, last 2 years, K-high two-tone, unpaired, disconnected flop, facing a 33% c-bet. The field folds 46.0% against GTO's 38.8% (range 37.1–40.4%): 5.6 pp above the top of the range. Here the field folds more than GTO does. This is one spot, not the field average. Check it on your board.

Nota de rodapé da seção (PT): "Um spot, não a média do field. Ferramenta de estudo · 18+. A Aura não é site de apostas e não oferece jogo."
Footnote (EN): "One spot, not the field average. Study tool · 18+. Aura is not a betting site and does not offer gambling."
(Os números de escala de 08/10 saíram deste rodapé: ver Pendências, item 8.)

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

Texto completo, com URLs, em `discord.md` (mesma pasta). PT e EN, abaixo de 1.200 caracteres cada, com os marcadores contados. Tamanho real e emojis: ver `discord.md`. **Só postar depois do teste logado, do P-61 no ar e da confirmação dos marcadores.**

---

# (d) E-mail

Texto, assuntos, preheader e notas técnicas em `email.md`. Corpo curto, um exemplo (CO × BB) e a comparação field × GTO dele. Botão "Conhecer o Modo GTO" / "See GTO Mode". O HTML atual (`email-pt.html` e `email-en.html`) é da versão de 08/10 e precisa ser atualizado por outro agente conforme `email.md`. A imagem do e-mail (`email/modo-gto-pt.png` e `-en.png`) tem os mesmos números do exemplo de 08/10 (46,0% e 38,8%, faixa 37,1–40,4%), a reconfirmar.

---

## Números usados (de `numeros-verificados.md`, 08/10, leitura de produção; a reconfirmar no snapshot de 13/10)

| Número no texto | Valor | Seção da fonte | Onde aparece | Estado |
|---|---|---|---|---|
| Spot do exemplo (antigo N1) | CO × BB · SRP · 30–60bb (GTO a 40bb) · Regular (Vanilla) · flop K-high, two-tone, sem par, desconectado · c-bet de 33% | Exemplo (a) | Linha de apoio do feed; legendas, Discord, landing, e-mail | a reconfirmar |
| Field folda (N2) | 46,0% (EN 46.0%) | Exemplo (a), `potPercentage` do `actionSize` 2 | Barras (feed, stories, carrossel 1 e 2); legendas, Discord, landing, e-mail | a reconfirmar |
| GTO folda e faixa (N3) | 38,8% (38,78 na API); faixa 37,1–40,4% (37,13–40,43) | Exemplo (a), `gtoFold` e `gtoBand.fold` | Barras com a faixa como sombreado; legendas, Discord, landing, e-mail | a reconfirmar |
| Diferença (N4) | +5,6 pp (acima do topo da faixa, como a tela mostra; 7,2 é contra o centro) | Exemplo (a) | Só texto: legendas, Discord, landing (o e-mail novo não a cita) | a reconfirmar |
| Pré-flop (N5) | RFI do CO, Regular, 30–50bb (GTO a 40bb): field abre 31,6%, GTO abre 37,0%, −5,4 pp | Exemplo (b) e "Pré-flop" (37 %) | Captura do slide 4; legenda do carrossel e landing (bullet 2). O −5,4 pp não é citado no texto | a reconfirmar (`[[CONFIRMAR-PREFLOP]]`) |
| Escala (N6) | 30 situações, 2.330 flops, 6.980.568 nós de turn e river, 225 decisões de pré-flop (08/10) | "Pós-flop" e "Pré-flop" | **Fora de todas as peças** nesta versão (descreviam a cobertura antiga) | aguardando fonte nova |
| Spot da abertura (N7) | `[[N7: spot]]` | HUB (a fornecer) | Slide 5 (apoio), legenda do carrossel | pendente |
| Field aposta (N8) | `[[N8: % do field]]` | HUB (a fornecer) | Slide 5 (barra), legenda do carrossel | pendente |
| GTO aposta e faixa (N9) | `[[N9: % GTO e faixa]]` | HUB (a fornecer) | Slide 5 (barra e faixa), legenda do carrossel | pendente |
| Diferença da abertura (N10) | `[[N10: diferença em pp]]` | HUB (a fornecer) | Slide 5 (gap), legenda do carrossel | pendente |

Não usados, por instrução da fonte e da HUB: as 10.216 mãos e as 23,8 milhões de oportunidades; contagens de linhas; o candidato SB × BB 3-bet (amostra pequena); RFI do BTN a 40bb (51%), que fica disponível para peças de sustentação.
