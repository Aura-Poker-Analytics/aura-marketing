# Verdade Canônica do Produto — Aura 2.0 (gabarito de marketing)

**Consolidado:** 2026-07-09 por workflow multi-agente (5 agentes sonnet estudaram `aura-context` + `aura-landing`), verificado pela Fábrica.
**Uso:** é o GABARITO de tudo que a copy pode afirmar. Qualquer peça (arte, legenda, landing, ad) checa contra aqui. Resolve conflito em favor da confirmação mais recente do dono.

---

## 0. O que a Aura É / NÃO É
- **É** uma categoria própria: **inteligência de exploit da POPULAÇÃO (field) de MTT** — mede o que o field realmente faz (frequências reais), não teoria.
- **NÃO é tracker**: não mostra winrate/ROI/bankroll pessoal do herói (o lake só tem `chipswon` bruto do vencedor, sem payout por jogador).
- **NÃO é solver**: não compara com GTO, não tem overlay solver×pool, não calcula EV por spot. Hoje é 100% **descritivo** (frequência observada) + um sinal de exploit real: **pressão de fold vs MDF** (heurística, nunca chamada de "GTO"). ⚠️ Sobre o que o sinal de MDF **não** prova, ver §10.

## 1. Número-herói e prova
- **500M+ mãos auditadas** (nunca "bilhões" — confirmado pelo dono, 09/07).
- **7 salas cobertas**: PokerStars/PS_ES, GGPoker, WPN, Coin, Chico, WPT, Pacific (confirmado pelo dono como verdade de marketing).
  - *Interno, não publicar:* ~89% do volume carregado hoje é família PokerStars. Falar em "7 salas cobertas", nunca em proporção/volume por sala.
- 100% anonimizado (nenhuma mão ligada a nick/conta/jogador). Toda frequência vem com **intervalo de confiança (Wilson) + tamanho de amostra**; nada é mostrado sem massa crítica. Dataset **atualizado trimestralmente**.
- ⚠️ Depoimentos hoje no site (Lucas M., Ana P., Rafael C.) são **FICTÍCIOS** — remover, não usar como prova social.

## 2. Hotspot Analysis ("Exploit Cards") — o módulo-vitrine, liderar pelo VALOR (leaks ranqueados)
- Cards dos spots mais exploráveis do pool, por street (Flop/Turn/River) × direção: **Overfold** (pool foge do MDF → blefar mais) e **Overdefend** (pool defende demais → mais valor).
- Cada card: ação+size, defesa real vs MDF, desvio em pontos, **selo de confiança** por amostra (High ≥5.000 / Med ≥1.000 / Low <1.000; piso 500 mãos), **drill-down por posição e textura** embutido no card.
- Métrica é 100% frequência observada (pressão de fold) — **nunca EV, bb/100 ou lucro**.
- **Gating (correção do dono 09/07): NÃO é full-free.** No plano grátis, apenas **ALGUNS exploit cards** são revelados (preview dos principais). O **board completo ranqueado + os filtros** são do plano pago. Copy: "preview dos top exploit cards, grátis; o board completo destrava no upgrade". **PROIBIDO** afirmar "Hotspot completo/inteiro/full grátis".

## 3. Preflop Analysis
- Mede RFI%, 3-bet%, 4-bet%, Cold Call%, Squeeze%, família Steal, Fold vs 3-bet/4-bet — por **posição (21 combinações), stack (6 buckets BB), buy-in (5 faixas), estágio (6 fases), tipo de torneio (Vanilla/KO/Mystery), arquétipo de vilão (reg agressivo/reg tight/fish), cenário (SRP vs 3-bet pot), janela temporal**.
- Sizing de RFI/3-bet em **múltiplos de BB** (NÃO %pot — %pot é regra só do pós-flop).
- Cada célula: frequência + IC 95% + amostra. Filtros combináveis/empilháveis sem limite no pago.
- **Gating:** módulo acessível no grátis, mas **amostra limitada — buy-in ≤$22, Vanilla, Early Game**. Fora disso é pago; sub-linhas de sizing/drill-down borradas no grátis.
- NÃO existe: overlay solver×pool, EV, hole cards/range do vilão, stack coverage no RFI, limped pots.
- ✅ **Node-by-Node ESTÁ NO AR** (confirmado pelo dono, 27/07 — antes constava aqui como "dormente").
  Árvore de decisão navegável: a cada nó, de quem é a vez, frequência de cada ação e o `n` daquele
  recorte, com filtro de textura do flop (naipes / pareado / conectividade) e barra de frescor do dado.
  Números do módulo são **reais** — não marcar como ilustrativo.
  Convenção de cor por AÇÃO (nunca por ranking): Check `#5B8FD6` · Bet `#B58A12` ·
  Fold `#0E9AD4` · Call `#2FA37B` · Raise `#D9603F`.
  Asset de marketing pronto: `instagram/templates/shots/mockup-node-by-node.png`
  (interface recriada em `instagram/templates/mockup-node.html`, não é captura de tela).

## 4. Postflop Analysis
- Unifica **Pool Action** (bet/check/raise/fold) + **Pool Reaction** (fold/call/raise a cada ação) na mesma tela. Flop/turn/river, sempre **IP vs OOP**.
- Sizing de **bet em %pot** (convenção de solver — não citar concorrente), 6 buckets. Painel **MDF** com badge **Overfold/Overdefend** por tamanho de aposta.
- Textura de board por street (tom, high card, pareamento, overcard, flush draw, conectividade, stack coverage) — **13+ dimensões**. Filtros empilháveis; breakdown 1 eixo por vez.
- **Gating:** amostra limitada no grátis (1 filtro + 1 breakdown abertos; reação com blur; quebra por size travada). Profundidade completa = pago.
- ⚠️ **Raise ainda aparece em MÚLTIPLO na UI** (dado migrado, rótulo não): NÃO afirmar "raise em %pot visível". Bet em %pot, ok.

## 5. Team Mode
- Mesmos 3 módulos apontando para catálogo reservado do time. **Não** é módulo/UI separada; comparação "time vs field" é **roadmap**, não existe.
- Vendido como "fale conosco" (sem preço público).
- ⚠️ Roteamento multi-tenant não ativo no runtime de prod (catálogo hardcoded) — não afirmar "banco 100% isolado e ativo".

## 6. Pricing (confirmado em pricing.ts) — Stripe LIVE
- **Grátis:** $0 pra sempre, sem cartão.
- **Individual:** $29/mês · $149/semestre (≈$24,83/mês, −14%) · $259/ano (≈$21,58/mês, −25%, "mais popular").
- **Team/Stable:** sob consulta.

## 7. Compliance — regra de ouro
- PROIBIDO promessa de lucro/ganho ("lucra", "prints", "deixando dinheiro na mesa", "faça dinheiro"). A Aura mostra o **LEAK** (desvio de MDF), não o lucro → reframe para "explorar o gap / oportunidade de exploração".
- Sem dinheiro/luxo; 18+; sem dado de cliente; sem concorrente nominal (GTO Wizard só referência interna de convenção); números de mock/UI são ilustrativos.

## 8. ⚠️ FLAGS OPERACIONAIS — reconciliar produto ANTES de publicar
Estas peças de marketing afirmam coisas que o dono confirmou como intenção, mas que o **código/landing ainda não refletem**. Antes de publicar, engenharia (ou o dono ao vivo) precisa reconciliar — senão a copy fica descolada do produto (o problema que estamos justamente corrigindo):

1. ✅ **Hotspot gating RESOLVIDO (09/07):** o dono confirmou que **NÃO é full-free** — grátis revela só alguns exploit cards (preview); board completo + filtros = pago. Bate com o código (`entitlements.ts` já era teased). Toda a copy foi reescrita para "preview / upgrade destrava o board completo". Não afirmar "Hotspot completo grátis". (Era o item nº 1; fechado.)
2. 🟠 **Raise não está em %pot na UI** (só o bet). Copy evita afirmar isso — manter.
3. 🟠 **Team Mode não isolado/ativo** no runtime — não usar "banco 100% isolado" em copy B2B.

## 9. Banco de claims
**APROVADOS (100% verdadeiros e vendáveis):** field intelligence de MTT; 500M+ mãos auditadas; 7 salas; anonimizado + intervalo de confiança; atualização trimestral; Hotspot ranqueia exploits por desvio de MDF com selo de confiança; filtros ilimitados empilháveis (a 1.0 tinha trava de 3); sizing de bet em %pot; estágio de torneio/ICM/bolha (nenhum solver modela); Mystery Bounty/KO; reg vs fish; **Node-by-Node: árvore de decisão navegável, frequência e `n` por nó, filtro de textura do flop** (no ar desde 27/07 — ver §3); plano grátis sem cartão; **plano grátis = preview de cada módulo** (alguns exploit cards no Hotspot + amostra de Preflop ≤$22/Vanilla/Early + amostra de Postflop).
**PROIBIDOS:** qualquer promessa de lucro/EV/winrate; "solver overlay"/"vs GTO"; cobertura balanceada por sala; "raise em %pot"; "Team = banco isolado ativo"; depoimentos fictícios; **"Hotspot completo/full grátis" e Preflop/Postflop "completos" no grátis** (grátis é sempre PREVIEW/amostra; board completo + filtros = pago); **"defesa abaixo do MDF = leak/erro/gap explorável"** (ver §10).

---

## 10. ⚠️ FRONTEIRA DO SINAL DE MDF — o que ele mede e o que ele NÃO prova

Verificado em pesquisa com verificação adversarial (25 afirmações × 3 votos) —
detalhe e citações em [pesquisa-mdf-limites.md](pesquisa-mdf-limites.md). **Toda copy que usa o
painel de MDF checa contra aqui.**

**O que é verdade e pode afirmar:**
- MDF = `P/(P+B)` e o break-even de blefe = `B/(P+B)` são **complementos exatos**. "Defende abaixo do MDF" e "folda acima do break-even" são a mesma frase — mas **só sob a premissa de blefe de equity zero**, que é como o MDF é definido.
- A **medição** é sempre afirmável: "o field defende X% onde o MDF pede Y%". É descrição, não inferência.
- **Comparação relativa** (textura A vs textura B, vilão A vs vilão B) é a forma mais sólida: compara duas frequências medidas, com o MDF entrando só como baseline igual nos dois lados.

**O que NÃO se pode inferir do MDF sozinho:**
1. **Flop/turn:** solvers defendem rotineiramente **abaixo do MDF no equilíbrio**, porque quase todo candidato a blefe tem equity — o apostador não precisa do fold imediato. No equilíbrio o vilão **deve mesmo** ter blefes lucrativos. Logo defesa abaixo do MDF **não é leak**.
2. **River:** a objeção de equity futuro some, mas a defesa de equilíbrio ainda difere do MDF por **blockers/card removal** e por **falta de candidatos a blefe** no range do apostador.
3. **🚨 ICM (o mais grave pra nós — somos 100% MTT):** em spots com ICM o **MDF não é o benchmark correto**, porque ficha perdida vale mais que ficha ganha. Há solver de river com ICM em que o defensor paga **menos** que no chip-EV **mesmo com o agressor blefando mais**. Ou seja: **parte do "overfold" que medimos em bolha/mesa final é o field jogando CERTO.** O badge "Overfold" não distingue isso hoje.

**Regra de copy:** liderar por **descrição** e por **comparação relativa**. Nunca por inferência de
exploit a partir do desvio de MDF. Se precisar da leitura de EV, ela só vale com os quatro
qualificadores (blefe puro, desistir se pago, em fichas, estágio de ICM baixo) — o que raramente
cabe numa peça.

**Anotado, não resolvido (produto):** avaliar segmentar/renomear o badge "Overfold" por estágio,
já que em ICM alto ele nomeia como desvio algo que pode ser equilíbrio.
