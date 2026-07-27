/* ============================================================
   DECK — dados de todos os posts, injetados nos templates via ?p=<id>
   Cada template faz Object.assign(CONFIG, DECK[id]) — só sobrescreve
   o que estiver aqui; o resto usa o default do template.
   Arte em EN (vocabulário de poker). Legendas ficam no doc do programa.
   ============================================================ */
window.DECK = {

  /* ========== SEMANA 1 · LAUNCH ========== */

  /* D0 — hero reveal (carrossel-... nao; single image via launch-hero.html) */
  "w1-hero": {
    topLeft: "@aurapokeranalytics",
    topRight: "Now live",
    versionBadge: "2.0",
    headlineHtml: "The same game.<br><em>New information.</em>",
    sub: "Field intelligence for MTT grinders — the pool's real strategy, measured across 500M+ audited hands.",
    cta: "Create free account",
    ctaSub: "aura.poker · link in bio",
    showCards: true,
    footerLeft: "aura.poker",
  },

  /* D1 — CARROSSEL "MEET AURA 2.0" (5 slides) */
  "meet-capa": {
    kicker: "Launch · Aura 2.0",
    hookHtml: "Meet <em>Aura 2.0</em>",
    sub: "Not a tracker. Not a solver. The pool's real strategy — 500M+ audited hands, 7 rooms.",
    swipe: "Swipe →",
    handle: "@aurapokeranalytics",
    ui: {
      section: "Overfolds",
      spots: "12 spots",
      badge: "Overfold",
      title: "BB vs BTN · Flop · Bet 33% pot",
      poolPct: 48,
      mdfPct: 62,
      meta: "Desvio do MDF · <b>−14 pts</b> · Confiança alta · 480k mãos",
      row2badge: "Overfold",
      row2title: "SB vs CO · Turn · Bet 66% pot",
    },
  },
  "meet-preflop": {
    slideNumber: "02",
    slideIndicator: "2 / 5",
    kicker: "Preflop Analysis",
    titleHtml: "Every action, <em>every angle</em>",
    bodyHtml: [
      "RFI, 3-bet, 4-bet, squeeze, cold call, steal — every preflop action, sliced by position, stack, buy-in, tournament stage, format and villain type. What the field <b>actually does</b>.",
    ],
    mock: "preflop",
    handle: "@aurapokeranalytics",
  },
  "meet-postflop": {
    slideNumber: "03",
    slideIndicator: "3 / 5",
    kicker: "Postflop Analysis",
    titleHtml: "The pool's <em>reaction</em>, every street",
    bodyHtml: [
      "Bet, check, raise or fold — flop to river, IP vs OOP, bet sizing in <b>% pot</b>, with the MDF line marking over- and under-defense on every bar.",
    ],
    mock: "postflop",
    handle: "@aurapokeranalytics",
  },
  "meet-hotspot": {
    slideNumber: "04",
    slideIndicator: "4 / 5",
    kicker: "Hotspot Analysis",
    titleHtml: "The field's leaks, <em>ranked</em>",
    bodyHtml: [
      "The pool's most exploitable spots — ranked by overfold vs MDF, by street, with a confidence badge on every card. <b>Preview the top cards free</b>; unlock the full board on upgrade.",
    ],
    mock: "hotspot",
    handle: "@aurapokeranalytics",
  },
  "meet-cta": {
    headlineHtml: "Study the field. <em>Free.</em>",
    bullets: [
      "Free plan, forever — no card required",
      "Preview every module free — top exploit cards + samples",
      "Upgrade unlocks the full board & all filters · 500M+ audited",
    ],
    ctaLabel: "Create free account",
    ctaSub: "link in bio",
    tagline: "The same game. New information.",
    handle: "@aurapokeranalytics",
  },

  /* D3 — feature spotlight: Hotspot */
  "w1-spot-hotspot": {
    kicker: "Hotspot Analysis",
    titleHtml: "The pool's leaks, <em>ranked for you</em>",
    screenshotSrc: "",
    frameUrl: "beta.aura.poker",
    activeNav: "Hotspot",
    cards: [
      { badge: "Overfold", title: "BB vs BTN · Flop · Bet 33% pot", poolPct: 48, mdfPct: 62,
        meta: "Desvio do MDF · <b>−14 pts</b> · Confiança alta · 480k mãos" },
      { badge: "Overfold", title: "SB vs CO · Turn · Bet 66% pot", poolPct: 41, mdfPct: 55,
        meta: "Desvio do MDF · <b>−14 pts</b> · Confiança média · 210k mãos" },
    ],
    bullets: [
      "<b>Ranked leaks</b> — the field's most exploitable spots.",
      "<b>MDF on the bar</b> — pool's defense vs minimum.",
      "<b>Free to try</b> — preview the top cards, upgrade for the full board.",
    ],
    footerNote: "aura.poker",
  },

  /* D5 — feature spotlight: Postflop (via feature-spotlight com nav Postflop) */
  "w1-spot-postflop": {
    kicker: "Postflop Analysis",
    titleHtml: "Read the pool, <em>street by street</em>",
    screenshotSrc: "",
    frameUrl: "beta.aura.poker",
    activeNav: "Postflop",
    /* cards alinhados com w1-spot-hotspot (mesmos 2 leaks, lente Postflop):
       poolPct = defesa do pool (call+raise) → Fold = 100-poolPct, split Call/Raise ilustrativo */
    cards: [
      { badge: "Overfold", title: "BB vs BTN · Flop · Bet 33% pot", poolPct: 48, mdfPct: 62,
        meta: "Fold 52% · Call 39% · Raise 9% · 480k mãos" },
      { badge: "Overfold", title: "SB vs CO · Turn · Bet 66% pot", poolPct: 41, mdfPct: 55,
        meta: "Fold 59% · Call 31% · Raise 10% · 210k mãos" },
    ],
    bullets: [
      "<b>Every line</b> — fold / call / raise, every sizing, every street.",
      "<b>MDF on the bar</b> — over- and under-defense at a glance.",
      "<b>20+ filters</b> — buy-in, stage, stack, board texture, reg vs fish.",
    ],
    footerNote: "aura.poker",
  },

  /* ========== SEMANA 2 ========== */

  /* Carrossel "Preflop in 60s" */
  "w2-pre-capa": {
    kicker: "Preflop in 60s",
    hookHtml: "The field's <em>range</em>, exposed",
    sub: "RFI, 3-bet, steal — how the pool really opens, filtered by position, stack and stage.",
    swipe: "Swipe →",
    handle: "@aurapokeranalytics",
  },
  "w2-pre-slide1": {
    slideNumber: "02", slideIndicator: "2 / 4",
    kicker: "Preflop Analysis",
    titleHtml: "RFI & 3-bet, <em>by position</em>",
    bodyHtml: ["See how the pool opens and 3-bets by seat — reg vs fish, stack and buy-in included."],
    mock: "preflop", handle: "@aurapokeranalytics",
  },
  "w2-pre-slide2": {
    slideNumber: "03", slideIndicator: "3 / 4",
    kicker: "Preflop Analysis",
    titleHtml: "Stage, ICM & <em>tournament type</em>",
    bodyHtml: ["Six stages, early game to the ICM bubble and final table — Vanilla, KO or Mystery Bounty."],
    mock: "preflop", handle: "@aurapokeranalytics",
  },
  "w2-pre-cta": {
    headlineHtml: "Try Preflop. <em>Free.</em>",
    bullets: ["Free sample — ≤$22, Vanilla, Early Game", "Hotspot — preview the top exploit cards", "500M+ audited MTT hands"],
    ctaLabel: "Create free account", ctaSub: "link in bio",
    tagline: "The same game. New information.", handle: "@aurapokeranalytics",
  },

  /* L3 card: "Can you answer…?" (feature-spotlight, nav Postflop) */
  "w2-l3-defend": {
    kicker: "Can you answer this?",
    titleHtml: "How much does the BB <em>really</em> defend?",
    screenshotSrc: "", frameUrl: "beta.aura.poker", activeNav: "Postflop",
    cards: [
      { badge: "Overfold", title: "BB vs BTN · Flop · Bet 33% pot", poolPct: 48, mdfPct: 62,
        meta: "MDF says 62% · the pool defends <b>48%</b> · 480k mãos" },
    ],
    bullets: [
      "<b>The answer isn't the solver's</b> — it's what the field does.",
      "<b>48% vs 62%</b> — 14 points of overfold to attack.",
      "<b>Check the top spots</b> — free in Hotspot.",
    ],
    footerNote: "aura.poker",
  },

  /* Feature spotlight: tournament-stage filter */
  "w2-spot-stage": {
    kicker: "Filter · Tournament stage",
    titleHtml: "The bubble field is a <em>different animal</em>",
    screenshotSrc: "", frameUrl: "beta.aura.poker", activeNav: "Hotspot",
    cards: [
      { badge: "Overfold", title: "Bubble · BB vs BTN · Flop · Bet 33%", poolPct: 43, mdfPct: 62,
        meta: "Desvio do MDF · <b>−19 pts</b> · Confiança alta · 120k mãos" },
      { badge: "Overfold", title: "ITM · SB vs CO · Turn · Bet 66%", poolPct: 46, mdfPct: 57,
        meta: "Desvio do MDF · <b>−11 pts</b> · Confiança média · 90k mãos" },
    ],
    bullets: [
      "<b>Stage-aware</b> — early, pre-bubble, bubble, ITM, final table.",
      "<b>ICM pressure</b> — where the field over-folds under the money.",
      "<b>MTT-native</b> — no solver models this.",
    ],
    footerNote: "aura.poker",
  },

  /* ========== SEMANA 3 ========== */

  /* Carrossel "Postflop — read the pool" (P8) */
  "w3-post-capa": {
    kicker: "Module tour · Postflop",
    hookHtml: "Read the pool, <em>sizing by sizing</em>",
    sub: "Fold, call, raise — for every bet size, in % of pot, the solver's convention.",
    swipe: "Swipe →", handle: "@aurapokeranalytics",
    ui: {
      section: "Overfolds", spots: "9 spots", badge: "Overfold",
      title: "BB vs BTN · Flop · Bet 33% pot", poolPct: 48, mdfPct: 62,
      meta: "Desvio do MDF · <b>−14 pts</b> · Confiança alta · 480k mãos",
      row2badge: "Overfold", row2title: "SB vs CO · Turn · Bet 66% pot",
    },
  },
  "w3-post-slide1": {
    slideNumber: "02", slideIndicator: "2 / 4",
    kicker: "Postflop Analysis",
    titleHtml: "Pick the <em>sizing</em>, get the read",
    bodyHtml: ["33%, 66%, overbet — each sizing gets its own fold / call / raise, in <b>% of pot</b>, the solver convention."],
    mock: "postflop",
    postflop: {
      streets: ["Flop", "Turn", "River"],
      activeStreet: 0,
      context: "IP — BTN (RFI)",
      actions: [
        { name: "Bet 33% pot", pct: 62 },
        { name: "Bet 66% pot", pct: 24 },
        { name: "Check", pct: 14 },
      ],
      reactionTitle: "Pool reaction vs Bet 33% pot",
      reactions: [
        { name: "Fold", pct: 52, kind: "fold" },
        { name: "Call", pct: 39, kind: "call" },
        { name: "Raise", pct: 9, kind: "raise" },
      ],
      mdfPct: 62,
      sample: "480k hands · $22–$109",
    },
    handle: "@aurapokeranalytics",
  },
  "w3-post-slide2": {
    slideNumber: "03", slideIndicator: "3 / 4",
    kicker: "Postflop Analysis",
    titleHtml: "Stack <em>20+ filters</em>, no cap",
    bodyHtml: ["Buy-in, stage, board texture, stack depth, villain type — stack as many filters as you like. No 3-filter cap."],
    mock: "postflop",
    postflop: {
      streets: ["Flop", "Turn", "River"],
      activeStreet: 1,
      context: "OOP — SB vs CO · Turn",
      actions: [
        { name: "Bet 66% pot", pct: 55 },
        { name: "Bet 33% pot", pct: 20 },
        { name: "Check", pct: 25 },
      ],
      reactionTitle: "Pool reaction vs Bet 66% pot",
      reactions: [
        { name: "Fold", pct: 59, kind: "fold" },
        { name: "Call", pct: 31, kind: "call" },
        { name: "Raise", pct: 10, kind: "raise" },
      ],
      mdfPct: 55,
      sample: "210k hands · Bubble stage",
    },
    handle: "@aurapokeranalytics",
  },
  "w3-post-cta": {
    headlineHtml: "Attack the field. <em>Free.</em>",
    bullets: ["Preview every module free — no card", "Postflop & Hotspot: free sample, upgrade for full", "500M+ audited hands"],
    ctaLabel: "Create free account", ctaSub: "link in bio",
    tagline: "The same game. New information.", handle: "@aurapokeranalytics",
  },

  /* L3 card: "Can you answer…?" preflop */
  "w3-l3-rfi": {
    kicker: "Can you answer this?",
    titleHtml: "Does your pool <em>over-open</em> the CO?",
    screenshotSrc: "", frameUrl: "beta.aura.poker", activeNav: "Preflop",
    cards: [
      { badge: "Overfold", title: "CO · RFI vs reference", poolPct: 31, mdfPct: 24,
        meta: "Pool opens <b>31%</b> vs 24% reference — 7 pts too wide · 1.2M mãos" },
    ],
    bullets: [
      "<b>Wider isn't random</b> — the field has a shape you can read.",
      "<b>3-bet lighter</b> where it over-opens and over-folds.",
      "<b>Preflop grid</b> — free to start.",
    ],
    footerNote: "aura.poker",
  },

  /* ========== SEMANA 4 ========== */

  /* Carrossel "Hotspot — how to use exploit cards" */
  "w4-hs-capa": {
    kicker: "How to · Hotspot",
    hookHtml: "From <em>leak</em> to line",
    sub: "How to turn an Aura exploit card into a decision at the table.",
    swipe: "Swipe →", handle: "@aurapokeranalytics",
    ui: {
      section: "Overfolds", spots: "12 spots", badge: "Overfold",
      title: "BB vs BTN · Flop · Bet 33% pot", poolPct: 48, mdfPct: 62,
      meta: "Desvio do MDF · <b>−14 pts</b> · Confiança alta · 480k mãos",
      row2badge: "Overfold", row2title: "SB vs CO · Turn · Bet 66% pot",
    },
  },
  "w4-hs-slide1": {
    slideNumber: "02", slideIndicator: "2 / 4",
    kicker: "Read the card",
    titleHtml: "Pool defends <em>48%</em>, MDF says 62%",
    bodyHtml: ["The bar falling short of the MDF mark = the field folds too much here. That 14-point gap is the exploit."],
    mock: "hotspot", handle: "@aurapokeranalytics",
  },
  "w4-hs-slide2": {
    slideNumber: "03", slideIndicator: "3 / 4",
    kicker: "Take the line",
    titleHtml: "So you <em>bet more, cheaper</em>",
    bodyHtml: ["Against an over-folding field, a small, frequent c-bet attacks that gap. The card shows you where; you bring the aggression."],
    mock: "hotspot", handle: "@aurapokeranalytics",
  },
  "w4-hs-cta": {
    headlineHtml: "Find your spots. <em>Free.</em>",
    bullets: ["Ranked exploit cards, free", "MDF vs pool on every card", "No card required"],
    ctaLabel: "Create free account", ctaSub: "link in bio",
    tagline: "The same game. New information.", handle: "@aurapokeranalytics",
  },

  /* L5 CTA — "1 month live" milestone (post P13, distinct creative from meet-cta/P10) */
  "w4-cta-month": {
    headlineHtml: "One month <em>live</em>.",
    bullets: [
      "Top exploit cards + module samples, <b>free</b>",
      "Upgrade for the full board & all filters",
      "500M+ hands audited, <b>7 rooms covered</b>",
    ],
    ctaLabel: "Create free account",
    ctaSub: "link in bio",
    tagline: "The same game. New information.",
    handle: "@aurapokeranalytics",
  },

  /* Feature spotlight: Preflop grid */
  "w4-spot-preflop": {
    kicker: "Preflop Analysis",
    titleHtml: "The whole field, <em>one screen</em>",
    screenshotSrc: "", frameUrl: "beta.aura.poker", activeNav: "Preflop",
    cards: [
      { badge: "Overfold", title: "CO · RFI vs reference", poolPct: 31, mdfPct: 24,
        meta: "Opens <b>31%</b> vs 24% ref · +7 pts · 1.2M mãos" },
      { badge: "Overfold", title: "BTN · RFI vs reference", poolPct: 44, mdfPct: 47,
        meta: "Opens <b>44%</b> vs 47% ref · −3 pts · 1.1M mãos" },
    ],
    bullets: [
      "<b>Every seat</b> — RFI, 3-bet, defense, deltas built in.",
      "<b>20+ filters</b> — stack, buy-in, stage, format, villain type.",
      "<b>Free to $22</b> — upgrade unlocks every buy-in & filter.",
    ],
    footerNote: "aura.poker",
  },

  /* ===== REPLANEJAMENTO 13/07 — posts com SCREENSHOT REAL (shot-showcase) ===== */
  "shot-postflop-sizings": {
    layout: "hero", kicker: "Postflop · real screen",
    titleHtml: "Defense vs MDF, <em>every sizing</em>",
    shotSrc: "shots/postflop1.png", shotBg: "#0B1120", frameH: 600, badge: "3.2M hands",
    caption: "Raise vs flop c-bet, BTN caller. The pool's real defense measured against the MDF mark, per bet size — on 3.2M hands.",
    footerNote: "aura.poker · real product", handle: "@aurapokeranalytics",
  },
  "shot-filters": {
    layout: "split", kicker: "20+ filters",
    titleHtml: "Slice the field <em>any way</em> you want",
    shotSrc: "shots/filtros1.png", shotBg: "#0B1120",
    bullets: [
      "<b>Position, stage, buy-in</b> — RFI vs caller seat.",
      "<b>Board texture</b> — paired, connectedness, flush draws.",
      "<b>Stack coverage</b> — IP covering vs covered.",
      "<b>Stack it all</b> — no 3-filter cap like the old Aura.",
    ],
    footerNote: "aura.poker · real product", handle: "@aurapokeranalytics",
  },
  "shot-preflop-ref": {
    layout: "hero", kicker: "Preflop · real screen",
    titleHtml: "Every preflop action, <em>one grid</em>",
    shotSrc: "shots/1.png", shotBg: "#0B1120", frameH: 760, badge: "Total Global",
    caption: "RFI, 3-bet, 4-bet, steal, open-limp, squeeze — by seat, vs the whole-field reference. The green/red deltas are your read.",
    footerNote: "aura.poker · real product", handle: "@aurapokeranalytics",
  },

  /* POST: distribuicao de tamanhos. Dado real da coluna Total (aura-total2):
     ~20% 9,3% (137K) · 33% 19,5% (286K) · 42% 24,5% (360K) · 55% 16,5% (242K)
     · ~75% 16,6% (244K) · overpot 13,6% (200K). Soma 100%, ~1,47M maos — que
     e justamente 13,9% de 10,6M (a fatia em que houve XR).
     ⚠️ FLAG CONHECIDA: a distribuicao pertence a acao XR (raise) e o gabarito
     §4 diz que raise aparece em MULTIPLO na UI, nao em %pot. O PO decidiu
     publicar assim mesmo (27/07). Se o rotulo do raise for corrigido no
     produto, revisar este post antes de repostar ou virar anuncio. */
  "shot-size-mix": {
    layout: "hero", kicker: "Postflop · real screen",
    titleHtml: "The size the field <em>actually picks</em>",
    shotSrc: "shots/crop-sizedist.png", shotBg: "#0B1120", frameH: 620, badge: "",
    caption: "42% is the most-used size, at 24.5%. The field goes overpot 13.6% of the time. Every row shows its own sample.",
    footerNote: "aurapoker.com · real product", handle: "@aurapokeranalytics",
  },

  /* POST: textura de board muda o field. Comparacao REAL lado a lado — o crop
     traz as colunas "Total" e "Disconnected" do proprio produto, entao a
     comparacao e visivel na tela, nao afirmada na legenda.
     Numeros: XR Flop CBet 13,9% (10,6M maos) vs 11,5% em board desconexo
     (3,1M maos). Contexto: SRP, RFI CO, caller BB, ultimos 2 anos.
     Frequencia observada — nao e tamanho de raise (ver flag §4 do gabarito). */
  "shot-texture-split": {
    layout: "hero", kicker: "Postflop · real screen",
    titleHtml: "Same spot. <em>Different board.</em>",
    shotSrc: "shots/crop-postflop-wide.png", shotBg: "#0B1120", frameH: 780, badge: "",
    caption: "The field check-raises a flop c-bet 13.9% of the time — but 11.5% on a disconnected board. Same spot, measured per texture.",
    footerNote: "aurapoker.com · real product", handle: "@aurapokeranalytics",
  },

  /* analogo de referencia do PREFLOP, mas pro POSTFLOP. Tela real (aura-total2
     recortada: rail de contexto + coluna Total). Descritivo — sem inferir leak,
     ver pesquisa-mdf-limites.md §10. */
  "shot-postflop-ref": {
    layout: "hero", kicker: "Postflop · real screen",
    titleHtml: "The whole postflop, <em>one screen</em>",
    shotSrc: "shots/postflop-ref.png", shotBg: "#0B1120", frameH: 770, badge: "Total",
    caption: "Action %, size distribution and defense vs MDF per size — by scenario, position and board texture, all on real hands.",
    footerNote: "aura.poker · real product", handle: "@aurapokeranalytics",
  },
  "shot-villain": {
    layout: "hero", kicker: "Villain type · real screen",
    titleHtml: "Reg or fish? <em>Different field.</em>",
    shotSrc: "shots/preflop_disag.png", shotBg: "#0B1120", frameH: 560, badge: "Aggro Reg",
    caption: "The same spot, disaggregated by villain archetype and stack — because an aggro reg and a fish don't leak the same way.",
    footerNote: "aura.poker · real product", handle: "@aurapokeranalytics",
  },
  "shot-cbet-reaction": {
    layout: "hero", kicker: "Postflop · real screen",
    titleHtml: "How the field <em>answers</em> a c-bet",
    shotSrc: "shots/postflop2.png", shotBg: "#0B1120", frameH: 380, badge: "3.2M hands",
    caption: "Fold, call or raise vs a flop c-bet — the pool's real reaction, in one line. Fold 33%, Call 55%, Raise 12%.",
    footerNote: "aura.poker · real product", handle: "@aurapokeranalytics",
  },
  /* ===== REEL DE LANÇAMENTO — cenas 1080×1920 (reel-scene.html) ===== */
  "reel-s1": { type: "title", showLogo: true,
    titleHtml: "Está <em>no ar.</em>", sub: "", footer: "" },
  "reel-s2": { type: "title", showLogo: false, kicker: "Aura 2.0",
    titleHtml: "Não é tracker.<br>Não é <em>solver.</em>",
    sub: "Tracker mostra as SUAS mãos. Solver mostra o equilíbrio teórico.", footer: "" },
  "reel-s3": { type: "title", showLogo: false, kicker: "É outra categoria",
    titleHtml: "É o que o field<br><em>realmente faz.</em>",
    sub: "<b>500M+ mãos auditadas</b> · 7 salas · MTT", footer: "" },
  "reel-s4": { type: "shot", kicker: "Preflop Analysis",
    titleHtml: "Todo o preflop<br>do <em>field</em>",
    shotSrc: "shots/1.png", badge: "Total Global",
    sub: "RFI, 3-bet, 4-bet, steal — por posição, com os deltas.", footer: "" },
  "reel-s5": { type: "shot", kicker: "20+ filtros",
    titleHtml: "Fatia do <em>seu jeito</em>",
    shotSrc: "shots/filtros1.png", badge: "",
    sub: "Posição, estágio, buy-in, textura de board, tipo de vilão.", footer: "" },
  "reel-s6": { type: "shot", kicker: "Postflop Analysis",
    titleHtml: "Overfold vs MDF,<br><em>size por size</em>",
    shotSrc: "shots/postflop1.png", badge: "3.2M mãos",
    sub: "Cada barra vermelha aquém da marca = o field foldando demais.", footer: "" },
  "reel-s7": { type: "shot", kicker: "A reação real do pool",
    titleHtml: "Fold <em>33%</em> · Call 55%<br>Raise 12%",
    shotSrc: "shots/postflop2.png", badge: "3.2M mãos",
    sub: "Passivo e call-heavy — vs c-bet no flop.", footer: "" },
  "reel-s8": { type: "title", showLogo: true, kicker: "",
    titleHtml: "Conta <em>grátis</em>",
    sub: "Preview de cada módulo, sem cartão.<br><b>aurapoker.com</b> · link na bio", footer: "" },

  /* ===== LAUNCH REEL — cenas EN (arte em ingles, p/ mercado global) =====
     s6 usa moldura DESCRITIVA (defesa medida vs MDF), nao "over-folding" —
     ver pesquisa-mdf-limites.md §3/§10. A versao PT (reel-s6) ainda usa a
     redacao antiga; sincronizar quando for reencodar o reel PT. */
  "reel-s1-en": { type: "title", showLogo: true,
    titleHtml: "It's <em>live.</em>", sub: "", footer: "" },
  "reel-s2-en": { type: "title", showLogo: false, kicker: "Aura 2.0",
    titleHtml: "Not a tracker.<br>Not a <em>solver.</em>",
    sub: "A tracker shows YOUR hands. A solver shows theoretical equilibrium.", footer: "" },
  "reel-s3-en": { type: "title", showLogo: false, kicker: "A different category",
    titleHtml: "It's what the field<br><em>actually does.</em>",
    sub: "<b>500M+ audited hands</b> · 7 rooms · MTT", footer: "" },
  "reel-s4-en": { type: "shot", kicker: "Preflop Analysis",
    titleHtml: "The field's<br>whole <em>preflop</em>",
    shotSrc: "shots/1.png", badge: "Global Total",
    sub: "RFI, 3-bet, 4-bet, steal — by seat, with the deltas.", footer: "" },
  "reel-s5-en": { type: "shot", kicker: "20+ filters",
    titleHtml: "Slice it <em>your way</em>",
    shotSrc: "shots/filtros1.png", badge: "",
    sub: "Position, stage, buy-in, board texture, villain type.", footer: "" },
  "reel-s6-en": { type: "shot", kicker: "Postflop Analysis",
    titleHtml: "Defense vs MDF,<br><em>size by size</em>",
    shotSrc: "shots/postflop1.png", badge: "3.2M hands",
    sub: "Real pool defense measured against the MDF mark, per size.", footer: "" },
  "reel-s7-en": { type: "shot", kicker: "The pool's real reaction",
    titleHtml: "Fold <em>33%</em> · Call 55%<br>Raise 12%",
    shotSrc: "shots/postflop2.png", badge: "3.2M hands",
    sub: "Passive and call-heavy — vs a flop c-bet.", footer: "" },
  "reel-s8-en": { type: "title", showLogo: true, kicker: "",
    titleHtml: "Free <em>account</em>",
    sub: "Preview of every module, no card.<br><b>aurapoker.com</b> · link in bio", footer: "" },

  "shot-search": {
    layout: "split", kicker: "Spot search",
    titleHtml: "Any postflop spot, <em>one search</em>",
    shotSrc: "shots/busca.png", shotBg: "#0B1120",
    bullets: [
      "<b>Type the line</b> — 'turn delayed c-bet', 'float turn'…",
      "<b>Flop to river</b>, IP and OOP, with the pool's frequency.",
      "<b>Jump straight</b> to the exact spot you're studying.",
    ],
    footerNote: "aura.poker · real product", handle: "@aurapokeranalytics",
  },

  /* ==========================================================
     CAMPANHA AURA-PAID01 — cenas dos 3 videos de ANUNCIO (paid-scene.html)
     9:16 · PT-BR · zonas seguras · legenda queimada · sem "link na bio".

     PROCEDENCIA DOS NUMEROS — todos lidos das telas reais:
       auta-total.png  → Preflop, Breakdown "Player Type"
                         (contexto: All Tournaments · Any Stage · Any Buy-in · Last 2 Years)
       aura-total2.png → Postflop, Breakdown "Flop Connectedness"
                         (contexto: SRP · RFI: CO · Caller: BB · Last 2 Years)
     NENHUM numero e de solver. A Aura nao e solver (product-truth-aura.md §0):
     MDF e identidade matematica, nao output de solver — por isso a copy diz
     "a matematica/MDF", nunca "o solver diz X%".
     ========================================================== */

  /* ---------- V1 · jargao preflop puro (replica do vencedor historico) ---------- */
  "p1-s1": { kicker: "Preflop · MTT", big: 'RFI de <em>50%</em><br>no BTN',
    heroBg: "shots/crop-preflop-table.png",   // v2: produto REAL ja no frame 1
    line: "É o que o reg agressivo do field faz. Medido, não estimado.",
    caption: "RFI de 50% no botão. Isso é o field — não é teoria." },
  "p1-s2": { kicker: "Mesmo spot, vilão diferente",
    line: "O field não é uma média. São perfis com frequências diferentes.",
    block: { type:"vs", delta:"15 pts",
      a:{ lb:"Reg agressivo", v:"50%", sb:"RFI no BTN" }, aHot:true,
      b:{ lb:"Reg tight", v:"35%", sb:"RFI no BTN" } },
    caption: "Reg agressivo abre 50% do botão. Reg tight, 35%." },
  /* v2 s3: PRINT REAL emoldurado (era recriacao vetorial da mesma tabela —
     redundante e menos crivel). Crop nativo 700x560, sem borrao. */
  "p1-s3": { kicker: "A tela real",
    block: { type:"shot", src:"shots/crop-preflop-table.png", w:920,
      title:"Aura · Preflop Analysis", cap:"produto real, não mockup" },
    caption: "Frequência observada, com tamanho de amostra e intervalo de confiança." },
  "p1-s4": { kicker: "Reg agressivo · todas as posições",
    block: { type:"stats", rows:[
      { k:"Fold vs RFI", v:"73%" }, { k:"3-Bet", v:"10%" }, { k:"Steal Attempt", v:"42%" } ] },
    line: "Cada número desses é um spot que você joga toda sessão.",
    caption: "Fold vs RFI, 3-bet, steal attempt — o field inteiro, medido." },
  /* v2 s5: era so texto — agora mostra o painel de filtros REAL */
  "p1-s5": { kicker: "20+ filtros · recorta até o micro-spot",
    block: { type:"shot", src:"shots/crop-filters-rail.png", w:640, chrome:false },
    caption: "Estágio (do early à mesa final) e buy-in — combináveis sem trava." },

  /* ---------- V2 · dados reais vs teoria (angulo desocupado na Ads Library) ---------- */
  "p2-s1": { kicker: "Postflop · MTT", big: 'A matemática<br>diz <em>64,5%</em>',
    heroBg: "shots/crop-exploit-cards.png",   // v2: produto REAL ja no frame 1
    line: "O field defende 57,7%.",
    caption: "MDF de 64,5%. O field defende 57,7%." },
  /* s2: DESCRITIVO, sem inferir exploit. A leitura "abaixo do MDF logo tem leak" nao se
     sustenta no flop nem em torneio (ICM) — ver pesquisa-mdf-limites.md §3 e §6. */
  "p2-s2": { kicker: "C-bet de 55% do pote",
    line: "MDF é matemática. Defesa real é comportamento medido.",
    block: { type:"bars", rows:[
      { sz:"55% do pote", badge:"Overfold 6,8 pts", def:57.7, mdf:64.5, defL:"57,7%", mdfL:"64,5%" } ] },
    caption: "O field defende 57,7% onde a matemática pede 64,5%." },
  /* v2 s3: PRINT REAL dos exploit cards (era recriacao vetorial dos mesmos numeros) */
  "p2-s3": { kicker: "Em todo tamanho de aposta",
    block: { type:"shot", src:"shots/crop-exploit-cards.png", w:900,
      title:"Aura · Postflop Analysis", cap:"produto real, não mockup" },
    caption: "33%, 42%, 55% do pote: o field fica aquém do MDF em todos." },
  "p2-s4": { kicker: "A base por trás disso",
    block: { type:"stats", rows:[
      { k:"Mãos só nesse spot", v:"10,6M" }, { k:"Mãos auditadas", v:"<em>500M+</em>" },
      { k:"Salas cobertas", v:"7" } ] },
    caption: "10,6 milhões de mãos só nesse spot. 500M+ no total." },
  "p2-s5": { big: 'Solver mostra o<br><em>equilíbrio</em>', bigSm: true,
    line: "A Aura mostra o que o field <b>realmente faz</b> — em 500M+ mãos reais.",
    caption: "Equilíbrio é o ponto de partida. O field é o alvo." },

  /* ---------- V3 · leak / variancia (padrao que ressoa em PT) ---------- */
  "p3-s1": { kicker: "Field intelligence · MTT", big: 'Não é <em>azar</em>',
    heroBg: "shots/crop-sizedist.png",   // v2: produto REAL ja no frame 1
    line: "É padrão. E padrão dá pra medir.",
    caption: "Não é azar. É padrão — e padrão dá pra medir." },
  "p3-s2": { kicker: "C-bet de 55% · textura do flop",
    line: "Mesmo tamanho de aposta. Board diferente, field diferente.",
    block: { type:"vs", delta:"+3 pts",
      a:{ lb:"Board conectado", v:"6,9%", sb:"overfold vs MDF" },
      b:{ lb:"Board desconexo", v:"9,9%", sb:"overfold vs MDF" }, bHot:true },
    caption: "Em board desconexo o pool overfolda 9,9% — contra 6,9% no conectado." },
  "p3-s3": { kicker: "E no overpot o buraco é maior",
    line: "Quase três vezes mais pressão de fold, na mesma linha.",
    block: { type:"vs", delta:"+5,3 pts",
      a:{ lb:"Board conectado", v:"2,9%", sb:"overfold no overpot" },
      b:{ lb:"Board desconexo", v:"8,2%", sb:"overfold no overpot" }, bHot:true },
    caption: "Overpot em board desconexo: 8,2% de overfold contra 2,9%." },
  /* v2 s4: PRINT REAL da coluna "Disconnected" — prova os numeros do proprio video
     (11,5% · 3,1M maos · overfolds 11,0/11,2/9,9). Crop nativo 514x812. */
  "p3-s4": { kicker: "A tela real, filtrada por textura",
    block: { type:"shot", src:"shots/crop-disconnected-col.png", w:520,
      title:"Aura · Postflop · board desconexo" },
    caption: "Conectividade, pareamento, high card, flush draw — 13+ dimensões." },
  "p3-s5": { big: 'O leak é do<br><em>field</em>', bigSm: true,
    line: "A Aura mostra <b>onde</b> ele está — e em qual textura de board.",
    caption: "O leak não é seu. É do field. E dá pra explorar." },

  /* ---------- CTA (mesma cena final nos 3) ---------- */
  "p-cta": { cta: true, line: "500M+ mãos auditadas · 7 salas",
    ctaBtn: "Criar conta grátis", ctaSub: "Preview de cada módulo. Sem cartão." },

  /* ==========================================================
     AURA-PAID01 — cenas EN (mercado global). lang:"en" troca os rotulos
     fixos da UI (paid-scene.html). Numeros com PONTO decimal (padrao EN).
     Mesma procedencia real e mesmo enquadramento descritivo das cenas PT.
     ========================================================== */

  /* V1 · jargao preflop */
  "p1-s1-en": { lang:"en", kicker:"Preflop · MTT", big:'RFI of <em>50%</em><br>on the BTN',
    heroBg:"shots/crop-preflop-table.png", heroFocus:true,
    line:"That's what the field's aggro reg does. Measured, not estimated.",
    caption:"50% RFI on the button. That's the field — not theory." },
  "p1-s2-en": { lang:"en", kicker:"Same spot, different villain",
    line:"The field isn't an average. It's profiles with different frequencies.",
    block:{ type:"vs", delta:"15 pts",
      a:{ lb:"Aggro reg", v:"50%", sb:"RFI on the BTN" }, aHot:true,
      b:{ lb:"Tight reg", v:"35%", sb:"RFI on the BTN" } },
    caption:"Aggro reg opens 50% of the button. Tight reg, 35%." },
  "p1-s3-en": { lang:"en", kicker:"The real screen",
    block:{ type:"shot", src:"shots/crop-preflop-table.png", w:920,
      title:"Aura · Preflop Analysis", cap:"real product, not a mockup" },
    caption:"Observed frequency, with sample size and confidence interval." },
  "p1-s4-en": { lang:"en", kicker:"Aggro reg · all positions",
    block:{ type:"stats", rows:[
      { k:"Fold vs RFI", v:"73%" }, { k:"3-Bet", v:"10%" }, { k:"Steal Attempt", v:"42%" } ] },
    line:"Every one of these is a spot you play every session.",
    caption:"Fold vs RFI, 3-bet, steal attempt — the whole field, measured." },
  "p1-s5-en": { lang:"en", kicker:"20+ filters · slice to the micro-spot",
    block:{ type:"shot", src:"shots/crop-filters-rail.png", w:640, chrome:false },
    caption:"Stage (early to final table) and buy-in — stack them with no cap." },

  /* V2 · dados reais vs teoria */
  "p2-s1-en": { lang:"en", kicker:"Postflop · MTT", big:'The math<br>says <em>64.5%</em>',
    heroBg:"shots/crop-exploit-cards.png", heroFocus:true,
    line:"The field defends 57.7%.",
    caption:"MDF of 64.5%. The field defends 57.7%." },
  "p2-s2-en": { lang:"en", kicker:"55% pot c-bet",
    line:"MDF is math. Real defense is measured behavior.",
    block:{ type:"bars", rows:[
      { sz:"55% pot", badge:"Overfold 6.8 pts", def:57.7, mdf:64.5, defL:"57.7%", mdfL:"64.5%" } ] },
    caption:"The field defends 57.7% where the math asks 64.5%." },
  "p2-s3-en": { lang:"en", kicker:"At every bet size",
    block:{ type:"shot", src:"shots/crop-exploit-cards.png", w:900,
      title:"Aura · Postflop Analysis", cap:"real product, not a mockup" },
    caption:"33%, 42%, 55% pot: the field sits below MDF in all of them." },
  "p2-s4-en": { lang:"en", kicker:"The base behind it",
    block:{ type:"stats", rows:[
      { k:"Hands in this spot", v:"10.6M" }, { k:"Audited hands", v:"<em>500M+</em>" },
      { k:"Rooms covered", v:"7" } ] },
    caption:"10.6 million hands in this spot alone. 500M+ in total." },
  "p2-s5-en": { lang:"en", big:'A solver shows<br>the <em>equilibrium</em>', bigSm:true,
    line:"Aura shows what the field <b>actually does</b> — across 500M+ real hands.",
    caption:"Equilibrium is the starting point. The field is the target." },

  /* V3 · leak / variancia */
  "p3-s1-en": { lang:"en", kicker:"Field intelligence · MTT", big:"It's not <em>variance</em>",
    heroBg:"shots/crop-sizedist.png", heroFocus:true,
    line:"It's a pattern. And patterns can be measured.",
    caption:"It's not variance. It's a pattern — and patterns can be measured." },
  "p3-s2-en": { lang:"en", kicker:"55% c-bet · flop texture",
    line:"Same bet size. Different board, different field.",
    block:{ type:"vs", delta:"+3 pts",
      a:{ lb:"Connected board", v:"6.9%", sb:"overfold vs MDF" },
      b:{ lb:"Disconnected board", v:"9.9%", sb:"overfold vs MDF" }, bHot:true },
    caption:"On a disconnected board the pool overfolds 9.9% — vs 6.9% on the connected one." },
  "p3-s3-en": { lang:"en", kicker:"And on the overpot the gap is bigger",
    line:"Almost three times the fold pressure, on the same line.",
    block:{ type:"vs", delta:"+5.3 pts",
      a:{ lb:"Connected board", v:"2.9%", sb:"overfold on overpot" },
      b:{ lb:"Disconnected board", v:"8.2%", sb:"overfold on overpot" }, bHot:true },
    caption:"Overpot on a disconnected board: 8.2% overfold vs 2.9%." },
  "p3-s4-en": { lang:"en", kicker:"The real screen, filtered by texture",
    block:{ type:"shot", src:"shots/crop-disconnected-col.png", w:520,
      title:"Aura · Postflop · disconnected board" },
    caption:"Connectedness, pairing, high card, flush draw — 13+ dimensions." },
  "p3-s5-en": { lang:"en", big:"The leak is the<br><em>field's</em>", bigSm:true,
    line:"Aura shows <b>where</b> it is — and on which board texture.",
    caption:"The leak isn't yours. It's the field's. And you can read it." },

  /* CTA (mesma cena final nos 3 EN) */
  "p-cta-en": { lang:"en", cta:true, line:"500M+ audited hands · 7 rooms",
    ctaBtn:"Create free account", ctaSub:"Preview of every module. No card." },

  /* ==========================================================
     VARIANTE -B (v3) — CAMADA DE PERSUASAO. Desafiante do teste A/B;
     a v2 (sem sufixo) continua sendo o CONTROLE e nao foi tocada.

     O que muda vs a v2:
      1. frame 1 abre TENSAO (pergunta/dor), nao fato
      2. callout de audiencia nos primeiros 2s — diz pra quem e
      3. cada cena de dado fecha o "e dai?" com CONSEQUENCIA DE DECISAO
         (nunca de resultado/lucro — proibido no gabarito e reprovavel pela Meta)
      4. prova social ("500M+ maos · 7 salas") vira selo PERSISTENTE no rodape
      5. numeros com <n> = count-up; barras com data-grow; data-in = reveal em beat

     O jargao denso fica INTACTO — e ele que filtra o publico (CTR 12,85% do
     vencedor historico veio dai). A missao foi somar tensao, nao trocar.
     ========================================================== */

  /* ---------- V1-B · preflop: contra QUAL reg você está jogando? ---------- */
  "b1-s1": { callout:"Pra quem joga MTT online", kicker:"Preflop · MTT",
    heroBg:"shots/crop-preflop-table.png", heroFocus:true,
    proof:"500M+ mãos auditadas · 7 salas",
    big:'Dois regs.<br>Mesmo <em>botão</em>.',
    line:'<span data-in="0.55"><n>15</n> pontos de diferença no RFI.</span>',
    caption:"Contra qual dos dois você está jogando agora?" },
  "b1-s2": { kicker:"O mesmo spot, dois perfis", proof:"500M+ mãos auditadas · 7 salas",
    block:{ type:"vs", delta:"15 pts",
      a:{ lb:"Reg agressivo", v:"<n>50%</n>", sb:"RFI no BTN" }, aHot:true,
      b:{ lb:"Reg tight", v:"<n>35%</n>", sb:"RFI no BTN" } },
    caption:"Você sabe contra qual perfil está — antes de apertar o botão." },
  "b1-s3": { kicker:"A tela real", proof:"500M+ mãos auditadas · 7 salas",
    block:{ type:"shot", src:"shots/crop-preflop-table.png", w:920,
      title:"Aura · Preflop Analysis", cap:"produto real, não mockup" },
    caption:"Frequência medida, com amostra e intervalo de confiança. Não é estimativa." },
  "b1-s4": { kicker:"Reg agressivo · todas as posições", proof:"500M+ mãos auditadas · 7 salas",
    block:{ type:"stats", rows:[
      { k:"Fold vs RFI", v:"<n>73%</n>" }, { k:"3-Bet", v:"<n>10%</n>" }, { k:"Steal Attempt", v:"<n>42%</n>" } ] },
    caption:"Você entra na mesa sabendo a frequência real que vai enfrentar." },
  "b1-s5": { kicker:"20+ filtros · recorta até o micro-spot", proof:"500M+ mãos auditadas · 7 salas",
    block:{ type:"shot", src:"shots/crop-filters-rail.png", w:640, chrome:false },
    caption:"O recorte é seu: estágio, buy-in, tipo de torneio. O field muda em cada um." },

  /* ---------- V2-B · a distância entre a matemática e o field ---------- */
  "b2-s1": { callout:"Pra quem joga MTT online", kicker:"Postflop · MTT",
    heroBg:"shots/crop-exploit-cards.png", heroFocus:true,
    proof:"500M+ mãos auditadas · 7 salas",
    /* o numero do TITULO fica cheio desde o frame 0 — ele e a capa do anuncio.
       O count-up vive no reveal (57,7%), que entra depois do beat. */
    big:'A matemática<br>diz <em>64,5%</em>',
    line:'<span data-in="0.5">O field faz <b><n>57,7%</n></b>. Você joga <em>nessa distância</em>.</span>',
    caption:"MDF 64,5% · field 57,7%. A distância é onde a decisão acontece." },
  "b2-s2": { kicker:"C-bet de 55% do pote", proof:"500M+ mãos auditadas · 7 salas",
    line:"MDF é matemática. Defesa real é comportamento medido.",
    block:{ type:"bars", rows:[
      { sz:"55% do pote", badge:"Overfold 6,8 pts", def:57.7, mdf:64.5, defL:"<n>57,7%</n>", mdfL:"64,5%" } ] },
    caption:"Você sabe o tamanho exato onde o field se afasta da marca." },
  "b2-s3": { kicker:"Em todo tamanho de aposta", proof:"500M+ mãos auditadas · 7 salas",
    block:{ type:"shot", src:"shots/crop-exploit-cards.png", w:900,
      title:"Aura · Postflop Analysis", cap:"produto real, não mockup" },
    caption:"33%, 42%, 55% — a defesa medida em cada size, sobre 10,6M mãos." },
  "b2-s4": { kicker:"A base por trás disso", proof:"500M+ mãos auditadas · 7 salas",
    block:{ type:"stats", rows:[
      { k:"Mãos só nesse spot", v:"<n>10,6M</n>" }, { k:"Mãos auditadas", v:"<em><n>500M+</n></em>" },
      { k:"Salas cobertas", v:"<n>7</n>" } ] },
    caption:"Amostra desse tamanho é o que separa leitura de achismo." },
  "b2-s5": { big:'Solver mostra o<br><em>equilíbrio</em>', bigSm:true,
    proof:"500M+ mãos auditadas · 7 salas",
    line:"A Aura mostra o que o field <b>realmente faz</b> — em 500M+ mãos reais.",
    caption:"Equilíbrio é o ponto de partida. O field é o alvo." },

  /* ---------- V3-B · a dor primeiro, o dado depois ---------- */
  "b3-s1": { callout:"Pra quem joga MTT online", kicker:"Field intelligence · MTT",
    heroBg:"shots/crop-sizedist.png", heroFocus:true,
    proof:"500M+ mãos auditadas · 7 salas",
    big:'Você não está<br><em>correndo mal.</em>',
    line:'<span data-in="0.6">O field mudou de comportamento. <b>Você não viu.</b></span>',
    caption:"Não é azar. É padrão — e padrão dá pra medir." },
  "b3-s2": { kicker:"C-bet de 55% · textura do flop", proof:"500M+ mãos auditadas · 7 salas",
    line:"Mesmo tamanho de aposta. Board diferente, field diferente.",
    block:{ type:"vs", delta:"+3 pts",
      a:{ lb:"Board conectado", v:"<n>6,9%</n>", sb:"overfold vs MDF" },
      b:{ lb:"Board desconexo", v:"<n>9,9%</n>", sb:"overfold vs MDF" }, bHot:true },
    caption:"Você lê a textura antes de escolher a linha." },
  "b3-s3": { kicker:"E no overpot a distância é maior", proof:"500M+ mãos auditadas · 7 salas",
    block:{ type:"vs", delta:"+5,3 pts",
      a:{ lb:"Board conectado", v:"<n>2,9%</n>", sb:"overfold no overpot" },
      b:{ lb:"Board desconexo", v:"<n>8,2%</n>", sb:"overfold no overpot" }, bHot:true },
    caption:"Quase três vezes mais pressão de fold, na mesma linha." },
  "b3-s4": { kicker:"A tela real, filtrada por textura", proof:"500M+ mãos auditadas · 7 salas",
    block:{ type:"shot", src:"shots/crop-disconnected-col.png", w:520,
      title:"Aura · Postflop · board desconexo" },
    caption:"3,1M mãos só nesse recorte. Conectividade, pareamento, flush draw — 13+ dimensões." },
  "b3-s5": { big:'O leak é do<br><em>field</em>', bigSm:true,
    proof:"500M+ mãos auditadas · 7 salas",
    line:"A Aura mostra <b>onde</b> ele está — e em qual textura de board.",
    caption:"O leak não é seu. É do field. E dá pra ler." },

  "p-cta-b": { cta:true, proof:"500M+ mãos auditadas · 7 salas",
    line:"Sem cartão. Preview de cada módulo.",
    ctaBtn:"Criar conta grátis", ctaSub:"O board completo destrava no upgrade." },

  /* ---------- VARIANTE -B · EN ---------- */
  "b1-s1-en": { lang:"en", callout:"For MTT grinders", kicker:"Preflop · MTT",
    heroBg:"shots/crop-preflop-table.png", heroFocus:true,
    proof:"500M+ audited hands · 7 rooms",
    big:'Two regs.<br>Same <em>button</em>.',
    line:'<span data-in="0.55"><n>15</n> points apart on RFI.</span>',
    caption:"Which one are you up against right now?" },
  "b1-s2-en": { lang:"en", kicker:"Same spot, two profiles", proof:"500M+ audited hands · 7 rooms",
    block:{ type:"vs", delta:"15 pts",
      a:{ lb:"Aggro reg", v:"<n>50%</n>", sb:"RFI on the BTN" }, aHot:true,
      b:{ lb:"Tight reg", v:"<n>35%</n>", sb:"RFI on the BTN" } },
    caption:"You know which profile you're facing — before you act." },
  "b1-s3-en": { lang:"en", kicker:"The real screen", proof:"500M+ audited hands · 7 rooms",
    block:{ type:"shot", src:"shots/crop-preflop-table.png", w:920,
      title:"Aura · Preflop Analysis", cap:"real product, not a mockup" },
    caption:"Measured frequency, with sample size and confidence interval. Not an estimate." },
  "b1-s4-en": { lang:"en", kicker:"Aggro reg · all positions", proof:"500M+ audited hands · 7 rooms",
    block:{ type:"stats", rows:[
      { k:"Fold vs RFI", v:"<n>73%</n>" }, { k:"3-Bet", v:"<n>10%</n>" }, { k:"Steal Attempt", v:"<n>42%</n>" } ] },
    caption:"You sit down knowing the real frequency you'll face." },
  "b1-s5-en": { lang:"en", kicker:"20+ filters · slice to the micro-spot", proof:"500M+ audited hands · 7 rooms",
    block:{ type:"shot", src:"shots/crop-filters-rail.png", w:640, chrome:false },
    caption:"Your slice: stage, buy-in, tournament type. The field shifts in each one." },

  "b2-s1-en": { lang:"en", callout:"For MTT grinders", kicker:"Postflop · MTT",
    heroBg:"shots/crop-exploit-cards.png", heroFocus:true,
    proof:"500M+ audited hands · 7 rooms",
    big:'The math<br>says <em>64.5%</em>',
    line:'<span data-in="0.5">The field does <b><n>57.7%</n></b>. You play <em>in that gap</em>.</span>',
    caption:"MDF 64.5% · field 57.7%. The gap is where the decision happens." },
  "b2-s2-en": { lang:"en", kicker:"55% pot c-bet", proof:"500M+ audited hands · 7 rooms",
    line:"MDF is math. Real defense is measured behavior.",
    block:{ type:"bars", rows:[
      { sz:"55% pot", badge:"Overfold 6.8 pts", def:57.7, mdf:64.5, defL:"<n>57.7%</n>", mdfL:"64.5%" } ] },
    caption:"You know the exact size where the field drifts from the mark." },
  "b2-s3-en": { lang:"en", kicker:"At every bet size", proof:"500M+ audited hands · 7 rooms",
    block:{ type:"shot", src:"shots/crop-exploit-cards.png", w:900,
      title:"Aura · Postflop Analysis", cap:"real product, not a mockup" },
    caption:"33%, 42%, 55% — defense measured at every size, across 10.6M hands." },
  "b2-s4-en": { lang:"en", kicker:"The base behind it", proof:"500M+ audited hands · 7 rooms",
    block:{ type:"stats", rows:[
      { k:"Hands in this spot", v:"<n>10.6M</n>" }, { k:"Audited hands", v:"<em><n>500M+</n></em>" },
      { k:"Rooms covered", v:"<n>7</n>" } ] },
    caption:"A sample this size is what separates a read from a hunch." },
  "b2-s5-en": { lang:"en", big:'A solver shows<br>the <em>equilibrium</em>', bigSm:true,
    proof:"500M+ audited hands · 7 rooms",
    line:"Aura shows what the field <b>actually does</b> — across 500M+ real hands.",
    caption:"Equilibrium is the starting point. The field is the target." },

  "b3-s1-en": { lang:"en", callout:"For MTT grinders", kicker:"Field intelligence · MTT",
    heroBg:"shots/crop-sizedist.png", heroFocus:true,
    proof:"500M+ audited hands · 7 rooms",
    big:"You're not<br><em>running bad.</em>",
    line:'<span data-in="0.6">The field changed how it plays. <b>You didn\'t see it.</b></span>',
    caption:"It's not variance. It's a pattern — and patterns can be measured." },
  "b3-s2-en": { lang:"en", kicker:"55% c-bet · flop texture", proof:"500M+ audited hands · 7 rooms",
    line:"Same bet size. Different board, different field.",
    block:{ type:"vs", delta:"+3 pts",
      a:{ lb:"Connected board", v:"<n>6.9%</n>", sb:"overfold vs MDF" },
      b:{ lb:"Disconnected board", v:"<n>9.9%</n>", sb:"overfold vs MDF" }, bHot:true },
    caption:"You read the texture before you pick the line." },
  "b3-s3-en": { lang:"en", kicker:"And on the overpot the gap is bigger", proof:"500M+ audited hands · 7 rooms",
    block:{ type:"vs", delta:"+5.3 pts",
      a:{ lb:"Connected board", v:"<n>2.9%</n>", sb:"overfold on overpot" },
      b:{ lb:"Disconnected board", v:"<n>8.2%</n>", sb:"overfold on overpot" }, bHot:true },
    caption:"Almost three times the fold pressure, on the same line." },
  "b3-s4-en": { lang:"en", kicker:"The real screen, filtered by texture", proof:"500M+ audited hands · 7 rooms",
    block:{ type:"shot", src:"shots/crop-disconnected-col.png", w:520,
      title:"Aura · Postflop · disconnected board" },
    caption:"3.1M hands in this slice alone. Connectedness, pairing, flush draw — 13+ dimensions." },
  "b3-s5-en": { lang:"en", big:'The leak is the<br><em>field\'s</em>', bigSm:true,
    proof:"500M+ audited hands · 7 rooms",
    line:"Aura shows <b>where</b> it is — and on which board texture.",
    caption:"The leak isn't yours. It's the field's. And you can read it." },

  "p-cta-b-en": { lang:"en", cta:true, proof:"500M+ audited hands · 7 rooms",
    line:"No card. Preview of every module.",
    ctaBtn:"Create free account", ctaSub:"The full board unlocks on upgrade." },

  /* ==========================================================
     CAMPANHA DE DESCOBERTA — 4 celulas (PT). Design validado pelo PO 25/07,
     em docs/02-paid/matriz-descoberta-4-celulas.md.

     NAO E CAMPANHA DE CONVERSAO. E instrumento de medicao de topo de funil:
     cada reel isola UMA hipotese de persona; os 4 juntos formam o experimento.

     🔴 OS 4 PRIMEIROS FRAMES SAO LITERAIS (doc §2). Kicker, gancho, beat e
     legenda de cada cena 1 estao aprovados palavra por palavra — mexer
     invalida a comparabilidade do teste. Qualquer mudanca volta pra Midia Paga.

     Padroes iguais nos 4 (doc §3): consequencia de DECISAO por cena (nunca
     resultado financeiro) · selo de prova persistente no rodape · print real
     ja na cena 1 · CTA identico (variavel de controle) · 18+ em todo quadro.
     ========================================================== */

  /* ---------- CELULA 1 · SOLVER — persona: reg que estuda solver ---------- */
  "d1-s1": { heroLogo:true, kicker:"MTT · pra quem estuda solver",  // 🔴 LITERAL
    heroBg:"shots/crop-exploit-cards.png", heroFocus:true,
    proof:"500M+ mãos auditadas · 7 salas",
    /* PO 25/07 (2a rodada): "equilibrio" -> "GTO". Mudanca de gancho aprovado —
       o doc §2 precisa ser atualizado pra Midia Paga nao trabalhar com spec velha. */
    /* quebra depois de "decorou": "VOCÊ DECOROU O" nao cabe em 1 linha a 104px
       e o "O" cai sozinho. Ajuste tipografico, palavras seguem literais. */
    big:'Você decorou<br>o <em>GTO.</em>',                       // 🔴 LITERAL (v2)
    line:'<span data-in="0.55">Seu oponente não.</span>',      // 🔴 LITERAL (beat)
    caption:"GTO é o ponto de partida. O adversário real é outro assunto." },
  /* v2: barra unica de MDF reprovada. Shot dos 6 sizes (Exploitative Sizes) —
     mensagem: comparar a resposta do field size a size. */
  /* v2.1 (PO 26/07): removida a legenda do rodape — a cena fica so com o shot. */
  "d1-s2": { kicker:"Defesa do field · size a size", proof:"500M+ mãos auditadas · 7 salas",
    line:"20%, 33%, 42%, 55%, 75%, overpot — lado a lado, cada um com a própria amostra.",
    block:{ type:"shot", src:"shots/crop-exploit-cards.png", w:900,
      title:"Aura · Postflop Analysis" },
    caption:"" },
  /* v2.1 (PO 26/07): cena "A tela real" (d1-s3) removida — repetia o mesmo shot
     de d1-s2 sem adicionar informacao nova. Ids seguintes NAO renumerados aqui
     (ficam como estao no deck); quem controla a sequencia e o CELLS.ids do
     build-descoberta.mjs, que ja tira "d1-s3" da lista. */
  "d1-s4": { kicker:"A base por trás disso", proof:"500M+ mãos auditadas · 7 salas",
    block:{ type:"stats", rows:[
      { k:"Mãos só nesse spot", v:"<n>10,6M</n>" }, { k:"Mãos auditadas", v:"<em><n>500M+</n></em>" },
      { k:"Salas cobertas", v:"<n>7</n>" } ] },
    caption:"Toda frequência vem com tamanho de amostra e intervalo de confiança." },
  /* v2.4 (PO 26/07, 5a rodada): headline trocado por pedido do PO — "vira anuncio
     da Aura", nao so a conclusao da cena 1. Mesmo padrao big+block+caption do d4-s1. */
  "d1-s5": { big:'Descubra o que o <em>field</em><br>realmente faz.', bigSm:true,
    proof:"500M+ mãos auditadas · 7 salas",
    block:{ type:"twofocus", src:"shots/mockup-two-devices.png", focus:"pre" },
    caption:"Ferramenta de estudo. Você continua decidindo na mesa." },

  /* ---------- CELULA 2 · EXPLOIT — persona: exploitativo ----------
     v2: legendas (caption) removidas de TODAS as cenas — caixa do rodape some. */
  "d2-s1": { heroLogo:true, kicker:"Postflop · c-bet de 55% do pote",  // 🔴 LITERAL
    heroBg:"shots/crop-sizedist.png", heroFocus:true,
    proof:"500M+ mãos auditadas · 7 salas",
    big:'A matemática<br>diz <em>64,5%</em>.',                 // 🔴 LITERAL
    /* numero SEM count-up de proposito: este frame e literal e instrumento de
       medicao — o count-up exibiria "41,5%" por ~0,6s, que nao e o gancho aprovado */
    line:'<span data-in="0.55">O field defende <b>57,7%</b>.</span>',  // 🔴 LITERAL (beat)
    caption:"" },
  /* v2.2 (PO 26/07, 3a rodada): sub-label "distância vs MDF" -> "Overfold vs MDF" a
     pedido do PO. "Overfold" ja e termo estabelecido no deck (badge em varias celulas
     — ver "badge:'Overfold'" acima); deixa de ser so a distancia numerica e nomeia
     o padrao. Doc/roteiro atualizados pra nao citar mais "distância vs MDF" como o
     termo de compliance desta celula. */
  "d2-s2": { kicker:"Mesma aposta, textura diferente", proof:"500M+ mãos auditadas · 7 salas",
    line:"O board muda o comportamento do field.",
    block:{ type:"vs", delta:"3 pts",
      a:{ lb:"Board conectado", v:"<n>6,9%</n>", sb:"Overfold vs MDF" },
      b:{ lb:"Board desconexo", v:"<n>9,9%</n>", sb:"Overfold vs MDF" }, bHot:true },
    caption:"" },
  /* v2.2 (PO 26/07, 3a rodada): Postflop 2x continua bloqueado no LOCAL (ver nota
     tecnica na matriz) — em vez de manter o crop antigo como placeholder, PO pediu
     pra reusar aqui o mockup "two devices" que ja existe (mesmo asset de d1-s5/
     d3-s5/d4-s2). */
  /* v2.4 (PO 26/07, 5a rodada): kicker "A tela real, filtrada por textura" ->
     headline "big" (mesmo tratamento do d1-s5, "vira anuncio da Aura").
     v2.5 (PO 26/07, 6a rodada): ordem trocada com d2-s4 (agora toca DEPOIS do
     2o comparativo "vs", como transicao pro headline/mockup). Caption "Baseado
     em dados, não palpite." moveu pra d2-s5 (evita repetir a mesma frase em
     duas cenas consecutivas); esta cena fica sem caption. */
  "d2-s3": { big:'Descubra o que o <em>field</em><br>faz em cada textura de board.', bigSm:true,
    proof:"500M+ mãos auditadas · 7 salas",
    block:{ type:"twofocus", src:"shots/mockup-two-devices.png", focus:"post" },
    caption:"" },
  /* v2.5 (PO 26/07, 6a rodada): sub-label "distância no overpot" -> "Overfold vs MDF"
     — mesmo ajuste de terminologia aplicado em d2-s2 na v2.2 (ficou faltando aqui). */
  "d2-s4": { kicker:"E no overpot a distância é maior", proof:"500M+ mãos auditadas · 7 salas",
    block:{ type:"vs", delta:"5,3 pts",
      a:{ lb:"Board conectado", v:"<n>2,9%</n>", sb:"Overfold vs MDF" },
      b:{ lb:"Board desconexo", v:"<n>8,2%</n>", sb:"Overfold vs MDF" }, bHot:true },
    caption:"" },
  "d2-s5": { big:'O número é<br>do <em>field</em>', bigSm:true,
    proof:"500M+ mãos auditadas · 7 salas",
    /* v2.3 (PO 26/07): "tamanho" -> "size" — loanword ja estabelecido no deck
       (ver "size por size" em p1/p2, "size a size" no d1-s2).
       v2.5 (PO 26/07, 6a rodada): "Descrição, não palpite." -> "Baseado em
       dados, não palpite." — frase que antes estava na caption de d2-s3
       (removida de lá pra nao repetir nas duas cenas). */
    line:"Frequência observada, por textura e por size. <b>Baseado em dados, não palpite.</b>",
    caption:"" },

  /* ---------- CELULA 3 · CATEGORIA — controle do experimento ---------- */
  /* PO 25/07 (2a rodada): lockup grande na cena 1 — sinaliza "app novo" antes
     mesmo de ler o gancho. Faz sentido justo nesta celula, que e a mais ampla.
     v2: logo PNG completa (Ativo 80@2x). Se piorar vs lockup SVG aprovado, reverter. */
  "d3-s1": { kicker:"MTT", heroLogo:true,                      // 🔴 LITERAL
    heroBg:"shots/crop-preflop-table.png", heroFocus:true,
    proof:"500M+ mãos auditadas · 7 salas",
    big:'Não é solver.<br>Não é <em>tracker</em>.',            // 🔴 LITERAL
    line:'<span data-in="0.55">É o que o field <b>inteiro</b> faz.</span>',  // 🔴 LITERAL (beat)
    caption:"O mesmo jogo — novas informações." },             // 🔴 LITERAL (selo)
  "d3-s2": { kicker:"O que cada um responde", proof:"500M+ mãos auditadas · 7 salas",
    block:{ type:"stats", rows:[
      { k:"Solver", v:"o equilíbrio" }, { k:"Tracker", v:"as SUAS mãos" },
      { k:"Aura", v:"<em>o field</em>" } ] },
    caption:"Três perguntas diferentes. A Aura responde a terceira." },
  /* v2.4 (PO 26/07, 5a rodada): texto que estava no caption (rodape) subiu pra
     "line" (acima do shot, mais em destaque) — pedido do PO. Caption eliminado,
     nao duplica o texto. */
  "d3-s3": { kicker:"A tela real", proof:"500M+ mãos auditadas · 7 salas",
    line:"RFI, 3-bet, 4-bet, steal — por posição, com amostra e intervalo de confiança.",
    block:{ type:"shot", src:"shots/crop-preflop-table.png", w:920,
      title:"Aura · Preflop Analysis" },
    caption:"" },
  "d3-s4": { kicker:"Medido em", proof:"500M+ mãos auditadas · 7 salas",
    block:{ type:"stats", rows:[
      { k:"Mãos auditadas", v:"<em><n>500M+</n></em>" }, { k:"Salas cobertas", v:"<n>7</n>" },
      { k:"Atualização", v:"trimestral" } ] },
    caption:"100% anonimizado. Nenhuma mão ligada a jogador." },
  /* v2.1 (PO 26/07): legenda do rodape removida. */
  "d3-s5": { big:'O mesmo jogo<br><em>novas informações</em>', bigSm:true,
    proof:"500M+ mãos auditadas · 7 salas",
    block:{ type:"twofocus", src:"shots/mockup-two-devices.png", focus:"pre" },
    caption:"" },

  /* ---------- CELULA 4 · PIONEIRO — testa POSICIONAMENTO, nao persona ----------
     Sequencia deliberada do doc §2: o gancho faz SENTIR o ineditismo, a linha
     NOMEIA a categoria. A legenda do rodape FOI REMOVIDA na v2 (PO 26/07) —
     o instrumento do teste passa a ser gancho + linha; doc §2 atualizado. */
  /* v2.1 (PO 26/07): rebalanco de enfase — palavras seguem 🔴 LITERAIS, so
     tipografia mudou. "Isso não existia." estava dominando o frame (104px);
     cai pra bigSm. Kicker "Inteligência de field · MTT" ganha peso (classe
     .lg) pra competir de igual com o headline — e a categoria do posicionamento,
     nao so um rotulo. A linha "Mass Data Analysis..." desce (margin-top). */
  "d4-s1": { kicker:"Inteligência de field · MTT", kickerLg:true, heroLogo:true,  // 🔴 LITERAL
    heroBg:"shots/crop-postflop-wide.png", heroFocus:true,
    proof:"500M+ mãos auditadas · 7 salas",
    big:'Isso não <em>existia</em>.', bigSm:true,               // 🔴 LITERAL
    line:'<span data-in="0.55" style="display:block;margin-top:26px">Mass Data Analysis aplicada a MTT.</span>',  // 🔴 LITERAL
    caption:"" },
  /* v2.4 (PO 26/07, 5a rodada): kicker "População, não amostra" -> pedido do PO. */
  "d4-s2": { kicker:"Os padrões do field a um clique de distância", proof:"500M+ mãos auditadas · 7 salas",
    block:{ type:"twofocus", src:"shots/mockup-two-devices.png", focus:"post" },
    caption:"" },
  /* v2.2 (PO 26/07, 3a rodada): cena "A tela real" (d4-s3, mockup-preflop-app.png)
     removida a pedido do PO. Ids seguintes NAO renumerados aqui (ficam como estao
     no deck); quem controla a sequencia e o CELLS.ids do build-descoberta.mjs, que
     ja tira "d4-s3" da lista — mesmo padrao usado em d1-s3 na v2.1. */
  /* PO 25/07 (2a rodada): "exemplificar os 6 estagios". Em vez de dizer "6",
     mostra o painel REAL com eles nomeados (Pre Bubble, Early ITM, FT...) —
     exemplifica e ainda cumpre "usar os prints de filtros". */
  "d4-s4": { kicker:"Do Early-Game à Mesa Final", proof:"500M+ mãos auditadas · 7 salas",
    block:{ type:"shot", src:"shots/crop-filters-rail.png", w:620, chrome:false },
    caption:"" },
  "d4-s5": { big:'Inteligência<br>de <em>field</em>', bigSm:true,
    proof:"500M+ mãos auditadas · 7 salas",
    line:"O mesmo jogo — <b>novas informações</b>.",
    caption:"" },

  /* CTA IDENTICO nos 4 — e variavel de controle do experimento (doc §3.4).
     Nao personalizar por celula: diferenca no CTA contamina a leitura. */
  "d-cta": { cta:true, proof:"500M+ mãos auditadas · 7 salas",
    line:"500M+ mãos auditadas · 7 salas",
    ctaBtn:"Criar conta grátis", ctaSub:"Preview de cada módulo. Sem cartão." },

  /* ================================================================
     CAMPANHA DE DESCOBERTA — VERSOES EN (26/07, apos aprovacao PT v2.3).
     Vocabulario alinhado ao que ja existia em EN no deck (p1/p2/p3, b1/b2/b3):
     field, size, MDF, 500M+ audited hands · 7 rooms, Create free account.
     Numeros: virgula decimal PT -> ponto decimal EN (10,6M -> 10.6M etc).
     Render so apos pedido explicito do PO (ver matriz §6). ================= */

  /* ---------- CELULA 1 · SOLVER (EN) ---------- */
  "d1-s1-en": { lang:"en", heroLogo:true, kicker:"MTT · for solver students",
    heroBg:"shots/crop-exploit-cards.png", heroFocus:true,
    proof:"500M+ audited hands · 7 rooms",
    big:'You memorized<br>the <em>GTO.</em>',
    line:'<span data-in="0.55">Your opponent didn\'t.</span>',
    caption:"GTO is the starting point. The real opponent is a different matter." },
  "d1-s2-en": { lang:"en", kicker:"Field Defense % · size by size", proof:"500M+ audited hands · 7 rooms",
    line:"20%, 33%, 42%, 55%, 75%, overpot — side by side, each with its own sample.",
    block:{ type:"shot", src:"shots/crop-exploit-cards.png", w:900,
      title:"Aura · Postflop Analysis" },
    caption:"" },
  "d1-s4-en": { lang:"en", kicker:"The database behind it", proof:"500M+ audited hands · 7 rooms",
    block:{ type:"stats", rows:[
      { k:"Hands in this spot alone", v:"<n>10.6M</n>" }, { k:"Hands audited", v:"<em><n>500M+</n></em>" },
      { k:"Rooms covered", v:"<n>7</n>" } ] },
    caption:"Every frequency comes with sample size and confidence interval." },
  "d1-s5-en": { lang:"en", big:'GTO is the <em>start</em>',
    proof:"500M+ audited hands · 7 rooms",
    block:{ type:"twofocus", src:"shots/mockup-two-devices.png", focus:"pre" },
    caption:"A study tool. You still make the call at the table." },

  /* ---------- CELULA 2 · EXPLOIT (EN) ---------- */
  "d2-s1-en": { lang:"en", heroLogo:true, kicker:"Postflop · 55% pot c-bet",
    heroBg:"shots/crop-sizedist.png", heroFocus:true,
    proof:"500M+ audited hands · 7 rooms",
    big:'The math<br>says <em>64.5%</em>.',
    line:'<span data-in="0.55">The field defends <b>57.7%</b>.</span>',
    caption:"" },
  "d2-s2-en": { lang:"en", kicker:"Same bet, different texture", proof:"500M+ audited hands · 7 rooms",
    line:"The board changes the field's behavior.",
    block:{ type:"vs", delta:"3 pts",
      a:{ lb:"Connected board", v:"<n>6.9%</n>", sb:"Overfold vs MDF" },
      b:{ lb:"Disconnected board", v:"<n>9.9%</n>", sb:"Overfold vs MDF" }, bHot:true },
    caption:"" },
  "d2-s3-en": { lang:"en", kicker:"The real screen, filtered by texture", proof:"500M+ audited hands · 7 rooms",
    block:{ type:"twofocus", src:"shots/mockup-two-devices.png", focus:"post" },
    caption:"" },
  "d2-s4-en": { lang:"en", kicker:"And on the overpot the gap is bigger", proof:"500M+ audited hands · 7 rooms",
    block:{ type:"vs", delta:"5.3 pts",
      a:{ lb:"Connected board", v:"<n>2.9%</n>", sb:"Overfold vs MDF" },
      b:{ lb:"Disconnected board", v:"<n>8.2%</n>", sb:"Overfold vs MDF" }, bHot:true },
    caption:"" },
  "d2-s5-en": { lang:"en", big:'The number is<br>the <em>field\'s</em>', bigSm:true,
    proof:"500M+ audited hands · 7 rooms",
    line:"Observed frequency, by texture and by size. <b>Real Data, not a guess.</b>",
    caption:"" },

  /* ---------- CELULA 3 · CATEGORIA (EN) ---------- */
  "d3-s1-en": { lang:"en", kicker:"MTT", heroLogo:true,
    heroBg:"shots/crop-preflop-table.png", heroFocus:true,
    proof:"500M+ audited hands · 7 rooms",
    big:"It's not a solver.<br>It's not a <em>tracker</em>.",
    line:'<span data-in="0.55">It\'s what the <b>entire</b> field does.</span>',
    caption:"The same game — new information." },
  "d3-s2-en": { lang:"en", kicker:"What each one answers", proof:"500M+ audited hands · 7 rooms",
    block:{ type:"stats", rows:[
      { k:"Solver", v:"the equilibrium" }, { k:"Tracker", v:"YOUR hands" },
      { k:"Aura", v:"<em>the field</em>" } ] },
    caption:"Three different questions. Aura answers the third." },
  "d3-s3-en": { lang:"en", kicker:"The real screen", proof:"500M+ audited hands · 7 rooms",
    block:{ type:"shot", src:"shots/crop-preflop-table.png", w:920,
      title:"Aura · Preflop Analysis" },
    caption:"RFI, 3-bet, 4-bet, steal — by position, with sample size and confidence interval." },
  "d3-s4-en": { lang:"en", kicker:"Measured in", proof:"500M+ audited hands · 7 rooms",
    block:{ type:"stats", rows:[
      { k:"Hands audited", v:"<em><n>500M+</n></em>" }, { k:"Rooms covered", v:"<n>7</n>" },
      { k:"Update", v:"quarterly" } ] },
    caption:"100% anonymized. No hand linked to a player." },
  "d3-s5-en": { lang:"en", big:'The same game<br><em>new information</em>', bigSm:true,
    proof:"500M+ audited hands · 7 rooms",
    block:{ type:"twofocus", src:"shots/mockup-two-devices.png", focus:"pre" },
    caption:"" },

  /* ---------- CELULA 4 · PIONEIRO (EN) ---------- */
  "d4-s1-en": { lang:"en", kicker:"Field intelligence · MTT", kickerLg:true, heroLogo:true,
    heroBg:"shots/crop-postflop-wide.png", heroFocus:true,
    proof:"500M+ audited hands · 7 rooms",
    big:'This never <em>existed</em>.', bigSm:true,
    line:'<span data-in="0.55" style="display:block;margin-top:26px">Mass Data Analysis applied to MTT.</span>',
    caption:"" },
  "d4-s2-en": { lang:"en", kicker:"The field's data, not a sample", proof:"500M+ audited hands · 7 rooms",
    block:{ type:"twofocus", src:"shots/mockup-two-devices.png", focus:"post" },
    caption:"" },
  "d4-s4-en": { lang:"en", kicker:"From Early Game to the Final Table", proof:"500M+ audited hands · 7 rooms",
    block:{ type:"shot", src:"shots/crop-filters-rail.png", w:620, chrome:false },
    caption:"" },
  "d4-s5-en": { lang:"en", big:'Field<br><em>intelligence</em>', bigSm:true,
    proof:"500M+ audited hands · 7 rooms",
    line:"The same game — <b>new information</b>.",
    caption:"" },

  /* CTA EN — mesma regra do PT: identico nos 4, variavel de controle. */
  "d-cta-en": { lang:"en", cta:true, proof:"500M+ audited hands · 7 rooms",
    line:"500M+ audited hands · 7 rooms",
    ctaBtn:"Create free account", ctaSub:"Preview of every module. No card." },
};
