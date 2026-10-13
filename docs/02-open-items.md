# Open items before going live

1. **Contact details are placeholders**: `hello@susantumuhairwe.com`, `+256 700 000 000`. Set in `tools/build_site.py` (EMAIL, PHONE_*), rebuild.
2. **Netlify Forms**: submit a live test after the first deploy and confirm it appears in the dashboard.
3. **Domain**: `SITE_URL` and the `og:image` use the current netlify address. Update when the final domain is known. No `sitemap.xml` / `robots.txt` yet.
4. **Social links**: none exist yet; none were invented.
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
