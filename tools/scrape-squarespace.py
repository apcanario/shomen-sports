#!/usr/bin/env python3
"""Fetch the old Squarespace site as JSON and save raw responses to docs/scrape/.

Usage:  python tools/scrape-squarespace.py
Output: docs/scrape/<slug>.json, docs/scrape/home.html, docs/scrape/site.css
"""
import json
import pathlib
import re
import sys

import requests

BASE = "https://www.shomen-sports.com"
PAGES = {
    "home": "/",
    "atletas": "/atletas",
    "loja": "/loja",
    "p-kumite-aka-ao": "/loja/p/kumite-aka-ao",
    "p-cintos-kumite": "/loja/p/cintos-kumite",
    "p-corta-vento": "/loja/p/corta-vento",
    "p-tshirt-preta": "/loja/p/tshirt-preta",
}
OUT = pathlib.Path(__file__).resolve().parent.parent / "docs" / "scrape"
UA = {"User-Agent": "Mozilla/5.0 (site-migration scraper)"}


def fetch(url: str) -> requests.Response:
    r = requests.get(url, headers=UA, timeout=60)
    print(f"{r.status_code} {url}")
    if r.status_code != 200:
        print(f"!! BLOCKED {url} -> {r.status_code}", file=sys.stderr)
    return r


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for slug, path in PAGES.items():
        r = fetch(f"{BASE}{path}?format=json-pretty")
        if r.status_code == 200:
            (OUT / f"{slug}.json").write_text(r.text, encoding="utf-8")

    home = fetch(BASE + "/")
    if home.status_code == 200:
        (OUT / "home.html").write_text(home.text, encoding="utf-8")
        css_links = re.findall(r'<link[^>]+rel="stylesheet"[^>]+href="([^"]+)"', home.text)
        css_links += re.findall(r'<link[^>]+href="([^"]+)"[^>]+rel="stylesheet"', home.text)
        print("stylesheets:", css_links)
        for i, href in enumerate(dict.fromkeys(css_links)):
            url = href if href.startswith("http") else BASE + href
            r = fetch(url)
            if r.status_code == 200:
                (OUT / f"site-{i}.css").write_text(r.text, encoding="utf-8")
        icons = re.findall(r'<link[^>]+rel="(?:icon|apple-touch-icon[^"]*|shortcut icon)"[^>]+href="([^"]+)"', home.text)
        icons += re.findall(r'<link[^>]+href="([^"]+)"[^>]+rel="(?:icon|apple-touch-icon[^"]*|shortcut icon)"', home.text)
        print("icons:", icons)
        (OUT / "head-icons.json").write_text(json.dumps(icons, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
