# Susan Tumuhairwe: website

Nutrition & Wellness Coach (ventures: Nourish & Thrive, Women Prosper, Speaking & Workshops).
Rebuilt on the **Skyline Blueprint** (`../skyline-blueprint/`): one calm green palette, no gradients, no per-venture colour themes.

## Structure
```
site/                  what gets published (Netlify publish dir)
  index.html           Meet Susan (home)
  nourish-and-thrive.html
  women-prosper.html
  speaking-and-workshops.html
  contact.html         Netlify Form
  css/ js/ fonts/ images/ favicon.svg
    css/client.css     everything that is Susan-specific (frame, script type, top-bar branch edge, accents, rails, fold blocks, phone layout, tab bar)
    css/art.css        GENERATED flat artwork (leaf divider mask, banner branch)
    css/tokens.css     colours; the two page sprinkles are at the bottom
    js/client.js       swipe rails, Read more / "I want to know more" with auto-fold on scroll
    fonts/             Jost (body) and Satisfy (the name and quotations only)
tools/
  build_site.py        regenerates the 5 pages from shared parts + data
  make_art.py          regenerates css/art.css
  optimise_images.py   original photos -> web-ready webp and greyscale banners (see docs)
docs/                  transformation brief, open items
netlify.toml           publish dir, cache and security headers
serve.ps1              local preview on http://localhost:8080
```

## Working on it
- Edit copy/facts in `tools/build_site.py`, then `python3 tools/build_site.py` (all pages stay consistent).
- Colours live **only** in `site/css/tokens.css` (one green palette on every page, plus a small `nourish` / `prosper` accent block at the bottom). Client-only rules live in `site/css/client.css`.
- Each page picks its accent sprinkle with `<html data-venture="...">` (set per page in `PAGES` in `build_site.py`). Only small accents change (leaf marks, dividers, rail dots, banner tagline, Women Prosper's button); the palette never does.
- `base.css`, `components.css`, `responsive.css`, `main.js`, `icons.js` are blueprint copies. Do not edit them here;
  improve the blueprint and copy them back.
- Preview with `serve.ps1` (not by double-clicking the HTML).

## Deploy (Netlify)
Publish directory `site`. The contact form uses Netlify Forms; after the first deploy, submit a test message and
check Forms in the Netlify dashboard. See `docs/02-open-items.md` before going live.
