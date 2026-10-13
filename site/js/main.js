/* Skyline Blueprint: behaviours. Vanilla JS, no dependencies.
   Each block is independent and does nothing if its markup is absent. */
(function () {
  'use strict';
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---- Footer year ---- */
  $$('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* ---- Sticky header: fixes itself once the top bar has scrolled away ---- */
  var header = $('.header');
  if (header) {
    var spacer = document.createElement('div');
    spacer.className = 'header__spacer';
    header.parentNode.insertBefore(spacer, header.nextSibling);
    var stickAt = function () { var t = $('.topbar'); return t && t.offsetHeight ? t.offsetHeight + 40 : 40; };
    var onScroll = function () {
      var stuck = window.scrollY > stickAt();
      if (stuck !== header.classList.contains('is-stuck')) {
        header.classList.toggle('is-stuck', stuck);
        spacer.style.height = stuck ? header.offsetHeight + 'px' : '0';
      }
      var tt = $('.to-top');
      if (tt) tt.classList.toggle('is-visible', window.scrollY > 300);
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* ---- Back to top ---- */
  var toTop = $('.to-top');
  if (toTop) toTop.addEventListener('click', function () {
    window.scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' });
  });

  /* ---- Search overlay ---- */
  var overlay = $('.search-overlay');
  if (overlay) {
    var input = $('.search-overlay__input', overlay);
    var openSearch = function () { overlay.classList.add('is-open'); setTimeout(function () { input && input.focus(); }, 60); };
    var closeSearch = function () { overlay.classList.remove('is-open'); };
    $$('[data-search-open]').forEach(function (b) { b.addEventListener('click', openSearch); });
    $$('[data-search-close]').forEach(function (b) { b.addEventListener('click', closeSearch); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeSearch(); });
  }

  /* ---- Mobile drawer ---- */
  var toggleDrawer = function (open) { document.body.classList.toggle('drawer-open', open); };
  $$('[data-drawer-open]').forEach(function (b) { b.addEventListener('click', function () { toggleDrawer(true); }); });
  $$('[data-drawer-close]').forEach(function (b) { b.addEventListener('click', function () { toggleDrawer(false); }); });
  $$('.drawer__more').forEach(function (b) {
    b.addEventListener('click', function () {
      var li = b.closest('.drawer__item');
      var open = li.classList.toggle('is-open');
      b.setAttribute('aria-expanded', String(open));
    });
  });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') toggleDrawer(false); });

  /* ---- Pill tabs ---- */
  $$('[data-tabs]').forEach(function (root) {
    var tabs = $$('[role="tab"]', root);
    var pick = function (tab) {
      tabs.forEach(function (t) {
        var on = t === tab;
        t.setAttribute('aria-selected', String(on));
        t.tabIndex = on ? 0 : -1;
        var p = document.getElementById(t.getAttribute('aria-controls'));
        if (p) p.hidden = !on;
      });
    };
    tabs.forEach(function (t, i) {
      t.addEventListener('click', function () { pick(t); });
      t.addEventListener('keydown', function (e) {
        var n = e.key === 'ArrowRight' ? i + 1 : e.key === 'ArrowLeft' ? i - 1 : null;
        if (n === null) return;
        var next = tabs[(n + tabs.length) % tabs.length]; pick(next); next.focus();
      });
    });
  });

  /* ---- Accordion: one open at a time ---- */
  $$('[data-accordion]').forEach(function (root) {
    var heads = $$('.accordion__head', root);
    heads.forEach(function (h) {
      h.addEventListener('click', function () {
        var open = h.getAttribute('aria-expanded') === 'true';
        heads.forEach(function (o) {
          o.setAttribute('aria-expanded', 'false');
          document.getElementById(o.getAttribute('aria-controls')).hidden = true;
        });
        if (!open) {
          h.setAttribute('aria-expanded', 'true');
          document.getElementById(h.getAttribute('aria-controls')).hidden = false;
        }
      });
    });
  });

  /* ---- Hero slider: fade, auto-advance 6s, pauses on hover/focus ---- */
  $$('[data-hero]').forEach(function (hero) {
    var slides = $$('.hero__slide', hero), dots = $$('.hero__dot', hero), i = 0, timer;
    if (slides.length < 2) return;
    var show = function (n) {
      i = (n + slides.length) % slides.length;
      slides.forEach(function (s, k) { s.classList.toggle('is-active', k === i); });
      dots.forEach(function (d, k) { d.setAttribute('aria-current', String(k === i)); });
    };
    var play = function () { if (!reduce) { stop(); timer = setInterval(function () { show(i + 1); }, 6000); } };
    var stop = function () { clearInterval(timer); };
    dots.forEach(function (d, k) { d.addEventListener('click', function () { show(k); play(); }); });
    hero.addEventListener('mouseenter', stop); hero.addEventListener('mouseleave', play);
    hero.addEventListener('focusin', stop); hero.addEventListener('focusout', play);
    show(0); play();
  });

  /* ---- Scroll reveal (content stays visible if JS or IO is unavailable) ---- */
  var rev = $$('.reveal');
  if (rev.length && 'IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); } });
    }, { threshold: 0.12 });
    rev.forEach(function (el) { io.observe(el); });
  } else { rev.forEach(function (el) { el.classList.add('is-in'); }); }

  /* ---- File library: live filter ---- */
  $$('[data-filter-input]').forEach(function (inp) {
    var rows = $$(inp.getAttribute('data-filter-input') + ' tbody tr');
    inp.addEventListener('input', function () {
      var q = inp.value.trim().toLowerCase();
      rows.forEach(function (r) { r.hidden = q && r.textContent.toLowerCase().indexOf(q) === -1; });
    });
  });

  /* ---- Contact form: validate, then POST (Netlify Forms by default) ---- */
  $$('[data-contact-form]').forEach(function (form) {
    var status = $('[data-form-status]', form);
    var say = function (msg, cls) { if (status) { status.textContent = msg; status.className = 'form__status ' + (cls || ''); } };
    var fields = $$('[required]', form);
    var check = function (f) {
      var bad = !f.value.trim() || (f.type === 'email' && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(f.value.trim()));
      f.setAttribute('aria-invalid', String(bad));
      var err = f.parentNode.querySelector('.form__error'); if (err) err.hidden = !bad;
      return !bad;
    };
    /* Re-check live only once a field has been flagged. Checking on blur would hide the error text
       between mouse-down and mouse-up on the submit button, shifting it and swallowing the click. */
    fields.forEach(function (f) { f.addEventListener('input', function () { if (f.getAttribute('aria-invalid') === 'true') check(f); }); });
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var ok = fields.map(check).every(Boolean);
      if (!ok) { say('Please check the highlighted fields.', 'is-error'); var first = fields.find(function (f) { return f.getAttribute('aria-invalid') === 'true'; }); if (first) first.focus(); return; }
      var btn = $('button[type="submit"]', form); if (btn) btn.disabled = true;
      say('Sending...', '');
      fetch(form.getAttribute('data-endpoint') || '/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams(new FormData(form)).toString()
      }).then(function (r) {
        if (!r.ok) throw new Error('bad status');
        form.reset(); fields.forEach(function (f) { f.removeAttribute('aria-invalid'); });
        say(form.getAttribute('data-success') || 'Thank you. Your message has been sent.', 'is-ok');
      }).catch(function () {
        say(form.getAttribute('data-failure') || 'Sorry, your message could not be sent. Please try again or use the contact details on this page.', 'is-error');
      }).then(function () { if (btn) btn.disabled = false; });
    });
  });

  /* ---- Pre-select a form option from the URL: contact.html?topic=coaching ---- */
  $$('[data-query-select]').forEach(function (sel) {
    var v = new URLSearchParams(window.location.search).get(sel.getAttribute('data-query-select'));
    if (v && Array.prototype.some.call(sel.options, function (o) { return o.value === v; })) sel.value = v;
  });
})();
