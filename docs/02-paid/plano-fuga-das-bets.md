# Plano: fugir do ecossistema de bets e atingir o público certo

**Criado:** 2026-08-12 · **Contexto:** encerramento da descoberta paga no IG BR (AURA-DISC01 + DISC02)
**Orçamento:** R$465 gastos · **~R$1.035 preservados** do teto de R$1.500

---

## 1. Por que o Instagram BR está encerrado (e não é culpa de criativo)

**Evidência acumulada — 3 criativos × 2 públicos × landing auditada:**

| Teste | Público | Criativo | Resultado no site |
|---|---|---|---|
| DISC01 (4 células) | interesses de conteúdo (Poker strategy, WPT, Poker tournament) | 4 enquadramentos | 0,18s/sessão |
| DISC02 `regs-fishes` | identidade (PokerStars + Pro Player + LAL1%) | promessa específica de spot, registro de jogador | 0,18s/sessão |
| DISC02 `plataforma-mda` | idem | apresentação da plataforma, gancho-pergunta | 0,11s/sessão |

Landing auditada ao vivo (12/08, mobile, URL do anúncio): DOM 280ms, UTMs intactas,
consent não bloqueia, hero coerente com o anúncio. **Tráfego não-pago na mesma página: 90–200s.**

**A prova qualitativa:** spam de comentários de bets em todos os reels pagos.
O pool de interesse "poker" no IG BR é habitado pelo ecossistema de apostas
(bots de "grupo VIP/sinais", público condicionado a clicar em carta/ficha achando
que é promo de bet). CTR alto + 2s de sessão é a assinatura disso.
**Não existe segmentação dentro desse pool que escape dele — o problema é quem
habita o pool, não como fatiamos.**

Reinterpretação histórica: os "seguidores ruins" de 01/2026 provavelmente eram
esse mesmo ecossistema (não o objetivo PROFILE_VISIT, como documentado antes).

---

## 2. Os três eixos da reformulação

### Eixo A — mudar QUEM: intenção declarada (Google Search) 🥇 prioridade

Quem digita a busca não é bot de bet e não está rolando feed — está **procurando**.

- **Orçamento:** R$25/dia · leitura em 3–4 semanas (volume de busca de nicho é baixo, mas hiperqualificado)
- **Estrutura:** 1 campanha Search BR · 4 grupos de anúncio:
  1. **Concorrente/alternativa** — "gto wizard", "gto wizard alternativa", "alternativa ao solver", "hand2note", "holdem manager alternativa"
  2. **Estudo de MTT** — "como estudar mtt", "estudo de poker mtt", "planilha de estudo poker", "range de mtt por posição"
  3. **Categoria/dado** — "estatísticas de field poker", "tendências da população poker", "population tendencies mtt", "frequência de fold field"
  4. **Exploit/MDA (dono da categoria)** — "mda poker", "mass data analysis poker", "exploit poker", "poker exploitativo", "exploitative poker", "como explorar o field"
- **⚠️ Armadilhas de correspondência (keywords do PO que precisam de âncora):**
  - "MDA" sozinho → NÃO usar: ambíguo (exame MDA, sigla médica, MDMA). Só "mda poker" / frase exata.
  - "Solver" sozinho → NÃO usar: captura Excel Solver e matemática. Só "poker solver" / "solver de poker" / "solver poker gratis".
  - "GTO wizard" → usar sim (marca de concorrente é leilão permitido no Google; só não pode aparecer no TEXTO do anúncio). É provavelmente a keyword de maior intenção da lista inteira.
  - "mda poker" / "mass data analysis poker" → volume ~zero (categoria que NÓS estamos criando), mas custa centavos ser dono dela desde já.
- **Negativas obrigatórias (a muralha anti-bet):** aposta, apostas, bet, bets, bônus, bonus, cassino, casino, slot, tigrinho, roleta, banca, sinal, sinais, grupo vip, telegram, plataforma pagando, saque, depósito, "jogo do tigre", freebet, odds, palpite
- **Conversão:** GA4 `sign_up` já existe como key event → vincular Google Ads ao GA4 e importar. Zero instrumentação nova.
- **Landing:** a atual serve (responde à busca de categoria). UTM: `utm_source=google&utm_medium=cpc&utm_campaign=search-br&utm_content=<grupo>`
- **Dependência:** criar conta Google Ads (ação do PO — agente não cria contas). Vincular ao GA4 property 506294082.

### Eixo B — mudar ONDE: Meta internacional EN 🥈 teste secundário

A praga tigrinho/sinais é fortemente BR. Nos mercados tier-1 de poker o pool de
interesse contém a base real de jogadores (mercados regulados, cultura de estudo).

- **Geo:** UK, CA, DE, NL, AT (excluir US no primeiro teste — CPM proibitivo pro orçamento)
- **Público:** mesma fórmula de identidade (PokerStars + Professional Poker Player + expansão) — ela funcionou em atrair; o que falhou foi o pool BR
- **Criativo:** versão EN do `disc02-plataforma-mda` (fábrica — prompt pronto, mesma estrutura, textos EN)
- **Landing:** conferir URL EN (toggle 🇺🇸 na landing) e usar o link que já abre em inglês
- **Orçamento:** R$20/dia · mesmo gate: engajamento real/sessão no GA4, ~130 sessões
- **Kill switch:** se aparecer spam de bet/cassino nos comentários OU 0,2s/sessão de novo → o problema é o formato IG em si, e Meta sai do mix global também

### Eixo C — de graça e permanente: linguagem + orgânico

- **Pesquisa de linguagem verbatim** (lacuna §9 do product-marketing.md): Discord de times BR,
  2+2, r/poker, comentários de canais de estudo. Como o grinder descreve a própria dor.
  Alimenta copy dos eixos A e B e da landing.
- **Orgânico segue como motor principal BR** — é o único canal que comprovadamente engaja
  (bio 12s, direto 91s, orgânico 200s). Calendário de 30d já existe.
- **Moderação anti-bet no IG** (proteção reputacional, vale pro orgânico também):
  Instagram → Configurações → Palavras ocultas → filtro personalizado com a lista de
  negativas acima. Esconder (não apagar) os comentários existentes.

---

## 3. O que fica explicitamente FORA

- ❌ Qualquer campanha de interesse/identidade no IG BR — pool contaminado, questão encerrada
- ❌ Lookalikes sobre seguidores/engajadores IG — semente exposta ao mesmo ecossistema
- ❌ Retargeting de visitantes — pools abaixo do mínimo de entrega (~20 pessoas úteis)
- ❌ "Mais um criativo" no setup atual — 3 falharam identicamente; a variável criativo está esgotada

## 4. Gates de decisão

| Quando | O quê |
|---|---|
| Search D14 | ≥1 cadastro OU CPC < R$4 com sessões >30s → escala pra R$40/dia. Zero absoluto → revisar keywords, não desligar ainda (volume baixo é esperado) |
| Meta EN D7 | mesmo gate de sempre: >5s/sessão continua · ~0,2s/sessão mata o eixo |
| 30d | consolidar: o canal pago vencedor (se houver) herda o orçamento restante |
