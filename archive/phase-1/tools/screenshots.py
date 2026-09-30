#!/usr/bin/env python3
"""Full-page screenshots of every page at 390px and 1280px, saved to docs/screenshots/.

Requires a local server and Playwright (optional dev dependency, not needed to run the site):
    python -m pip install playwright && python -m playwright install chromium
    python -m http.server 8000          # in another terminal
    python tools/screenshots.py http://localhost:8000
"""
import pathlib
import sys

from playwright.sync_api import sync_playwright

BASE = sys.argv[1].rstrip("/") if len(sys.argv) > 1 else "http://localhost:8000"
OUT = pathlib.Path(__file__).resolve().parent.parent / "docs" / "screenshots"
PAGES = ("index", "produtos", "atletas")
WIDTHS = (390, 1280)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for width in WIDTHS:
            ctx = browser.new_context(viewport={"width": width, "height": 844 if width < 720 else 800},
                                      device_scale_factor=1, color_scheme="dark")
            page = ctx.new_page()
            for name in PAGES:
                page.goto(f"{BASE}/{name}.html", wait_until="networkidle")
                # Force lazy images to load before capturing.
                page.evaluate("document.querySelectorAll('img[loading=lazy]').forEach(i => i.loading = 'eager')")
                page.wait_for_load_state("networkidle")
                overflow = page.evaluate("document.documentElement.scrollWidth - document.documentElement.clientWidth")
                out = OUT / f"{name}-{width}.png"
                page.screenshot(path=str(out), full_page=True)
                print(f"{out.name:<20} horizontal overflow: {overflow}px")
            ctx.close()
        browser.close()


if __name__ == "__main__":
    main()
