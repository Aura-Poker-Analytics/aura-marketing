# Field Trends: copy de lançamento

Status: rascunho para aprovação do Rafael. Não publicado, sem commit.
@aurapokeranalytics: a confirmar pelo Rafael. URLs com UTM prontas na tabela abaixo.
Fonte única dos números: `aura-main/_ops/field-trends-launch/numeros-verificados.md` (versão de 07/10, que apareceu durante a escrita e substituiu os marcadores `XX` do primeiro rascunho). Cada número usado está mapeado no bloco "Números usados" no fim. **Nenhum `XX` restou no pacote.**
Peças deste pacote: Discord (também em `discord.md`), Instagram (feed, story, carrossel), landing e e-mail (em `email.md`, `email-pt.html`, `email-en.html` e os `*.preview.html`).

## Pendências de produto (conferir antes de aprovar)
1. **Filtros.** O briefing cita filtros por buy-in, stack e posição. O STATE do produto de 06/10 lista posição como fora dos filtros desta versão do Field Trends (entram buy-in, stack, etapa, perfil, Regular/KO). Por isso o texto diz só **"buy-in e stack"**. Se posição entrou, trocar nas linhas: Discord PT/EN ("Filtros por buy-in e stack"), landing bullet 3 e e-mail (frase sob o botão). As artes e as legendas do Instagram não citam filtro por nome (a legenda diz só que "o resto é dos planos pagos").
2. **O que o plano Grátis vê (B2).** Pelo STATE e pelo roteiro de release (§6), o Grátis só vê um teaser (IP Flop CBet com buy-in até US$ 22), e qualquer filtro abre o paywall. Os cards "o que mudou", Regs e fish, filtros e a lista completa são dos planos pagos. O botão pedido pelo Rafael segue "Acesse grátis" / "Get free access", e perto dele (Discord, landing, e-mail) está a frase: PT "A conta grátis abre uma prévia do Field Trends; as variações significativas, os filtros e a lista completa de stats são dos planos pagos." / EN "The free account opens a Field Trends preview; the significant changes, filters and the full stat list are on paid plans." Nas legendas do Instagram (feed e carrossel) a frase é a versão curta: PT "Conta grátis, link na bio (abre só uma prévia)." / EN "Free account, link in bio (opens only a preview)." Nenhuma peça promete ao Grátis o painel de mudanças do field. Se o Rafael decidir abrir mais coisa no Grátis, ajustar essas frases. As artes seguem essa leitura: o slide 5 do carrossel diz "Open Field Trends" / "Free account · link in bio" e os stories dizem "Conta grátis" / "Free account".
3. **Só publicar depois do smoke logado do Rafael (estado real em 07/10, conforme `aura-main/_ops/field-trends-launch/roteiro-release.md` §8).** O roteiro registra como **já executados em 07/10**: promote do banco na Azure (`--verify` ok, GRANT ao papel read-only), publish da API (`deploy-4d370aa.zip`, app setting `FieldTrends__ExcludedQuarters__0=20251`), smoke anônimo (401 nas 4 rotas do Field Trends e nas demais conferidas) e a flag do front (#86 mesclado, `792e1b8`, bundle `index-BdNKbc3s.js` com `isFieldTrendsEnabled` verdadeiro). **Falta o smoke logado com conta paga, que o roteiro deixa com o Rafael** (o smoke com conta Grátis, previsto no §6, não consta como executado no §8). Nenhuma peça deste pacote deve sair antes desse smoke. Datas e ordem são do Rafael.
4. **2T26 em curso.** A fonte exige citar sempre "até o 2T26 (em curso)". Todo número com 2T26 leva a marca no texto. Se a publicação cair depois do fechamento do trimestre e os números forem relidos, reescrever sem "em curso".
5. **Os números do exemplo são do field inteiro, não de um spot.** Fold to IP Flop CBet (43,62% para 44,99%) é a média do field no flop, todas as posições. Por isso o exemplo diz "você dá c-bet IP no flop", sem BTN contra BB, sem textura de board e sem stack. Não acrescentar spot específico sem número do spot.
6. **`product-truth-aura.md`** não existe neste worktree nem no `aura-context`. Li `AGENTS.md`, `brand-kit.md`, o plano de marketing, os números verificados e o roteiro de release. Se o arquivo existir em outro lugar, vale uma conferência rápida das frases de produto.
7. **Stats citadas.** c-bet, fold to c-bet, donk e probe aparecem na fonte (IP Flop CBet, Fold to IP Flop CBet, Fold to OOP Flop Donk Bet, OOP Probe Bet), então a lista do briefing está coberta.
8. **Formato das artes (Rafael, 08/10).** Carrossel só em inglês, 5 slides (capa, os 5 cards, gráfico com a faixa, card do Fold to c-bet IP, CTA). A capa em PT-BR é o story (1080x1920, "O field mudou? / Trimestre a trimestre."); há também story EN e feed PT/EN, todos com a pílula NOVO MÓDULO / NEW MODULE. As artes não têm número digitado: os 43,62%, 44,99%, +1,36, ± 0,77 e 42,99% → 41,84% ficam só nas legendas, no Discord, na landing e no e-mail. Os únicos números nas artes são os dos cards do app (ver "Números usados").

## Regra de leitura do exemplo (A1)
O exemplo é do field inteiro, não de um spot: nenhuma peça afirma que o exploit continua valendo nem que o c-bet de bluff ganha fold equity sem o qualificador "em média, no field inteiro" e o convite "confira no seu spot". Frase longa (Discord, landing, e-mail): PT "No field inteiro, o fold to c-bet IP subiu 1,36 pp, então em média o c-bet de bluff IP tem um pouco mais de fold equity. Confira no seu spot." / EN "Across the whole field, the IP fold to c-bet rose 1.36 pp, so on average the IP bluff c-bet has a little more fold equity. Check it in your own spot." Versão curta (legendas do Instagram, feed e carrossel): PT "No field inteiro, o fold to c-bet IP subiu 1,36 pp: em média, o c-bet de bluff IP tem um pouco mais de fold equity. Confira no seu spot." / EN "Across the whole field, the IP fold to c-bet rose 1.36 pp: on average, the IP bluff c-bet has a little more fold equity. Check it in your own spot."
Regra do 2T26 (A4): todo número do 2T26 em texto leva "(2T26 em curso)" / "(2Q26 in progress)", inclusive o 41,84% do call e a soma de 75,7 milhões de mãos. Nas artes não há número do 2T26 digitado; os dos cards do app vêm do próprio print, e o rodapé de cada arte diz "2T26 em curso" / "2Q26 in progress".

## URLs por peça
Regra: Discord leva ao app (`https://www.aura.poker/`); Instagram e e-mail levam à landing (`https://www.aurapoker.com/`). Parâmetros: `utm_source=<fonte>&utm_medium=<meio>&utm_campaign=field-trends-launch&utm_content=<peça>`.

| Peça | Destino | utm_source | utm_content | URL |
|---|---|---|---|---|
| Discord PT | app | discord | discord-pt | https://www.aura.poker/?utm_source=discord&utm_medium=social&utm_campaign=field-trends-launch&utm_content=discord-pt |
| Discord EN | app | discord | discord-en | https://www.aura.poker/?utm_source=discord&utm_medium=social&utm_campaign=field-trends-launch&utm_content=discord-en |
| Feed (link na bio) | landing | instagram | feed | https://www.aurapoker.com/?utm_source=instagram&utm_medium=social&utm_campaign=field-trends-launch&utm_content=feed |
| Story (sticker de link) | landing | instagram | story | https://www.aurapoker.com/?utm_source=instagram&utm_medium=social&utm_campaign=field-trends-launch&utm_content=story |
| Carrossel (link na bio) | landing | instagram | carrossel | https://www.aurapoker.com/?utm_source=instagram&utm_medium=social&utm_campaign=field-trends-launch&utm_content=carrossel |
| Landing (botão de CTA, para o cadastro no app) | app | landing | field-trends (utm_medium=website) | https://www.aura.poker/Login?tab=signup&utm_source=landing&utm_medium=website&utm_campaign=field-trends-launch&utm_content=field-trends |
| E-mail PT | landing | email | pt | https://www.aurapoker.com/?utm_source=email&utm_medium=email&utm_campaign=field-trends-launch&utm_content=pt |
| E-mail EN | landing | email | en | https://www.aurapoker.com/?utm_source=email&utm_medium=email&utm_campaign=field-trends-launch&utm_content=en |

Observação: para o botão da landing mantive `utm_source=landing`, como no Field Ranges. Ajustar se o Rafael preferir outro valor.

## Rodapé padrão (um só)
- PT: "Dados: Aura · 11 trimestres, até o 2T26 (em curso) · 18+"
- EN: "Data: Aura · 11 quarters, through 2Q26 (in progress) · 18+"

Regra: o rodapé usa só o número de trimestres (nas legendas do Instagram, "Dados: Aura, 11 trimestres"; nas artes, a versão curta "Dados: Aura · 2T26 em curso"). O 75,7 milhões de mãos é do c-bet IP no flop, não do módulo inteiro, então só aparece colado a esse stat ("só o c-bet IP no flop soma 75,7 milhões de mãos") e nunca como base do módulo. Nenhuma arte nem legenda do Instagram usa esse número.

---

# (a) Instagram

## Legenda do feed (1080x1350)

Regra de texto (Rafael, 08/10): por arte, no máximo 1 título curto e 1 linha de apoio; a imagem do app fala. Sem diagrama, sem número digitado (os 43,62%, 44,99% e ± 0,77 saem das artes e ficam só nas legendas); os únicos números na arte são os que estão nos cards do app.

Texto na arte (PT), idêntico ao `instagram/feed-pt.png` (fonte: `instagram/src/build.py`):
- Pílula âmbar + kicker: NOVO MÓDULO · FIELD TRENDS
- Título: O FIELD MUDOU. E O SEU EXPLOIT?
- Imagem: os 5 cards do app (field inteiro, 1 ano)
- CTA (âmbar): Já na Aura · conta grátis, link na bio
- Rodapé: @aurapokeranalytics · Dados: Aura · 2T26 em curso · 18+

Texto na arte (EN), idêntico ao `instagram/feed-en.png`:
- Amber pill + kicker: NEW MODULE · FIELD TRENDS
- Title: THE FIELD CHANGED. YOUR EXPLOIT?
- Image: the 5 app cards (whole field, 1 year)
- CTA (amber): Now on Aura · free account, link in bio
- Footer: @aurapokeranalytics · Data: Aura · 2Q26 in progress · 18+

Nota de arte: selo "NOVO MÓDULO" / "NEW MODULE" (nunca "Beta"). A leitura do exemplo (fold to c-bet IP, faixa de variação normal, fold equity) fica só na legenda.

Legenda PT:
```
Novo módulo na Aura: Field Trends.

O field mudou. O seu exploit ainda vale? São 114 stats do pós-flop, e 23 das 114 mudaram de forma significativa no último ano.

Fold to c-bet IP no flop: 43,62% (2T25) → 44,99% (2T26 em curso), acima da faixa de variação normal (± 0,77 pp). O call foi de 42,99% para 41,84% (2T26 em curso).

No field inteiro, o fold to c-bet IP subiu 1,36 pp: em média, o c-bet de bluff IP tem um pouco mais de fold equity. Confira no seu spot.

Conta grátis, link na bio (abre só uma prévia). Dados: Aura, 11 trimestres. 18+.

#poker #pokerMTT #pokerestudo #pokerstrategy #aurapoker
```

Legenda EN:
```
New module on Aura: Field Trends.

The field changed. Does your exploit still hold? 114 postflop stats, and 23 of the 114 changed significantly over the past year.

IP flop fold to c-bet: 43.62% (2Q25) → 44.99% (2Q26 in progress), above the normal variation band (± 0.77 pp). The call went from 42.99% to 41.84% (2Q26 in progress).

Across the whole field, the IP fold to c-bet rose 1.36 pp: on average, the IP bluff c-bet has a little more fold equity. Check it in your own spot.

Free account, link in bio (opens only a preview). Data: Aura, 11 quarters. 18+.

#poker #MTT #pokerstrategy #pokerstudy #aurapoker
```

## Story (1080x1920)

Nota ao designer: o story PT-BR é a capa em português; o story EN espelha. Sem diagrama e sem número digitado; a imagem são 4 cards do app. Sem selo de fase nem convite a feedback. Sem legenda longa: uma linha de CTA (abaixo).

Linha de CTA do story (texto de postagem, não da arte): PT "Novo módulo na Aura: Field Trends. Conta grátis no link (abre uma prévia)." / EN "New module on Aura: Field Trends. Free account at the link (opens a preview)."

Texto na arte (PT), idêntico ao `instagram/story-pt.png` (fonte: `instagram/src/build.py`):
- Topo: logo; pílula NOVO MÓDULO + FIELD TRENDS
- Título: O FIELD MUDOU?
- Apoio: Trimestre a trimestre.
- Imagem: 4 cards do app
- Botão (sticker de link): Conta grátis
- Rodapé: Dados: Aura · 2T26 em curso · selo 18+

Texto na arte (EN), idêntico ao `instagram/story-en.png`:
- Top: logo; NEW MODULE pill + FIELD TRENDS
- Title: DID THE FIELD CHANGE?
- Support: Quarter by quarter.
- Image: 4 app cards
- Button (link sticker): Free account
- Footer: Data: Aura · 2Q26 in progress · 18+ badge

Instrução ao designer (fora do texto da arte): o botão de CTA é o sticker de link do Instagram, com o texto "Conta grátis" / "Free account". Sticker de enquete opcional: "O seu c-bet IP ainda vale?" / "Does your IP c-bet still hold?" com opções "Confiro a stat" / "Vou revisar" e "I will check the stat" / "I will review it".

## Carrossel (5 slides, 1080x1350, SÓ EM INGLÊS)

Texto idêntico ao das artes finais (`instagram/carrossel-en-01..05.png`; fonte: `instagram/src/build.py`). Arte e legenda só em inglês. Regra: 1 título curto + 1 linha de apoio por slide, sem parágrafo. Indicador "n / 5" no topo. Rodapé: @aurapokeranalytics · "Data: Aura · 2Q26 in progress" (slides 1 a 4; o 5 leva só o handle) · selo 18+. Os cards e o gráfico são capturas do app (imagem), não texto de arte. A capa em PT-BR é o story.

- Slide 1 (capa): pílula NEW MODULE + FIELD TRENDS / "DID THE FIELD CHANGE?" / "Quarter by quarter." / 2 cards do app (Fold to IP Flop CBet, Call vs IP Flop CBet)
- Slide 2: "WHAT CHANGED THIS YEAR" / "Change over 1 year." / os 5 cards do app
- Slide 3: "REAL CHANGE OR NORMAL VARIATION?" / "The shaded band is normal variation." / gráfico do app (IP Flop CBet %, com a faixa clareada só em cor)
- Slide 4: "FOLD TO C-BET IP" / "Above the normal variation band." / card do app Fold to IP Flop CBet
- Slide 5 (CTA): pílula NEW MODULE + FIELD TRENDS / "OPEN FIELD TRENDS" / botão "Free account · link in bio" / 18+

Contagem de palavras (título + apoio, sem pílula, kicker, rodapé nem texto dos prints): feed PT 7 + CTA 7; feed EN 5 + CTA 8; story PT 3 + 3 (+ botão 2); story EN 4 + 3 (+ botão 2); carrossel 1: 4 + 3; 2: 4 + 4; 3: 5 + 6; 4: 4 + 5; 5: 3 + botão 5.

Nota de arte: nenhum número digitado; só os que aparecem nos cards do app. Nunca "Beta".

### Legenda do carrossel (só EN)
```
New module on Aura: Field Trends.

Did the field change? 114 postflop stats, and 23 of the 114 moved significantly over the past year. Each stat has its own normal variation band: inside it, drift; outside it, the field changed.

Example, IP flop fold to c-bet: 43.62% (2Q25) → 44.99% (2Q26 in progress), outside the ± 0.77 pp band. The call went from 42.99% to 41.84% (2Q26 in progress).

Across the whole field, the IP fold to c-bet rose 1.36 pp: on average, the IP bluff c-bet has a little more fold equity. Check it in your own spot.

Free account, link in bio (opens only a preview). Data: Aura, 11 quarters. 18+.

#poker #MTT #pokerstrategy #pokerstudy #aurapoker
```

---

# (b) Landing

@aurapokeranalytics: a confirmar pelo Rafael. URL do CTA: ver a linha "Landing" da tabela "URLs por peça" no topo.

## Anúncio (kicker acima do título, com a pílula de novo módulo)
- PT: Novo módulo na Aura: Field Trends
- EN: New module on Aura: Field Trends

## Título
- PT: O field mudou. O seu exploit ainda vale?
- EN: The field changed. Does your exploit still hold?

## Subtítulo
- PT: Field Trends: 114 stats do field de MTT no pós-flop, trimestre a trimestre, com as mudanças significativas do último ano em destaque e a faixa de variação normal de cada stat para você separar mudança real de oscilação.
- EN: Field Trends: 114 MTT field stats on the postflop, quarter by quarter, with the significant changes of the past year highlighted and each stat's normal variation band, so you can tell a real change from drift.

## 3 bullets
PT:
- Stat por stat: 30 ações e 84 reações (c-bet, fold to c-bet, donk, probe e mais), em 11 trimestres. Só o c-bet IP no flop soma 75,7 milhões de mãos (a soma inclui o 2T26, em curso).
- Real ou variação normal: no último ano, 23 das 114 stats tiveram variação significativa. Exemplo: o fold to c-bet IP foi de 43,62% (2T25) para 44,99% (2T26 em curso), acima da faixa de ± 0,77 pp. Mudança real, e pequena. No field inteiro, o fold to c-bet IP subiu 1,36 pp, então em média o c-bet de bluff IP tem um pouco mais de fold equity. Confira no seu spot.
- Confira onde você joga: filtros por buy-in e stack (planos pagos).

EN:
- Stat by stat: 30 actions and 84 reactions (c-bet, fold to c-bet, donk, probe and more), over 11 quarters. The IP flop c-bet alone adds up to 75.7 million hands (the sum includes 2Q26, in progress).
- Real or normal variation: over the past year, 23 of the 114 stats had a significant change. Example: the IP fold to c-bet went from 43.62% (2Q25) to 44.99% (2Q26 in progress), above the ± 0.77 pp band. A real change, and a small one. Across the whole field, the IP fold to c-bet rose 1.36 pp, so on average the IP bluff c-bet has a little more fold equity. Check it in your own spot.
- Check where you play: buy-in and stack filters (paid plans).

Nota de rodapé da seção (PT): "Field inteiro, 2T25 a 2T26 (o 2T26 está em curso). Cada stat tem a sua própria faixa de variação normal. Filtros e lista completa de stats nos planos pagos. Dados: Aura, 11 trimestres."
Footnote (EN): "Whole field, 2Q25 to 2Q26 (2Q26 is in progress). Each stat has its own normal variation band. Filters and the full stat list on paid plans. Data: Aura, 11 quarters."
Frase sob o CTA (B2), PT: "A conta grátis abre uma prévia do Field Trends; as variações significativas, os filtros e a lista completa de stats são dos planos pagos." / EN: "The free account opens a Field Trends preview; the significant changes, filters and the full stat list are on paid plans." A nota de rodapé acima já repete a ideia ("Filtros e lista completa de stats nos planos pagos"); manter as duas.
CTA: PT "Criar conta grátis" / EN "Create free account". (Botão não alterado nesta rodada; se o Rafael quiser o mesmo "Acesse grátis" / "Get free access" do e-mail, trocar aqui.)
Números usados na landing: 114, 30, 84 (seção 3), 11 e 75,7 milhões (seções 1 e 2), 23 (seção 6), 43,62%, 44,99%, +1,36, ± 0,77 (seção 4). Ficam só no texto, nunca atribuídos a uma imagem.

## Alt text das imagens (2)

### Imagem 1: o que mudou no field
- PT: "Painel do Field Trends com as stats do field que mudaram de forma significativa no último ano, cada uma com a variação trimestre a trimestre."
- EN: "Field Trends panel with the field stats that changed significantly over the past year, each showing its quarter-by-quarter movement."

### Imagem 2: uma stat com a faixa de variação normal
- PT: "Gráfico trimestral de uma stat do field com a faixa de variação normal em volta da linha, mostrando se a mudança sai da faixa."
- EN: "Quarterly chart of a field stat with the normal variation band around the line, showing whether the change leaves the band."

### Imagem 3 (filtros): FICA FORA
Não há mockup de filtros, então o alt text da imagem 3 foi removido. O bullet 3 ("filtros por buy-in e stack (planos pagos)") segue só como texto. Se um mockup de filtros existir no futuro, escrever o alt text na hora.

- Nota para o designer: as imagens não mostram percentuais além dos que estão em `numeros-verificados.md`. Não atribuir a nenhuma imagem os números do texto. Não mostrar número de pré-flop nem de filtro por buy-in (a fonte manda não citar).

---

# (c) Discord

Texto completo, com URLs, em `discord.md` (mesma pasta). PT e EN, abaixo de 1.200 caracteres cada (estimativa manual, cerca de 1.160 PT e 1.170 EN), 3 emojis funcionais (📈 título, 🔎 convite, 👉 CTA), abre com o anúncio de novo módulo, sem selo de fase e sem pedido de feedback. Mantida igual ao `discord.md`. **Só postar depois do smoke logado com conta paga:** banco, API e flag já foram executados em 07/10 pelo `roteiro-release.md`; falta o smoke logado do Rafael.

**PT**
```
📈 **Novo módulo na Aura: Field Trends**

O field mudou, e o seu exploit ainda vale? Das 114 stats do pós-flop, 23 tiveram variação significativa no último ano, trimestre a trimestre.

**Exemplo de spot**
Você dá c-bet IP no flop. O field folda 43,62% (2T25) e 44,99% (2T26 em curso), acima da faixa de variação normal (± 0,77 pp). Mudança real, e pequena. O call caiu de 42,99% para 41,84% (2T26 em curso).
No field inteiro, o fold to c-bet IP subiu 1,36 pp, então em média o c-bet de bluff IP tem um pouco mais de fold equity. Confira no seu spot.

**O que você vê**
- As mudanças significativas do último ano
- A faixa de variação normal de cada stat
- Filtros por buy-in e stack

**Base:** 75,7 mi de mãos só no c-bet IP no flop, em 11 trimestres (3T23 a 2T26, sem o 1T25). A soma inclui o 2T26, em curso.

🔎 Veja no Field Trends se o field mudou nas stats que você explora.

A conta grátis abre uma prévia do Field Trends; as variações significativas, os filtros e a lista completa de stats são dos planos pagos.
👉 Acesse grátis: https://www.aura.poker/?utm_source=discord&utm_medium=social&utm_campaign=field-trends-launch&utm_content=discord-pt
```

**EN**
```
📈 **New module on Aura: Field Trends**

The field changed, does your exploit still hold? Of the 114 postflop stats, 23 had a significant change over the past year, quarter by quarter.

**Example spot**
You c-bet IP on the flop. The field folds 43.62% (2Q25) and 44.99% (2Q26 in progress), above the normal variation band (± 0.77 pp). A real change, and a small one. The call dropped from 42.99% to 41.84% (2Q26 in progress).
Across the whole field, the IP fold to c-bet rose 1.36 pp, so on average the IP bluff c-bet has a little more fold equity. Check it in your own spot.

**What you see**
- The significant changes of the past year
- The normal variation band of every stat
- Buy-in and stack filters

**Data:** 75.7M hands on the IP flop c-bet alone, over 11 quarters (3Q23 to 2Q26, excluding 1Q25). The sum includes 2Q26, still in progress.

🔎 See in Field Trends whether the field changed in the stats you exploit.

The free account opens a Field Trends preview; the significant changes, filters and the full stat list are on paid plans.
👉 Get free access: https://www.aura.poker/?utm_source=discord&utm_medium=social&utm_campaign=field-trends-launch&utm_content=discord-en
```

---

# (d) E-mail

Texto, assuntos, preheader e notas técnicas em `email.md`. HTML em `email-pt.html` e `email-en.html`; abrir do disco pelos `email-pt.preview.html` e `email-en.preview.html`. Assunto recomendado: a 1 ("Novo módulo na Aura: Field Trends" / "New module on Aura: Field Trends"); a 2 ("O field mudou. O seu exploit ainda vale?" / "The field changed. Does your exploit still hold?") fica como alternativa. O corpo abre com o anúncio e só depois traz a pergunta. A frase sob o botão diz que a conta grátis abre uma prévia.

---

## Pendências de número

**Nenhuma.** O `numeros-verificados.md` chegou durante a escrita e todos os `XX` foram trocados por número com fonte. Não sobrou marcador. O que segue em aberto é de produto, não de número (ver "Pendências de produto" no topo): filtro de posição, o que o Grátis vê e a aba no ar antes de publicar.

## Números usados (todos de `numeros-verificados.md`, versão de 07/10)

| Número no texto | Seção da fonte | Onde aparece |
|---|---|---|
| 114 stats (30 ações e 84 reações) | §3 | Discord, legendas do feed (PT/EN) e do carrossel (EN), landing (subtítulo, bullets 1 e 2), e-mail. Nenhuma arte |
| 23 das 114 com variação significativa em 1 ano | §6 | Discord, legendas do feed e do carrossel, landing bullet 2, e-mail. Nenhuma arte |
| 75,7 milhões de mãos (c-bet IP no flop, 11 trimestres, 3T23 a 2T26, sem o 1T25; a soma inclui o 2T26 em curso, e o texto diz isso) | §1 e §2 | Discord (Base), landing bullet 1. Nenhuma arte nem legenda do Instagram |
| 11 trimestres (3T23 a 2T26, em curso) | §2 | legendas do feed e do carrossel ("Dados: Aura, 11 trimestres"), Discord, landing (nota), e-mail (linha "Dados"). Nas artes, o rodapé diz só "2T26 em curso" / "2Q26 in progress" |
| Fold to IP Flop CBet 43,62% (2T25) para 44,99% (2T26), +1,36 pp, faixa ± 0,77 | §4 | Discord, legendas do feed e do carrossel, landing bullet 2, e-mail. Digitado em nenhuma arte |
| Call vs IP Flop CBet 42,99% para 41,84% | §5 | Discord, legendas do feed e do carrossel. Digitado em nenhuma arte |
| Números dos cards do app (aparecem só dentro do print, nunca digitados): 45,0% / 1,4 (Fold to IP Flop CBet), 41,8% / 1,1 (Call vs IP Flop CBet), 43,8% / 0,9 (OOP Probe Bet), 12,9% / 0,6 (Raise vs IP Float Flop), 28,0% / 1,1 (Fold to OOP Flop Donk Bet) | §4, §5, §7 e "Outras mudanças reais" (44,99 / +1,36; 41,84 / −1,15; 43,76 / −0,87; 12,88 / −0,65; 28,02 / +1,13; o app arredonda como mostra) | Artes: feed PT/EN, stories PT/EN e carrossel EN (slides 1, 2 e 4). Todos em `numeros-verificados.md` |

Não usados, por instrução da fonte: qualquer número de pré-flop, de filtro por buy-in e o 78,9% do Grátis. As outras mudanças reais da fonte (donk, probe) aparecem só como números dentro dos cards do app nas artes; no texto, e o delayed c-bet inteiro, ficaram de fora para não pesar; podem entrar em peças de sustentação.
