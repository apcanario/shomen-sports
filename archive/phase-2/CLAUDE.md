# CLAUDE.md — maintenance guide for the Shomen Sports site

Static site, no build step, served by GitHub Pages from the `main` branch root. Portuguese (pt-PT) only.

## Phases and the archive rule

- **Phase 1** (done): content + basic dark layout. Snapshot in `archive/phase-1/`.
- **Phase 2** (this): the Shomen HUD visual system (Tomorrow + Geist Mono, panels, micro-labels, key colour per page, restrained motion).
- **Before starting any new phase**, copy everything in the repo (except `.git` and the contents of `archive/`) into a new versioned folder `archive/phase-N/` and commit that snapshot first. Pedro's rule, no exceptions.

## File map

```
index.html                 Início: hero (3 stacked lines, HOJE in key colour), Compromisso panel, product tiles, statement bands, athletes strip, contact panel
produtos.html              Produtos (blue key): one <article class="panel product"> per product, centred stack, contact panel
atletas.html               Atletas (red + green keys): left rail + one <article class="panel athlete"> per athlete, alternating image side, contact panel
components.html            Internal kit page (noindex, not in the nav): every component in every key colour. Screenshot it after CSS changes.
assets/css/hud.css         The only stylesheet: tokens, base, grain, micro-labels/rules/readouts/chips/reticle, panel, photo, buttons, nav, layout pieces, motion, debug grid
assets/js/main.js          Mobile nav overlay + load stagger + one-time scroll reveal. Nothing else.
assets/fonts/              Tomorrow-Light/Regular/Black.woff2, GeistMono-Regular/Bold.woff2 (+ OFL licences). Converted from shomen-engine/fonts with fonttools.
assets/img/grain.png       200×200 greyscale noise, tiled at 2.8 % opacity over photos and panels
assets/img/originals/      Full-resolution source photos and logo PNGs (never edit, never mirror)
assets/img/*-1600.webp     Generated renditions (tools/optimise-images.py)
assets/img/*-800.webp      Generated renditions
assets/img/SOURCES.md      Where every original came from (URL + pixel size). None of the product photos is an identified athlete.
docs/squarespace-tokens.md Phase 1 record of the old Squarespace theme (historical; Phase 2 tokens are in hud.css)
docs/screenshots/          Phase 1 review screenshots
docs/screenshots/phase-2/  Phase 2 review screenshots (390 + 1280, all pages + components)
docs/scrape/*.json         Raw JSON of the old site, kept for content re-checks
tools/optimise-images.py   Generates the WebP renditions
tools/screenshots.py       Full-page screenshots + overflow/console check (Playwright, optional dev dependency)
tools/scrape-squarespace.py, tools/download-assets.py   One-off migration scripts (kept for the record)
archive/phase-1/           Frozen snapshot of Phase 1
CNAME, .nojekyll, robots.txt, sitemap.xml, favicon.ico, apple-touch-icon.png   GitHub Pages / SEO plumbing
```

## Design tokens (`assets/css/hud.css`, `:root`)

```css
--bg:#090A0E; --panel:rgba(14,16,22,.85); --panel-solid:#0E1016;
--white:#F5F6F8; --grey:#969CA8; --dim:#464C5A;
--red:#FF2A50; --blue:#54C8FF; --green:#22E080; --yellow:#FFD23F;
--line:rgba(245,246,248,.12); --tick:rgba(245,246,248,.4);
--key: var(--red);   /* set per page / per athlete via [data-key] */
```

Type: **Tomorrow** 300 Light and 900 Black only (400 Regular only for copy sitting on a photo, e.g. hero micro-labels). **Geist Mono** only for numbers and codes (dates, weights, sizes, rankings, `REF.` lines, counters). Everything that is a label, heading or nav item is uppercase. Scale: hero `clamp(56px,12vw,150px)` (the Início hero is additionally capped with `min(…, 7.8vw)` so its three lines fit the 1200px wrap), h2 `clamp(36px,7vw,88px)`, band/fact h2 `clamp(28px,4.2vw,52px)`, h3 34px, body 18px, micro 13px tracked `.14em`.

Contrast: `--grey` on `--bg` is 7.2:1 (AA at 13px). `--dim` on `--bg` is 2.3:1, so **dim is for graphics only** (reticle, empty readout dashes), never for text.

## Key colour per page

| Page | `<body data-key>` | Notes |
|---|---|---|
| Início | `red` | HOJE, primary button, active nav dot, rule underlines |
| Produtos | `blue` | Data/spec page. Chips, readout labels, primary button |
| Atletas | `red` on body; per athlete panel `data-key` | Leonor **red**, André **green**, Martim red, Guilherme green, Santiago red (rotate red/green, never blue) |
| components.html | `red` | Sections repeat the kit in red, blue and green |

Rules: white does the talking; key colour ≤ 10 % of any viewport. Yellow only as a 2–4 px micro-accent (`.micro--tick`, reticle centre dot). Grey/dim for secondary text and rules, never a surface. The logo (`union.png`) is always pure white, never tinted, never on a colour block, never inside a panel with corner ticks. Text writes `SHOMEN` (no macron).

## FX ban

No glitch, VHS, scanlines, chromatic aberration, matrix rain, parallax, marquee, cursor followers, count-up counters, typewriter. No motion that touches text, the logo or a face. No photo duotone or colour overlay (a bottom fade or vignette to `--bg` is allowed). No mirrored photos. No `border-radius` other than 0. The grain is not an effect; it stays on.

Motion ceiling (all in `main.js` + the "Motion" block of `hud.css`): nav + hero micro-labels fade/translate in with a 120 ms stagger on load; `[data-reveal="scroll"]` panels fade/translate in once (IntersectionObserver, threshold .2); buttons invert on hover; product thumbs go from 70 % to 100 % opacity on hover. `prefers-reduced-motion` disables all of it.

## Component list (class → what it is)

- `.panel` (+ `.panel--flush`): `--panel` fill, 1px `--line` border, four 8px corner ticks (`::before`), grain (`::after`). Content gets `position: relative` automatically.
- `.micro` (+ `--dot` key square, `--tick` yellow tick, `--white`): 13px Light tracked uppercase label. `.microbar` lays several out space-between.
- `.mono`: Geist Mono for numbers/codes inside any text.
- `.rule` / `.rule--key`: 1px line / 2px key colour, 48px, used as a heading underline.
- `.readout` (+ `--sm`, `--text`, `--end`): micro-label over a mono value. `.readouts` is the list version (`.val` mono + `.lab` Light) used for achievements.
- `.chips` / `.chip` (+ `--key`): mono size chips.
- `.reticle`: 24px inline SVG crosshair, `--dim`, yellow centre dot. Max one per section.
- `.btn` (+ `--primary`, `--block`): 48px, Black, uppercase, 1px white border, inverts on hover. `.actions` groups them.
- `.nav` / `.nav__*`: sticky bar with blur, logo white left, Light uppercase items, key dot on `aria-current="page"`, full-screen overlay under 720px with 46px Black items.
- `.photo` (+ `--fade`, `--vignette`, `--4x5`, `--1x1`, `--3x2`): image wrapper with grain; `img.pos-top` keeps heads in frame.
- Layout: `.wrap`, `.section`, `.section__head`, `.grid--4/3/2`, `.hero`, `.tile`, `.band`, `.strip`, `.fact`, `.rail-layout` + `.rail`, `.athlete` (+ `--flip`), `.name` (`__first` Light / `__last` Black key), `.product` + `.thumbs` + `.spec`, `.contact`, `.footer`.
- `body.debug`: 12-column guide overlay for alignment checks. Never ship it active.

## How to add an athlete panel

1. Photo into `assets/img/originals/`, run `python tools/optimise-images.py`.
2. In `atletas.html`, copy an existing `<article class="panel panel--flush athlete" …>` (or uncomment the Guilherme/Santiago skeletons). Set `id`, `data-key` (next in the red/green rotation), add `athlete--flip` if the previous panel had the image on the left, fill the photo (`alt` in pt-PT, `pos-top` if the head is near the top edge), the `ATLETA // NN` counter, the name (`.name__first` / `.name__last`), achievements as `<li><span class="val">7x</span><span class="lab">…</span></li>` (leave `.val` empty when the line does not start with a numeral; wrap weights/years in the label with `<span class="mono">`), and the `@handle` link (omit rather than guess).
3. Update the counters: the rail list, `ATLETAS // NN`, and the `ATLETAS APOIADOS` readouts on `atletas.html` and `index.html` (count only live, un-commented panels).

## How to add a product panel

1. Photos into `assets/img/originals/`, run `python tools/optimise-images.py`.
2. In `produtos.html`, copy an `<article class="panel product" …>`. Set `id`, `PRODUTO // NN`, `REF. <SKU>` (real SKU from the old store: KU01, BE01, CV01, TS02), the main `<figure>` + `.thumbs`, name, description paragraphs (verbatim), `.spec` readouts (`MATERIAL`, `APROVAÇÃO`, `TECIDO` only when the copy has that line), and the `TAMANHOS` chips.
3. Add or swap a `.tile` on `index.html` if it should be featured. No prices, no cart, ever.

## Content rules (short version)

- Copy from the old site is reproduced verbatim, including capitalisation quirks (`CONTACTa-NOS`, `pÓDIO`, `FIca`). Headings are uppercased by CSS. Never fix copy silently; flag with `<!-- TODO: typo? … -->`.
- No prices anywhere. Purchase path is contact only: `info@shomen-sports.com` and `@shomen_sports`.
- Never mirror or flip a photo. Use `object-position` (`pos-top`) instead of tighter crops. Check every crop at 390px.
- Only outbound links: Instagram and `mailto:`. No analytics, no CDN, no external fonts.
- Invented micro-labels are listed in the Phase 2 PR description; new ones go there too so Pedro can veto.

## Open TODOs (search the HTML for `TODO`)

- `index.html`: Compromisso copy is a draft for Pedro's review.
- `produtos.html`: "Ultra Level" in the Corta Vento description is probably "Ultra Leve".
- `atletas.html`: Martim Sá's Instagram is missing; André Aguiar's handle differs between the old site (`_aguiar05._`) and the rebuild brief (`aguiar05.`); Guilherme and Santiago Gonçalves panels are commented out pending photo + achievements.

## Checks before pushing

```bash
python -m http.server 8000
python tools/screenshots.py http://localhost:8000
grep -n "Inter\|glitch\|scanline\|border-radius" assets/css/*.css
grep -rn "squarespace\|€\|Carrinho\|Reservar\|cart" *.html assets/css
```

Screenshots must show 0px overflow and 0 console errors on every page at 390 and 1280. The first grep may only return `border-radius: 0`; the second must return nothing.
