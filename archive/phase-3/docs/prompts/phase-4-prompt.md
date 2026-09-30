Prompt — Shōmen website Phase 4: exploratory one-pager (paste into Claude Code, inside the `shomen-sports` repo)

Phase 3 is live at https://shomen-sports.com (branch `main`, single self-contained `index.html`). Phase 4 is **exploratory**: same content, same visual system, but we push layout, rhythm, type sizes and motion to make the page feel like one continuous, dynamic piece, and we make it more compact so fewer people drop before the products and the contact. Work on a branch `phase-4-onepager`, commit per step, push, open a PR against `main`.

**Rule 0 — archive first.** Before touching anything, copy everything in the repo (except `.git` and the contents of `archive/`) into `archive/phase-3/` and commit that snapshot on `main`. Then branch.

## What does not change

- Content: every product, athlete, achievement, contact detail and heading is reproduced verbatim from Phase 3 (including quirks like `CONTACTa-NOS`, `pÓDIO`, `FIca`). The Compromisso copy stays as in Phase 3 (no prize-money mention). Flag typos with `<!-- TODO -->`, never fix silently.
- Visual system: tokens, Tomorrow 300/900 (+400 over photos), Geist Mono for numbers/codes, uppercase labels and headings, panels with corner ticks, micro-labels, readouts, chips, reticle, grain. **Red and blue only** as highlights; key colour per section as in Phase 3 (red pages/sections, blue for products).
- Single file: everything (CSS, JS, fonts, grain) stays inline in `index.html`; only photos in `assets/img/`. `python tools/inline-assets.py` before every commit; `grep -c 'url("assets/' index.html` must be 0.
- Still banned: glitch, VHS, scanlines, chromatic aberration, matrix rain, anything that distorts text/logo/faces, duotones, mirrored photos, prices, cart, external requests, `border-radius`.
- `prefers-reduced-motion` turns every animation off; the page must read perfectly static.

## Goals, in priority order

1. **Truly one page.** No pop-ups as the primary path. Products open **inline** (expanding panel, horizontal scroller with an active card, or a tabbed spec sheet under the tiles: prototype at least two of these and pick one). The `<dialog>` from Phase 3 may survive only as a "ver galeria completa" fallback for the full thumbnail set. Nav is anchors + scroll-spy only.
2. **Compact.** Target page length ≤ 5.5 viewport heights at 390 px (Phase 3 is ~13) and ≤ 5 at 1280 px. Every section must justify its height: hero ≤ 100vh with the first product visible on scroll one; Compromisso to one panel with the fact heading and one paragraph visible, the rest behind a "ler mais" reveal; product tiles denser (4-up at ≥ 720 px, 2-up at 390 px, photo aspect 4/5 → 1/1 if it saves height); bands merged into one horizontal statement strip; athletes as a compact roster (name + surname + top 2 readouts, "+ n" reveals the rest); contact folded into the footer band.
3. **Dynamic.** More things move, but only in the Phase 3 vocabulary, taken further:
   - Scroll-driven: hero photo parallax + slow zoom, section headings that slide in from the side they are aligned to, micro-label rows that "type on" (letters appear with a mono cursor, ≤ 600 ms, text never distorted), readouts that settle, `rule--key` growing, panels that enter with a 1-frame tick flash. Use `animation-timeline: scroll()` / `view()` where supported with the IntersectionObserver fallback.
   - Ambient: ticker strip, drifting vertical word, rotating reticle arms, scrolling ruler, a slow key-colour glow behind the hero (radial, ≤ 25 % opacity, per the post engine).
   - Interactive: tile hover zoom + tick highlight, active product card grows, thumbnails crossfade, buttons sweep, nav dot slides between items instead of appearing.
   - Nothing bounces, nothing loops faster than 4 s, no marquee text larger than the micro size, no counters counting up, no cursor followers.
4. **Type and rhythm.** Explore bigger jumps: hero `clamp(48px, 9vw, 140px)` with line-height 1.05, section titles that can go to the 88 px scale even for two-line headings, body 17–18 px, micro 13 px. Explore one **display moment** per viewport (one huge word or number) and keep everything else small. Check no line ever overlaps another and every heading fits its container at 390 px and 1280 px.

## Exploration method

- Build **three layout variants** of the page skeleton first, as `docs/explorations/phase-4/variant-{a,b,c}.html` (same content, different section order/rhythm/density), screenshot each at 390 and 1280 into `docs/screenshots/phase-4/explorations/`, and write a one-paragraph verdict per variant in `docs/explorations/phase-4/README.md` (what it does to drop-off risk, what it costs). Pick one, say why, then build it into `index.html`.
- Variant axes to vary (pick ≥ 3 per variant): section order (products before Compromisso vs after), hero type (photo full-bleed vs split with the vertical word), products (expanding panel vs horizontal scroller vs tabbed sheet), athletes (roster list vs stacked cards vs marquee of names with a detail panel), where the display moment sits, nav (top bar vs left rail on desktop).
- Keep a **motion inventory** in the PR: every animation, its trigger, duration, easing, and the reduced-motion behaviour.

## Verification before you say done

1. `python tools/screenshots.py http://localhost:8000 docs/screenshots/phase-4 index` → 0 px overflow, 0 console errors at 390 and 1280. Look at them: no overlapping lines, no cropped faces (`object-position`), key colour ≤ 10 % of any viewport, no Light-weight text sitting on an unfaded photo.
2. Page height printed in the PR for 390 and 1280 (Playwright `document.body.scrollHeight`) with the Phase 3 numbers next to them.
3. Headless motion test (Playwright, `reduced_motion="no-preference"`): reveals fire, parallax vars update, product open/close works with keyboard (Enter/Space/Esc), scroll-spy follows sections, mobile menu opens/closes. Then the same page with `reduced_motion="reduce"`: no transforms, everything visible.
4. Nu validator 0 errors; Lighthouse accessibility ≥ 95 (run with `--port=9222` against a running Chromium, chrome-launcher can't spawn here).
5. Greps: `grep -n "green\|yellow\|glitch\|scanline\|border-radius" index.html` → only `border-radius: 0`; `grep -rn "squarespace\|€\|Carrinho\|Reservar\|cart\|prémio" index.html` → nothing; `grep -c 'url("assets/' index.html` → 0.

## Handoff

- Update `CLAUDE.md`: Phase 4 note, the chosen variant and why, the compactness targets, the motion inventory, how to add a product/athlete in the new structure.
- PR description: the three variants with screenshots and verdicts, page-height before/after, the motion inventory, invented micro-labels (veto list), and the three things most likely to need toning down.
- Do not touch DNS, Pages settings or the archive folders. Push the branch and open the PR; don't merge.
