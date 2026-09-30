# Squarespace 7.1 design tokens (extracted)

Source: `site.css` linked from the homepage `<head>` of https://www.shomen-sports.com/ (saved as `docs/scrape/site-7.css`). Extracted on 2026-09-30.

## Colour theme variables (`:root`)

| Variable | Raw HSL (h, s, l) | Hex |
|---|---|---|
| `--white-hsl` | `60,9.09%,97.84%` | `#FAFAF9` |
| `--black-hsl` | `235.71,70%,3.92%` | `#030411` |
| `--accent-hsl` | `349.04,100%,54.9%` | `#FF1943` |
| `--lightAccent-hsl` | `0,0%,93.73%` | `#EFEFEF` |
| `--darkAccent-hsl` | `235.38,13.13%,19.41%` | `#2B2C38` |
| `--safeLightAccent-hsl` | `0,0%,100%` | `#FFFFFF` |
| `--safeDarkAccent-hsl` | `349.04,100%,54.9%` | `#FF1943` |
| `--safeInverseAccent-hsl` | `0,0%,100%` | `#FFFFFF` |
| `--safeInverseLightAccent-hsl` | `0,0%,0%` | `#000000` |
| `--safeInverseDarkAccent-hsl` | `0,0%,100%` | `#FFFFFF` |

Sanity check: `--black-hsl` is a near-black with a blue cast, `--white-hsl` a warm off-white, `--accent-hsl` a saturated red (matches the logo hexagon and the `colorData` averages `ff1943` Squarespace stored for the OG image). Palette shape is as expected.

## Derived values used by the new site

| Token | Derivation | HSL | Hex |
|---|---|---|---|
| `--color-bg` | `--black-hsl` as is | `235.71,70%,3.92%` | `#030411` |
| `--color-card` | `--black-hsl` lightness +5 points | `235.71,70%,8.92%` | `#070927` |
| `--color-border` | `--black-hsl` lightness +12 points (1px borders only) | `235.71,70%,15.92%` | `#0C1045` |
| `--color-text` | `--white-hsl` as is | `60,9.09%,97.84%` | `#FAFAF9` |
| `--color-accent` | `--accent-hsl` as is | `349.04,100%,54.9%` | `#FF1943` |

## Section themes used on the old pages

Squarespace section themes seen in the scraped HTML: `dark` (hero), `light-bold` (shop teaser, contact), `black` (statement bands, athletes), `black-bold` (footer). Their resolved variables:

### `black`

- `--siteBackgroundColor`: `hsla(var(--black-hsl),1)`
- `--headingLargeColor`: `hsla(var(--white-hsl),1)`
- `--headingMediumColor`: `hsla(var(--white-hsl),1)`
- `--paragraphMediumColor`: `hsla(var(--white-hsl),1)`
- `--primaryButtonBackgroundColor`: `hsla(var(--safeLightAccent-hsl),1)`
- `--primaryButtonTextColor`: `hsla(var(--safeInverseLightAccent-hsl),1)`
- `--navigationLinkColor`: `hsla(var(--white-hsl),1)`

### `black-bold`

- `--siteBackgroundColor`: `hsla(var(--black-hsl),1)`
- `--headingLargeColor`: `hsla(var(--safeLightAccent-hsl),1)`
- `--headingMediumColor`: `hsla(var(--safeLightAccent-hsl),1)`
- `--paragraphMediumColor`: `hsla(var(--white-hsl),1)`
- `--primaryButtonBackgroundColor`: `hsla(var(--safeLightAccent-hsl),1)`
- `--primaryButtonTextColor`: `hsla(var(--safeInverseLightAccent-hsl),1)`
- `--navigationLinkColor`: `hsla(var(--safeLightAccent-hsl),1)`

### `dark`

- `--siteBackgroundColor`: `hsla(var(--darkAccent-hsl),1)`
- `--headingLargeColor`: `hsla(var(--white-hsl),1)`
- `--headingMediumColor`: `hsla(var(--white-hsl),1)`
- `--paragraphMediumColor`: `hsla(var(--white-hsl),1)`
- `--primaryButtonBackgroundColor`: `hsla(var(--safeLightAccent-hsl),1)`
- `--primaryButtonTextColor`: `hsla(var(--safeInverseLightAccent-hsl),1)`
- `--navigationLinkColor`: `hsla(var(--white-hsl),1)`

### `light-bold`

_No dedicated rule block found in site.css (theme falls back to the `white`/default light mapping)._

## Typography (for the record only — the new site uses self-hosted Inter)

- `--heading-font-font-family`: `"Anton"`
- `--heading-font-font-weight`: `400`
- `--heading-font-text-transform`: `uppercase`
- `--body-font-font-family`: `"Epilogue"`
- `--body-font-font-weight`: `500`

Headings: Anton 400, uppercase. Body: Epilogue 500. Both were loaded from Squarespace's font CDN; neither is used in the rebuild.
