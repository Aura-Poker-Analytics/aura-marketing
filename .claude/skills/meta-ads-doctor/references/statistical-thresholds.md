# Statistical thresholds — when you are allowed to conclude something

Most bad ad decisions are not analysis errors. They are decisions made on samples too small to support any conclusion, dressed up in confident language.

---

## The rule of three

You spent money, got N visits, and zero conversions. What does that prove?

For a zero-event outcome, the 95% confidence upper bound on the true rate is approximately **3/N**.

| Visits | 0 conversions means the true rate could still be as high as |
|---|---|
| 100 | 3.0% |
| 200 | 1.5% |
| 300 | 1.0% |
| 575 | 0.52% |
| 1,000 | 0.30% |

Read the 575 row carefully. After 575 visits with zero conversions, you have **not** proven the conversion rate is zero. You have proven it is probably below 0.52%. If your business model needs 2%, that is a decisive result. If it needs 0.4%, you have learned nothing yet.

**Always state the threshold you need before you look at the result.** Otherwise you will rationalize whatever number appears.

---

## How many visits before judging an offer

Work backwards from the conversion rate you need.

To detect a rate of `p` with reasonable confidence, you need roughly `3/p` visits just to expect a handful of events, and considerably more to measure it precisely.

| Needed conversion rate | Minimum visits for a real verdict |
|---|---|
| 5% | ~150 |
| 2% | ~300 |
| 1% | ~600 |
| 0.5% | ~1,200 |

For a subscription product in the $30–50/month range with cold traffic, 1–2% visit-to-trial is a reasonable planning assumption. That puts the decision point around **300 visits** — which at $0.45 per visit is about $135 of spend.

Deciding at 50 visits is not "moving fast." It is flipping a coin and then explaining the result.

---

## Picking winning creatives

### The impression floor

Below **300 impressions**, a creative's CTR is noise. Full stop.

Worked example from a real ad set:

| Creative | Impressions | Clicks | CTR |
|---|---|---|---|
| Creative A | 59 | 4 | 6.8% |
| Creative B | 637 | 32 | 5.0% |

Creative A has the higher CTR. Creative A is not better. With 59 impressions, the 95% confidence interval on 6.8% spans roughly 2% to 17% — it overlaps almost every other creative in the set. One additional click would have moved it to 8.5%.

Creative B's 5.0% on 637 impressions is a real number.

### The culling rule

Cut a creative when **both** are true:

1. It has **≥300 impressions**
2. Its cost per landing page view is **more than 2× the leader's**

Below 300 impressions, do nothing no matter how bad it looks. A creative that appears terrible at 200 impressions frequently recovers — one observed case went from $0.94 per click to $0.25 per click the following day on the same creative, purely because the first sample was small.

### Cull by pausing ads

Pause the individual ads. Do not edit the ad set to remove them. Ad-level pauses do not reset ad set learning; targeting edits do.

### Meta will not give you clean data

Meta concentrates delivery on whatever it predicts will be cheapest, so weak creatives never accumulate enough impressions to prove themselves. You will not get a balanced test unless you deliberately build one (separate ad sets, one creative each, equal budgets — expensive, and only worth it for high-spend accounts).

Meta's allocation is a legitimate signal, but understand what it is a signal about: **predicted cost per optimization event**, not business value. If you optimize for landing page views, Meta finds creatives that get cheap landing page views. That is not the same as finding creatives that get customers.

---

## Comparing two numbers honestly

Before saying "X outperformed Y," check:

1. **Do both have enough volume?** If either is under 300 impressions, the answer is no.
2. **Would one extra event change the ranking?** If yes, the difference is noise.
3. **Did anything else change between them?** Placement, time of day, day of week, audience. If yes, you are not comparing creatives.
4. **Is the metric the one that matters?** CTR ranks differently from cost per visit, which ranks differently from cost per customer.

That last point bites regularly. A creative can lead on CTR and lose on cost per visit, because its clicks do not survive the page load. From a real ad set:

| Creative | CTR | Cost/visit |
|---|---|---|
| Cursor | 5.2% | $1.13 |
| Claude Cowork | 5.0% | $0.32 |

Nearly identical CTR, 3.5× different cost per visit. Ranking by CTR would have picked the wrong one.

---

## Thresholds must be derived, not assumed

A target like "$0.35 per visit is good" is meaningless unless you can state where 0.35 came from.

The honest derivation runs backwards from unit economics:

```
target cost per customer  = LTV ÷ desired LTV:CAC ratio
target cost per trial     = target cost per customer × trial-to-paid rate
target cost per visit     = target cost per trial × visit-to-trial rate
```

Every term needs to be measured on **this traffic**, not borrowed from elsewhere. A 2.5% conversion rate observed on organic visitors — people who already knew the brand — does not transfer to cold Reels traffic. Using it produces a cost-per-visit target that looks comfortably green while the campaign converts at zero.

If you have not measured the conversion rate on this traffic yet, say so, and treat the threshold as provisional. A green metric derived from an unmeasured assumption is worse than no metric, because it stops people from asking questions.

---

## Reporting language

Match the confidence of your language to the strength of the evidence.

| Sample | Say |
|---|---|
| Under threshold | "Not enough data to judge yet — need N more" |
| At threshold, clear gap | "X outperforms Y on cost per visit" |
| At threshold, small gap | "No meaningful difference between X and Y" |
| Zero events at N | "Conversion rate is below ~3/N; whether that is a failure depends on the target" |

Never present a ranked leaderboard without impression counts next to each row. The counts are what tell the reader which rows to believe.
