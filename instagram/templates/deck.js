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
};
