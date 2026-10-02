#!/usr/bin/env python3
"""Generate 1600w and 800w WebP renditions for every image in assets/img/originals/.

Usage:  python tools/optimise-images.py            # only missing/outdated outputs
        python tools/optimise-images.py --force    # regenerate everything

Output: assets/img/<name>-1600.webp and assets/img/<name>-800.webp (quality 82).
Images narrower than a target width are not upscaled: the rendition is written at the
original width instead, so <srcset> descriptors in the HTML should use the real width
(the script prints it).

Requires Pillow:  python -m pip install pillow

Never flips or mirrors images (gi lettering must stay readable). Never touches the originals.
Non-photo assets (logo PNGs, favicon, OG image) are skipped: they are used as-is.
"""
import pathlib
import sys

from PIL import Image, ImageOps

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "assets" / "img" / "originals"
DST = ROOT / "assets" / "img"
WIDTHS = (1600, 800)
QUALITY = 82
SKIP = {"union.png", "group-137.png", "group-26-1.png", "social-media-image.png", "favicon.ico"}


def main() -> None:
    force = "--force" in sys.argv
    for src in sorted(SRC.iterdir()):
        if src.name in SKIP or src.suffix.lower() not in (".jpg", ".jpeg", ".png", ".webp"):
            continue
        stem = src.stem
        with Image.open(src) as im:
            im = ImageOps.exif_transpose(im)  # honour EXIF orientation, never mirror
            if im.mode not in ("RGB", "RGBA"):
                im = im.convert("RGB")
            for w in WIDTHS:
                out = DST / f"{stem}-{w}.webp"
                if out.exists() and not force and out.stat().st_mtime >= src.stat().st_mtime:
                    continue
                target_w = min(w, im.width)
                target_h = round(im.height * target_w / im.width)
                resized = im.resize((target_w, target_h), Image.LANCZOS)
                resized.save(out, "WEBP", quality=QUALITY, method=6)
                print(f"{out.name:<60} {target_w}x{target_h} {out.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
