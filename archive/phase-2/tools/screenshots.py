#!/usr/bin/env python3
"""Full-page screenshots of the site at 390px and 1280px.

Requires a local server and Playwright (optional dev dependency, not needed to run the site):
    python -m pip install playwright && python -m playwright install chromium
    python -m http.server 8000          # in another terminal
    python tools/screenshots.py http://localhost:8000 [out_dir] [page ...]

Defaults: out_dir = docs/screenshots/phase-2, pages = index produtos atletas components.
Prints the horizontal overflow of each page (must be 0).
"""
import pathlib
import sys

from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = sys.argv[1].rstrip("/") if len(sys.argv) > 1 else "http://localhost:8000"
OUT = ROOT / (sys.argv[2] if len(sys.argv) > 2 else "docs/screenshots/phase-2")
PAGES = sys.argv[3:] or ["index", "produtos", "atletas", "components"]
WIDTHS = (390, 1280)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for width in WIDTHS:
            ctx = browser.new_context(viewport={"width": width, "height": 844 if width < 720 else 800},
                                      device_scale_factor=1, color_scheme="dark", reduced_motion="reduce")
            page = ctx.new_page()
            errors = []
            page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
            page.on("pageerror", lambda e: errors.append(str(e)))
            for name in PAGES:
                page.goto(f"{BASE}/{name}.html", wait_until="networkidle")
                page.evaluate("document.querySelectorAll('img[loading=lazy]').forEach(i => i.loading = 'eager')")
                page.wait_for_load_state("networkidle")
                page.wait_for_timeout(300)
                overflow = page.evaluate("document.documentElement.scrollWidth - document.documentElement.clientWidth")
                out = OUT / f"{name}-{width}.png"
                page.screenshot(path=str(out), full_page=True)
                print(f"{out.name:<24} overflow: {overflow}px  console errors: {len(errors)}")
                errors.clear()
            ctx.close()
        browser.close()


if __name__ == "__main__":
    main()
