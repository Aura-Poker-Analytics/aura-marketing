# Verdade Canônica do Produto — Aura 2.0 (gabarito de marketing)

**Consolidado:** 2026-07-09 por workflow multi-agente (5 agentes sonnet estudaram `aura-context` + `aura-landing`), verificado pela Fábrica.
**Uso:** é o GABARITO de tudo que a copy pode afirmar. Qualquer peça (arte, legenda, landing, ad) checa contra aqui. Resolve conflito em favor da confirmação mais recente do dono.

---

## 0. O que a Aura É / NÃO É
- **É** uma categoria própria: **inteligência de exploit da POPULAÇÃO (field) de MTT** — mede o que o field realmente faz (frequências reais), não teoria.
- **NÃO é tracker**: não mostra winrate/ROI/bankroll pessoal do herói (o lake só tem `chipswon` bruto do vencedor, sem payout por jogador).
- **NÃO é solver**: não compara com GTO, não tem overlay solver×pool, não calcula EV por spot. Hoje é 100% **descritivo** (frequência observada) + um sinal de exploit real: **pressão de fold vs MDF** (heurística, nunca chamada de "GTO").

## 1. Número-herói e prova
- **500M+ mãos auditadas** (nunca "bilhões" — confirmado pelo dono, 09/07).
- **7 salas cobertas**: PokerStars/PS_ES, GGPoker, WPN, Coin, Chico, WPT, Pacific (confirmado pelo dono como verdade de marketing).
  - *Interno, não publicar:* ~89% do volume carregado hoje é família PokerStars. Falar em "7 salas cobertas", nunca em proporção/volume por sala.
- 100% anonimizado (nenhuma mão ligada a nick/conta/jogador). Toda frequência vem com **intervalo de confiança (Wilson) + tamanho de amostra**; nada é mostrado sem massa crítica. Dataset **atualizado trimestralmente**.
- ⚠️ Depoimentos hoje no site (Lucas M., Ana P., Rafael C.) são **FICTÍCIOS** — remover, não usar como prova social.

## 2. Hotspot Analysis ("Exploit Cards") — o ativo de oferta mais forte, sempre liderar com ele
- Cards dos spots mais exploráveis do pool, por street (Flop/Turn/River) × direção: **Overfold** (pool foge do MDF → blefar mais) e **Overdefend** (pool defende demais → mais valor).
- Cada card: ação+size, defesa real vs MDF, desvio em pontos, **selo de confiança** por amostra (High ≥5.000 / Med ≥1.000 / Low <1.000; piso 500 mãos), **drill-down por posição e textura** embutido no card.
- Métrica é 100% frequência observada (pressão de fold) — **nunca EV, bb/100 ou lucro**.
- **Gating (LEI do dono): Hotspot é COMPLETO e grátis, sem trava de filtros.**

## 3. Preflop Analysis
- Mede RFI%, 3-bet%, 4-bet%, Cold Call%, Squeeze%, família Steal, Fold vs 3-bet/4-bet — por **posição (21 combinações), stack (6 buckets BB), buy-in (5 faixas), estágio (6 fases), tipo de torneio (Vanilla/KO/Mystery), arquétipo de vilão (reg agressivo/reg tight/fish), cenário (SRP vs 3-bet pot), janela temporal**.
- Sizing de RFI/3-bet em **múltiplos de BB** (NÃO %pot — %pot é regra só do pós-flop).
- Cada célula: frequência + IC 95% + amostra. Filtros combináveis/empilháveis sem limite no pago.
- **Gating:** módulo acessível no grátis, mas **amostra limitada — buy-in ≤$22, Vanilla, Early Game**. Fora disso é pago; sub-linhas de sizing/drill-down borradas no grátis.
- NÃO existe: overlay solver×pool, EV, hole cards/range do vilão, stack coverage no RFI, limped pots, Node-by-Node (dormente).

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

1. 🔴 **Hotspot "completo e grátis" vs código "teased".** `entitlements.ts` (2026-07-06) e `pricing.ts` (2026-07-07) ainda limitam o Hotspot grátis a **2 exploit cards por bucket + filtros travados**. Toda a nova copy grita "Hotspot completo, sem trava de filtro, grátis" (meet-hotspot, w1-spot-hotspot, w2-pre-cta, w3-post-cta, w4-cta-month, w4-spot-preflop). **Se o produto ao vivo não liberar o Hotspot completo, essa copy é falsa contra o produto.** Ação: eng ajusta `getModuleAccess('hotspot')`/`HOTSPOT_FREE_VISIBLE_LIMIT` para "full", OU o dono reconfirma olhando o produto ao vivo. **Este é o item nº 1 a resolver antes do P3 (hoje) e do carrossel ir com essa promessa.**
2. 🟠 **Raise não está em %pot na UI** (só o bet). Copy evita afirmar isso — manter.
3. 🟠 **Team Mode não isolado/ativo** no runtime — não usar "banco 100% isolado" em copy B2B.

## 9. Banco de claims
**APROVADOS (100% verdadeiros e vendáveis):** field intelligence de MTT; 500M+ mãos auditadas; 7 salas; anonimizado + intervalo de confiança; atualização trimestral; Hotspot ranqueia exploits por desvio de MDF com selo de confiança; filtros ilimitados empilháveis (a 1.0 tinha trava de 3); sizing de bet em %pot; estágio de torneio/ICM/bolha (nenhum solver modela); Mystery Bounty/KO; reg vs fish; plano grátis sem cartão; Hotspot completo grátis (ver flag §8.1).
**PROIBIDOS:** qualquer promessa de lucro/EV/winrate; "solver overlay"/"vs GTO"; cobertura balanceada por sala; "raise em %pot"; "Team = banco isolado ativo"; depoimentos fictícios; Preflop/Postflop "completos" no grátis.
