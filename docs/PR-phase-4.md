# Phase 4: exploratory one-pager (compact, inline products, more motion)

Same content and visual system as Phase 3, rebuilt as one continuous page: products open inline, Compromisso folds behind "Ler mais", the two bands became one statement strip, athletes are a compact roster, contact sits in the footer band. Everything still lives in one self-contained `index.html`. Phase 3 is archived in `archive/phase-3/`. Not merged; DNS, Pages settings and archives untouched.

## The three variants

Skeletons in `docs/explorations/phase-4/` (`_build.py` assembles `variant-a/b/c.html` from one set of verbatim content fragments), screenshots in `docs/screenshots/phase-4/explorations/`, verdicts in `docs/explorations/phase-4/README.md`.

| Variant | Axes | 390 px | 1280 px | Verdict |
|---|---|---|---|---|
| **A "Directo"** — chosen | products before Compromisso · full-bleed hero · expanding panel (accordion) · roster · display moment = hero `h1` then `03` · top bar | 4 637 px / 5.5 vh | 4 102 px / 5.1 vh | Shortest path from hero to contact; first product on screen on scroll one; nothing behind a gesture; the sheet costs height only when asked for. Cost: athlete portraits shrink to thumbnails in the closed state. |
| B "Rail" | Compromisso first · split hero + vertical word · horizontal scroller with an active card · 3-up cards · display moment = `03` at 220 px · left rail nav | 6 700 px / 7.9 vh | 5 292 px / 6.6 vh | Strongest desktop first screens, but on a phone the rail folds back into a top bar, the split hero costs a screen, the scroller shows 1.5 of 4 products and leaks 74 px of overflow. Tallest on mobile. |
| C "Ficha" | products first · full-bleed hero · tabbed spec sheet, one product always open · name tabs + detail panel · display moment = `REF.` at 160 px · top bar | 6 596 px / 7.8 vh | 5 573 px / 7.0 vh | Zero clicks to a full product and a good `KU01` moment, but the permanent sheet pushes everything after products below four screens; name-tab athletes are compact but dry. |

Screenshots: `docs/screenshots/phase-4/explorations/variant-{a,b,c}-{390,1280}.png`. Kept from the rejected variants: the `03` display moment (B) and the sliding nav dot (B's rail dot, now horizontal); C's "always one open" survives as the `#p-kit` deep link.

## Page height, before / after

| | Phase 3 | Phase 4 | target |
|---|---|---|---|
| 390 × 844 | 10 802 px · **12.8 vh** | 4 412 px · **5.2 vh** | ≤ 5.5 vh |
| 1280 × 800 | 7 813 px · **9.8 vh** | 3 985 px · **5.0 vh** | ≤ 5 vh |

`document.body.scrollHeight`, sheet closed, reduced motion. With the kit sheet, "Ler mais" and Leonor's "+ 04" all open: 6 749 px / 5 369 px (`index-open-*.png`).

## Verification

- `tools/screenshots.py` → `index-390.png`, `index-1280.png`: 0 px overflow, 0 console errors at both widths. No overlapping lines (h2 line-height 1.04, hyphenated headings wrapped in `.nobr`), faces kept with `object-position`, key colour ≤ 3.6 % of any viewport (pixel count over every half-viewport scroll step), no Light text over an unfaded photo (hero scrim + brightness .55).
- `tools/motion-test.py` (Playwright, `reduced_motion="no-preference"`): hero words rise, 5/19 reveals fire in the first viewport and 19/19 after a scroll, hero parallax runs as a scroll-driven CSS animation (Chromium) and as the JS `--py` fallback when `CSS.supports` is stubbed out, progress bar and readout settle work, scroll-spy follows Atletas and Contacto, Enter opens the sheet and Esc closes it with focus back on the tile, Space opens the second product, Fechar closes, thumbnails swap the main photo, the gallery dialog opens with all 18 kit photos and Esc closes only the dialog, "Ler mais" and "+ n" expand, the mobile menu opens and Esc closes it, no overflow with the sheet open, no page errors. With `reduced_motion="reduce"`: all revealed, no transforms, no ambient animations, `sda` off, the sheet still opens. **0 failures.**
- Nu validator: **0 errors** (4 warnings: `role="list"` on the thumbnail lists, kept for Safari).
- Lighthouse (Chromium on `--port=9222`): accessibility **100**, best practices 100, mobile and desktop.
- Greps: `url("assets/` → 0; `green|yellow|glitch|scanline|border-radius` → only `border-radius: 0`; `squarespace|€|Carrinho|Reservar|cart|prémio` → nothing.

## Motion inventory

Vocabulary from Phase 3, taken further. `prefers-reduced-motion: reduce` turns every animation off (static page, everything visible, interactions instant). Nothing bounces, nothing loops faster than 4 s, no marquee larger than micro, no counters counting up, no cursor followers.

| Motion | Trigger | Duration / easing | Reduced |
|---|---|---|---|
| Hero words rise | load (+40 ms) | .7 s ease-out, 60 ms stagger | static |
| Nav bar, hero micro-labels, buttons, readouts stagger in | load, `--i` | .6 s ease-out, 80 ms steps | static |
| Micro-labels type on (mono `_` cursor, steady, no blink) | reveal | ≤ 600 ms, 22 ms/char, final width reserved so nothing shifts | off |
| Readout digits settle | reveal, sheet open | 700 ms random digits → value | off |
| `[data-reveal]` fade + rise 14 px; section heads slide 28 px from their aligned side | IntersectionObserver, once | .6 s ease-out | static |
| `.rule--key` grows | reveal | .7 s ease-out, .25 s delay | static |
| `.readouts li` cascade | reveal, "+ n" | .45 s, 60 ms stagger | static |
| Panel tick flash | reveal, sheet open | 150 ms, 60 ms stagger | off |
| Hero photo parallax + slow zoom | `animation-timeline: scroll(root)` over 0–100 vh (translateY → 28 vh, scale 1.14 → 1.24) | linear with scroll | static `scale(1.02)` |
| Hero mouse tilt | pointer devices | direct | off |
| Statement + roster thumbnails drift | `animation-timeline: view()` entry → exit (6 % → −6 %) | linear with scroll | static |
| JS parallax fallback | scroll, only without scroll-driven support | rAF, factor .28 / .1 | off |
| Nav key dot slides between items | scroll-spy | .45 s ease-out | jumps |
| Ticker · vertical word · ruler · reticle arms | ambient | 48 s · 9 s · 4 s · 24 s | off |
| Hero key-colour glow (radial, ≤ .22 opacity) | ambient | 8 s ease-in-out | static .12 |
| Tile hover: zoom 1.05, ticks + name to key colour, `ABRIR →` | hover / focus | .8 s / .3 s | off |
| Active tile grows | sheet open | scale 1.02, .5 s | off |
| Sheet open / close (grid rows 0fr ↔ 1fr) | click, Enter, Space, Fechar, Esc | .55 s ease-out | instant |
| "Ler mais" / "+ n" | click | .5 s rows + .4 s opacity | instant |
| Thumbnail crossfade | click | 200 ms + .3 s | instant |
| Buttons sweep, chips, thumb lift, `+` rotates | hover | .4 s / .25 s / .3 s | off |
| Menu overlay + items rise | toggle, < 720 px | .3 s / .5 s, 70 ms stagger | off |
| Gallery dialog + backdrop | "Ver galeria completa" | .45 s / .3 s | off |

The scroll-driven `animation-timeline` / `animation-range` declarations are added by the script (only when supported) so the stylesheet validates; keyframes stay in CSS.

## Invented micro-labels (veto list)

Not from the old site; any of these can be cut without touching the content rule. Carried over from Phase 2/3: `SHOMEN // KARATE // PORTUGAL`, `EST. 2025`, ticker items (`KUMITE`, `FNK-P`, `WKF`, `TEAM SHOMEN`, `AKA`, `AO`), `O NOSSO COMPROMISSO`, `SEC. 02`, `ATLETAS APOIADOS`, `Equipamento`, `04 // KU01 · BE01 · CV01 · TS02`, `PRODUTO // 01`, `REF. KU01`, `MATERIAL` / `APROVAÇÃO` / `TECIDO` / `TAMANHOS`, `Competição`, `Materiais`, `TEAM SHOMEN // ÉPOCA 2026/27`, `ATLETAS // 03`, `ATLETA // 01`, `WKF // KUMITE`, `Palmarés`, `Contacto // encomendas e parcerias`, `ABRIR →`, `Encomendar por email`. **New in Phase 4:** `FECHAR` (on the open tile and in the sheet), `Ler mais` / `Ler menos`, `+ 04` / `+ 03` / `Ver`, `Palmarés completo`, `Ver galeria completa (18)`, `Galeria completa`, the lead sentence "Abre cada produto para ver a galeria, a descrição e os tamanhos."

## Three things most likely to need toning down

1. **The type-on micro-labels.** Every section head, the hero and the strip labels type on when they enter. It is the most "HUD" gesture on the page; if it reads as gimmicky, drop `data-type` from all but the hero (one JS attribute per label, nothing else changes).
2. **The hero glow + slow zoom together.** The red radial glow (8 s pulse) under a photo that also parallaxes and zooms with scroll is the busiest screen. First candidate: remove `.hero__glow`; second: cap the zoom at 1.18 in `heroScroll`.
3. **The panel tick flash.** Every panel flashes its corner ticks red/blue for 150 ms as it enters, and again when the sheet opens. Cheap to remove (one `flash()` call in the script). Related: the athlete thumbnails at 72–96 px are small for portraits; if the roster feels too anonymous, the `.row__big` photo could show on desktop in the closed state at the cost of ~150 px per row.

## Open TODOs (unchanged)

Compromisso copy for Pedro's review; "Ultra Level" probably "Ultra Leve"; Martim's Instagram missing; André's handle differs between old site and brief; Guilherme and Santiago pending photo + achievements (Phase 3 skeletons in the archive).

🤖 Generated with [Claude Code](https://claude.com/claude-code)
