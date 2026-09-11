# Case study — finding the leak, and recovering the campaign

A complete worked diagnosis from a real campaign. Account identifiers are removed; every number is real.

**Setup:** cold traffic campaign for a $39/month paid community with a 7-day trial. Objective `OUTCOME_TRAFFIC`, optimizing for `LANDING_PAGE_VIEWS`. Budget $31/day. Geo US/UK/CA/AU/IE, ages 20–65, Advantage+ audience. Eleven static image creatives, each hooked on a recognizable AI tool name. Advantage+ placements.

---

## Day 5: the symptom

Four days in. The dashboard looked fine.

| Metric | Value | Dashboard verdict |
|---|---|---|
| Spend | $130.88 | on pace |
| Impressions | 37,069 | fine |
| Clicks | 728 | fine |
| CTR | 1.96% | above 1% target — green |
| Visits | 580 | fine |
| Cost per visit | $0.23 | well under $0.35 target — green |
| **Purchases** | **0** | — |

Everything green except the only column that mattered.

---

## Mistake #1: a threshold nobody derived

The $0.35 cost-per-visit target had been computed backwards from a 2.5% conversion rate. That 2.5% came from the community's **organic** traffic — people who already followed the brand and arrived warm.

Cold Reels traffic is a different population. Applying the organic conversion rate to it produced a target that read green for four days while the campaign converted at zero.

**Lesson:** every threshold must state where it came from. A target derived from an unmeasured assumption is worse than no target, because green metrics stop people asking questions. See `statistical-thresholds.md`.

---

## Mistake #2: blaming tracking

The initial read was "the platform is not sending the registration event — tracking is broken."

That was wrong, and the reasoning was invalid. With zero signups, a working pixel and a broken pixel produce identical campaign data. Absence of `offsite_conversion.*` in the campaign report proves nothing on its own.

Checking Events Manager settled it:

| Event | Count | Source |
|---|---|---|
| PageView | 583 | Browser |
| TestEvent | 4 | CAPI |
| **Purchase** | **2** | Multiple |

Two purchases existed. Zero appeared in campaign insights. So both came from organic traffic.

That reframed the whole problem. The offer *could* convert — just not for anyone arriving from these ads. Ads: 580 visits, 0 sales. Organic: 2 sales.

A second finding: the platform fired **`Purchase`** for a trial start on a paid group, not `CompleteRegistration`. Optimizing for the wrong event name would have starved the ad set of signal entirely.

See `tracking-verification.md`.

---

## The actual cause: placement breakdown

One query, run on day 5, explained everything:

| Placement | Impressions | Spend | Visits | CPM |
|---|---|---|---|---|
| **Instagram Reels** | **33,619** | **$108.62** | **510** | **$3.23** |
| Facebook Reels | 896 | $6.30 | 25 | $7.03 |
| Instagram Stories | 826 | $3.18 | 10 | $3.86 |
| Instagram Feed | 598 | $7.81 | 16 | $13.06 |
| Facebook Feed | 312 | $1.79 | 4 | $5.75 |

**90% of the budget went to Reels** — 85% to Instagram Reels alone.

Advantage+ placements had done exactly what it was told: find the cheapest landing page views. The cheapest landing page views on Meta come from people swiping through Reels at speed, catching a link on the way past. They arrive on the page without ever having decided to evaluate anything.

Feed — the placement where someone stops and reads — received 20 visits across the entire four days. It had never been tested. It had been sampled.

The $3.23 CPM had been read as efficiency for four days. It was a warning the whole time.

---

## The fix, and how it went wrong

Placements were switched to feed-only:

```json
{
  "publisher_platforms": ["facebook", "instagram"],
  "facebook_positions": ["feed"],
  "instagram_positions": ["stream"]
}
```

Applied at 10:52. Delivery collapsed within the hour.

| Hour | Impressions | Spend |
|---|---|---|
| 07 | 436 | $1.21 |
| 08 | 557 | $1.34 |
| 09 | 429 | $1.23 |
| 10 | 291 | $0.75 |
| **11** | **1** | **$0.00** |
| 12 | 1 | $0.01 |
| 13 | 1 | $0.00 |
| 14 | 1 | $0.01 |
| 15 | 6 | $0.04 |
| 16 | 1 | $0.02 |

**12 impressions and $0.14 across six hours**, against 300–550 per hour before.

The CPM told the story: $2.40–3.10 before the edit, $10–20 after. The bid model had been calibrated against $3 Reels inventory. Feed inventory cost 4–7× more. The ad set could no longer win auctions at all.

Two failures stacked: a learning-phase reset from the targeting change, and a bid model mismatched to the new inventory. The first recovers on its own. The second does not.

Separately, Ads Manager began throwing `Invalid request. (#1)` and showing an empty campaign table. An API check confirmed the account was completely healthy — `account_status: 1`, no disable reason, no spend cap, valid payment method. **The UI error was unrelated to the stall.** Chasing it would have wasted hours.

---

## Rebuild instead of wait

The standing plan had been to wait until morning. That was wrong, and the reasoning that justified it was wrong: "another edit is another learning reset" does not apply to **creating a new ad set**, because a new ad set has no learning history to reset. The stalled ad set had nothing worth salvaging — its accumulated learning was calibrated to inventory no longer being bought.

Rebuild, at 16:14 the same day:

1. New ad set created `PAUSED`, feed placements set **at creation** rather than as an edit.
2. All 11 ads recreated with the **existing creative IDs** — so the ads pointed at the same page posts and kept their accumulated likes, comments and saves.
3. Pixel tracking spec carried onto each ad.
4. Old ad set paused first, then the new one activated.

Elapsed time: about 15 minutes. Ads passed re-review within the hour.

---

## Result

| Metric | Reels period | Feed period | Change |
|---|---|---|---|
| CTR | 1.96% | 3.53% | +80% |
| CPM | $3.53 | $10.19 | 3× worse |
| Cost per visit | $0.23 | $0.48 | 2× worse |
| Visits per day | ~135 | ~65 | half |

**And the CTR gain proves nothing about the creatives.** Feed structurally outperforms Reels on CTR because the ad occupies a different position in a different browsing mode. The same 11 images simply moved somewhere they get clicked more. Reporting that as a creative win would have been a third mistake.

Also worth noting: the 3.53% is **all clicks**. Link CTR was 2.87% — 57 link clicks out of 70 total. The rest were reactions and profile taps.

---

## What the numbers could and could not support

After 580 Reels visits with zero purchases, the rule of three gives a 95% upper bound of roughly **0.52%**. That was decisive against a 2% planning assumption, and told you nothing at all about a 0.4% one.

Creative culling could not begin either. After a full day on feed, impression counts per creative ran from 26 to 637. Only four creatives had cleared 300 impressions. The apparent leader on CTR — 6.8% — had 59 impressions and was pure noise; the real leader had 5.0% on 637.

One creative went from $0.94 per click to $0.25 per click overnight, unchanged. Anyone who had killed it on day one for poor performance would have killed a winner.

---

## The remaining hypothesis

Zero conversions across 625 visits, with the pixel confirmed working and the offer proven convertible on organic traffic, points at a message match problem.

All 11 creatives hook on tool names. Someone curious about an AI tool clicks, and lands on a page selling a $39/month community. The hook works — CTR proves that. The hook and the offer are simply not the same proposition.

Which leads to the sequencing decision. Cutting to the best three creatives might improve cost per visit by 15–20%. Twenty percent better traffic into a funnel converting at zero is still zero. **Fix the page first**, keep all creatives running while it is rewritten — the creative data accumulates for free in the meantime.

---

## Six transferable lessons

1. **Run the placement breakdown first.** One query explained four days of failure.
2. **Cheap CPM is a warning, not a win.** Inventory stays cheap because it does not convert for the people measuring.
3. **Zero conversions never proves broken tracking.** Get evidence from outside the campaign report.
4. **Set configuration at creation, not by editing.** Edits reset learning and can break the bid model.
5. **When an ad set stalls after an edit and does not recover in ~6 hours, rebuild.** New ad sets have no learning to lose.
6. **Read every threshold's derivation before trusting its colour.** Green from a borrowed conversion rate is the most expensive number on a dashboard.
