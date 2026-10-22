#!/usr/bin/env python3
"""
Susan Tumuhairwe: page generator (built on the Skyline Blueprint).

Regenerates the five pages in ../site from shared parts (top bar, header, drawer, footer,
banner) and one body function per page. Copy and facts live in the data blocks near the top;
change them there, run `python3 build_site.py`, and every page stays consistent.

Only blueprint components are used (see ../../skyline-blueprint/docs/03-components.md).
Client-only rules live in site/css/client.css.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "site")

ORG = "Susan Tumuhairwe"
ROLE = "Nutrition &amp; Wellness Coach"
EMAIL = "hello@susantumuhairwe.com"
PHONE_DISPLAY = "+256 784 717 586"
PHONE_TEL = "+256784717586"
OFFICE = "Interservice Tower, Lumumba Avenue, Kampala"
MAPS = "https://maps.google.com/?q=Interservice+Tower,+Lumumba+Avenue,+Kampala"
# Social handles (owner supplied). Facebook has no handle yet, only the profile name, so it links to a name search:
# replace FB_URL with the real profile link (see docs/02-open-items.md).
FB_URL = "https://www.facebook.com/search/top?q=Susan%20Tumuhairwe"
SOCIAL = [
    ("instagram", "Instagram", "@Susan_assy", "https://www.instagram.com/susan_assy/"),
    ("tiktok", "TikTok", "@Susan_assy", "https://www.tiktok.com/@susan_assy"),
    ("tiktok", "TikTok (Women Prosper)", "@Women.Prosper5", "https://www.tiktok.com/@women.prosper5"),
    ("facebook", "Facebook", "Susan Tumuhairwe", FB_URL),
]
YEAR = 2026
SITE_URL = "https://cool-cannoli-89234f.netlify.app"   # replace with the final domain when known


def icon(name, cls=""):
    c = ("icon " + cls).strip()
    return f'<svg class="{c}" aria-hidden="true"><use href="#i-{name}"></use></svg>'


def soc(name):
    """Social icon as a round badge in the network's own colour (Instagram red-pink, Facebook blue, TikTok black)."""
    return f'<span class="soc soc--{name}">{icon(name)}</span>'


def si(name):  # stroked icon
    return icon(name, "icon--stroke")


# --------------------------------------------------------------------------
# NAVIGATION  (6 to 7 top-level items maximum; here 5)
# --------------------------------------------------------------------------
NAV = [
    ("Home", "index.html", None),
    ("Nourish &amp; Thrive", "nourish-and-thrive.html", [
        ("My approach", "nourish-and-thrive.html#approach"),
        ("Six areas I work in", "nourish-and-thrive.html#areas"),
        ("Real food, real meals", "nourish-and-thrive.html#meals"),
        ("Client stories", "nourish-and-thrive.html#stories")]),
    ("Women Prosper", "women-prosper.html", [
        ("What you&rsquo;ll gain", "women-prosper.html#gain"),
        ("Success stories", "women-prosper.html#stories")]),
    ("Speaking &amp; Workshops", "speaking-and-workshops.html", [
        ("Areas of expertise", "speaking-and-workshops.html#expertise"),
        ("Client feedback", "speaking-and-workshops.html#feedback")]),
    ("Contact", "contact.html", None),
]

# Bottom tab bar on phones: short labels, venture logos in place of icons
TABS = [
    ("Home", "index.html", ("icon", "home")),
    ("Nourish", "nourish-and-thrive.html", ("logo", "logo-nourish-and-thrive.webp")),
    ("Prosper", "women-prosper.html", ("logo", "logo-women-prosper.webp")),
    ("Speaking", "speaking-and-workshops.html", ("icon", "mic")),
    ("Contact", "contact.html", ("icon", "chat")),
]
TAB_FOR_ACTIVE = {"Home": "Home", "Nourish &amp; Thrive": "Nourish", "Women Prosper": "Prosper",
                  "Speaking &amp; Workshops": "Speaking", "Contact": "Contact"}

# Browser theme colour: the same green everywhere (page sprinkles are at the bottom of site/css/tokens.css)
THEME_COLOR = {"susan": "#2d6a3e", "nourish": "#2d6a3e", "prosper": "#2d6a3e"}

TAGLINES = {
    "nourish": "Simple habits, real transformation.",
    "prosper": "When women prosper, everyone around them prospers.",
    "speaking": "Healthy people build thriving organisations.",
    "contact": "I read every message myself.",
}


def name_script(cls=""):
    c = ("script " + cls).strip()
    return f'<span class="{c}">{ORG}</span>'


# --------------------------------------------------------------------------
# SHARED PARTS
# --------------------------------------------------------------------------
def topbar_branch():
    """The slanted edge of the top-bar tab, drawn as a leafy branch: a gold stem along the slant with leaves
    growing out of it into the dark bar. Flat fills only; colours come from CSS (tab green, page sprinkle)."""
    leaf = "M0 0 C 5 -9 19 -12 30 -2 C 19 8 5 9 0 0 Z"
    P = [(2, 50), (10, 36), (18, 20), (27, 0)]          # the stem (same slant as the old straight edge)

    def pt(t):
        u = 1 - t
        return tuple(u**3 * P[0][i] + 3 * u**2 * t * P[1][i] + 3 * u * t**2 * P[2][i] + t**3 * P[3][i] for i in (0, 1))
    leaves = ""
    for t, ang, sc, cls in ((0.14, -22, .82, "tb-leaf"), (0.30, -128, .6, "tb-leaf2"), (0.42, 16, .8, "tb-leaf"),
                            (0.58, -128, .58, "tb-leaf2"), (0.70, -26, .78, "tb-leaf"), (0.86, 14, .66, "tb-leaf")):
        x, y = pt(t)
        leaves += f'<path class="{cls}" d="{leaf}" transform="translate({x:.1f} {y:.1f}) rotate({ang}) scale({sc})"/>'
    x, y = pt(0.99)
    leaves += f'<path class="tb-tip" d="{leaf}" transform="translate({x:.1f} {y + 4:.1f}) rotate(-34) scale(.62)"/>'
    return ('<svg class="topbar__branch" viewBox="0 0 60 50" width="60" height="50" aria-hidden="true" focusable="false">'
            '<path class="tb-fill" d="M0 0 H27 C18 20 10 36 2 50 H0 Z"/>'
            '<path class="tb-stem" d="M2 50 C10 36 18 20 27 0" fill="none"/>' + leaves + '</svg>')


# Top-bar tab text: Home keeps Susan's title; every other page names its own venture.
TOPBAR_TEXT = {"Home": ROLE, "Nourish &amp; Thrive": "Nourish &amp; Thrive", "Women Prosper": "Women Prosper",
               "Speaking &amp; Workshops": "Speaking &amp; Workshops", "Contact": "Get in Touch"}


def topbar(active="Home"):
    links = [
        (f"mailto:{EMAIL}", "Email Susan", "mail", "icon--stroke"),
        (f"tel:{PHONE_TEL}", "Call Susan", "phone", ""),
        (MAPS, "Office location: Interservice Tower, Lumumba Avenue, Kampala", "pin", ""),
    ]
    lis = "".join(f'<li><a href="{h}" aria-label="{n}">{icon(i, c)}</a></li>' for h, n, i, c in links)
    lis += "".join(f'<li class="topbar__soc"><a href="{u}" aria-label="{n}: {hdl}" target="_blank" rel="noopener">{soc(i)}</a></li>'
                   for i, n, hdl, u in SOCIAL)
    return f"""<div class="topbar">
      <p class="topbar__title"><span class="topbar__text"><span class="topbar__ghost" aria-hidden="true">{ROLE}</span><span class="topbar__label">{TOPBAR_TEXT.get(active, ROLE)}</span></span>{topbar_branch()}</p>
      <ul class="topbar__social">{lis}</ul>
    </div>"""


def header(active):
    items = []
    for label, target, sub in NAV:
        cur = ' aria-current="page"' if label == active else ""
        if sub:
            lis = "".join(f'<li><a class="panel__link" href="{t}">{n}</a></li>' for n, t in sub)
            items.append(f'<li class="nav__item"><a class="nav__link"{cur} href="{target}">{label}</a><ul class="panel">{lis}</ul></li>')
        else:
            items.append(f'<li class="nav__item"><a class="nav__link"{cur} href="{target}">{label}</a></li>')
    return f"""<header class="header">
      <a class="brand" href="index.html" aria-label="{ORG}, home">
        <span class="brand__stack"><span class="brand__text">{ORG}</span><span class="brand__tag">{ROLE}</span></span>
      </a>
      <nav class="nav" aria-label="Primary">
        <ul class="nav__list">{"".join(items)}</ul>
        <button class="icon-btn nav__toggle" type="button" aria-label="Open menu" data-drawer-open>{si("menu")}</button>
      </nav>
    </header>"""


def drawer():
    rows = ""
    for label, target, sub in NAV:
        if sub:
            sub_html = "".join(f'<a href="{t}">{n}</a>' for n, t in sub)
            rows += (f'<li class="drawer__item"><div class="drawer__row"><a class="drawer__link" href="{target}">{label}</a>'
                     f'<button class="drawer__more" type="button" aria-expanded="false" aria-label="Toggle {label} submenu">{icon("chevron-right")}</button></div>'
                     f'<div class="drawer__sub">{sub_html}</div></li>')
        else:
            rows += f'<li class="drawer__item"><div class="drawer__row"><a class="drawer__link" href="{target}">{label}</a></div></li>'
    return f"""<div class="drawer-scrim" data-drawer-close></div>
  <aside class="drawer" aria-label="Menu">
    <div class="drawer__bar"><button class="drawer__close" type="button" aria-label="Close menu" data-drawer-close>{si("close")}</button></div>
    <ul class="drawer__list">{rows}</ul>
  </aside>"""


def tabbar(active):
    cur_label = TAB_FOR_ACTIVE.get(active)
    out = ""
    for label, href, (kind, val) in TABS:
        cur = ' aria-current="page"' if label == cur_label else ""
        glyph = (f'<img src="images/{val}" alt="" width="28" height="28">' if kind == "logo" else si(val))
        out += f'<a class="tabbar__item" href="{href}"{cur}><span class="tabbar__glyph">{glyph}</span><span class="tabbar__label">{label}</span></a>'
    return f'<nav class="tabbar" aria-label="Quick navigation">{out}</nav>'


FOOT_MEALS = [("p013-meal-tomato-egg", "Tomato, avocado and boiled egg"), ("p010-meal-salad-box", "Mixed salad lunch box"),
              ("p014-meal-beans-posho", "Beans, posho and avocado"), ("p011-meal-beans-veg", "Beans and mixed vegetables"),
              ("p016-meal-fish-plantain", "Fish stew and plantain"), ("p012-meal-breakfast", "A balanced breakfast plate")]


def footer():
    photos = "".join(f'<a href="nourish-and-thrive.html#meals"><img src="images/{n}.webp" alt="{a}" loading="lazy" width="81" height="81"></a>' for n, a in FOOT_MEALS)
    return f"""<footer class="footer">
      <div class="footer__grid">
        <div>
          <h3 class="footer__title">Get in Touch</h3>
          <ul class="footer__list">
            <li>{si("mail")}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
            <li>{icon("phone")}<a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
            <li>{icon("pin")}<a href="{MAPS}">{OFFICE}</a></li>
          </ul>
          <ul class="footer__list footer__social">{"".join(f'<li>{soc(i)}<a href="{u}" target="_blank" rel="noopener" aria-label="{n}">{hdl}</a></li>' for i, n, hdl, u in SOCIAL)}</ul>
        </div>
        <div>
          <h3 class="footer__title">Explore</h3>
          <ul class="footer__list footer__links">
            <li><a href="index.html">Home</a></li>
            <li><a href="nourish-and-thrive.html">Nourish &amp; Thrive</a></li>
            <li><a href="women-prosper.html">Women Prosper</a></li>
            <li><a href="speaking-and-workshops.html">Speaking &amp; Workshops</a></li>
            <li><a href="contact.html">Book a consultation</a></li>
          </ul>
        </div>
        <div>
          <h3 class="footer__title">Our Ventures</h3>
          <div class="footer__logos">
            <a href="nourish-and-thrive.html" aria-label="Nourish &amp; Thrive"><img src="images/logo-nourish-and-thrive.webp" alt="" loading="lazy" width="100" height="106"></a>
            <a href="women-prosper.html" aria-label="Women Prosper"><img src="images/logo-women-prosper.webp" alt="" loading="lazy" width="100" height="100"></a>
          </div>
        </div>
        <div class="footer__food">
          <h3 class="footer__title">Real Food</h3>
          <div class="footer__photos">{photos}</div>
        </div>
      </div>
      <div class="footer__small">
        <span>Copyright &copy; <span data-year>{YEAR}</span> {ORG}. All rights reserved.</span>
        <span>{ROLE} &middot; Kampala, Uganda</span>
      </div>
    </footer>"""


def banner(title, crumbs, image, venture):
    trail = '<li><a href="index.html">Home</a></li>' + "".join(f"<li>{c}</li>" for c in crumbs)
    kick = f'<p class="banner__kicker">{TAGLINES[venture]}</p>'
    emblem = {"nourish": ("nourish-and-thrive.html", "logo-nourish-and-thrive.webp", "Nourish &amp; Thrive"),
              "prosper": ("women-prosper.html", "logo-women-prosper.webp", "Women Prosper")}.get(venture)
    if emblem:
        extra = f'<span class="banner__emblem"><img src="images/{emblem[1]}" alt="{emblem[2]} logo" width="160" height="160"></span>'
        cls = " banner--emblem"
    else:
        extra = '<span class="banner__branch" aria-hidden="true"></span>'
        cls = " banner--branch"
    return f"""<section class="banner{cls}" aria-label="Page title" style="background-image:url(images/{image})">
      <div class="banner__text">{kick}<h1 class="banner__title">{title}</h1><ol class="crumbs">{trail}</ol></div>
      {extra}
    </section>"""


def page(file, title, description, body, active=None, ban="", og_title=None, preload="", venture="susan"):
    full_title = title if file == "index.html" else f"{title} | {ORG}"
    return f"""<!doctype html>
<html lang="en" data-venture="{venture}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{full_title}</title>
  <meta name="description" content="{description}">
  <meta name="theme-color" content="{THEME_COLOR[venture]}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{og_title or full_title}">
  <meta property="og:description" content="{description}">
  <meta property="og:image" content="{SITE_URL}/images/og-cover.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <link rel="preload" href="fonts/Jost-var-latin.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="fonts/Satisfy-latin.woff2" as="font" type="font/woff2" crossorigin>
{preload}  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Roboto+Condensed:wght@600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/fonts.css">
  <link rel="stylesheet" href="css/tokens.css">
  <link rel="stylesheet" href="css/art.css">
  <link rel="stylesheet" href="css/base.css">
  <link rel="stylesheet" href="css/components.css">
  <link rel="stylesheet" href="css/responsive.css">
  <link rel="stylesheet" href="css/client.css">
  <script>document.documentElement.className += ' js';</script>
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <div class="site">
    {topbar(active)}
    {header(active)}
    {ban}
    <main id="main">
{body}
    </main>
    {footer()}
  </div>
  {drawer()}
  {tabbar(active)}
  <button class="to-top" type="button" aria-label="Back to top">{si("arrow-up")}</button>
  <script src="js/icons.js"></script>
  <script src="js/main.js"></script>
  <script src="js/client.js"></script>
</body>
</html>
"""


# --------------------------------------------------------------------------
# COMPONENT HELPERS (markup follows docs/03-components.md exactly)
# --------------------------------------------------------------------------
def pill(label, href, kind="orange", ico="calendar"):
    return f'<a class="btn-pill btn-pill--{kind}" href="{href}">{si(ico)} {label}</a>'


def infobox(ico, title, text, variant=""):
    v = f" {variant}" if variant else ""
    return (f'<div class="infobox{v}"><span class="infobox__icon">{si(ico)}</span>'
            f'<h3 class="infobox__title">{title}</h3><p class="infobox__text">{text}</p></div>')


def session(ico, title, text, img, pos, wash, disc):
    """Speaking topic tile: a photo under a flat green wash (greyscale photo, one flat tint, like the banners).
    Each tile has its own wash and icon-disc colour so the six do not read as one block."""
    return (f'<article class="session" style="--wash:{wash};--disc:{disc}">'
            f'<span class="session__bg" style="background-image:url(images/{img});background-position:{pos}"></span>'
            f'<span class="session__icon">{si(ico)}</span>'
            f'<h3 class="session__title">{title}</h3><p class="session__text">{text}</p></article>')


def service(img, alt, title, text, badge, href, label, cutout=False, pos=None, badge_logo=None):
    cls = " service__media--cutout" if cutout else ""
    style = f' style="object-position:{pos}"' if pos else ""
    if badge_logo:
        b = f'<span class="service__badge service__badge--logo"><img src="images/{badge_logo}" alt="" width="64" height="64"></span>'
    else:
        b = f'<span class="service__badge">{si(badge)}</span>'
    return (f'<article class="service"><div class="service__media{cls}">'
            f'<img src="images/{img}" alt="{alt}" loading="lazy"{style}>{b}</div>'
            f'<div class="service__body"><h3 class="service__title">{title}</h3><p class="service__text">{text}</p></div>'
            f'<a class="service__more" href="{href}"><span>{label}</span>{si("arrow-right")}</a></article>')


def section(inner, first=False, sid=None):
    cls = "section container" if first else "section section--flush-top container"
    i = f' id="{sid}"' if sid else ""
    return f'<section class="{cls}"{i}>{inner}</section>'


def heading(text, intro=None):
    s = f'<h2 class="heading-blue heading-centre">{text}</h2>'
    if intro:
        s += f'<div class="section-intro"><p>{intro}</p></div>'
    return s


def cta_panel(title, text, buttons):
    return section(f'''<div class="panel-grey text-centre cta">
        <h2 class="heading-blue">{title}</h2>
        <div class="section-intro"><p data-clamp>{text}</p></div>
        <div class="btn-row btn-row--centre">{buttons}</div>
      </div>''')


def photo(img, alt, w, h, ratio=None, cutout=False, pos=None):
    cls = "photo-frame" + (" photo-frame--cutout" if cutout else "")
    st = []
    if ratio:
        st.append(f"aspect-ratio:{ratio}")
    if pos:
        st.append(f"object-position:{pos}")
    style = f' style="{";".join(st)}"' if st else ""
    return f'<img class="{cls}" src="images/{img}" alt="{alt}" width="{w}" height="{h}" loading="lazy"{style}>'


# --------------------------------------------------------------------------
# PAGES
#   class "rail"  = on phones the list becomes one horizontally swiping row (less vertical scrolling);
#                   on larger screens it stays a normal grid.
#   data-clamp    = on phones the paragraph shows 3 lines with a "Read more" toggle.
# --------------------------------------------------------------------------
def more(inner, label="I want to know more", chips=None):
    """Phones only: the content is folded away behind a button and folds itself again once the reader scrolls past it.
    Optional chips (a list of short names) are shown on phones while it is folded, as a one-glance summary.
    On larger screens everything is simply shown."""
    ch = ""
    if chips:
        ch = '<ul class="more__chips" aria-hidden="true">' + "".join(f"<li>{c}</li>" for c in chips) + "</ul>"
    return f'<div class="more" data-more="{label}">{ch}<div class="more__extra">{inner}</div></div>'


def rail(label):
    return f'rail" data-rail="{label}'


def body_home():
    slides = [
        ("p023-meditation-shore.webp", "50% 55%", "nourish-and-thrive.html", "Health first. Everything else follows."),
        ("p009-susan-table.webp", "50% 33%", "contact.html", "Whatever brought you here, you&rsquo;re in the right place"),
        ("p019-susan-speaking.webp", "50% 20%", "speaking-and-workshops.html", "Inspire, educate &amp; empower your audience"),
    ]
    sl = ""
    for i, (img, pos, href, cap) in enumerate(slides):
        act = " is-active" if i == 0 else ""
        sl += (f'<div class="hero__slide{act}" style="background-image:url(images/{img});background-position:{pos}">'
               f'<div class="hero__caption"><a href="{href}">{cap}</a></div></div>')
    dots = "".join(f'<button class="hero__dot" aria-label="Slide {i+1}" aria-current="{"true" if i == 0 else "false"}"></button>' for i in range(3))

    # Four tiles. Nourish & Thrive and Women Prosper carry their logos in place of an icon.
    tiles = (
        f'<a class="tile" href="contact.html"><span class="tile__icon">{si("calendar")}</span><h3 class="tile__title">Book a Consultation</h3></a>'
        '<a class="tile" href="nourish-and-thrive.html"><span class="tile__icon tile__icon--logo"><img src="images/logo-nourish-and-thrive.webp" alt="" width="72" height="72"></span><h3 class="tile__title">Nourish &amp; Thrive</h3></a>'
        '<a class="tile" href="women-prosper.html"><span class="tile__icon tile__icon--logo"><img src="images/logo-women-prosper.webp" alt="" width="72" height="72"></span><h3 class="tile__title">Women Prosper</h3></a>'
        f'<a class="tile" href="speaking-and-workshops.html"><span class="tile__icon">{si("mic")}</span><h3 class="tile__title">Speaking &amp; Workshops</h3></a>')

    top = f"""      <h1 class="visually-hidden">{ORG}: Nutrition &amp; Wellness Coach</h1>
      <section class="hero" data-hero aria-roledescription="carousel" aria-label="Featured">
        {sl}
        <div class="hero__dots">{dots}</div>
      </section>
      <section class="quick" aria-label="Quick links"><div class="quick__grid {rail("Quick links")}">{tiles}</div></section>"""

    welcome = section(f"""<div class="split">
          <div class="prose">
            <h2 class="heading-blue">Helping Women Build Healthier Lives, Stronger Confidence &amp; Greater Financial Freedom</h2>
            <p>Hello and Welcome. I am <span class="script">Susan Assy Tumuhairwe</span>, a CPD-Certified Nutrition and Wellness Coach, entrepreneur, and speaker. I am passionate about helping people live healthier, more fulfilling lives.</p>
            {more('<p>Through <strong>Nourish &amp; Thrive by Susan</strong>, I empower individuals, particularly women, to make informed health choices, build sustainable wellness habits, and take charge of their wellbeing through practical nutrition and lifestyle guidance.</p><p>Through <strong>Women Prosper</strong>, I inspire and empower women to explore entrepreneurship, develop their potential, and pursue financial independence.</p><p>As a speaker, I share practical insights on nutrition and wellness, personal development, women&rsquo;s empowerment, and entrepreneurship, inspiring individuals and communities to take positive steps towards lasting change.</p><p class="lede">My mission is simple: to educate, empower, and inspire people to nourish their health, grow their potential, and thrive in life.</p>', "Read more")}
            <div class="btn-row">
              {pill("Book a Consultation", "contact.html")}
              {pill("Explore the ventures", "#ventures", "blue", "arrow-right")}
            </div>
          </div>
          {photo("p003-susan-hero.webp", "Susan Tumuhairwe holding a large plate of fresh salad", 525, 786, ratio="1/1", cutout=True)}
        </div>""", first=True)

    quote = section(f"""<div class="panel-grey text-centre quote-panel">
          <h2 class="heading-blue hide-m">Health First. Everything Else Follows.</h2>
          <blockquote class="quote">&ldquo;Every woman deserves the opportunity to live a healthy, confident, and fulfilling life.&rdquo;</blockquote>
          <p class="quote__by">&mdash; {name_script()}</p>
        </div>""")

    ventures = section(heading("Three Ways We Can Work Together",
                               "Each venture carries its own identity, and its own doorway into a healthier, more confident, more prosperous life.") + more(f"""<div class="services {rail("Ventures")}">""" + service("p013-meal-tomato-egg.webp", "Plate of sliced tomato, avocado and boiled eggs", "Nourish &amp; Thrive",
                                           "Practical nutrition, healthy habits and personalised coaching for hormones, gut, metabolism, bones and healthy aging.",
                                           "leaf", "nourish-and-thrive.html", "Build lasting health", badge_logo="logo-nourish-and-thrive.webp")
                       + service("p024-women-team.webp", "Four women smiling together around a laptop in an office", "Women Prosper",
                                 "Build an additional income while growing in confidence and leadership, inside a community of women who lift each other up.",
                                 "sprout", "women-prosper.html", "Explore the opportunity", pos="50% 30%", badge_logo="logo-women-prosper.webp")
                       + service("p007-speaker-mic.webp", "Susan speaking with a microphone", "Speaking &amp; Workshops",
                                 "Sessions that inspire healthier living, stronger leadership and personal growth, tailored to your audience.",
                                 "mic", "speaking-and-workshops.html", "Book a session", cutout=True)
                       + "</div>", "Explore the three ventures"), sid="ventures")

    steps = section(heading("Small, Consistent Steps, Taken Together", "Three simple moves, from your first message to lasting change.") + more(f"""
        <div class="panel-plain"><div class="grid grid--3 {rail("How it works")}">""" +
                    infobox("chat", "Start the conversation", "Book a consultation and tell me where you are right now: your health, your goals, your challenges. I read every message myself.") +
                    infobox("edit", "Get a personalised plan", "No one-size-fits-all advice. Together we shape practical, evidence-informed strategies that fit your real, everyday life.") +
                    infobox("chart", "Build lasting change", "With encouragement and accountability, small choices become habits, and habits become energy, confidence and lasting wellbeing.") +
                    "</div></div>"))

    closing = cta_panel("Whether It&rsquo;s Your Health, a New Income, or Your Next Event, You&rsquo;re in the Right Place",
                        "Healthy living should be realistic, enjoyable and sustainable, not overwhelming. Let&rsquo;s take the first step together.",
                        pill("Book a Consultation", "contact.html") + pill("See how I coach", "nourish-and-thrive.html", "blue", "arrow-right"))
    return top + "\n" + welcome + "\n" + quote + "\n" + ventures + "\n" + steps + "\n" + closing


def body_nourish():
    intro = section(f"""<div class="split">
          <div class="prose">
            <h2 class="heading-blue">Helping Women Build Lasting Health</h2>
            <p>Good health is one of the greatest gifts you can give yourself and those you love: the energy to care for your family, chase your goals, and enjoy life to the fullest.</p>
            <div class="btn-row">
              {pill("Book a consultation", "contact.html?topic=coaching")}
              {pill("How I can help", "#areas", "blue", "arrow-right")}
            </div>
          </div>
          {photo("p009-susan-table.webp", "Susan Tumuhairwe at a table with a balanced meal and a warm drink", 1024, 1024, ratio="4/3", pos="50% 30%")}
        </div>""", first=True)

    approach = section(heading("Every Woman Is Different, and So Is Every Health Journey",
                               "I don&rsquo;t believe in one-size-fits-all nutrition advice. Lasting health isn&rsquo;t built through extreme diets or quick fixes. It grows from small, consistent choices.") + f"""
        """ + more(f"""<div class="grid grid--2 {rail("My approach")}">""" +
                       infobox("book", "Evidence-informed", "Recommendations grounded in current nutrition research, while staying practical, realistic and easy to apply.", "infobox--tint-blue") +
                       infobox("target", "Personalised", "Your body, lifestyle and goals are unique. Together we&rsquo;ll create an approach that works for you.", "infobox--tint-grey infobox--dark-icon") +
                       infobox("sprout", "Sustainable", "Rather than temporary solutions, we build healthy habits you can maintain for years to come.", "infobox--tint-grey infobox--dark-icon") +
                       infobox("heart", "Holistic", "Nutrition, movement, sleep, stress, mindset and relationships: I support the whole person, not just symptoms.", "infobox--tint-blue") +
                       "</div>"), sid="approach")

    ask = "contact.html?topic=coaching"
    areas = section(heading("Six Areas I Work in Most",
                            "Whatever brought you here, whether it&rsquo;s nutrition, a health condition, or simply feeling your best, I&rsquo;m here to guide and support you every step of the way.") + f"""
        """ + more(f"""<div class="services {rail("Areas I work in")}">""" +
                    service("p025-pregnancy-smile.webp", "Smiling expectant mother holding an ultrasound scan", "Hormonal Health",
                            "Hormones affect energy, mood, metabolism, fertility and sleep. I support women through every stage: PMS, PCOS, fertility, pregnancy, perimenopause and menopause.", "heart", ask, "Book a consultation", pos="50% 12%") +
                    service("p010-meal-salad-box.webp", "Lunch box of mixed salad with boiled egg and avocado", "Gut Health",
                            "A healthy gut is the foundation of good health: better digestion, less bloating, a stronger microbiome, and natural detoxification working well.", "leaf", ask, "Book a consultation") +
                    service("p026-waist-measure.webp", "Woman measuring her waist with a tape, with a healthy meal in front of her", "Metabolic Health",
                            "Healthy weight management, insulin resistance, type&nbsp;2 diabetes, blood pressure, fatty liver, cholesterol and low energy, through practical coaching.", "chart", ask, "Book a consultation", pos="50% 25%") +
                    service("p027-stretch-workout.webp", "Woman stretching on a mat at home, working out", "Bone &amp; Joint Health",
                            "Strong bones and healthy joints keep you active and independent, with habits that protect bone health and support mobility.", "shield-check", ask, "Book a consultation", pos="50% 50%") +
                    service("p020-susan-outdoors.webp", "Susan Tumuhairwe photographed outdoors", "Healthy Aging",
                            "Vitality, independence and quality of life as you grow older, through nourishing nutrition, regular movement, restorative sleep and preventive health.", "clock", ask, "Book a consultation", pos="50% 15%") +
                    service("p028-supplement.webp", "A hand holding a single phytonutrient supplement capsule", "Supplementation Guidance",
                            "Food comes first. But when age, stress, pregnancy or medication raise your needs, I help you choose supplements wisely, as a complement, never a replacement.", "book", ask, "Book a consultation", pos="50% 0%") +
                    "</div>", "I want to know more", chips=["Hormonal", "Gut", "Metabolic", "Bone &amp; joint", "Healthy aging", "Supplements"]), sid="areas")

    meals_data = [("p013-meal-tomato-egg", "Plate of sliced tomato, avocado and boiled eggs", "Tomato, avocado &amp; egg"),
                  ("p010-meal-salad-box", "Lunch box of mixed salad with boiled egg and avocado", "Mixed salad lunch box"),
                  ("p014-meal-beans-posho", "Plate of beans with posho and sliced avocado", "Beans, posho &amp; avocado"),
                  ("p011-meal-beans-veg", "Plate of beans with mixed vegetables and avocado", "Beans &amp; mixed vegetables"),
                  ("p016-meal-fish-plantain", "Fish stew with greens, plantain and avocado", "Fish stew &amp; plantain"),
                  ("p012-meal-breakfast", "Breakfast plate of banana, boiled egg, greens and groundnuts", "A balanced breakfast plate"),
                  ("p017-meal-fish-greens", "Plate of fish with greens and groundnuts", "Fish, greens &amp; groundnuts"),
                  ("p015-meal-pumpkin-tray", "Tray of pumpkin, beans and fresh tomato salad", "Pumpkin, beans &amp; tomato salad")]
    gal = "".join(f'<li class="gallery__item"><figure style="margin:0"><img src="images/{n}.webp" alt="{a}" loading="lazy" width="400" height="400"><figcaption class="gallery__cap">{c}</figcaption></figure></li>' for n, a, c in meals_data)
    meals = section(heading("This Is What Real Food Actually Looks Like",
                            "No extreme diets, no quick fixes: everyday meals built from food you already know, in balanced portions you can keep up.") +
                    more(f'<ul class="gallery rail rail--all" data-rail="Meals">{gal}</ul>', "Show me the meals"), sid="meals")

    stories = section(f"""<div class="split">
          {photo("p023-meditation-shore.webp", "Woman sitting in a calm meditation pose on the shore at sunrise", 1200, 801, ratio="4/3")}
          <div class="prose">
            <h2 class="heading-blue">Lasting Change Begins with Small, Consistent Steps</h2>
            <p>I&rsquo;m privileged to work with women who have transformed their health by improving their nutrition, building healthier habits and making sustainable lifestyle changes.</p>
            {more("<p>From increased energy and healthy weight loss to better management of chronic conditions and renewed confidence, these stories are a reminder that meaningful change is possible.</p>", "Read more")}
          </div>
        </div>""", sid="stories")

    closing = cta_panel("You Don&rsquo;t Have to Have Everything Figured Out Before You Begin",
                        "Lose weight, improve digestion, balance hormones, or manage a chronic condition: every journey begins with a single step. I&rsquo;ll bring the knowledge, tools, encouragement and accountability.",
                        pill("Book a consultation today", "contact.html?topic=coaching"))
    return intro + "\n" + approach + "\n" + areas + "\n" + meals + "\n" + stories + "\n" + closing


def body_prosper():
    intro = section(f"""<div class="split">
          <div class="prose">
            <h2 class="heading-blue">Build an Additional Income While Growing in Confidence and Leadership</h2>
            <p>Financial wellbeing opens doors: more choices, greater security, and the freedom to invest in yourself and support your family.</p>
            <div class="btn-row">
              {pill("Explore the opportunity", "contact.html?topic=prosper")}
              {pill("What you&rsquo;ll gain", "#gain", "blue", "arrow-right")}
            </div>
          </div>
          {photo("p022-susan-suit.webp", "Susan Tumuhairwe in a tailored suit, portrait", 880, 1100, ratio="4/4.2", pos="50% 15%")}
        </div>""", first=True)

    gain = section(f"""<div class="prose" style="max-width:820px;margin:0 auto">
          <h2 class="heading-blue heading-centre">More Than an Income: a Way to Grow</h2>
          <p>I founded Women Prosper as a community that empowers women to build an additional income while developing the confidence, skills and leadership needed to thrive. You&rsquo;ll find support, mentorship and encouragement here.</p>
        </div>
        """ + more(f"""<div class="panel-plain" style="margin-top:24px"><div class="grid grid--3 {rail("What you will find")}">""" +
                         infobox("lightbulb", "No experience needed", "Just a willingness to learn, grow and take action. Everything else can be taught.") +
                         infobox("users", "Real mentorship", "From someone who has built what she teaches.") +
                         infobox("heart", "A community", "That celebrates every win with you.") +
                         f"""</div></div>
        <div class="stack"><div class="grid grid--5 {rail("What you will gain")}">""" +
                         infobox("coins", "An Additional Income", "An extra source of income for your real goals: school fees, less financial pressure, savings for the future, or simply more freedom and flexibility.", "infobox--tint-blue") +
                         infobox("sprout", "Personal Growth", "Success begins with personal development: confidence, communication, a stronger mindset, and abilities you may never have realised you had.", "infobox--tint-grey infobox--dark-icon") +
                         infobox("users", "Leadership Skills", "Practical leadership for every area of life: inspiring others, building meaningful relationships, and leading with integrity at home and at work.", "infobox--tint-blue") +
                         infobox("heart", "A Supportive Community", "Success is easier when you don&rsquo;t do it alone: encouraging women who learn together, celebrate one another, and support each other at every stage.", "infobox--tint-grey infobox--dark-icon") +
                         infobox("target", "Purpose &amp; Impact", "As you grow, you help other women improve their health, confidence and financial wellbeing, an impact that reaches families and generations.", "infobox--tint-blue") +
                         "</div></div>", "I want to know more", chips=["No experience needed", "Mentorship", "Community", "Extra income", "Leadership"]), sid="gain")

    stories = section(f"""<div class="split">
          <div class="prose">
            <h2 class="heading-blue">Women Discovering Strengths They Never Knew They Had</h2>
            <p>Some have built an additional income. Others have grown in confidence, stepped into leadership, earned promotions, or found a community that believes in them.</p>
            {more("<p>Every story is unique, but they all show what&rsquo;s possible when women are equipped, encouraged and empowered to grow.</p>", "Read more")}
          </div>
          {photo("p018-susan-seated.webp", "Susan Tumuhairwe seated, photographed at an event", 592, 1000, ratio="4/3", pos="50% 55%")}
        </div>""", sid="stories")

    closing = cta_panel("Because When Women Prosper, Families Prosper, Communities Prosper, and Future Generations Benefit",
                        "If you&rsquo;re looking for an opportunity to earn an additional income inside a community that values growth, service and encouragement, I&rsquo;d love to help you explore what&rsquo;s possible.",
                        pill("Let&rsquo;s talk about it", "contact.html?topic=prosper"))
    return intro + "\n" + gain + "\n" + stories + "\n" + closing


def body_speaking():
    intro = section(f"""<div class="split">
          <div class="prose">
            <h2 class="heading-blue">Inspire, Educate &amp; Empower Your Audience</h2>
            <p>I partner with businesses, NGOs, churches, schools and community groups to deliver sessions that inspire healthier living, stronger leadership and personal growth.</p>
            <div class="btn-row">
              {pill("Book Susan to speak", "contact.html?topic=speaking")}
              {pill("Areas of expertise", "#expertise", "blue", "arrow-right")}
            </div>
          </div>
          {photo("p007-speaker-mic.webp", "Susan Tumuhairwe speaking with a microphone", 428, 429, ratio="4/3", cutout=True)}
        </div>""", first=True)

    expertise = section(heading("Six Sessions I&rsquo;m Asked for Most",
                                "Every session is tailored to your audience, combining evidence-informed knowledge with practical strategies participants can apply immediately.") + f"""
        """ + more(f'''<div class="grid grid--3 {rail("Session topics")}">''' +
                        session("users", "Workplace Health &amp; Wellbeing", "Help your team improve their health, energy, resilience and productivity. Healthy employees are more engaged and better equipped to perform at their best.", "p024-women-team.webp", "50% 30%", "#16381f", "#c9a24a") +
                        session("heart", "Women&rsquo;s Health", "Evidence-informed guidance on hormonal health, fertility, pregnancy, perimenopause and menopause, empowering women to make informed decisions.", "p025-pregnancy-smile.webp", "50% 20%", "#2f6b4f", "#d05a9e") +
                        session("clock", "Healthy Aging", "How nutrition, movement, sleep and other healthy habits help people maintain vitality, independence and quality of life as they grow older.", "p020-susan-outdoors.webp", "50% 35%", "#3f5a22", "#8aa64a") +
                        session("bowl", "Nutrition for Everyday Life", "Simple, practical advice that helps individuals and families make healthier food choices. No restrictive diets, no unrealistic expectations.", "p013-meal-tomato-egg.webp", "50% 50%", "#1e5a52", "#e6cd8a") +
                        session("sprout", "Leadership &amp; Personal Growth", "Strong leadership starts with personal growth: confidence, resilience, purpose, and influence that reaches workplaces and communities.", "p019-susan-speaking.webp", "30% 30%", "#2d6a3e", "#6fae85") +
                        session("shield-check", "Ethical Entrepreneurship", "How ethical leadership, genuine relationships and a service-first mindset create sustainable success, for entrepreneurs and teams building with integrity.", "p018-susan-seated.webp", "50% 55%", "#12301d", "#c9a24a") +
                        "</div>" + '''<div class="divider-label"><span>All sessions are customised to you, to be:</span></div>''' + f'''<div class="panel-plain"><div class="grid grid--2 {rail("How I speak")}">''' +
                        infobox("target", "Practical", "Simple and actionable strategies to implement immediately.") +
                        infobox("users", "Engaging", "Interactive, thought-provoking, built for participation.") +
                        infobox("book", "Evidence-informed", "Grounded in current nutrition, wellness and leadership principles.") +
                        infobox("edit", "Tailored", "Customised to your event&rsquo;s goals, audience and objectives.") +
                        "</div></div>", "I want to know more", chips=["Workplace wellbeing", "Women&rsquo;s health", "Healthy aging", "Everyday nutrition", "Leadership", "Ethical business"]), sid="expertise")

    feedback = section("""<div class="prose" style="max-width:820px;margin:0 auto">
          <h2 class="heading-blue heading-centre">The Real Measure Is the Impact on the People in the Room</h2>
          <p data-clamp>Corporate teams, community groups, churches, professional organisations: my goal is always the same, sessions people leave with valuable knowledge and tools they use long after the event.</p>
        </div>""", sid="feedback")

    closing = cta_panel("Planning a Conference, Wellness Programme, Retreat or Community Event?",
                        "I&rsquo;d be delighted to help create an experience that educates, inspires, and equips your audience with practical tools they&rsquo;ll use long after the session ends.",
                        pill("Discuss your next event", "contact.html?topic=speaking"))
    return intro + "\n" + expertise + "\n" + feedback + "\n" + closing


def body_contact():
    cards = (infobox("mail", "Email", f'<a href="mailto:{EMAIL}">{EMAIL}</a>', "infobox--tint-blue") +
             infobox("phone", "Phone / WhatsApp", f'<a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>', "infobox--tint-grey infobox--dark-icon") +
             infobox("pin", "Office", f'<a href="{MAPS}">{OFFICE}</a>', "infobox--tint-blue"))
    # icon() for phone/pin are filled glyphs; infobox() uses stroked icons, so fix those two
    cards = cards.replace(si("phone"), icon("phone")).replace(si("pin"), icon("pin"))
    form = f"""<form class="form" name="contact" method="POST" action="contact.html" data-netlify="true" netlify-honeypot="bot-field" novalidate data-contact-form data-success="Thank you. Your message has been sent, and I will reply personally.">
            <input type="hidden" name="form-name" value="contact">
            <p class="visually-hidden"><label>Leave this empty: <input name="bot-field" tabindex="-1" autocomplete="off"></label></p>
            <div class="form__row">
              <div class="form__field"><label class="form__label" for="cf-name">Your name</label>
                <input class="form__input" id="cf-name" name="name" type="text" autocomplete="name" required>
                <p class="form__error" hidden>Please tell me your name.</p></div>
              <div class="form__field"><label class="form__label" for="cf-email">Email address</label>
                <input class="form__input" id="cf-email" name="email" type="email" autocomplete="email" inputmode="email" required>
                <p class="form__error" hidden>Please enter a valid email address.</p></div>
            </div>
            <div class="form__field"><label class="form__label" for="cf-topic">I&rsquo;m interested in</label>
              <select class="form__select form__input" id="cf-topic" name="topic" data-query-select="topic">
                <option value="coaching">Health &amp; nutrition coaching (Nourish &amp; Thrive)</option>
                <option value="prosper">The Women Prosper opportunity</option>
                <option value="speaking">Speaking or a workshop</option>
                <option value="other">Something else</option>
              </select></div>
            <div class="form__field"><label class="form__label" for="cf-message">Message</label>
              <textarea class="form__textarea form__input" id="cf-message" name="message" rows="4" required></textarea>
              <p class="form__error" hidden>Please add a short message.</p></div>
            <div><button class="btn-pill btn-pill--orange" type="submit">Send message {si("arrow-right")}</button></div>
            <p class="form__status" role="status" aria-live="polite" data-form-status></p>
          </form>"""
    return section(f"""<div class="grid grid--2 contact-layout" style="gap:40px;align-items:start">
          <div>
            <div class="prose">
              <h2 class="heading-blue">Let&rsquo;s Start the Conversation</h2>
              <p>Tell me a little about where you are right now and what you would like to change. I read every message myself.</p>
              <ul class="hide-m">
                <li>One-to-one health and nutrition coaching</li>
                <li>The Women Prosper opportunity</li>
                <li>Speaking at your event or running a workshop</li>
              </ul>
            </div>
            <div class="grid {rail("Contact details")}" style="gap:16px;margin-top:24px">{cards}</div>
            <h3 class="contact-follow__title">Follow along</h3>
            <ul class="contact-follow">{"".join(f'<li><a href="{u}" target="_blank" rel="noopener">{soc(i)}<span><b>{n}</b>{hdl}</span></a></li>' for i, n, hdl, u in SOCIAL)}</ul>
          </div>
          <div class="panel-grey">{form}</div>
        </div>""", first=True)


# file, title, description, body, active nav label, banner tuple (title, crumbs, image) or None, preload, venture
PAGES = [
    ("index.html", "Susan Tumuhairwe | Nutrition & Wellness Coach",
     "Susan Tumuhairwe is a Nutrition & Wellness Coach, speaker, and founder of Nourish & Thrive and Women Prosper, helping women build healthier lives, stronger confidence and greater financial freedom.",
     body_home, "Home", None,
     '  <link rel="preload" as="image" href="images/p023-meditation-shore.webp" fetchpriority="high">\n', "susan"),
    ("nourish-and-thrive.html", "Nourish & Thrive",
     "Nutrition coaching for women: practical, evidence-informed, personalised and sustainable. Simple habits, real transformation.",
     body_nourish, "Nourish &amp; Thrive", ("Nourish &amp; Thrive", ["Nourish &amp; Thrive"], "banner-shore.jpg"), "", "nourish"),
    ("women-prosper.html", "Women Prosper",
     "Build an additional income while growing in confidence and leadership, inside a community of women who lift each other up.",
     body_prosper, "Women Prosper", ("Women Prosper", ["Women Prosper"], "banner-prosper.jpg"), "", "prosper"),
    ("speaking-and-workshops.html", "Speaking & Workshops",
     "Talks, workshops and training on healthy living, leadership and personal growth for businesses, NGOs, churches, schools and community groups.",
     body_speaking, "Speaking &amp; Workshops", ("Speaking &amp; Workshops", ["Speaking &amp; Workshops"], "banner-speaking.jpg"), "", "speaking"),
    ("contact.html", "Contact",
     "Book a consultation with Susan Tumuhairwe, or ask about the Women Prosper opportunity, speaking and workshops.",
     body_contact, "Contact", ("Contact", ["Contact"], "banner-shore.jpg"), "", "contact"),
]

# speaking and contact use the default (teal) theme
THEME_OF = {"speaking": "susan", "contact": "susan"}


def esc_attr(s):
    return s.replace('"', "&quot;").replace("&", "&amp;").replace("&amp;amp;", "&amp;")


def main():
    for fname, title, desc, fn, active, ban, pre, ven in PAGES:
        theme = THEME_OF.get(ven, ven)
        b = banner(ban[0], ban[1], ban[2], ven) if ban else ""
        html = page(fname, title.replace("&", "&amp;"), esc_attr(desc), fn(), active, b, preload=pre, venture=theme)
        with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
            f.write(html)
        print("wrote", fname)


if __name__ == "__main__":
    main()
