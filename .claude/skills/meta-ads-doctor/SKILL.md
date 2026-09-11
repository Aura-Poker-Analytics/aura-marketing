---
name: meta-ads-doctor
description: Diagnose why a Meta (Facebook/Instagram) ad campaign is spending money without converting, and decide what to change. Reads campaign data through the Meta Marketing API, finds the actual failure point — placement mix, delivery stall, tracking, sample size, or offer mismatch — and returns a ranked diagnosis with a specific next action. Use when ads run but nothing converts, when delivery suddenly drops, when deciding whether to edit or rebuild an ad set, when picking winning creatives, or when a cheap cost-per-click is not turning into sales. Triggers on "ads not converting", "facebook ads not working", "no sales from ads", "delivery stopped", "should I kill this creative", "meta ads audit", "почему реклама не конвертит", "открутка встала", "какой креатив лучше".
---

# Meta Ads Doctor

A campaign that spends money and returns nothing is not one problem. It is five possible problems that look identical from the dashboard. This skill separates them.

The dashboard shows you cost per click. It does not show you that 90% of your budget went to an ad placement where nobody buys, that your last edit silently killed delivery, or that your sample is too small to mean anything. Those are the things that actually decide whether the campaign works.

---

## Hard rules — never skip

1. **Never change a live campaign without explicit approval.** Read data freely. Before any write — pausing, editing targeting, changing budget, creating an ad set — state exactly what will change and wait for a clear yes. Money is moving.

2. **Diagnose before prescribing.** Do not recommend "test new creatives" or "raise the budget" until you have run the placement breakdown and the tracking check. Most zero-conversion campaigns fail for a reason that no amount of new creative fixes.

3. **Never call a winner on an insufficient sample.** See `references/statistical-thresholds.md`. A creative with 6.8% CTR on 59 impressions is noise, not a winner. Saying otherwise costs the user real money.

4. **Zero conversions is not evidence of broken tracking.** A working pixel and a broken pixel produce identical data when nobody converts. Verify tracking independently before blaming it. See `references/tracking-verification.md`.

5. **Cost thresholds must come from an observed conversion rate, not an assumed one.** A "$0.35 per visit is good" target derived from a conversion rate you have never measured on this traffic is a made-up number. State where every threshold comes from.

6. **Report what the data says, including when it contradicts an earlier recommendation.** If you told the user to do something and the data now says it was wrong, say so plainly and move on.

---

## Diagnostic order

Run these in order. Each step is cheap and rules out a whole class of failure. Stop when you find the cause — do not run all five and present a list.

### 1. Is the account actually delivering?

Symptoms: spend far below budget, impressions collapsed, "no results" in Ads Manager.

Check `account_status`, `disable_reason`, `spend_cap`, and payment validity through the API — **not** through the Ads Manager UI, which throws misleading errors that have nothing to do with delivery. Then confirm campaign, ad set, and ads are all `ACTIVE` with `effective_status: ACTIVE` (not `PENDING_REVIEW`, `DISAPPROVED`, or `IN_PROCESS`).

If the account is healthy but delivery is dead → `references/delivery-diagnosis.md`

### 2. Where did the money actually go?

This is the step people skip, and it is the highest-yield check in the whole process.

Pull insights with `breakdown: platform_position` over the campaign's full run. Automatic placements routinely concentrate 80–95% of spend into the cheapest inventory available, which is almost never the inventory that converts. Cheap CPM is not a win — it is a signal about who is seeing the ad and in what mental state.

→ `references/placement-audit.md`

### 3. Is tracking actually working?

Only after the above. Distinguishing "nobody converted" from "conversions are invisible" requires evidence outside the campaign report.

→ `references/tracking-verification.md`

### 4. Is there enough data to conclude anything?

Before declaring the offer broken, the creative dead, or a winner found — check whether the sample supports the claim. Most campaign post-mortems are performed on samples too small to distinguish success from failure.

→ `references/statistical-thresholds.md`

### 5. Are the metrics saying what you think they are?

CTR that doubled after a placement change is not a creative improvement. "Clicks" in the report is not link clicks. Cost per landing page view is not cost per click.

→ `references/metric-traps.md`

---

## The core decision table

| Symptom | Most likely cause | First action |
|---|---|---|
| Spend normal, clicks cheap, zero sales | Wrong placement mix, or offer/traffic mismatch | Placement breakdown |
| Spend collapsed after an edit | Learning reset + bid model mismatch | Rebuild, do not wait |
| Clicks but no landing page views | Page load failure, or slow mobile page | Compare `link_click` vs `landing_page_view` |
| Conversions in the pixel, none in the campaign | Attribution window, or organic conversions | Check `offsite_conversion.*` in insights |
| One creative looks amazing | Probably sample size | Impression count before anything else |
| High CTR, zero conversions | Hook promises something the page does not sell | Awareness-level audit |

---

## Edit or rebuild?

The single most expensive mistake in this domain is editing a live ad set to fix it.

Significant edits — targeting, placements, optimization goal, large budget swings — reset the learning phase. Worse, the bid model was calibrated against the inventory the ad set was previously buying. Change the inventory and the bid model can fail to win auctions at all. Delivery does not degrade gracefully; it can go to near zero.

**Rule:** if an ad set has stalled after an edit and shows no recovery within roughly 6 hours, rebuild it rather than waiting or editing again. A new ad set has no learning history to lose, so the usual "every change is another reset" argument does not apply to creating one.

When rebuilding:
- Set the intended configuration **at creation**, not as an edit afterwards.
- Reuse existing creative IDs. The ads then point at the same underlying page posts, so accumulated likes, comments, and shares carry over as social proof.
- Create the ad set paused, add all ads, then activate — so it does not spend with only one ad live.
- Pause the old ad set first to avoid both spending in parallel.

Full procedure and the failure signature: `references/delivery-diagnosis.md`

---

## Culling creatives

Meta does not distribute impressions evenly, so you will never get clean data on every creative. Its allocation is itself a signal — but it is a signal about predicted cost per optimization event, not about long-term business value.

**Working rule:** cut a creative once it has **≥300 impressions** and its cost per landing page view is **more than double the leader's**. Below 300 impressions, do nothing regardless of how the numbers look.

Cull by **pausing individual ads**, not by editing the ad set. Ad-level pauses are routine and do not disturb ad set learning the way targeting edits do.

Detail and worked examples: `references/statistical-thresholds.md`

---

## Sequencing: creative or landing page first?

When conversions are zero, fix the page before optimizing creative selection.

The arithmetic is blunt. Cutting to the best three creatives might improve cost per visit by 15–20%. Twenty percent better traffic into a funnel that converts at zero is still zero. The page is the difference between nothing and something.

They are also measured at different funnel stages, so the work can run in parallel: creative selection is judged on CTR and cost per visit, the page on visit-to-signup rate. Leave the ads running while the page is rewritten — the creative data accumulates for free.

---

## Reference files

| File | Read it when |
|---|---|
| `references/delivery-diagnosis.md` | Delivery stalled, dropped, or never started |
| `references/placement-audit.md` | Traffic is cheap but does not convert |
| `references/tracking-verification.md` | You need to know if the pixel is lying |
| `references/statistical-thresholds.md` | Deciding a winner, a loser, or a verdict |
| `references/metric-traps.md` | A metric moved and you want to know if it means anything |
| `references/case-study.md` | A full worked diagnosis with real numbers |

---

## API notes

This skill assumes access to the Meta Marketing API through an MCP server or equivalent. The calls it relies on:

- `get_account_info` — `account_status`, `disable_reason`, `spend_cap`, `funding_source_details`, `timezone_name`
- `get_campaigns` / `get_adsets` / `get_ads` — status and `effective_status`
- `get_adset_details` — targeting, `bid_strategy`, `optimization_goal`, `budget_remaining`
- `get_insights` — with `level`, `time_range`, and `breakdown`

The breakdowns that matter: `platform_position` (where the money went), `hourly_stats_aggregated_by_advertiser_time_zone` (when delivery died), `publisher_platform` (Facebook vs Instagram).

Always read `timezone_name` from the account before interpreting hourly data. Hourly breakdowns are in advertiser time, not yours.
