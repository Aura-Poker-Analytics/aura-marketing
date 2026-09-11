# Delivery diagnosis — when the ads stop showing

Delivery problems look like account problems and are almost never account problems. Work the checks in this order.

---

## Step 1 — Rule out the account (2 minutes)

The Ads Manager UI produces alarming errors that have nothing to do with delivery. Errors like `Не удается создать черновик: Invalid request. (#1)`, "You will not be able to edit any ads in this account", empty campaign tables, and "some data failed to load" are usually a stale browser session or a date filter that excludes the campaign's run — not a restriction.

Check the account through the API instead:

| Field | Healthy value | What it means if not |
|---|---|---|
| `account_status` | `1` | 2 = disabled, 3 = unsettled, 7 = pending review, 9 = grace period |
| `disable_reason` | `0` | Non-zero explains the disable |
| `spend_cap` | `0` or above spend | A hit spend cap stops delivery silently |
| `funding_source_details` | present, valid | No payment method = no delivery |
| capabilities | includes `HAS_VALID_PAYMENT_METHODS` | |

Then confirm the whole chain is live: campaign `ACTIVE` → ad set `ACTIVE` → ads `ACTIVE` **and** `effective_status: ACTIVE`.

`effective_status` is the one that matters. An ad can be `status: ACTIVE` while `effective_status` is `PENDING_REVIEW`, `IN_PROCESS`, `DISAPPROVED`, or `ADSET_PAUSED` — and it will not deliver.

If everything above is healthy, the account is not the problem. Move on.

---

## Step 2 — Find the moment it died

Pull hourly data in advertiser time zone:

```
get_insights(
  object_id: <adset_id>,
  level: "adset",
  time_range: "today",
  breakdown: "hourly_stats_aggregated_by_advertiser_time_zone"
)
```

Read `timezone_name` from the account first. The hours are in advertiser time, not yours.

You are looking for a cliff, not a slope. A healthy ad set with a fresh budget delivers a few hundred impressions an hour. A stall looks like this:

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

Then line the cliff up against `updated_time` on the ad set. If they match within an hour, your edit caused it.

---

## Step 3 — Read the CPM, not just the volume

This is the diagnostic that tells you *why* the edit killed delivery, and it is the one people miss.

Compare CPM before and after the cliff. In the example above:

- Before: CPM $2.40–$3.10
- After: CPM $10–$20

That jump is the whole story. The ad set had been buying cheap inventory. Its bid model was calibrated against that price level. When the targeting changed, the eligible inventory became 4–7× more expensive, and the model could no longer win auctions. Volume collapsed not because Meta throttled the ad set, but because it stopped being competitive.

Two things happen together after a significant edit:

1. **Learning phase reset.** Meta re-enters the exploration period and delivers conservatively.
2. **Bid model mismatch.** The learned bid is wrong for the new inventory.

The first recovers on its own. The second may not.

---

## Step 4 — Wait or rebuild?

**Wait** if: delivery is reduced but continuing, CPM is in the expected range for the new inventory, and less than a few hours have passed.

**Rebuild** if: delivery is near zero, six or more hours have passed with no recovery trend, or the CPM gap between old and new inventory is more than about 3×.

The argument for waiting is usually "any further change is another learning reset." That argument does not apply to **creating a new ad set**, because a new ad set has no learning history to reset. The stalled ad set has nothing left to salvage — its accumulated learning is calibrated to inventory you are no longer buying.

---

## Step 5 — Rebuild procedure

Order matters. Do each step and verify before the next.

1. **Create the new ad set `PAUSED`**, with the intended configuration set at creation — placements, optimization goal, bid strategy, budget, targeting. Never create it "close enough" and then edit.

2. **Create every ad, reusing existing creative IDs.** Pull `creative.id` from the old ads and pass it to `create_ad`. The new ads then reference the same underlying page posts, so likes, comments, shares, and saves carry over. Rebuilding with fresh creatives throws that social proof away.

3. **Carry the pixel tracking spec** onto each ad:
   ```json
   [{"action.type": ["offsite_conversion"], "fb_pixel": ["<pixel_id>"]}]
   ```

4. **Pause the old ad set first.** If the campaign uses ad-set-level budgets, leaving both active means both spend.

5. **Activate the new ad set.**

6. **Verify** — new ad set `ACTIVE`, all ads present, `effective_status` progressing through `IN_PROCESS` / `PENDING_REVIEW` toward `ACTIVE`.

Expect new ads to sit in review briefly even when the creatives were previously approved. Minutes to a couple of hours is normal.

---

## What resets learning and what does not

| Change | Resets learning |
|---|---|
| Targeting (geo, age, interests, placements) | Yes |
| Optimization goal or conversion event | Yes |
| Bid strategy | Yes |
| Budget change over ~20% | Yes |
| Adding a new ad to the ad set | Partial |
| **Pausing an individual ad** | **No** |
| Renaming anything | No |

This is why creative culling is done by pausing ads, not by editing the ad set.

---

## Budget proration

A newly activated ad set does not get its full daily budget on day one. `budget_remaining` is prorated against the hours left in the advertiser's day. An ad set created at 16:14 on a $31/day budget will show roughly $10 remaining, not $31. This is expected and not a sign of a spend cap.
