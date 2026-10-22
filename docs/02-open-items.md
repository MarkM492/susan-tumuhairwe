# Open items before going live

1. **Contact details**: phone is now the real +256 784 717 586 and the office is Interservice Tower, Lumumba Avenue, Kampala (`PHONE_*`, `OFFICE`, `MAPS` in `tools/build_site.py`). The email `hello@susantumuhairwe.com` is still a placeholder: confirm the real address.
2. **Netlify Forms**: submit a live test after the first deploy and confirm it appears in the dashboard.
3. **Domain**: `SITE_URL` and the `og:image` use the current netlify address. Update when the final domain is known. No `sitemap.xml` / `robots.txt` yet.
4. **Social links**: handles supplied by Susan (Instagram @Susan_assy, TikTok @Susan_assy, TikTok @Women.Prosper5, Facebook "Susan Tumuhairwe"). The Instagram and TikTok links are built from those handles; **Facebook has no handle, so it links to a name search**. Replace `FB_URL` in `build_site.py` with her real profile or page link, and check the other three links open the right accounts.
5. **Backdrop**: flat pale green (no wide, calm photo available). A calm landscape could be set via `--backdrop-image` later.
6. **Images**: meal photos appear in both the service cards and the gallery; the studio photo (p021) has a strong purple background (greyscaled in the banner); a few originals are low-resolution.
7. **Copy**: fixed (duplicate "No experience needed" card removed from Women Prosper).
8. **Content omitted until real**: success stories, testimonials.
9. **Not built**: focus trap in the mobile drawer, site search.
10. **Nav font**: Roboto Condensed still loads from Google Fonts. Self-host it too if you want zero third-party requests.
11. **Accent sprinkles**: gold by default, olive on Nourish & Thrive, pink on Women Prosper. Change in `tokens.css` (bottom) if you want different accents.
12. **Frame width**: measured identical across pages; if Mark still sees a difference on a device, get the window width or a screenshot.
13. **Taglines in script**: the banner taglines for Speaking and Contact ("Healthy people build thriving organisations.", "I read every message myself.") and are written from her copy; adjust in `build_site.py` (`TAGLINES`).
14. **Tab bar logos** are small on phones (30px); the Nourish & Thrive logo is fine line art, so a simplified mark would read better at that size.
15. **Supplement photo** carries the text "The World's first phyto nutrient supplement since 1958". It is used as supplied; confirm Susan wants that claim on the site, or crop it out (see docs/01 phase 8).
