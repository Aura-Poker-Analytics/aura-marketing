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
    titleHtml: "The pool <em>overfolds</em> every sizing",
    shotSrc: "shots/postflop1.png", shotBg: "#0B1120", frameH: 600, badge: "3.2M hands",
    caption: "Raise vs flop c-bet, BTN caller. Real pool defense vs MDF, per bet size — every red bar is an overfold to attack.",
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
    line: "É o que o reg agressivo do field faz. Medido, não estimado.",
    caption: "RFI de 50% no botão. Isso é o field — não é teoria." },
  "p1-s2": { kicker: "Mesmo spot, vilão diferente",
    line: "O field não é uma média. São perfis com frequências diferentes.",
    block: { type:"vs", delta:"15 pts",
      a:{ lb:"Reg agressivo", v:"50%", sb:"RFI no BTN" }, aHot:true,
      b:{ lb:"Reg tight", v:"35%", sb:"RFI no BTN" } },
    caption: "Reg agressivo abre 50% do botão. Reg tight, 35%." },
  "p1-s3": { kicker: "A tela real",
    block: { type:"preflop", title:"Reg Aggro", right:"▲▼ vs Global", cols:["CO","BTN","SB"], hi:"RFI",
      rows:[["RFI","29%","36%","50%","45%"],["Fold vs RFI","73%","83%","79%","77%"],
            ["3-Bet","10%","9%","10%","12%"],["Fold to 3-Bet","50%","52%","60%","62%"],
            ["4-Bet","19%","18%","15%","18%"],["Steal Att.","42%","36%","50%","45%"]] },
    caption: "Frequência observada, com tamanho de amostra e intervalo de confiança." },
  "p1-s4": { kicker: "Reg agressivo · todas as posições",
    block: { type:"stats", rows:[
      { k:"Fold vs RFI", v:"73%" }, { k:"3-Bet", v:"10%" }, { k:"Steal Attempt", v:"42%" } ] },
    line: "Cada número desses é um spot que você joga toda sessão.",
    caption: "Fold vs RFI, 3-bet, steal attempt — o field inteiro, medido." },
  "p1-s5": { big: 'Recorta por <em>posição</em>,<br>stack, estágio<br>e tipo de vilão', bigSm: true,
    line: "Filtros empilháveis: buy-in, KO, Mystery Bounty, bolha, mesa final.",
    caption: "20+ filtros combináveis até o micro-spot exato." },

  /* ---------- V2 · dados reais vs teoria (angulo desocupado na Ads Library) ---------- */
  "p2-s1": { kicker: "Postflop · MTT", big: 'A matemática<br>diz <em>64,5%</em>',
    line: "O field defende 57,7%.",
    caption: "MDF de 64,5%. O field defende 57,7%." },
  "p2-s2": { kicker: "C-bet de 55% do pote",
    line: "MDF é matemática. Defesa real é comportamento. O gap é o alvo.",
    block: { type:"bars", rows:[
      { sz:"55% do pote", badge:"Overfold 6,8 pts", def:57.7, mdf:64.5, defL:"57,7%", mdfL:"64,5%" } ] },
    caption: "A distância entre a linha amarela e a barra é o gap explorável." },
  "p2-s3": { kicker: "Em todo tamanho de aposta",
    block: { type:"postflop", head:"XR Flop CBet", sub:"10,6M mãos · CO abre, BB paga", val:"13,9%",
      sect:"Tamanhos exploráveis", rows:[
        { sz:"33% do pote", badge:"Overfold 9,4%", def:65.8, mdf:75.2, defL:"65,8%", mdfL:"75,2%" },
        { sz:"42% do pote", badge:"Overfold 9,0%", def:61.4, mdf:70.4, defL:"61,4%", mdfL:"70,4%" },
        { sz:"55% do pote", badge:"Overfold 6,8%", def:57.7, mdf:64.5, defL:"57,7%", mdfL:"64,5%" } ] },
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
    line: "É padrão. E padrão dá pra medir.",
    caption: "Não é azar. É padrão — e padrão dá pra medir." },
  "p3-s2": { kicker: "C-bet de 55% · textura do flop",
    line: "Mesmo tamanho de aposta. Board diferente, field diferente.",
    block: { type:"vs", delta:"+3 pts",
      a:{ lb:"Board conectado", v:"6,9%", sb:"overfold vs MDF" },
      b:{ lb:"Board desconexo", v:"9,9%", sb:"overfold vs MDF" }, bHot:true },
    caption: "Em board desconexo o pool superfolda 9,9% — contra 6,9% no conectado." },
  "p3-s3": { kicker: "E no overpot o buraco é maior",
    line: "Quase três vezes mais pressão de fold, na mesma linha.",
    block: { type:"vs", delta:"+5,3 pts",
      a:{ lb:"Board conectado", v:"2,9%", sb:"overfold no overpot" },
      b:{ lb:"Board desconexo", v:"8,2%", sb:"overfold no overpot" }, bHot:true },
    caption: "Overpot em board desconexo: 8,2% de overfold contra 2,9%." },
  "p3-s4": { kicker: "A tela real, filtrada por textura",
    block: { type:"postflop", head:"XR Flop CBet", sub:"3,1M mãos · board desconexo", val:"11,5%",
      sect:"Tamanhos exploráveis", rows:[
        { sz:"33% do pote", badge:"Overfold 11,0%", def:64.2, mdf:75.2, defL:"64,2%", mdfL:"75,2%" },
        { sz:"42% do pote", badge:"Overfold 11,2%", def:59.2, mdf:70.4, defL:"59,2%", mdfL:"70,4%" },
        { sz:"55% do pote", badge:"Overfold 9,9%", def:54.6, mdf:64.5, defL:"54,6%", mdfL:"64,5%" } ] },
    caption: "Conectividade, pareamento, high card, flush draw — 13+ dimensões." },
  "p3-s5": { big: 'O leak é do<br><em>field</em>', bigSm: true,
    line: "A Aura mostra <b>onde</b> ele está — e em qual textura de board.",
    caption: "O leak não é seu. É do field. E dá pra explorar." },

  /* ---------- CTA (mesma cena final nos 3) ---------- */
  "p-cta": { cta: true, line: "500M+ mãos auditadas · 7 salas",
    ctaBtn: "Criar conta grátis", ctaSub: "Preview de cada módulo. Sem cartão." },
};
