#!/usr/bin/env python3
"""Headless behaviour check of index.html (Phase 4 one-pager).

    python -m http.server 8000            # in another terminal
    python tools/motion-test.py http://localhost:8000

With reduced_motion="no-preference": reveals fire, the hero parallax runs (scroll-driven CSS or the
JS --py fallback), the product sheet opens/closes with the keyboard (Enter, Space, Esc), scroll-spy
follows the sections, the mobile menu opens/closes, "ler mais" / "+ n" / gallery work.
With reduced_motion="reduce": no transforms on revealed elements, everything visible, no running
ambient animations. Prints one line per check and exits 1 on any failure. Also prints page heights.
"""
import sys

from playwright.sync_api import sync_playwright

BASE = sys.argv[1].rstrip("/") if len(sys.argv) > 1 else "http://localhost:8000"
URL = f"{BASE}/index.html"
fails = []


def check(name, ok, detail=""):
    print(f"{'ok  ' if ok else 'FAIL'} {name}" + (f"  ({detail})" if detail else ""))
    if not ok:
        fails.append(name)


def motion(page, width):
    page.goto(URL, wait_until="networkidle")
    page.wait_for_timeout(600)
    n_reveal = page.evaluate("document.querySelectorAll('[data-reveal]').length")
    n_in = page.evaluate("document.querySelectorAll('[data-reveal].is-in').length")
    check(f"{width}: hero words rise (hero.is-in)", page.evaluate("document.querySelector('.hero').classList.contains('is-in')"))
    check(f"{width}: reveals fire only in view first", 0 < n_in < n_reveal, f"{n_in}/{n_reveal}")
    # scroll through the page: everything reveals, parallax updates
    height = page.evaluate("document.body.scrollHeight")
    for y in range(0, height, 300):
        page.evaluate(f"window.scrollTo(0, {y})")
        page.wait_for_timeout(40)
    page.wait_for_timeout(500)
    n_in = page.evaluate("document.querySelectorAll('[data-reveal].is-in').length")
    check(f"{width}: every reveal fired after a full scroll", n_in == n_reveal, f"{n_in}/{n_reveal}")
    sda = page.evaluate("document.documentElement.classList.contains('sda')")
    page.evaluate("window.scrollTo(0, 400)")
    page.wait_for_timeout(200)
    hero_t = page.evaluate("getComputedStyle(document.querySelector('.hero__photo img')).transform")
    py = page.evaluate("document.querySelector('.hero__photo').style.getPropertyValue('--py')")
    check(f"{width}: hero parallax active ({'scroll-driven CSS' if sda else 'JS fallback'})", hero_t != "none" and (sda or py != ""), f"transform={hero_t[:40]} --py={py}")
    check(f"{width}: progress bar moves", page.evaluate("document.querySelector('.progress').style.transform") not in ("", "scaleX(0)"))
    check(f"{width}: readouts settled to the real value", page.evaluate("[...document.querySelectorAll('[data-settle]')].map(e => e.textContent).join(',')") == "03,04,2025,03")
    check(f"{width}: type-on finished (no cursor left)", page.evaluate("document.querySelectorAll('[data-type].is-typing').length") == 0)
    # scroll spy
    page.evaluate("document.getElementById('atletas').scrollIntoView()")
    page.wait_for_timeout(500)
    check(f"{width}: scroll-spy follows Atletas", page.evaluate("document.querySelector('[data-spy][aria-current=\"true\"]')?.getAttribute('data-spy')") == "atletas")
    page.evaluate("document.getElementById('contacto').scrollIntoView()")
    page.wait_for_timeout(500)
    check(f"{width}: scroll-spy follows Contacto", page.evaluate("document.querySelector('[data-spy][aria-current=\"true\"]')?.getAttribute('data-spy')") == "contacto")
    # product sheet with the keyboard
    page.evaluate("window.scrollTo(0, 0)")
    first = page.locator(".tile__btn").first
    first.focus()
    page.keyboard.press("Enter")
    page.wait_for_timeout(700)
    check(f"{width}: Enter opens the product sheet", page.evaluate("document.querySelector('.sheet').classList.contains('is-open') && document.getElementById('prod-kit').classList.contains('is-active') && location.hash === '#p-kit'"))
    check(f"{width}: sheet has real height", page.evaluate("document.querySelector('.sheet').getBoundingClientRect().height") > 400)
    page.keyboard.press("Escape")
    page.wait_for_timeout(700)
    check(f"{width}: Esc closes it and focus returns to the tile", page.evaluate("!document.querySelector('.sheet').classList.contains('is-open') && document.activeElement === document.querySelector('.tile__btn') && location.hash === ''"))
    check(f"{width}: closed sheet has no height", page.evaluate("document.querySelector('.sheet').getBoundingClientRect().height") < 2)
    page.locator(".tile__btn").nth(1).focus()
    page.keyboard.press("Space")
    page.wait_for_timeout(700)
    check(f"{width}: Space opens the second product", page.evaluate("document.getElementById('prod-cintos').classList.contains('is-active')"))
    page.locator("#prod-cintos [data-close-product]").click()
    page.wait_for_timeout(700)
    check(f"{width}: Fechar closes it", page.evaluate("!document.querySelector('.sheet').classList.contains('is-open')"))
    # thumbnails crossfade + gallery dialog
    page.locator(".tile__btn").first.click()
    page.wait_for_timeout(700)
    page.locator("#prod-kit .thumbs button").nth(2).click()
    page.wait_for_timeout(900)
    check(f"{width}: thumbnail swaps the main photo", page.evaluate("document.querySelector('#prod-kit [data-main] img').src.includes('img_5612')"))
    page.locator("#prod-kit [data-gallery]").click()
    page.wait_for_timeout(500)
    check(f"{width}: gallery dialog opens with the full set", page.evaluate("document.getElementById('galeria').open && document.querySelectorAll('#galeria .modal__grid li').length") == 18)
    page.keyboard.press("Escape")
    page.wait_for_timeout(400)
    check(f"{width}: Esc closes the gallery, sheet stays open", page.evaluate("!document.getElementById('galeria').open && document.querySelector('.sheet').classList.contains('is-open')"))
    # ler mais / + n
    page.locator("[data-toggle='compromisso-more']").click()
    page.wait_for_timeout(700)
    check(f"{width}: ler mais reveals the rest of Compromisso", page.evaluate("document.getElementById('compromisso-more').getBoundingClientRect().height") > 60)
    check(f"{width}: full palmarés visible (12 results)", page.evaluate("[...document.querySelectorAll('.palmares li')].filter(l => l.offsetParent && getComputedStyle(l).opacity === '1').length") == 12)
    check(f"{width}: glitch layers present on photos without faces", page.evaluate("document.querySelectorAll('.photo[data-glitch] .glitch').length") == 8)
    page.evaluate("window.scrollBy(0, 120)")
    page.wait_for_timeout(100)
    check(f"{width}: HUD shapes burst while scrolling", page.evaluate("document.querySelector('.fx').classList.contains('is-scrolling')"))
    # mobile menu
    if width < 720:
        page.locator(".nav__toggle").click()
        page.wait_for_timeout(400)
        check("390: menu opens", page.evaluate("document.getElementById('nav-menu').classList.contains('is-open') && document.querySelector('.nav__toggle').getAttribute('aria-expanded') === 'true'"))
        page.keyboard.press("Escape")
        page.wait_for_timeout(400)
        check("390: Esc closes the menu", page.evaluate("!document.getElementById('nav-menu').classList.contains('is-open')"))
    overflow = page.evaluate("document.documentElement.scrollWidth - document.documentElement.clientWidth")
    check(f"{width}: no horizontal overflow with the sheet open", overflow == 0, f"{overflow}px")


def reduced(page, width):
    page.goto(URL, wait_until="networkidle")
    page.wait_for_timeout(400)
    res = page.evaluate("""() => {
      const bad = [];
      document.querySelectorAll('[data-reveal], .hero__title .w, .readouts li, .rule--key').forEach(e => {
        const cs = getComputedStyle(e);
        if (cs.opacity !== '1' || (cs.transform !== 'none' && !e.classList.contains('rule--key'))) bad.push(e.className);
        if (e.classList.contains('rule--key') && cs.transform !== 'none' && cs.transform !== 'matrix(1, 0, 0, 1, 0, 0)') bad.push('rule');
      });
      const anim = [];
      document.querySelectorAll('.ticker__track, .hero__vword, .hero__ruler, .hero__glow, .reticle__arms, .hero__photo img, .fx__s').forEach(e => {
        if (getComputedStyle(e).animationName !== 'none') anim.push(e.className || e.tagName);
      });
      return { bad, anim, sda: document.documentElement.classList.contains('sda') };
    }""")
    check(f"{width} reduce: all revealed, no transforms", len(res["bad"]) == 0, ",".join(res["bad"][:5]))
    check(f"{width} reduce: no ambient animations", len(res["anim"]) == 0, ",".join(res["anim"][:5]))
    check(f"{width} reduce: scroll-driven class off", not res["sda"])
    check(f"{width} reduce: no glitch layers", page.evaluate("document.querySelectorAll('.glitch').length") == 0)
    print(f"{width} reduce: page height {page.evaluate('document.body.scrollHeight')}px")
    page.locator(".tile__btn").first.click()
    page.wait_for_timeout(200)
    check(f"{width} reduce: sheet still opens", page.evaluate("document.querySelector('.sheet').classList.contains('is-open')"))


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for width, height in ((390, 844), (1280, 800)):
            ctx = browser.new_context(viewport={"width": width, "height": height}, reduced_motion="no-preference", color_scheme="dark")
            page = ctx.new_page()
            errors = []
            page.on("pageerror", lambda e: errors.append(str(e)))
            motion(page, width)
            check(f"{width}: no page errors", not errors, "; ".join(errors)[:200])
            ctx.close()
            ctx = browser.new_context(viewport={"width": width, "height": height}, reduced_motion="reduce", color_scheme="dark")
            reduced(ctx.new_page(), width)
            ctx.close()
            # browsers without scroll-driven animations: the JS parallax fallback must update --py
            ctx = browser.new_context(viewport={"width": width, "height": height}, reduced_motion="no-preference", color_scheme="dark")
            page = ctx.new_page()
            page.add_init_script("CSS.supports = () => false")
            page.goto(URL, wait_until="networkidle")
            page.evaluate("window.scrollTo(0, 400)")
            page.wait_for_timeout(300)
            check(f"{width} legacy: JS parallax fallback sets --py", not page.evaluate("document.documentElement.classList.contains('sda')") and page.evaluate("document.querySelector('.hero__photo').style.getPropertyValue('--py')") != "")
            ctx.close()
        browser.close()
    print(f"\n{len(fails)} failure(s)")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
