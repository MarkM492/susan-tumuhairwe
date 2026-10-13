#!/usr/bin/env python3
"""
Susan Tumuhairwe site: image optimisation.

Reads the originals (a folder of webp/png files) and writes web-ready versions into
../site/images. Re-run any time a source image changes.

    python3 optimise_images.py <source-images-dir> [jost-ttf]

Rules
  * Cut-out portraits (transparent webp) and small files are copied as they are.
  * Logos are shrunk to 400px (they are only shown small).
  * Large photos are re-encoded at quality 74.
  * banner-*.jpg are built from two photos, then darkened with ONE flat tint (no gradients),
    as the blueprint banner requires: dark, with any subject on the right so the title can sit left.
  * og-cover.jpg (1200x630) is rebuilt in the new flat style for social sharing.
"""
import os, sys, shutil
from PIL import Image, ImageDraw, ImageFont, ImageOps

SRC = sys.argv[1]
JOST = sys.argv[2] if len(sys.argv) > 2 else None
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "site", "images")
os.makedirs(OUT, exist_ok=True)

INK = (18, 48, 29)          # --c-navy


def save_webp(im, name, q=74):
    im.save(os.path.join(OUT, name), "WEBP", quality=q, method=6)


for f in sorted(os.listdir(SRC)):
    if not f.endswith(".webp"):
        continue
    p = os.path.join(SRC, f)
    im = Image.open(p)
    if f.startswith("logo-"):
        im.thumbnail((400, 400), Image.LANCZOS)
        save_webp(im, f, 82)
    elif im.mode == "RGBA" or os.path.getsize(p) < 90_000:
        shutil.copy(p, os.path.join(OUT, f))
    else:
        save_webp(im.convert("RGB"), f, 74)


def finish(box, name):
    """Banners are saved as plain dark greyscale. The page theme colours them with ONE flat CSS wash
    (.banner::before, derived from --c-navy), so the same photo can serve any venture hue."""
    g = ImageOps.grayscale(box)
    g = Image.blend(g, Image.new("L", g.size, 0), 0.30).convert("RGB")
    g.save(os.path.join(OUT, name), "JPEG", quality=72, optimize=True, progressive=True)


# shore: calm sea and horizon taken from the right-hand side of the photo (no face behind the headline)
im = Image.open(os.path.join(SRC, "p023-meditation-shore.webp")).convert("RGB")
region = im.crop((520, 90, 1200, 90 + round(680 * 280 / 1200)))
finish(region.resize((1200, 280), Image.LANCZOS), "banner-shore.jpg")

# speaking: portrait pushed to the right; the left is filled by mirroring the blurred background
im = Image.open(os.path.join(SRC, "p019-susan-speaking.webp")).convert("RGB")
pad = 330
canvas = Image.new("RGB", (im.width + pad, im.height))
canvas.paste(im, (pad, 0))
canvas.paste(im.crop((0, 0, pad, im.height)).transpose(Image.FLIP_LEFT_RIGHT), (0, 0))
finish(canvas.crop((0, 90, 1200, 90 + 280)), "banner-speaking.jpg")

# prosper: studio portrait on the deep purple backdrop; the left is filled with the backdrop's own flat edge
im = Image.open(os.path.join(SRC, "p022-susan-suit.webp")).convert("RGB")
canvas = Image.new("RGB", (1200, im.height))
canvas.paste(im.crop((0, 0, 40, im.height)).resize((460, im.height), Image.BILINEAR), (0, 0))
canvas.paste(im, (400, 0))
finish(canvas.crop((0, 165, 1200, 165 + 280)), "banner-prosper.jpg")

# ---- og-cover.jpg ----
W, H = 1200, 630
og = Image.new("RGB", (W, H), INK)
d = ImageDraw.Draw(og)
cut = Image.open(os.path.join(SRC, "p003-susan-hero.webp")).convert("RGBA")
ch = 560
cut = cut.resize((int(cut.width * ch / cut.height), ch), Image.LANCZOS)
panel = Image.new("RGB", (cut.width + 120, H), (223, 231, 224))   # --c-photo-bg
og.paste(panel, (W - panel.width, 0))
og.paste(cut, (W - panel.width + 60, H - ch), cut)


def font(size, weight="Bold"):
    if JOST:
        f = ImageFont.truetype(JOST, size)
        try:
            f.set_variation_by_name(weight)
        except Exception:
            pass
        return f
    return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", size)


d.text((70, 170), "Susan", font=font(110), fill="white")
d.text((70, 290), "Tumuhairwe", font=font(110), fill="white")
d.rectangle((72, 440, 132, 444), fill=(201, 162, 74))
d.text((70, 462), "Nutrition & Wellness Coach", font=font(40, "Medium"), fill=(207, 226, 213))
d.text((70, 530), "Nourish & Thrive  |  Women Prosper  |  Speaking", font=font(26, "Regular"), fill=(160, 190, 170))
og.save(os.path.join(OUT, "og-cover.jpg"), "JPEG", quality=80, optimize=True, progressive=True)
print("done")
