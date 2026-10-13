/* Susan Tumuhairwe: client behaviours (kept apart from the blueprint's main.js).
   1. Rails: ".rail" lists swipe sideways on phones; ".rail--all" (gallery) swipes at every width.
      Adds dots (phones) and arrows (larger screens) and keeps them in step with the scroll position.
   2. Read more / "I want to know more": folded content on phones that folds itself again once scrolled past. */
(function () {
  'use strict';
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var phone = window.matchMedia('(max-width: 767px)');
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---- 1. rails ---- */
  var arrowIcon = '<svg class="icon icon--stroke" aria-hidden="true"><use href="#i-arrow-right"></use></svg>';
  $$('.rail').forEach(function (rail) {
    var label = rail.getAttribute('data-rail') || 'List';
    rail.setAttribute('role', 'group');
    rail.setAttribute('aria-label', label + ' (swipe sideways)');
    rail.setAttribute('tabindex', '0');
    var items = Array.prototype.slice.call(rail.children);
    var always = rail.classList.contains('rail--all');

    // dots (phones)
    var dots = document.createElement('div');
    dots.className = 'rail-dots'; dots.setAttribute('aria-hidden', 'true');
    items.forEach(function (it, i) {
      var b = document.createElement('button'); b.type = 'button'; b.tabIndex = -1; b.setAttribute('aria-label', 'Go to item ' + (i + 1));
      b.addEventListener('click', function () { rail.scrollTo({ left: it.offsetLeft - rail.offsetLeft - parseFloat(getComputedStyle(rail).paddingLeft || 0), behavior: reduce ? 'auto' : 'smooth' }); });
      dots.appendChild(b);
    });

    // wrapper (needed for the arrows)
    var wrap = rail;
    if (always) {
      wrap = document.createElement('div'); wrap.className = 'rail-wrap';
      rail.parentNode.insertBefore(wrap, rail); wrap.appendChild(rail);
      ['prev', 'next'].forEach(function (d) {
        var a = document.createElement('button'); a.type = 'button'; a.className = 'rail-arrow rail-arrow--' + d;
        a.setAttribute('aria-label', d === 'prev' ? 'Previous' : 'Next'); a.innerHTML = arrowIcon;
        a.addEventListener('click', function () {
          var step = (items[1] ? items[1].offsetLeft - items[0].offsetLeft : rail.clientWidth) * (rail.clientWidth > 700 ? 3 : 1);
          rail.scrollBy({ left: d === 'prev' ? -step : step, behavior: reduce ? 'auto' : 'smooth' });
        });
        wrap.appendChild(a);
      });
    }
    wrap.parentNode.insertBefore(dots, wrap.nextSibling);

    var update = function () {
      var max = rail.scrollWidth - rail.clientWidth;
      var overflow = max > 4;
      wrap.classList && wrap.classList.toggle('has-overflow', overflow && always);
      dots.style.display = overflow && phone.matches ? '' : 'none';
      var idx = 0, best = 1e9;
      items.forEach(function (it, i) { var d = Math.abs(it.offsetLeft - rail.offsetLeft - rail.scrollLeft - parseFloat(getComputedStyle(rail).paddingLeft || 0)); if (d < best) { best = d; idx = i; } });
      if (rail.scrollLeft >= max - 4) idx = items.length - 1;
      $$('button', dots).forEach(function (b, i) { b.setAttribute('aria-current', String(i === idx)); });
      if (always) {
        var p = wrap.querySelector('.rail-arrow--prev'), n = wrap.querySelector('.rail-arrow--next');
        if (p) p.disabled = rail.scrollLeft <= 4; if (n) n.disabled = rail.scrollLeft >= max - 4;
      }
    };
    rail.addEventListener('scroll', function () { window.requestAnimationFrame(update); }, { passive: true });
    window.addEventListener('resize', update);
    window.addEventListener('load', update);
    update();
  });

  /* ---- 2. Read more / "I want to know more" (phones only) ----
     Long paragraphs ([data-clamp]) and card groups (.more) are folded away behind a button.
     Once opened, an item folds itself again as soon as the reader has scrolled past it (its button, which sits at
     its foot, rises above an edge just under the sticky header). Folding happens above the reader's view, so the
     scroll position is corrected to keep whatever they are reading exactly where it was. */
  var items3 = [], seq = 0;
  var tellRails = function () { window.dispatchEvent(new Event('resize')); };

  var register = function (root, btn, getOpen, setOpenState, labelClosed) {
    var it = { root: root, btn: btn, open: false, labelClosed: labelClosed };
    it.set = function (open) {
      it.open = open; setOpenState(open);
      btn.setAttribute('aria-expanded', String(open));
      var l = btn.querySelector('.more__label') || btn; l.textContent = open ? 'Show less' : labelClosed;
      if (open) window.requestAnimationFrame(tellRails);
    };
    it.fold = function () {            // fold without moving what the reader is looking at
      var before = btn.getBoundingClientRect().bottom;
      it.set(false);
      var after = btn.getBoundingClientRect().bottom;
      if (after !== before) window.scrollBy({ top: after - before, left: 0, behavior: 'instant' });
    };
    btn.addEventListener('click', function () { if (it.open) it.fold(); else it.set(true); });
    items3.push(it); return it;
  };

  $$('.more').forEach(function (root) {
    var extra = root.querySelector('.more__extra'); if (!extra) return;
    if (!extra.id) extra.id = 'more-' + (++seq);
    var b = document.createElement('button');
    b.type = 'button'; b.className = 'more__btn'; b.setAttribute('aria-controls', extra.id); b.setAttribute('aria-expanded', 'false');
    b.innerHTML = '<span class="more__label"></span>';
    root.appendChild(b);
    var label = root.getAttribute('data-more') || 'I want to know more';
    var it = register(root, b, null, function (open) { root.classList.toggle('is-open', open); }, label);
    b.querySelector('.more__label').textContent = label;
  });

  $$('[data-clamp]').forEach(function (p) {
    var b = document.createElement('button');
    b.type = 'button'; b.className = 'clamp-toggle'; b.textContent = 'Read more'; b.setAttribute('aria-expanded', 'false');
    p.parentNode.insertBefore(b, p.nextSibling);
    register(p, b, null, function (open) { p.classList.toggle('is-open', open); }, 'Read more');
    var fit = function () {
      if (!phone.matches) { b.hidden = true; return; }
      var open = p.classList.contains('is-open');
      b.hidden = !open && p.scrollHeight <= p.clientHeight + 2;
    };
    window.addEventListener('resize', fit); window.addEventListener('load', fit); fit();
  });

  var edge = function () { var h = document.querySelector('.header'); return (h ? h.offsetHeight : 62) + 24; };
  var ticking = false;
  var watch = function () {
    ticking = false;
    if (!phone.matches) return;
    var line = edge();
    items3.forEach(function (it) { if (it.open && it.btn.getBoundingClientRect().bottom < line) it.fold(); });
  };
  window.addEventListener('scroll', function () { if (!ticking) { ticking = true; window.requestAnimationFrame(watch); } }, { passive: true });

  /* ---- 3. Scroll-in animation (the way vce-environment.com does it: fade up, slide in from the side, staggered) ----
     Elements are tagged here, so the markup stays clean. Each one eases in the first time it scrolls into view and
     the tag is removed afterwards, so hover effects behave normally. Nothing animates for reduced-motion readers,
     and without JavaScript everything is simply visible. */
  if (!reduce && 'IntersectionObserver' in window) {
    var tagged = [];
    var tag = function (el, kind, delay) {
      if (!el || el.classList.contains('anim') || el.closest('.anim')) return;
      if (phone.matches && el.closest('.more__extra')) return;      // folded content has its own opening animation
      el.classList.add('anim', 'anim--' + kind);
      el.style.setProperty('--anim-delay', (delay || 0).toFixed(2) + 's');
      tagged.push(el);
    };
    var seq = function (list, kind, base, step) {
      list.forEach(function (el, i) { tag(el, kind, base + Math.min(i, 6) * step); });
    };
    var each = function (sel, fn) { $$(sel).forEach(fn); };

    // banner titles arrive on load, one line after another
    each('.banner__text', function (b) { seq(Array.prototype.slice.call(b.children), 'up', 0.05, 0.14); });
    each('.banner__emblem', function (e) { tag(e, 'zoom', 0.25); });
    // whole panels first, so their contents are not animated a second time
    each('.panel-grey, .cta, .quote-panel', function (el) { tag(el, 'up', 0); });
    // text blocks: heading, copy, buttons one after another
    each('.prose, .section-intro', function (b) { seq(Array.prototype.slice.call(b.children), 'up', 0, 0.13); });
    each('main > section > .heading-blue, main > section > .heading-centre', function (h) { tag(h, 'up', 0); });
    // photos slide in from the side they sit on
    each('.split', function (sp) {
      var img = sp.querySelector(':scope > img'); if (!img) return;
      var last = sp.lastElementChild === img;
      tag(img, phone.matches ? 'up' : (last ? 'right' : 'left'), 0.1);
    });
    // card groups: on phones the swipe row arrives as one piece, elsewhere the cards stagger
    ['.rail', '.gallery'].forEach(function (sel) {
      each(sel, function (r) {
        if (phone.matches || r.classList.contains('rail--all')) { tag(r.closest('.rail-wrap') || r, 'up', 0.05); return; }
        seq(Array.prototype.slice.call(r.children), 'up', 0.05, 0.16);
      });
    });
    each('.quick__grid', function (g) { if (!g.classList.contains('anim')) seq(Array.prototype.slice.call(g.children), 'up', 0, 0.14); });
    each('.footer__grid > div', function (d, i) { tag(d, 'up', i * 0.14); });
    each('.form, .contact-layout > div', function (el, i) { tag(el, 'up', i * 0.14); });

    var settle = function (el) {                     // restore normal hover behaviour once the entrance is over
      var d = parseFloat(el.style.getPropertyValue('--anim-delay')) || 0;
      window.setTimeout(function () {
        el.classList.remove('anim', 'anim--up', 'anim--right', 'anim--left', 'anim--zoom', 'is-in');
        el.style.removeProperty('--anim-delay');
      }, (d + 1.1) * 1000 + 150);
    };
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        io.unobserve(e.target);
        e.target.classList.add('is-in');
        settle(e.target);
      });
    }, { threshold: 0, rootMargin: '0px 0px -9% 0px' });
    tagged.forEach(function (el) { io.observe(el); });
  }
})();
