# AURA-PAID01 · EN — English ad creatives (global market)

**Companion to the PT-BR set in the parent folder.** Same 3 angles, same real numbers, same specs —
translated art, English UI labels. For a global/EN paid test (Fase 2 of the plan foresaw evaluating EN).
**No ad was created, uploaded or activated by an agent.**

## Files

| File | Duration | Size |
|---|---|---|
| `paid01-v1-preflop-en.mp4` | 17.9s | 3.8 MB |
| `paid01-v2-field-en.mp4` | 17.9s | 3.5 MB |
| `paid01-v3-leak-en.mp4` | 17.9s | 3.9 MB |

All **1080×1920 (9:16) · 30fps · H.264 · faststart · NO AUDIO**. Each ships with a `-thumb.png`
(the first frame / hook).

## ⚠️ Filenames carry an `-en` suffix — this is intentional

The PT brief said filenames = `utm_content`, don't rename. These EN videos are **separate ads**, so a
distinct `utm_content` is correct — `paid01-v1-preflop-en` vs `paid01-v1-preflop` keeps the two
languages apart in `tbl_user` attribution. Do **not** collapse them to the same name.

## Language note

The brief made the PT-BR set deliberately Portuguese (BR under-served). This EN set is the opposite
bet: the global/EN market. Run them as a **separate campaign or ad set**, not mixed with the PT ads —
otherwise the auction blends two audiences and you can't read either.

## Same guard-rails, same descriptive MDF framing

Identical to the PT set: no profit/EV/winrate claims, "preview of every module, no card", 18+, no
nominal competitor, "500M+" never "billions". V2 scene 2 uses the descriptive framing ("the field
defends X where the math asks Y"), not "overfold = leak" — see
[pesquisa-mdf-limites.md](../../../docs/00-strategy/pesquisa-mdf-limites.md) §10. Same two brief
deviations documented in the parent [README](../README.md) apply (V1 hook, V3 "redline").

## Regenerate

```
node instagram/build-paid-en.mjs            # render 18 EN scenes + encode the 3 MP4s
node instagram/build-paid-en.mjs --guides   # render only, with safe zones drawn
```
Template: `instagram/templates/paid-scene.html` (pass `lang:"en"` in the deck entry to switch the
fixed UI labels). Scene content: `instagram/templates/deck.js` (keys `p1-s*-en`, `p2-s*-en`,
`p3-s*-en`, `p-cta-en`).
