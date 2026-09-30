# CLAUDE.md — maintenance guide for the Shomen Sports site

Static site, no build step, served by GitHub Pages from the `main` branch root. Portuguese (pt-PT) only.

## Phase note

**Phase 1 = content + layout.** Motion and identity work is Phase 2 — don't add it during content updates. That means: no animations, no transitions beyond a plain hover, no scroll effects, no gradients, no shadows beyond a 1px border, no custom graphics, no new colours.

## File map

```
index.html                 Início: hero, Compromisso, product teaser, statement bands, athletes teaser, contact
produtos.html              Produtos: one <article class="product"> per product, contact CTA
atletas.html               Atletas: one <li class="card athlete"> per athlete, contact CTA
assets/css/style.css       The only stylesheet. Tokens at :root, then base, header, buttons, sections, hero, cards, bands, strip, contact, products, athletes, footer
assets/js/main.js          Mobile nav toggle only
assets/fonts/              InterVariable.woff2 (Inter 4.1, OFL licence alongside)
assets/img/originals/      Full-resolution source photos and logo PNGs (never edit, never mirror)
assets/img/*-1600.webp     Generated renditions (tools/optimise-images.py)
assets/img/*-800.webp      Generated renditions
assets/img/SOURCES.md      Where every original came from (URL + pixel size)
docs/squarespace-tokens.md Colours/fonts extracted from the old Squarespace theme and how the site tokens derive from them
docs/scrape/*.json         Raw JSON of the old site, kept for content re-checks
tools/optimise-images.py   Generates the WebP renditions
tools/screenshots.py       Full-page screenshots at 390/1280px into docs/screenshots/ (needs Playwright, optional)
tools/scrape-squarespace.py, tools/download-assets.py   One-off migration scripts (kept for the record)
docs/screenshots/          Review screenshots of each page at 390px and 1280px
CNAME, .nojekyll, robots.txt, sitemap.xml, favicon.ico, apple-touch-icon.png   GitHub Pages / SEO plumbing
```

## Design tokens

All in `assets/css/style.css` under `:root`. They come from the old Squarespace theme (see `docs/squarespace-tokens.md`); do not invent colours.

| Token | Value | Use |
|---|---|---|
| `--color-bg` | `hsl(235.71, 70%, 3.92%)` = `#030411` | Page background |
| `--color-card` | `hsl(235.71, 70%, 8.92%)` = `#070927` | Cards and product panels (background lightness +5) |
| `--color-border` | `hsl(235.71, 70%, 15.92%)` = `#0C1045` | 1px borders only |
| `--color-text` | `hsl(60, 9.09%, 97.84%)` = `#FAFAF9` | Text |
| `--color-text-muted` | text at 72% alpha | Captions, copyright |
| `--color-accent` | `hsl(349.04, 100%, 54.9%)` = `#FF1943` | Links, active nav item, primary button, `.eyebrow` labels. Nothing else is red. |

Type: Inter (self-hosted variable font), body 400, headings 700–800, uppercase for `h1`/`h2`/card titles. Sizes use `clamp()` steps `--text-0` … `--text-4`. Layout: `--max-width: 1100px`, `--gutter: 16px`, single column under 720px.

## How to add or edit a product

1. Put the new photos in `assets/img/originals/` (lowercase, hyphens, no spaces). Run:

   ```bash
   python tools/optimise-images.py
   ```

   It writes `<name>-1600.webp` and `<name>-800.webp` next to the originals' parent folder. Commit the originals and the WebPs.
2. In `produtos.html`, copy an existing `<article class="product" id="…">` block. Update: the `id`, the main `<figure>` (link to the original, `srcset` with both WebPs, `alt` in pt-PT describing the photo), the `<ul class="thumbs">` (one `<li>` per extra photo), the `<h2 class="product-title">`, the description paragraphs, and the `Tamanhos` block (delete it if the product has no sizes). Add `class="pos-top"` on a photo whose subject's head is near the top edge.
3. In `index.html`, the product teaser has four cards linking to `produtos.html#<id>`. Add or swap a card there if the product should be featured.
4. Add the new original + URL to `assets/img/SOURCES.md` if it came from somewhere worth recording.

## How to add or edit an athlete

1. Photo into `assets/img/originals/`, run `python tools/optimise-images.py`.
2. In `atletas.html`, copy an existing `<li class="card athlete" id="…">` (two commented-out skeletons for Guilherme and Santiago Gonçalves are already there). Fill in the photo, the name in `<h2 class="card-title">`, one `<li>` per achievement, and the Instagram link (omit the link rather than guessing a handle).
3. Update the `<!-- TODO -->` comments accordingly.

## Content rules (short version)

- Copy from the old site is reproduced verbatim, including capitalisation quirks (e.g. `CONTACTa-NOS`, `pÓDIO`). Headings are uppercased by CSS, so the quirks are not visible. Don't "fix" copy silently; flag suspected typos with an HTML comment (`<!-- TODO: typo? … -->`).
- No prices anywhere: not in text, `alt`, comments or `SOURCES.md`. No cart, no checkout, no "Reservar", no "Adicionar ao Carrinho". The purchase path is contact only: `info@shomen-sports.com` and Instagram `@shomen_sports`.
- Never mirror or flip a photo (gi lettering must read correctly). Use `object-position` to keep faces in frame instead of cropping tighter.
- No new sections, testimonials, newsletter forms, cookie banners, analytics or external requests. Only outbound links allowed are Instagram and `mailto:`.
- Brand text is `SHOMEN` / `Shomen` without the macron; the macron exists only in the logo artwork.
- `alt` text is pt-PT and describes what is in the photo.
- Vanilla HTML/CSS/JS only. No frameworks, no preprocessors, no npm.

## Open TODOs (search the HTML for `TODO`)

- `index.html`: Compromisso copy is a draft for Pedro's review.
- `produtos.html`: "Ultra Level" in the Corta Vento description is probably "Ultra Leve".
- `atletas.html`: Martim Sá's Instagram is missing; André Aguiar's handle differs between the old site (`_aguiar05._`) and the rebuild brief (`aguiar05.`); Guilherme and Santiago Gonçalves need photos and achievements.

## Checks before pushing

```bash
python -m http.server 8000
```

Load all three pages at 390px and 1280px. No console errors, no horizontal scroll, no network requests except the site's own files. Then:

```bash
grep -rn "squarespace\|€\|Carrinho\|Reservar\|cart" *.html assets/css
```

must return nothing.
