# Transformation brief

**Source:** https://cool-cannoli-89234f.netlify.app/ (original files kept untouched in `07_Web_Projects\trial-web-1`).
**Goal:** transform and optimise on the Skyline Blueprint. Remove colour and gradient clutter. Blueprint wins on conflicts.

## What changed
| Old site | New site |
|---|---|
| Multiple colours and gradients, a different theme per venture | One green palette, flat colours, same look on every page |
| Aurora/gradient backdrop | Flat sage backdrop around a white 1200px sheet |
| Marquee, story rotators, carousels | Static grids, service cards, info boxes, gallery |
| Mixed fonts | Jost only (self-hosted, 25 KB) |
| Unstructured long pages | Blueprint templates: banner + breadcrumbs, top bar, mega/dropdown nav, footer with logos and photos |
| Full-size photos | Optimised webp (about 1.4 MB for all 24 images), cut-out portraits on flat tint |
| Public "coming soon" developer notes | Removed |
| Contact via basic form | Netlify Form with validation, honeypot, success/failure messages |

## Page mapping
- Meet Susan (`index.html`): hero, welcome, ventures as service cards, gallery, CTA.
- Nourish & Thrive: banner, intro, programmes as service cards, meal gallery, CTA.
- Women Prosper: banner, intro, tracks, CTA.
- Speaking & Workshops: banner, topics, formats, CTA.
- Contact: contact cards, form (topic pre-selects from `?topic=`), map link.

## Dropped
Marquee, carousels, story rotators, per-venture colours, gradients, decorative blobs, "coming soon" notes,
success stories and testimonials (no real content yet).

## Accessibility and performance
One h1 per page, labelled form fields, visible focus, alt text, `font-display: swap`, immutable asset caching,
no layout overflow at 390px (tested 5 pages x desktop/mobile).


---

# Phase 2: customisation to Susan (12 Oct 2026)

Requests from Mark, and what was done.

| Request | Done |
|---|---|
| Less vertical scrolling, especially on mobile; use horizontal scrolling for related items | Swipe **rails** for tiles, featured cards, venture cards, service cards, info boxes, contact cards and the meal gallery; Read more folds on long paragraphs; slimmer header, hero and banner; compact footer; **bottom tab bar** with the two logos. Phone page length (390px): Home 8.3 to 4.0 screens, Nourish & Thrive 10.5 to 4.0, Women Prosper 6.5 to 3.1, Speaking 5.9 to 2.7, Contact 3.2 to 1.7. Desktop gallery is also a one-row rail with arrows |
| Satisfy for quotes and the name | Self-hosted Satisfy (23 KB, Apache 2.0). Used for the brand name, the home quote, banner taglines and the name inside paragraphs. Nowhere else |
| "Meet Susan" becomes Home | Nav, drawer, footer, tab bar, breadcrumbs and active state all say Home |
| Page colour matches the logo | **Revised in Phase 2b** (see below): every page stays on the first-draft green; logo colours are sprinkled as small accents only. Banners are greyscale photos under one flat green wash |
| Use the logos as the iconography | Home tiles, venture card badges, tab bar, banner emblems (gold-ringed white disc) and footer |
| Remove the word "free" | Removed everywhere (buttons, copy, meta description) |
| Home tiles: remove "Real food, real meals" | Four tiles remain, on the first-draft green ramp. The "Real food" photo card stays in the featured row and the footer photo strip |
| A unique touch for header, footer and nav | The **sprig** signature, kept light: name in Satisfy in the header (the leaf mark beside it moved to the top-bar tab in Phase 3), leaf marker for the current/hover nav item, leaf bullets in dropdowns, leaf divider under headings, a faint branch in banners. (The header vine and the redesigned footer were removed in Phase 2b) |

Also: removed the duplicate "No Experience Needed" card on Women Prosper (it appeared twice); Women Prosper banner uses her studio portrait (greyscale, under the green wash); the favicon is the sprig mark.

## Phase 2b: revert and refine
Mark's feedback after reviewing Phase 2: the header vine crowded the header, the footer redesign was not wanted, and full per-page colour themes clashed.

| Feedback | Done |
|---|---|
| Revert the footer | Original four-column footer is back (Get in Touch, Explore, logo tiles, Real Food strip). Phones show it in two columns with the Real Food strip hidden |
| Remove the wavy line in the header | Header vine removed on desktop, tablet and phone |
| Women Prosper uses the pinkish hue, not purple | Pink (`#d05a9e`, from the logo) is its accent, with a pink CTA button |
| Too many colour clashes; sprinkle the logo colours, do not re-colour pages | All five pages are on the first-draft green again. Accents only: gold by default, olive on Nourish & Thrive, pink on Women Prosper (leaf divider, nav leaf marker, rail dots, tab-bar marker, banner tagline) |

Kept from Phase 2: Satisfy, Home rename, logos as icons, swipe rails, Read more, tab bar, no "free", four home tiles.
Phone length at 390px after the revert: Home 3.9, Nourish & Thrive 4.0, Women Prosper 3.1, Speaking 2.7, Contact 1.7 screens.

## Phase 3: frame, phone presentation, folding, header
| Feedback | Done |
|---|---|
| Same outer frame width on every page | Measured identical (1200px) at nine window sizes, but now locked: the scrollbar track is always reserved so a short page cannot be wider or shifted, and phone text-size inflation is switched off. If it still looks different on a device, send the window width or a screenshot |
| Centre or justify in phone view | Titles, intros, cards (tiles, info boxes, service cards, gallery captions) and buttons are centred; long paragraphs are justified with hyphenation; contact copy centred |
| "Read more" / "I want to know more" with auto-collapse | New `.more` blocks (Home steps, Nourish & Thrive approach, Women Prosper what you will find, Speaking how I speak) and the existing Read more paragraphs. Phones only. Opened content folds back automatically when the reader scrolls past it, and the scroll position is corrected so nothing jumps |
| Remove the leaf icon before the name | Header shows the name alone |
| Turn the top-bar tab's slanting edge into the leaf branch | The slant is now a stem with leaves growing into the bar; the stem and tip take the page accent (gold, olive, pink) |
| Cleanup and a little more accent | Accent line under banners, accent top edge on grey panels, offset accent shadow on photo frames, accent ring on info-box icons, accent bar under footer titles, accent underline on text links, accent on tile hover, text selection; favicon metadata stripped (8.5 KB to 0.7 KB); unused sprig symbol and brand-mark CSS removed |

## Phase 4: denser phone view, better grouping
Feedback: the phone view was still too long, and some directly related content sat outside its section.

| Change (phones only; desktop is unchanged) | Detail |
|---|---|
| Related content grouped into one fold block | Women Prosper: the paragraph, "What you will find" and the five "What you will gain" cards are one section. Speaking: "How I speak" and the six session topics are one section. Nourish & Thrive: the six areas, the meals gallery and the second story paragraph sit inside their own sections. Home: the three ventures, the steps and the second welcome paragraph |
| One-glance chips | While folded, Nourish & Thrive areas, Women Prosper benefits and Speaking topics show short name chips so the scope is visible without opening |
| Less duplicated content | The Home "Featured" strip (duplicates the tiles and venture cards) and the repeated quote heading are hidden; the footer drops its Explore list (the tab bar carries it) and keeps contact details and the two logos |
| Tighter rhythm | 20px side gutter, smaller section padding, 120px intro photos, 108px banners, compact service cards, headings 19.5px, call-to-action paragraphs fold with Read more, buttons shrink so pairs sit side by side |
Phone length at 390px (screens): Home 3.9 to 2.6, Nourish & Thrive 3.9 to 2.6, Women Prosper 3.0 to 2.2, Speaking 2.6 to 2.0, Contact 1.8 to 1.6.

## Phase 5: breathing space
Feedback: with so many colours and so much information the pages felt compact; more vertical white space was wanted even at the cost of more scrolling.

| Change | Detail |
|---|---|
| Section padding | 76px top and bottom on desktop (52px on phones), up from the blueprint's tighter rhythm |
| Gaps | Split layouts 72px, card grids 32px, service rows 44px; `.stack` spacer 56px |
| Panels | Grey panels 44px 40px; call-to-action band 64px 40px; three card wrappers switched from `panel-grey` to `panel-plain` so fewer grey boxes sit against each other; info boxes neutral |
| Result at 390px (screens) | Home 3.3, Nourish & Thrive 3.5, Women Prosper 2.9, Speaking 2.6, Contact 1.9 |
All of it lives in `client.css` section 10, so it can be tuned in one place (`--section-pad` and the gap values).

## Phase 6: scroll-in animation
Feedback: add in-flow animations as the reader scrolls so they are drawn down the page, in the way vce-environment.com does it. That site uses WOW.js with animate.css (`fadeInUp`, `fadeInRight`, delays in .2s steps); we reproduce the feel with a small IntersectionObserver and CSS transitions (no library, no copied code).

| Element | Effect |
|---|---|
| Section headings, intros, prose, panels, cards, tiles, rail rows, gallery, footer columns, form | Fade up 42px (30px on phones) over .95s, with a short stagger between siblings (`--anim-delay`) |
| Split-layout photos | Slide in from the right or left (64px) as the text fades up |
| Banner text and emblem | Play once on load |
| Heading leaf divider | The line draws out from the centre just after its heading appears |
Rules: each element animates once, then the script removes the classes (`settle()`) so hover effects behave normally; reveal starts when an element is 9% inside the viewport; with `prefers-reduced-motion` or no IntersectionObserver nothing is hidden. Code: `client.js` section 3, `client.css` section 11.
Checked at 1440px and 390px on all five pages: nothing left hidden, no horizontal overflow while slide-ins run, no script errors.

## Phase 7: client comments, first batch
Client feedback was split into batches. Done in this batch:

| Comment | Change |
|---|---|
| Home does not mention Women Prosper or speaking | Welcome copy replaced with Susan's own text (intro visible, Nourish & Thrive / Women Prosper / speaker paragraphs and the mission behind "Read more" on phones) |
| "Studio" | Replaced by the physical office: Interservice Tower, Lumumba Avenue, Kampala (footer, contact card, top-bar map link, aria label) |
| Phone number | +256 784 717 586 everywhere |
| Social handles | Top bar (desktop), footer (all sizes) and a "Follow along" block on Contact; TikTok glyph added to the blueprint icon set |
| Speaking: six sessions first | The six session cards now come before the four qualities (Practical, Engaging, Evidence-informed, Tailored) |
Next batch (not yet done): shorter Home scroll, box colours and icons on Speaking, business element in the title. The photo comments are done (phase 8).

## Phase 8: client photos
Photos supplied by Susan (placed straight in `site/images/`, not through `optimise_images.py`):

| Where | Photo |
|---|---|
| Home, Women Prosper card | `p024-women-team.webp`: four women (the previous photo included a man) |
| Nourish & Thrive, Hormonal Health | `p025-pregnancy-smile.webp` (replaces the ultrasound close-up) |
| Metabolic Health | `p026-waist-measure.webp` (tape around the waist) |
| Bone & Joint Health | `p027-stretch-workout.webp` (woman working out) |
| Supplementation Guidance | `p028-supplement.webp`: used as supplied, including its headline ("The World's first phyto nutrient supplement since 1958") and the Nourish & Thrive logo; crop position tuned for phones in `client.css` section 13 |
Old files (`p005`, `p006`, `p008`) are no longer referenced and can be deleted.

## Phase 9: client comments, last batch
| Comment | Change |
|---|---|
| Title should show the business (item 11) | The top-bar tab names the page's venture: Nourish & Thrive, Women Prosper, Speaking & Workshops, Get in Touch. Home keeps "Nutrition & Wellness Coach". Under the name "Susan Tumuhairwe" a small tagline now reads "Nutrition & Wellness Coach" (all pages, phones too) |
| Speaking boxes looked like ten continuous ones (item 8) | The six sessions are now photo tiles: greyscale photo under ONE flat green wash, each with its own wash and icon-disc colour (gold, pink, olive, light gold, sage). The four qualities stay as light boxes, separated by a divider reading "All sessions are customised to you, to be:" |
| Frame width differs when moving between pages | Measured identical (1200px sheet) on every page at nine window sizes. In Mark's Chrome the pages are opened as local files; Chrome remembers a separate zoom level for each local file, so one page can be at a different zoom than another. See `02-open-items.md` item 16 |

## Checking page length on a phone
`python3` with Playwright: open each page at 390x844 and divide `document.documentElement.scrollHeight` by 844.
