# CLAUDE.md — maintenance guide for the Shomen Sports site

Static site, **one file**: `index.html` at the repo root contains all markup, CSS, JS, the fonts (base64) and the grain texture (base64). Only the photos are external (`assets/img/`). Served by GitHub Pages from the `main` branch root. Portuguese (pt-PT) only.

## Phases and the archive rule

- **Phase 1** (content + basic dark layout) → `archive/phase-1/`
- **Phase 2** (HUD brand system, multi-page) → `archive/phase-2/`
- **Phase 3** (single self-contained `index.html`, red + blue only, products as modals) → `archive/phase-3/`
- **Phase 4** (branch `phase-4-onepager`, merged) → `archive/phase-4/`: truly one page, more compact, more motion. Products open **inline** in an expanding sheet under the tiles, Compromisso folds behind "Ler mais", the two bands became one statement strip, athletes are a roster with the **full palmarés as a grid of readouts** (Pedro's review: no "+ n"), the hero ends in a stats bar (CTAs + three settling numbers), contact lives in the footer band. Ambient HUD shapes drift behind the content and glitch (slice offsets); photos without faces get the same slice glitch. Layout is **Variant A "Directo"** of `docs/explorations/phase-4/` (products before Compromisso, full-bleed hero, accordion sheet, roster, top bar): chosen because it is the shortest path from hero to contact with nothing hidden behind a horizontal gesture. See the README there for the other two variants and the verdicts.
- **Phase 5** (this, branch `phase-5`): content and polish on top of Phase 4. Santiago Gonçalves is the fourth roster row (blue), André opens with his `#6` WKF Junior +76kg ranking, every single result is `1x` (the `—` fallback for an empty `.val` is gone), event names follow one convention (see below), and the label styles were unified (`--track-label`, 13 px micro everywhere, no 11/12 px text, no `--dim` text). WCAG 2.1 AA checked: white 18.3:1, grey 7.2:1, red 5.4:1, blue 10.4:1 on `--bg`; `--bg` on the key colour (primary button) 5.4:1 / 10.4:1.
- **Before starting any new phase**, copy everything in the repo (except `.git` and the contents of `archive/`) into a new versioned folder `archive/phase-N/` and commit that snapshot first. Pedro's rule, no exceptions.

## Compactness targets (Phase 4)

| | Phase 3 | Phase 4 | target |
|---|---|---|---|
| 390 px (844 px viewport) | 10 802 px · 12.8 vh | 5 060 px · 6.0 vh | ≤ 5.5 vh |
| 1280 px (800 px viewport) | 7 813 px · 9.8 vh | 4 346 px · 5.4 vh | ≤ 5 vh |

Phase 5 (one more athlete, 13 px palmarés labels): **5 779 px · 6.8 vh** at 390, **4 730 px · 5.9 vh** at 1280. The growth is all roster; nothing above the products moved.

Measured with `document.body.scrollHeight`, sheet closed, `prefers-reduced-motion: reduce`. The first cut (4 412 / 3 985 px) met the targets; Pedro's review asked for the full palmarés always visible and a stronger hero bar, which is the ~650 / ~360 px above target. Hero ≤ 92 vh; the first product tile is on screen on scroll one at both widths. Keep it that way: anything added to the top of the page pushes the products down.

## Shipping a new version

Edit `index.html` and swap it at the repo root; nothing else has to change unless new photos are added. Helper scripts:

```bash
python tools/optimise-images.py      # new photos in assets/img/originals/ → 1600w/800w WebP
python tools/inline-assets.py        # re-embed fonts/grain if you edited index.html with url("assets/...") references
```

`inline-assets.py` is idempotent: it only touches `url("assets/fonts/…")` / `url("assets/img/grain.png")` references, so you can author with file paths and inline before committing. The committed `index.html` must have zero `url("assets/` references (check with a grep).

`docs/explorations/phase-4/_build.py` assembled the three exploration variants and the **first cut** of the Phase 4 `index.html` (`--index`). `index.html` is the source of truth now: edit it directly and do not re-run `--index`, it would overwrite later hand edits.

## File map

```
index.html                 The site. Sections in order: nav, hero, ticker, Produtos (tiles → inline .sheet with the four .product panels), Compromisso (panel, "Ler mais"), statement strip, Atletas (roster), footer band with Contacto, then the gallery <dialog>, then the <script>.
assets/fonts/              Tomorrow-Light/Regular/Black.woff2, GeistMono-Regular/Bold.woff2 (+ OFL licences). Source for inline-assets.py.
assets/img/grain.png       200×200 greyscale noise. Source for inline-assets.py.
assets/img/originals/      Full-resolution photos and logo PNGs (never edit, never mirror)
assets/img/*-1600.webp, *-800.webp   Generated renditions
assets/img/SOURCES.md      Where every original came from
docs/explorations/phase-4/ The three skeleton variants (_build.py + _base.css/_base.js → variant-a/b/c.html) and README with verdicts
docs/screenshots/phase-4/  Phase 4 review screenshots (390 + 1280, closed and with the sheet / reveals open) + explorations/
docs/screenshots/phase-5/  Phase 5 screenshots (390 + 1280)
docs/scrape/*.json         Raw JSON of the old Squarespace site
docs/PR-phase-4.md         PR description (variants, heights, motion inventory, veto list, tone-down candidates)
tools/inline-assets.py     Embeds fonts + grain into index.html
tools/optimise-images.py   WebP renditions
tools/screenshots.py       Full-page screenshots + overflow/console check (Playwright)
tools/motion-test.py       Headless behaviour test: reveals, parallax, keyboard open/close, scroll-spy, menu, reduced motion
archive/                   Frozen phases
CNAME, .nojekyll, robots.txt, sitemap.xml, favicon.ico, apple-touch-icon.png
```

## Design tokens (`:root` inside index.html)

```css
--bg:#090A0E; --panel:rgba(14,16,22,.85); --panel-solid:#0E1016;
--white:#F5F6F8; --grey:#969CA8; --dim:#464C5A;
--red:#FF2A50; --blue:#54C8FF;
--line:rgba(245,246,248,.12); --tick:rgba(245,246,248,.4);
--key: var(--red); --alt: var(--blue);   /* [data-key="blue"] swaps them */
--fs-hero: clamp(48px, 9vw, 140px)  /* line-height 1.05 */
--fs-h2: clamp(40px, 7vw, 88px)     /* line-height 1.04, section titles */
--fs-h2-band: clamp(26px, 3.6vw, 44px)   /* Compromisso heading; the strip uses clamp(20px, 2.4vw, 30px) */
--fs-display: clamp(96px, 16vw, 220px)   /* the one display moment: "03" in Compromisso (capped at 160px there) */
--fs-body: 17px; --fs-micro: 13px   /* the only small size: micro-labels, palmarés/readout labels, tile refs, nav */
--track-micro: .14em; --track-label: .06em   /* palmarés + readout labels */
--space: clamp(48px, 6vw, 80px); --space-sm: clamp(24px, 4vw, 48px); --gap: 16px; --nav-h: 60px
```

**Highlights are red and blue only.** No green, no yellow, no other accent. Type: Tomorrow 300 Light + 900 Black (400 Regular only over photos), Geist Mono for numbers and codes, uppercase labels/headings. Headings with a hyphen (`Equipa-te`, `CONTACTa-NOS`) are wrapped in `.nobr` so they never break at the hyphen. One display moment per viewport: hero `h1`, the `04` (athletes count in Compromisso), the athletes title, `CONTACTa-NOS`; everything else stays small.

| Where | `data-key` |
|---|---|
| `<body>`, hero, Compromisso, strip, footer band | red |
| `#produtos` section (tiles, sheet) and the gallery `<dialog>` | blue |
| Roster rows | Leonor red, André blue, Martim red, Santiago blue (alternate; Guilherme would be red) |

`--dim` fails contrast on `--bg` (2.3:1): graphics only, never text. Key colour covers ≤ 4 % of any viewport (measured); keep it under 10 %.

## Motion inventory (Phase 4)

Everything lives in the "motion" CSS block and the `<script>`. `html.js` gates the hidden-before-reveal states, `html.sda` is added when `CSS.supports("animation-timeline: scroll()")` and motion is not reduced. **`prefers-reduced-motion: reduce` turns all of it off**: everything visible, no transforms, no ambient loops, transitions off; the sheet, "Ler mais", "+ n", menu and gallery still work, instantly. Nothing bounces, nothing loops faster than 4 s, no counters count up, no cursor followers.

| Motion | Trigger | Duration / easing | Reduced |
|---|---|---|---|
| Hero words rise (`.hero__title .w`) | load (+40 ms) | .7 s ease-out, 60 ms stagger | static |
| Nav bar, hero micro-labels, buttons, readouts stagger in | load, `--i` | .6 s ease-out, `--i` × 80 ms | static |
| Micro-labels **type on** (`[data-type]`, mono `_` cursor, no blink) | reveal | ≤ 600 ms (22 ms/char), label keeps its final width | off |
| Readout digits **settle** (`[data-settle]`) | reveal / sheet open | 700 ms random digits → value | off |
| `[data-reveal]` fade + rise 14 px; section heads slide 28 px from their side (`data-reveal="left"`) | IntersectionObserver, once, threshold .12 | .6 s ease-out | static |
| `.rule--key` grows | reveal | .7 s ease-out, .25 s delay | static |
| `.readouts li` / `.palmares li` cascade | reveal | .45 s, 50–60 ms stagger | static |
| Hero stats bar (three `[data-settle]` numbers, key rule) | load, `--i` | reveal .6 s + settle 700 ms | static |
| **HUD shapes** (`.fx`, fixed layer behind the content: frame, reticle, bar, bracket, square, cross) drift | ambient | 22–38 s ease-in-out alternate, 90 × 140 px travel | off |
| HUD shapes **slice glitch** (translateX ±8 px + `clip-path` insets, 3 frames, ~5 % of the cycle) | ambient | 8–14 s cycles, staggered delays | off |
| HUD shapes **burst** | while scrolling (`.fx.is-scrolling`, 600 ms after the last scroll event) | .5 s, 4 frames | off |
| **Image slice glitch** (`.photo[data-glitch]`: two clipped clones offset ±12 px, no colour fringes) on the hero photo, kit + belts tiles, sleeve photo. Never on faces, text or the logo | ambient | 8–10 s cycles, 3 frames each | off (clones not created) |
| Panel **tick flash** (`.is-flash`) | reveal, sheet open | 150 ms, 60 ms stagger | off |
| Hero photo **parallax + slow zoom** | `animation-timeline: scroll(root)`, 0–100 vh: translateY 0→28 vh, scale 1.14→1.24 | linear with scroll | `scale(1.02)` static |
| Hero mouse tilt (`--mx/--my`) | pointer devices | direct | off |
| Statement + roster thumbnails drift | `animation-timeline: view()`, entry→exit, translateY 6 %→−6 % | linear with scroll | static |
| JS parallax fallback (`--py`, `data-parallax`) | scroll, only when `html.sda` is absent | rAF | off |
| Progress line | scroll | direct | kept (state, not motion) |
| Nav key dot **slides** between items (`.nav__dot`) | scroll-spy (IO, −40 %/−55 % margins) | .45 s ease-out | jumps |
| Ticker strip | ambient | 48 s linear loop, pauses on hover | off |
| Vertical `SHOMEN` drift | ambient | 9 s ease-in-out | off |
| Hero ruler | ambient | 4 s linear | off |
| Reticle arms | ambient | 24 s linear | off |
| Hero key-colour **glow** (`.hero__glow`, radial) | ambient | 8 s ease-in-out, opacity .12→.22 | static .12 |
| Tile hover: photo zoom 1.05, ticks + name key colour, `ABRIR →` slides in | hover / focus | .8 s / .25–.4 s / .3 s | off |
| Active tile grows (`.tile.is-active`) | sheet open | scale 1.02, .5 s ease-out | off |
| Sheet open/close (`.sheet` grid rows 0fr↔1fr) | tile click, Enter/Space, Fechar, Esc | .55 s ease-out | instant |
| "Ler mais" / "+ n" (`.more`) | click | .5 s grid rows + .4 s opacity, `+` rotates 45° | instant |
| Thumbnail crossfade | click | 200 ms out, swap, .3 s in | instant |
| Buttons sweep, chips, thumbs lift, links | hover | .4 s / .25 s | off |
| Menu overlay + items rise | toggle (< 720 px) | .3 s / .5 s, 70 ms stagger | off |
| Gallery dialog + backdrop | "Ver galeria completa" | .45 s / .3 s | off |

Glitch is allowed since Pedro's Phase 4 review, **only** as horizontal slice offsets (`clip-path` + translate, a few frames, no colour fringes) on the HUD shapes and on photos without a face (`data-glitch`). Still banned: VHS, scanlines, chromatic aberration, matrix rain, anything that distorts text, the logo or a face, duotones, mirrored photos, `border-radius`. Photos: brightness/saturation filter on the hero for legibility is allowed.

## How to add or edit a product

1. Photos into `assets/img/originals/`, run `python tools/optimise-images.py`.
2. Copy a `<li class="panel panel--flush panel--hover tile">` in `#produtos`. Inside it a `<button class="tile__btn" data-product="<id>" aria-expanded="false" aria-controls="prod-<id>">` with the photo, `REF.`, name and one-line excerpt as **spans** (a button only takes phrasing content).
3. Copy an `<article class="panel product" id="prod-<id>" data-id="<id>" hidden>` block inside `.sheet__inner`: header (`PRODUTO // NN`, `REF.`, `Fechar` with `data-close-product`), main photo (`data-main`, link `data-main-link` to the original) + `ul.thumbs.thumbs--short` buttons (`data-src` 1600w, `data-full` original, `data-alt`; the first six show, the rest are reached through `Ver galeria completa` with `data-gallery`, so only add that button when there are more than six), name, description (verbatim), `.spec` readouts (`MATERIAL`, `APROVAÇÃO`, `TECIDO` only when the copy has that line), `TAMANHOS` chips, mailto button with the product in the subject.
4. Update `04 // KU01 · …` in the section head. `#p-<id>` deep-links open the sheet on load. No prices, no cart, ever.

## How to add or edit an athlete

1. Photo into `assets/img/originals/`, run the optimiser.
2. Copy an `<li class="panel panel--flush row">` in `#atletas`. Set `id`, `data-key` (next in the red/blue rotation), the photo (`.row__thumb`, 4:5, `alt` pt-PT, `pos-top` if the head is near the top; never `data-glitch` on a face), `ATLETA // NN`, the name (`.name__first` Light / `.name__last` Black), `@handle` (omit rather than guess), `PALMARÉS // NN` and every result as a cell of `ul.palmares`: `<li style="--i: n"><span class="val">7x</span><span class="lab">…</span></li>` (never an empty `.val`: a single win is `1x`; weights/years wrapped in `.mono`). The grid is 2 columns on phones, 3 from 720 px.
   Naming convention (Phase 5): rankings `#N` + `WKF Ranking <escalão> <peso>`; titles `Nx` + `Campeão/Campeã Nacional FNK-P`, `Vencedor/Vencedora Taça de Portugal FNK-P`, `Vencedor Karate1 Youth League <cidade> <ano> <escalão> <peso>`; placings `Nº` + `Lugar <prova>`; opens are `Open de <localidade>`; several opens in one cell: `Nx Vencedor Open de A, B e C`.
3. Update the counters: `ATLETAS // NN` and every `ATLETAS APOIADOS` readout (hero + Compromisso). Count only live rows. Guilherme Gonçalves is still pending photo + achievements (see TODOs).

## Content rules (short version)

- Product and athlete copy from the old site is verbatim, including quirks (`CONTACTa-NOS`, `pÓDIO`, `FIca`). Flag typos with `<!-- TODO: typo? -->`, never fix silently.
- Compromisso copy (Phase 3 draft, pending Pedro's review): commitment to high-quality competition equipment and to the next generation of champions. **Do not mention prize money.**
- No prices. Purchase path is contact only: `info@shomen-sports.com`, `@shomen_sports`.
- Never mirror or flip a photo; use `object-position` instead of tighter crops. Check every crop at 390px.
- Only outbound links: Instagram and `mailto:`. No analytics, no CDN, no external fonts.
- Brand text is `SHOMEN` (no macron); the macron lives only in the logo artwork.

## Open TODOs (search `index.html` for `TODO`)

- Compromisso copy is a Phase 3 draft for Pedro's review.
- "Ultra Level" in the Corta Vento description is probably "Ultra Leve".
- Martim Sá's and Santiago Gonçalves's Instagram handles are missing; André Aguiar's handle differs between the old site (`_aguiar05._`) and the rebuild brief (`aguiar05.`); Guilherme Gonçalves's row is not in the page yet (photo + achievements pending; the Phase 3 skeleton is in `archive/phase-3/index.html`).
- Santiago's national results were supplied without a federation; `FNK-P` was added for consistency with Leonor and André and must be confirmed (`<!-- TODO -->` in the row).

## Checks before pushing

```bash
python -m http.server 8000
python tools/screenshots.py http://localhost:8000 docs/screenshots/phase-5 index   # 0 px overflow, 0 console errors
python tools/motion-test.py http://localhost:8000                                   # 0 failures, prints page heights (expects the settle values 04,04,2025,04 and 20 palmarés cells)
grep -c 'url("assets/' index.html        # must be 0
grep -n "green\|yellow\|glitch\|scanline\|border-radius" index.html   # only border-radius: 0
grep -rin "squarespace\|€\|Carrinho\|Reservar\|cart\|prémio" index.html   # must be empty
```

Nu validator: `curl -s -H "Content-Type: text/html; charset=utf-8" --data-binary @index.html "https://validator.w3.org/nu/?out=json"` → 0 errors (four `role="list"` warnings are expected, they keep list semantics in Safari). Lighthouse: run Chromium with `--remote-debugging-port=9222` and `npx lighthouse http://localhost:8000/index.html --port=9222 --only-categories=accessibility` (chrome-launcher cannot spawn here); Phase 4 scores 100.
