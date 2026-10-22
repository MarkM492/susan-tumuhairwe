# Susan Tumuhairwe site: instructions for Claude

This is a client build on the Skyline Blueprint. Read `../skyline-blueprint/CLAUDE.md` first, then its
`docs/02-design-tokens.md` and `docs/03-components.md`. **Where an element cannot co-exist with the blueprint, the
blueprint wins** (owner's standing rule).

## Client rules
- Colour: ONE green palette on every page (the first draft). Owner's ruling: logo colours are only *sprinkled* as small accents,
  never used to re-colour a page (full per-page themes clashed). Sprinkle = `--c-sprinkle` (gold by default; olive on
  `data-venture="nourish"`; the logo's **pink, never purple**, on `prosper`, which also tints that page's CTA button).
  Colours only in `site/css/tokens.css`. The header has no decoration line and the footer is the original blueprint footer
  (four columns, logo tiles, Real Food strip); do not restyle either.
  **No gradients, no marquee, no auto-playing carousels** (the home hero fade is the one blueprint slider).
- The Nourish & Thrive and Women Prosper **logos are their icons**: tiles, service badges, tab bar, banner emblems, footer.
- Frame: every page is the same 1200px sheet (`--page-w`); the scrollbar track is always reserved (`html{overflow-y:scroll}`) so page length never changes the width. Do not give any page its own width or base text size. If the owner sees widths differ between pages, check browser zoom first: Chrome stores zoom per local file when pages are opened as `file://` (see docs/02 item 16).
- Header: the name in Satisfy (no icon beside it) with the title "Nutrition & Wellness Coach" as a small tag under it. The top-bar tab shows the page's venture (`TOPBAR_TEXT` in build_site.py); Home keeps the title. The top-bar tab's slanted edge is the leafy branch (`topbar_branch()` in `build_site.py`: gold/accent stem, green leaves). That branch is the one place the sprig lives; do not add it back to the header.
- Phones: titles, intros, cards and buttons are centred; long copy is justified (hyphenated). Related content stays in ONE section: heading, intro and teaser visible, everything else for that topic inside a single `more(...)` (optionally with `chips=[...]` as a folded-state summary). Card groups that are secondary are wrapped in `more(...)` ("I want to know more" button) and long paragraphs use `data-clamp` ("Read more"). An opened item folds itself again once the reader scrolls past it (see `client.js` section 2); never remove the scroll correction there.
- White space: generous vertical rhythm is deliberate (owner asked for it even if pages scroll more). Tune only in `client.css` section 10 (`--section-pad`, gaps, `.stack`). Do not tighten it to shorten pages; use folds instead.
- Scroll-in animation (`client.js` section 3 + `client.css` section 11, modelled on vce-environment.com's fade-up / side slide-in / stagger): elements get `.anim` classes from JS, reveal once via IntersectionObserver, then `settle()` strips the classes. No library. Never hide content when JS or the observer is missing, and keep `prefers-reduced-motion` honoured. New section types need a tagger line in `client.js`.
- Script type (Satisfy, `--font-script`): ONLY the name "Susan Tumuhairwe" and quotations/taglines. Never for headings or body.
- The first page and nav item is called **Home** (not "Meet Susan"). Never write "free" before "consultation".
- Minimise vertical scrolling, especially on phones: lists of cards use class `rail` (swipe row on phones, grid on desktop,
  with `data-rail="label"`); long paragraphs on phones get `data-clamp` (Read more). Phones get a bottom tab bar.
  Target: no page longer than about 4 screens at 390px. Check with the height script in docs/01.
- Fonts: self-hosted Jost (`site/fonts/`) for everything; Roboto Condensed 600 (loaded from Google Fonts) for the main nav only, per the blueprint. No third family.
- Back-port candidates for the blueprint: rails, Read more clamp, tab bar, page sprinkles. Do not edit blueprint copies here.
- Pages are generated: edit `tools/build_site.py`, run it, never hand-edit the HTML unless it is a one-off.
- Do not edit blueprint copies (`base/components/responsive.css`, `main.js`, `icons.js`) in this folder; change the
  blueprint and re-copy. Client-only CSS goes in `client.css`.
- Banner photos use an inline `background-image` on `.banner`.
- Keep Susan's wording. Social handles come only from Susan (see `SOCIAL` in build_site.py); no invented links, testimonials, statistics or "coming soon" notes.
- Placeholders still to replace are listed in `docs/02-open-items.md`.
- Check at 390px and 1280px: no horizontal scroll, one h1 per page, no console errors.
