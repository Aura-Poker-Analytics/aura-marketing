# Placement audit — where the money actually went

This is the highest-yield check in the whole diagnostic, and the one most people never run. If a campaign produces cheap clicks and zero sales, run this before anything else.

---

## The query

```
get_insights(
  object_id: <campaign_id or adset_id>,
  level: "adset",
  time_range: "maximum",
  breakdown: "platform_position"
)
```

Related breakdowns:
- `publisher_platform` — Facebook vs Instagram vs Audience Network vs Messenger
- `platform_position` — the specific surface (feed, reels, stories, explore, marketplace, in-stream)
- `device_platform` — mobile vs desktop

`platform_position` is the one that matters. Aggregate it into a table:

| Placement | Impressions | Spend | Visits | CPM | Cost/visit |
|---|---|---|---|---|---|
| Instagram Reels | 33,619 | $108.62 | 510 | $3.23 | $0.21 |
| Instagram Feed | 598 | $7.81 | 16 | $13.06 | $0.49 |
| Facebook Reels | 896 | $6.30 | 25 | $7.03 | $0.25 |
| Instagram Stories | 826 | $3.18 | 10 | $3.86 | $0.32 |
| Facebook Feed | 312 | $1.79 | 4 | $5.75 | $0.45 |

Read the spend column first, not the cost column.

---

## What automatic placements actually do

Advantage+ placements (formerly "automatic placements") optimize for the **cheapest** path to your optimization event. If you optimize for landing page views, it buys the cheapest landing page views available.

The cheapest inventory on Meta is short-form video feeds — Reels. So that is where the budget goes. In the table above, 90% of spend went to Reels — 85% to Instagram Reels alone.

This is not a bug. Meta did exactly what it was told. The problem is that "cheapest landing page view" and "most likely buyer" are different people.

**Reels traffic behaves differently from feed traffic.** Someone swiping through Reels is in a passive, high-velocity browsing state. A tap on a link is often incidental — they were moving fast and the link was in the way. Feed traffic is slower and more deliberate: the person stopped on a post and read it.

Both produce a `landing_page_view`. Only one of them arrived intending to evaluate an offer.

---

## The cheap-CPM trap

A $3 CPM feels like a win. It is usually a warning.

CPM is a market price. Advertisers bid inventory up to what it is worth to them. Inventory that stays cheap is cheap because the people who measure conversions found it did not convert. When your CPM is dramatically below the norm for your vertical, the first question is not "how did I get such a good deal" — it is "what does everyone else know about this inventory."

Rough current ranges for cold English-language traffic in developed markets:

| Placement | Typical CPM |
|---|---|
| Reels (IG/FB) | $3–8 |
| Stories | $4–9 |
| Facebook Feed | $8–20 |
| Instagram Feed | $10–25 |

If your blended CPM is at the bottom of that spread, pull the placement breakdown. You are probably buying almost entirely Reels.

---

## When to force placements manually

Force manual placements when:

- Spend is concentrated (>70%) in one placement, and that placement has no conversions.
- The offer requires reading — a considered purchase, a subscription, anything with a price to evaluate.
- Your creative is a static image. Static images are native to feed and alien to Reels, where everything else in the stream is full-screen video.

Do **not** force placements when:

- You have conversions coming in and are just trying to make CPM look better.
- You have fewer than a few hundred conversion events total. You do not yet know which placement works, and you will be guessing.

---

## How to set feed-only targeting

```json
{
  "publisher_platforms": ["facebook", "instagram"],
  "facebook_positions": ["feed"],
  "instagram_positions": ["stream"]
}
```

`stream` is Instagram's identifier for the main feed. This trips people up — it is not `feed`.

**Keep Advantage+ audience separate.** `targeting_automation.advantage_audience` is an audience feature, not a placement feature. Turning off automatic placements does not require turning off audience expansion, and usually you want to keep it.

---

## Expect the economics to change

Switching from Reels to feed makes every per-unit cost worse. That is the trade, and it should be stated up front so nobody panics at the dashboard:

| Metric | Reels | Feed | Change |
|---|---|---|---|
| CPM | $3.53 | $10.19 | ~3× worse |
| Cost per visit | $0.23 | $0.48 | ~2× worse |
| CTR | 1.96% | 3.53% | ~1.8× better |
| Visits per day at $31 | ~135 | ~65 | half |

You are buying fewer, more expensive, more attentive visitors. The bet is that the conversion rate difference more than covers a 2× cost increase. That bet is testable — but only after enough visits accumulate to measure a conversion rate at all.

**Critically: do not compare CTR across this switch and call it an improvement.** Feed structurally outperforms Reels on CTR because the ad occupies a different position in a different browsing mode. The creative did not get better. See `metric-traps.md`.

---

## Reading the breakdown when spend is lopsided

If one placement has 90% of spend, the other placements have not been tested — they have been sampled. Twenty visits from Instagram Feed tells you nothing about whether Instagram Feed works. Resist the temptation to rank placements by cost per visit when the impression counts differ by two orders of magnitude.

The correct read of a lopsided breakdown is: "we tested one placement and we do not have data on the others," not "Reels performed best."
