# Phase 2 — HUD brand system

Branch `phase-2-hud` → `main`. Phase 1 is frozen in `archive/phase-1/` (first commit on this branch, before any Phase 2 work).

## What changed per page

**Everywhere**
- New stylesheet `assets/css/hud.css` replaces `style.css`. Tokens exactly as briefed; Tomorrow 300/900 (+400 on photos) and Geist Mono 400/700 self-hosted (converted from `shomen-engine/fonts` with fonttools); Inter deleted.
- Component kit: panel (1px line, four 8px corner ticks, grain), micro-label (+ key dot / yellow tick variants), rule + `rule--key`, readout (+ list version for achievements), chips, 24px reticle, 48px buttons (invert on hover, primary = key fill), sticky blurred nav with key dot on the active item and a full-screen overlay menu on mobile (46px Black items), `body.debug` 12-col guide.
- `components.html` (noindex, not in the nav) renders the kit in red, blue and green.
- Grain: 200×200 noise PNG tiled at 2.8 % over every photo and panel.
- Motion: nav bar + hero micro-labels fade/translate in with a 120 ms stagger; panels reveal once on scroll (IntersectionObserver, threshold .2); button inversion and thumb opacity on hover. `prefers-reduced-motion` turns all of it off. Nothing else moves.
- `tools/screenshots.py` now also reports horizontal overflow and console errors; Phase 2 screenshots in `docs/screenshots/phase-2/`, Lighthouse summary in `docs/screenshots/phase-2/lighthouse.txt` (accessibility 100, best-practices 100 on all four pages).

**Início (red)**
- Hero: full-bleed photo with bottom fade, micro-label row `SHOMEN // KARATE // PORTUGAL` + `EST. 2025`, h1 as three stacked lines with `HOJE` in red, right-aligned readouts (`ATLETAS APOIADOS 03`, `EST. 2025`), vertical `SHOMEN` word on the right strip (desktop only).
- Compromisso: panel with the fact `A ÚNICA MARCA PORTUGUESA DE KARATE QUE PAGA PRÉMIOS AOS SEUS ATLETAS` as an h2 in Black, the three draft paragraphs in Light, readout `ATLETAS APOIADOS 03` (three live roster panels; the two commented-out ones are not counted).
- Produtos teaser: four panels, photo top, name Black, `REF.` in mono, one-line excerpt.
- Statement bands: photo left / text right on desktop, headings verbatim, vignette on the photos.
- Atletas teaser: 2×2 on mobile, 4 across on desktop. **No athlete labels**: none of the four photos is an identified athlete (they are product shoots, see `assets/img/SOURCES.md`), so nothing was guessed.
- Contacto: panel, mailto as the primary button.

**Atletas (red + green)**
- Head: `TEAM SHOMEN // ÉPOCA 2026/27`, h1, then a left rail (sticky on desktop) with the fact h2 at 34px, the `ATLETAS APOIADOS` readout, a numbered roster list and one reticle.
- One panel per athlete, image alternating left/right. Leonor red, André green, Martim red (rotation). Name = first name Light + surname Black in the athlete's key. Achievements as readouts: leading numeral (`#1`, `7x`, `5º`, `2x`) in mono, label Light, text verbatim (kept `7x` with a letter x as on the old site rather than `7×`). Weights and years inside labels are wrapped in mono. Instagram as a small mono `@handle`.
- Guilherme and Santiago Gonçalves panels remain commented-out skeletons (green / red in the rotation).

**Produtos (blue)**
- Centred stack. Each product is a panel: `PRODUTO // NN` + `REF. <SKU>` header, gallery (main + thumbs, no lightbox), name Black, mono `REF.`, description Light, `TAMANHOS` chips in mono, spec readouts. `REF.` codes are the **real SKUs** from the old store (KU01, BE01, CV01, TS02), not invented.
- Kit: `MATERIAL` / `4oz 100% Polyester` and `APROVAÇÃO` / `Aprovado para uso em todas as provas FNK-P.` became readouts; the size note stays under the chips. T-shirt: `TECIDO` / `Polyester` became a readout. Still no prices, no cart.

## Layout axes used (≥3 different choices per page)

| Page | Axes |
|---|---|
| Início | left-aligned 3-line hero, vertical word on the right strip, right-aligned readouts, photo-left bands, red key |
| Atletas | full-width head + left rail, alternating image side, two-line name, readout list, red/green keys |
| Produtos | centred stack, chips for sizes, spec readouts under the copy, blue key |

## Invented micro-labels (veto list)

Real words (PT-PT): `O NOSSO COMPROMISSO` (was the Phase 1 heading), `EQUIPAMENTO`, `EQUIPAMENTO // KUMITE`, `COMPETIÇÃO`, `MATERIAIS`, `TEAM SHOMEN`, `TEAM SHOMEN // ÉPOCA 2026/27`, `ATLETA // 01`, `PALMARÉS`, `ATLETAS APOIADOS`, `PRODUTO // 01`, `TAMANHOS`, `MATERIAL`, `APROVAÇÃO`, `TECIDO`, `CONTACTO // ENCOMENDAS E PARCERIAS`, `CONTACTO // ENCOMENDAS E INFORMAÇÕES`, `MENU` / `FECHAR`, `SHOMEN // KARATE // PORTUGAL`.
System codes (mono): `EST. 2025`, `SEC. 01`, `ATLETAS // 03`, `04 // KU01 · BE01 · CV01 · TS02`, `04 // FNK-P`, `WKF // KUMITE` (Leonor and André only, whose results are WKF kumite categories; not on Martim), `REF. KU01/BE01/CV01/TS02`, `REF. HUD-WEB-26` (components page only), `01 / 03` (components page only).

## Deviations worth knowing

- The hero `h1` uses the briefed `clamp(56px,12vw,150px)` token but is additionally capped at `7.8vw` so the three lines fit inside the 1200px wrap at 1280 (Tomorrow Black is ~0.81em per glyph; `COMEÇAM HOJE` at 150px needs ~1460px). On phones the lines wrap naturally.
- Long h2 sentences (the fact, the two bands) use `clamp(28px,4.2vw,52px)` instead of the 88px h2 scale; short section titles use the full 88px scale.
- `--dim` on `--bg` is 2.3:1, so dim is used for graphics only (reticle, empty readout dashes); all micro-label text is `--grey` (7.2:1).
- The nav's blur lives on a pseudo-element, and the mobile menu is a direct child of the header, because a `backdrop-filter` or a transform on the header traps the fixed overlay.

## Three things most likely to need toning down

1. **The load stagger on the hero micro-labels + nav bar** (6px rise, 400 ms, 120 ms steps). It is subtle in code but on a slow connection the labels may pop in after the photo.
2. **Scroll reveal on every panel** (12px rise). With many panels on Produtos it may read as "everything slides", even at 400 ms. Candidate to restrict to the first panel of each section.
3. **Thumbnail opacity hover (0.7 → 1)** on the product galleries: at 64px the dimmed state may just look faded rather than "inactive".

Also flag for a look on a real phone: the hero at 390px (three lines become four) and the yellow tick micro-accent (`ÉPOCA` label) which only appears on the components page.
