#!/usr/bin/env python3
"""Make index.html self-contained: embed the woff2 fonts and the grain PNG as data URIs.

Usage:  python tools/inline-assets.py            # rewrites index.html in place
Idempotent: url("...") references that are already data: URIs are left alone.
Photos stay as files under assets/img/ (they are content, not chrome).
"""
import base64
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
HTML = ROOT / "index.html"
MIME = {".woff2": "font/woff2", ".png": "image/png", ".svg": "image/svg+xml"}


def main() -> None:
    text = HTML.read_text(encoding="utf-8")

    def repl(m: re.Match) -> str:
        rel = m.group(1)
        path = ROOT / rel
        if not path.exists():
            raise SystemExit(f"missing asset: {rel}")
        data = base64.b64encode(path.read_bytes()).decode("ascii")
        print(f"inlined {rel} ({path.stat().st_size // 1024} KB)")
        return f'url("data:{MIME[path.suffix]};base64,{data}")'

    new = re.sub(r'url\("(assets/(?:fonts|img)/[^"]+\.(?:woff2|png|svg))"\)', repl, text)
    HTML.write_text(new, encoding="utf-8")
    print(f"index.html: {HTML.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
