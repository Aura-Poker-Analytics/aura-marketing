# Metric traps — when a number moves but means nothing

Every metric in this list has caused a wrong decision. They are ordered by how often.

---

## 1. CTR compared across placements

**The trap:** you switch from Reels to feed, CTR goes from 1.96% to 3.53%, and you conclude the creative got better.

It did not. Feed structurally produces higher CTR than Reels, for reasons that have nothing to do with your ad:

- In feed, the ad sits still and the link is a persistent element the reader can consider.
- In Reels, the ad is full-screen video the viewer is actively swiping past, and the link competes with the swipe gesture.
- Feed viewers have already stopped scrolling to read something. Reels viewers are in motion.

The same creative will show a materially higher CTR in feed than in Reels every time.

**The rule:** CTR is only comparable within the same placement. Comparing across a placement change measures the placement, not the creative.

---

## 2. "Clicks" is not link clicks

Meta's `clicks` field counts **all** clicks: the link, the page name, the profile photo, "See more" on truncated text, reactions, and image expansion.

```
clicks:      70    →  CTR 3.53%
link_click:  57    →  CTR 2.87%
```

The benchmark numbers you will find quoted publicly are usually link CTR. Comparing your all-clicks CTR against a link-CTR benchmark inflates your performance by 20–40%.

Always name which one you are reporting. In insights, `clicks` is the top-level field; link clicks are `actions[].action_type == "link_click"`.

---

## 3. Cheap CPM read as a win

Covered in `placement-audit.md`, repeated here because it is the most costly version of this class of error.

CPM is a market price set by other advertisers who measure conversions. Persistently cheap inventory is cheap because it does not convert for the people bidding on it. A CPM far below your vertical's norm is a diagnostic finding, not an achievement.

---

## 4. Cost per click read as cost per visit

`link_click` and `landing_page_view` are different events with different costs. The gap is people who clicked and left before the page loaded.

```
cost per link click:          $0.36
cost per landing page view:   $0.46
```

A 28% difference in this example. Optimize on the one that reflects an actual visitor.

---

## 5. High CTR with zero conversions read as encouraging

This is the trap that costs the most money, because it feels like progress.

High CTR with zero conversions is not a partial success. It is often a specific, diagnosable failure: **the hook promises something the destination does not sell.**

The mechanism is an awareness-level mismatch. Cold traffic sees a hook built around a recognizable, curiosity-triggering subject — a tool name, a number, a bold claim. They click because the hook worked. They land on a page selling a considered purchase that has nothing to do with the specific thing that got them to click. They leave.

You have optimized for attracting the wrong person efficiently.

**Diagnostic:** write down what the ad implicitly promises, then what the landing page actually sells, in one sentence each. If a stranger would not recognize them as the same offer, that is the problem — and no amount of creative testing fixes it, because every creative in the set makes the same promise.

---

## 6. Ranking creatives by the wrong metric

CTR ranking and cost-per-visit ranking produce different winners, because clicks do not survive the page load at the same rate across creatives.

| Creative | CTR | Cost/visit |
|---|---|---|
| A | 5.2% | $1.13 |
| B | 5.0% | $0.32 |

Rank by CTR and you pick A. Rank by cost per visit and you pick B, correctly.

Rank by whatever is closest to money. Cost per customer beats cost per trial beats cost per visit beats cost per click beats CTR.

---

## 7. Today's number treated as a trend

Daily numbers swing hard at low budgets. A creative that looks dead today frequently recovers tomorrow — one observed case moved from $0.94 to $0.25 per click overnight on an unchanged creative, purely because the first day's sample was 200 impressions.

Always show the period total next to today's number so the reader can see which one carries weight.

---

## 8. Frequency ignored

`frequency` above roughly 1.5 on cold traffic means you are re-serving the same people rather than reaching new ones. Combined with declining CTR over time, that is creative fatigue or an audience too small for the budget.

Early in a campaign, frequency near 1.0 is expected and healthy.

---

## 9. Comparing periods with different configurations

Once you change placements, targeting, or the optimization goal, the numbers before and after are from different experiments. Aggregating them produces a blended average that describes nothing that ever happened.

Split reporting at every significant configuration change. Freeze the previous period's totals and label them. A dashboard that silently averages a Reels period with a feed period will show a cost per visit that misrepresents both.

---

## 10. Attribution gaps read as zero performance

Default 7-day-click attribution misses anyone with a longer decision cycle. For subscriptions with a trial, the paid campaign is systematically undercredited.

Before concluding paid traffic produced nothing, check whether conversions exist in the pixel but are unattributed. Conversions with no `offsite_conversion.*` entry in campaign insights came from somewhere — often organic, sometimes ad-influenced but outside the window.

---

## Quick reference

| Metric | Safe to compare across | Never compare across |
|---|---|---|
| CTR | Creatives in the same ad set | Placements, formats |
| CPM | Same placement, same period | Placements, seasons |
| Cost per visit | Creatives, placements | — |
| Conversion rate | Traffic sources measured separately | Organic vs paid |
| Frequency | Same audience over time | Different audience sizes |
