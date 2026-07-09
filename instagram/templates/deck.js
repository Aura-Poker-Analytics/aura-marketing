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
    sub: "Field intelligence for MTT grinders — the pool's real strategy, measured across billions of hands.",
    cta: "Create free account",
    ctaSub: "aura.poker · link in bio",
    showCards: true,
    footerLeft: "aura.poker",
  },

  /* D1 — CARROSSEL "MEET AURA 2.0" (5 slides) */
  "meet-capa": {
    kicker: "Launch · Aura 2.0",
    hookHtml: "Meet <em>Aura 2.0</em>",
    sub: "Not a tracker. Not a solver. The pool's real strategy — across billions of MTT hands.",
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
    titleHtml: "Every position, <em>vs the field</em>",
    bodyHtml: [
      "How the pool opens, 3-bets and defends by position and stack — not solver theory, what players <b>actually do</b>.",
    ],
    mock: "preflop",
    handle: "@aurapokeranalytics",
  },
  "meet-postflop": {
    slideNumber: "03",
    slideIndicator: "3 / 5",
    kicker: "Postflop Analysis",
    titleHtml: "The pool's <em>response</em> to every line",
    bodyHtml: [
      "Pick the spot and sizing. Aura shows the field's fold / call / raise — with the <b>MDF line</b> right on the bar.",
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
      "The spots where the field is most exploitable, sorted for you — <b>free to explore</b> in the free plan.",
    ],
    mock: "hotspot",
    handle: "@aurapokeranalytics",
  },
  "meet-cta": {
    headlineHtml: "Study the field. <em>Free.</em>",
    bullets: [
      "Free plan, forever — no card required",
      "Hotspot + Preflop included",
      "Billions of real MTT hands",
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
      "<b>Ranked leaks</b> — the field's worst spots, sorted by exploitability.",
      "<b>MDF on the bar</b> — see how far the pool is from minimum defense.",
      "<b>Free tier</b> — Hotspot is included in the free plan.",
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
    cards: [
      { badge: "Overfold", title: "BB vs BTN · Flop · Bet 33% pot", poolPct: 48, mdfPct: 62,
        meta: "Fold 48% · Call 41% · Raise 11% · 480k mãos" },
      { badge: "Overfold", title: "BB vs BTN · Turn · Bet 66% pot", poolPct: 44, mdfPct: 58,
        meta: "Fold 44% · Call 43% · Raise 13% · 260k mãos" },
    ],
    bullets: [
      "<b>Every line</b> — fold / call / raise for each sizing.",
      "<b>MDF reference</b> — spot over- and under-defense instantly.",
      "<b>Filter it</b> — by stake, position and tournament stage.",
    ],
    footerNote: "aura.poker",
  },

  /* ========== SEMANA 2 ========== */

  /* Carrossel "Preflop in 60s" */
  "w2-pre-capa": {
    kicker: "Preflop in 60s",
    hookHtml: "The field <em>opens too much</em>",
    sub: "A 60-second tour of what Aura's Preflop module shows you.",
    swipe: "Swipe →",
    handle: "@aurapokeranalytics",
  },
  "w2-pre-slide1": {
    slideNumber: "02", slideIndicator: "2 / 4",
    kicker: "Preflop Analysis",
    titleHtml: "RFI by position, <em>vs the pool</em>",
    bodyHtml: ["The green/red deltas show where the field opens wider or tighter than your reference — your first read before the flop."],
    mock: "preflop", handle: "@aurapokeranalytics",
  },
  "w2-pre-slide2": {
    slideNumber: "03", slideIndicator: "3 / 4",
    kicker: "Preflop Analysis",
    titleHtml: "Filter by <em>stack & stage</em>",
    bodyHtml: ["Short stacks, bubble, deep early — the field plays each differently. Aura slices preflop by all of it."],
    mock: "preflop", handle: "@aurapokeranalytics",
  },
  "w2-pre-cta": {
    headlineHtml: "See your pool. <em>Free.</em>",
    bullets: ["Preflop grid in the free plan", "Billions of real MTT hands", "No card required"],
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
      "<b>Check any spot</b> — free in Hotspot.",
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

  /* Carrossel "Postflop — read the pool" */
  "w3-post-capa": {
    kicker: "Module tour · Postflop",
    hookHtml: "Read the pool, <em>not the solver</em>",
    sub: "How Aura's Postflop module turns raw frequencies into a read.",
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
    titleHtml: "Pick the <em>sizing</em>",
    bodyHtml: ["33%, 66%, overbet — the field reacts differently to each. Aura splits the pool's response by every sizing you use."],
    mock: "postflop", handle: "@aurapokeranalytics",
  },
  "w3-post-slide2": {
    slideNumber: "03", slideIndicator: "3 / 4",
    kicker: "Postflop Analysis",
    titleHtml: "The <em>MDF line</em> does the work",
    bodyHtml: ["When the pool's defense bar falls short of the MDF marker, that gap is your exploit — visible at a glance."],
    mock: "postflop", handle: "@aurapokeranalytics",
  },
  "w3-post-cta": {
    headlineHtml: "Attack the field. <em>Free.</em>",
    bullets: ["Postflop reads in the free plan", "MDF on every bar", "No card required"],
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
      "<b>Preflop grid</b> — free to explore.",
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
    bodyHtml: ["The bar shorter than the MDF mark = the field folds too much here. That 14-point gap is money left on the table."],
    mock: "hotspot", handle: "@aurapokeranalytics",
  },
  "w4-hs-slide2": {
    slideNumber: "03", slideIndicator: "3 / 4",
    kicker: "Take the line",
    titleHtml: "So you <em>bet more, cheaper</em>",
    bodyHtml: ["Against an over-folding field, a small c-bet prints. The card tells you where; you bring the aggression."],
    mock: "hotspot", handle: "@aurapokeranalytics",
  },
  "w4-hs-cta": {
    headlineHtml: "Find your spots. <em>Free.</em>",
    bullets: ["Ranked exploit cards, free", "MDF vs pool on every card", "No card required"],
    ctaLabel: "Create free account", ctaSub: "link in bio",
    tagline: "The same game. New information.", handle: "@aurapokeranalytics",
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
      "<b>Every seat</b> — RFI, 3-bet, defense by position.",
      "<b>Deltas built in</b> — wider/tighter than reference, color-coded.",
      "<b>Free tier</b> — preflop is in the free plan.",
    ],
    footerNote: "aura.poker",
  },
};
