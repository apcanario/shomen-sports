# CLAUDE.md — maintenance guide for the Shomen Sports site

Static site, **one file**: `index.html` at the repo root contains all markup, CSS, JS, the fonts (base64) and the grain texture (base64). Only the photos are external (`assets/img/`). Served by GitHub Pages from the `main` branch root. Portuguese (pt-PT) only.

## Phases and the archive rule

- **Phase 1** (content + basic dark layout) → `archive/phase-1/`
- **Phase 2** (HUD brand system, multi-page) → `archive/phase-2/`
- **Phase 3** (this): single self-contained `index.html`, red + blue only, products as modals, more motion.
- **Before starting any new phase**, copy everything in the repo (except `.git` and the contents of `archive/`) into a new versioned folder `archive/phase-N/` and commit that snapshot first. Pedro's rule, no exceptions.

## Shipping a new version

Edit `index.html` and swap it at the repo root; nothing else has to change unless new photos are added. Two helper scripts:

```bash
python tools/optimise-images.py      # new photos in assets/img/originals/ → 1600w/800w WebP
python tools/inline-assets.py        # re-embed fonts/grain if you edited index.html with url("assets/...") references
```

`inline-assets.py` is idempotent: it only touches `url("assets/fonts/…")` / `url("assets/img/grain.png")` references, so you can author with file paths and inline before committing. The committed `index.html` must have zero `url("assets/` references (check with a grep).

## File map

```
index.html                 The site. Sections in order: nav, hero, ticker, Compromisso, Produtos (tiles → <dialog>), bands, Atletas, Contacto, footer, then the four product <dialog>s, then the <script>.
assets/fonts/              Tomorrow-Light/Regular/Black.woff2, GeistMono-Regular/Bold.woff2 (+ OFL licences). Source for inline-assets.py.
assets/img/grain.png       200×200 greyscale noise. Source for inline-assets.py.
assets/img/originals/      Full-resolution photos and logo PNGs (never edit, never mirror)
assets/img/*-1600.webp, *-800.webp   Generated renditions
assets/img/SOURCES.md      Where every original came from
docs/screenshots/phase-3/  Review screenshots (390 + 1280)
docs/scrape/*.json         Raw JSON of the old Squarespace site
tools/inline-assets.py     Embeds fonts + grain into index.html
tools/optimise-images.py   WebP renditions
tools/screenshots.py       Full-page screenshots + overflow/console check (Playwright)
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
```

**Highlights are red and blue only.** No green, no yellow, no other accent. Type: Tomorrow 300 Light + 900 Black (400 Regular only over photos), Geist Mono for numbers and codes, uppercase labels/headings. Hero `h1` is capped at `6.4vw` with `line-height 1.08` so lines never touch; `h2--band` is the 52px scale for long sentences.

| Where | `data-key` |
|---|---|
| `<body>`, hero, Compromisso, bands, Contacto | red |
| `#produtos` section and every product `<dialog>` | blue |
| Athlete panels | Leonor red, André blue, Martim red, Guilherme blue, Santiago red (alternate) |

`--dim` fails contrast on `--bg` (2.3:1): graphics only, never text.

## Motion inventory (all in the `<script>` and the "motion" CSS block)

- Load: hero words rise in sequence; nav bar, hero micro-labels, buttons and readouts stagger in (`--i`).
- Scroll: every `[data-reveal]` fades/rises once (IntersectionObserver); `.rule--key` grows; `.readouts li` cascade; readout digits "settle" from random digits (`[data-settle]`).
- Parallax: hero photo (scroll factor .28 + mouse tilt on pointer devices), band and athlete photos (`data-parallax` factor relative to viewport centre). Images are scaled 1.14 inside `overflow:hidden` wrappers so no edges show.
- Ambient: ticker strip (48s loop, pauses on hover), vertical `SHOMEN` word drifts, hero ruler scrolls, reticle arms rotate.
- Hover: buttons fill with a left-to-right white sweep; tiles zoom the photo, turn the corner ticks and title to the key colour and reveal `ABRIR →`; chips and thumbnails highlight.
- Nav: scroll progress line at the top, key dot follows the section in view (scroll spy), overlay menu items rise in.
- Modals: fade/rise in with a blurred dark backdrop; thumbnails crossfade the main image; backdrop click, `Fechar` and Esc close; `#p-kit` etc. deep-link opens the product.
- `prefers-reduced-motion` disables all of the above (modals still work, without animation).

Still banned: glitch, VHS, scanlines, chromatic aberration, matrix rain, anything that distorts text, the logo or a face. Photos: brightness/saturation filter on the hero for legibility is allowed; no duotone, no mirroring.

## How to add or edit a product

1. Photos into `assets/img/originals/`, run `python tools/optimise-images.py`.
2. Copy a `<li class="panel panel--flush panel--hover tile">` in `#produtos` (photo, `REF.`, name, one-line excerpt, `data-dialog="p-<id>"` + `href="#p-<id>"`).
3. Copy a `<dialog class="modal" id="p-<id>" data-key="blue">` block: header (`PRODUTO // NN`, `REF.`), main photo + thumbnail buttons (`data-src` 1600w, `data-full` original, `data-alt`), name, description (verbatim), `.spec` readouts (`MATERIAL`, `APROVAÇÃO`, `TECIDO` only when the copy has that line), `TAMANHOS` chips, mailto button with the product in the subject.
4. Update `04 // KU01 · …` in the section head. No prices, no cart, ever.

## How to add or edit an athlete

1. Photo into `assets/img/originals/`, run the optimiser.
2. Copy an `<article class="panel panel--flush athlete">` in `#atletas` (or uncomment the Guilherme / Santiago skeletons). Set `data-key` (next in red/blue rotation), add `athlete--flip` if the previous panel had the image on the left, fill photo (`alt` pt-PT, `pos-top` if the head is near the top), `ATLETA // NN`, name (`.name__first` Light / `.name__last` Black), achievements as `<li style="--i: n"><span class="val">7x</span><span class="lab">…</span></li>` (empty `.val` when the line has no leading numeral; weights/years wrapped in `.mono`), `@handle` (omit rather than guess).
3. Update the counters: `ATLETAS // NN` and every `ATLETAS APOIADOS` readout (hero + Compromisso). Count only live panels.

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
- Martim Sá's Instagram is missing; André Aguiar's handle differs between the old site (`_aguiar05._`) and the rebuild brief (`aguiar05.`); Guilherme and Santiago Gonçalves panels are commented out pending photo + achievements.

## Checks before pushing

```bash
python -m http.server 8000
python tools/screenshots.py http://localhost:8000 docs/screenshots/phase-3 index
grep -c 'url("assets/' index.html        # must be 0
grep -n "green\|yellow\|glitch\|scanline" index.html   # must be empty
grep -rn "squarespace\|€\|Carrinho\|Reservar\|cart" index.html   # must be empty
```
