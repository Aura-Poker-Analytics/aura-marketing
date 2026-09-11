# Tracking verification — is the pixel lying?

The trap in this section is subtle and it catches people constantly, including experienced ones.

---

## The core problem

**A working pixel and a broken pixel produce identical campaign data when nobody converts.**

If your insights response contains no `offsite_conversion.*` actions, there are exactly two explanations:

1. Tracking is broken and conversions are invisible.
2. Tracking works fine and there were no conversions.

The campaign report cannot distinguish these. Any claim that "tracking is broken" based only on the absence of conversion events in the campaign report is unfounded. You need evidence from outside the campaign.

This matters because the two diagnoses lead to opposite actions. "Tracking is broken" sends you to debug the pixel. "Nobody converted" sends you to fix the offer. Guessing wrong wastes days.

---

## Getting evidence from outside the campaign

### 1. Events Manager — did the pixel fire at all?

Check the pixel's own event log, independent of any campaign. You want:

- **Last received timestamp.** If it is recent, the pixel is alive.
- **Event volume by type.** `PageView` should be substantial. If `PageView` is firing and purchase events are not, the base pixel works and only the conversion event is in question.
- **Event source.** Browser vs Server (CAPI). A `TestEvent` count from CAPI with zero real server events means someone set up CAPI and never finished.

If `PageView` shows hundreds of events and `Purchase` shows zero, tracking is probably fine — you have a conversion problem, not a measurement problem.

If `Purchase` shows a non-zero count while the campaign shows zero `offsite_conversion.*`, those purchases happened but were not attributed to the ads. That means they came from organic traffic — which is itself an important finding, because it proves the offer *can* convert and the paid traffic specifically does not.

### 2. Fire a test event yourself

Load the landing page and complete the action. Watch it appear in Events Manager. This takes two minutes and eliminates all ambiguity.

### 3. Check the event name matches the optimization goal

A frequent silent failure: the ad set optimizes for one event and the site fires a different one.

Platform-hosted communities and course platforms often map events in non-obvious ways. A free trial on a **paid** group can fire as `Purchase`, not `CompleteRegistration` or `StartTrial` — because from the platform's perspective a subscription was created. If your ad set optimizes for `CompleteRegistration` and the site only ever fires `Purchase`, the ad set will never receive a single optimization signal.

Verify the actual event name in Events Manager rather than assuming it from the user journey.

---

## Reading conversions in campaign insights

Conversion actions appear in the `actions` array of an insights response:

| Action type | Meaning |
|---|---|
| `link_click` | Clicked the link |
| `landing_page_view` | Page actually loaded |
| `offsite_conversion.fb_pixel_purchase` | Pixel purchase attributed to this ad |
| `offsite_conversion.fb_pixel_complete_registration` | Pixel registration attributed |
| `onsite_conversion.*` | Happened on Meta's surfaces, not your site |
| `post_engagement`, `page_engagement` | Interaction with the ad itself |

Only `offsite_conversion.*` reflects your website. `onsite_conversion.*` entries — messaging blocks, post saves, post likes — are Meta-side interactions and are not business conversions.

---

## The click-to-visit gap

Compare `link_click` against `landing_page_view` in the same response:

```
link_click:         57
landing_page_view:  45
```

That is a 21% drop-off — people clicked, then left before the page rendered and the pixel fired.

Rough interpretation:

| Drop-off | Read |
|---|---|
| 0–15% | Normal |
| 15–30% | Acceptable on mobile; check page speed |
| 30–50% | Page is slow — real revenue is being lost here |
| >50% | Something is broken: redirect chain, blocked script, or the page fails on mobile |

A high drop-off is one of the cheapest fixes available, because those people already agreed to visit.

---

## Attribution windows

Default attribution on Meta is 7-day click, 1-day view. Conversions outside that window exist in your business but never appear in the campaign report.

For a considered purchase with a trial period, this systematically undercounts. Someone who clicks on day 1, thinks about it, and subscribes on day 10 is invisible to the campaign. Check `attribution_spec` on the ad set and keep it in mind before concluding that paid traffic produced nothing.

---

## Checklist

Before concluding "tracking is broken":

- [ ] Pixel has a recent last-received timestamp
- [ ] `PageView` volume is consistent with reported `landing_page_view` count
- [ ] The conversion event you optimize for exists in Events Manager under that exact name
- [ ] A manual test event appears
- [ ] The gap between `link_click` and `landing_page_view` is within normal range
- [ ] You have checked whether conversions exist but are unattributed (organic)
- [ ] The attribution window covers your actual decision cycle

If every box is checked and there are still no conversions, tracking is fine. The problem is the offer, the traffic, or the page.
