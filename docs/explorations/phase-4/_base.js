/* SHOMEN — Phase 4 exploration script (shared by the variants; inlined into index.html later).
   nav overlay + scroll spy with a sliding dot + progress bar, reveal (IntersectionObserver) with
   type-on micro-labels, readout settle and tick flash, parallax fallback when scroll-driven
   animations are unsupported, inline product sheet (accordion or tabs), "ler mais" toggles,
   gallery dialog fallback. prefers-reduced-motion turns the motion off; everything still works. */
(function () {
  'use strict';
  var root = document.documentElement;
  root.classList.add('js');
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var fine = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  var sda = typeof CSS !== 'undefined' && CSS.supports && CSS.supports('animation-timeline: scroll()');
  if (sda && !reduce) {
    root.classList.add('sda');
    /* scroll-driven animations (Chromium, Safari 26+): hero parallax + slow zoom on the root scroll,
       the small statement/roster photos drift as they cross the viewport. Older browsers keep the JS parallax. */
    var st = document.createElement('style');
    st.textContent = 'html.sda .hero__photo img{animation:heroScroll linear both;animation-timeline:scroll(root);animation-range:0 100vh}' +
      'html.sda .statement .photo img,html.sda .row__thumb img{animation:viewDrift linear both;animation-timeline:view();animation-range:entry 0% exit 100%}';
    document.head.appendChild(st);
  }

  /* ---------- navigation ---------- */
  var toggle = document.querySelector('.nav__toggle');
  var menu = document.getElementById('nav-menu');
  function setMenu(open) {
    toggle.setAttribute('aria-expanded', String(open));
    menu.classList.toggle('is-open', open);
    root.classList.toggle('menu-open', open);
    toggle.querySelector('.nav__toggle-label').textContent = open ? 'Fechar' : 'Menu';
  }
  if (toggle && menu) {
    toggle.addEventListener('click', function () { setMenu(toggle.getAttribute('aria-expanded') !== 'true'); });
    menu.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', function () { setMenu(false); }); });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') { setMenu(false); toggle.focus(); }
    });
  }

  /* scroll spy: the key dot slides to the section in view */
  var spyLinks = Array.prototype.slice.call(document.querySelectorAll('[data-spy]'));
  var dot = document.querySelector('.nav__dot');
  var list = document.querySelector('.nav__list');
  function moveDot(a) {
    if (!dot || !list || !a) { return; }
    var r = a.getBoundingClientRect(), l = list.getBoundingClientRect();
    if (!r.width) { return; }
    var vertical = list.classList.contains('nav__list--rail');
    if (vertical) {
      dot.style.setProperty('--x', '0px');
      dot.style.setProperty('--y', (r.top - l.top + r.height / 2 - 3).toFixed(1) + 'px');
    } else {
      dot.style.setProperty('--x', (r.left - l.left + 14).toFixed(1) + 'px');
    }
  }
  function setSpy(id) {
    spyLinks.forEach(function (a) {
      if (a.getAttribute('data-spy') === id) { a.setAttribute('aria-current', 'true'); moveDot(a); } else { a.removeAttribute('aria-current'); }
    });
  }
  var spyTargets = {};
  spyLinks.forEach(function (a) {
    var id = a.getAttribute('data-spy');
    spyTargets[id] = id === 'top' ? document.querySelector('.hero') : document.getElementById(id);
  });
  if ('IntersectionObserver' in window) {
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) { return; }
        var id = Object.keys(spyTargets).find(function (k) { return spyTargets[k] === en.target; });
        if (id) { setSpy(id); }
      });
    }, { rootMargin: '-40% 0px -55% 0px', threshold: 0 });
    Object.keys(spyTargets).forEach(function (k) { if (spyTargets[k]) { spy.observe(spyTargets[k]); } });
  }
  window.addEventListener('resize', function () { moveDot(document.querySelector('[data-spy][aria-current="true"]')); });
  window.setTimeout(function () { moveDot(document.querySelector('[data-spy][aria-current="true"]')); }, 60);

  /* ---------- progress bar ---------- */
  var bar = document.querySelector('.progress');

  /* ---------- reveal: rise/slide once, then type-on, settle, tick flash ---------- */
  var revealEls = document.querySelectorAll('[data-reveal]');
  var hero = document.querySelector('.hero');
  function enter(el) {
    el.classList.add('is-in');
    settle(el);
    typeOn(el);
    flash(el);
  }
  function showAll() {
    revealEls.forEach(function (el) { el.classList.add('is-in'); });
    if (hero) { hero.classList.add('is-in'); }
  }
  if (reduce || !('IntersectionObserver' in window)) {
    showAll();
  } else {
    window.setTimeout(function () { if (hero) { hero.classList.add('is-in'); } }, 40);
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { enter(en.target); io.unobserve(en.target); }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -5% 0px' });
    revealEls.forEach(function (el) { io.observe(el); });
  }

  /* readout digits settle: cycle random digits briefly before showing the real value (700 ms) */
  function settle(scope) {
    if (reduce) { return; }
    scope.querySelectorAll('[data-settle]').forEach(function (el) {
      if (el.dataset.settled) { return; }
      el.dataset.settled = '1';
      var final = el.textContent;
      var start = performance.now();
      var dur = 700;
      (function tick(now) {
        var t = (now - start) / dur;
        if (t >= 1) { el.textContent = final; return; }
        el.textContent = final.replace(/\d/g, function (d, i) {
          return (i / final.length) < t ? d : String(Math.floor(Math.random() * 10));
        });
        window.requestAnimationFrame(tick);
      })(start);
    });
  }

  /* micro-labels type on: characters appear left to right with a mono cursor (≤ 600 ms).
     The label keeps its final width so nothing around it moves; text is never distorted. */
  function typeOn(scope) {
    if (reduce) { return; }
    var els = scope.matches('[data-type]') ? [scope] : Array.prototype.slice.call(scope.querySelectorAll('[data-type]'));
    els.forEach(function (el) {
      if (el.dataset.typed) { return; }
      el.dataset.typed = '1';
      var nodes = [];
      (function walk(n) {
        n.childNodes.forEach(function (c) {
          if (c.nodeType === 3 && c.nodeValue.trim()) { nodes.push({ node: c, text: c.nodeValue }); }
          else if (c.nodeType === 1) { walk(c); }
        });
      })(el);
      var total = nodes.reduce(function (s, n) { return s + n.text.length; }, 0);
      if (!total) { return; }
      el.style.minWidth = el.getBoundingClientRect().width.toFixed(1) + 'px';
      el.classList.add('is-typing');
      var dur = Math.min(600, 22 * total);
      var start = performance.now();
      (function tick(now) {
        var t = Math.min(1, (now - start) / dur);
        var shown = Math.floor(t * total), acc = 0;
        nodes.forEach(function (n) {
          var k = Math.max(0, Math.min(n.text.length, shown - acc));
          n.node.nodeValue = n.text.slice(0, k);
          acc += n.text.length;
        });
        if (t < 1) { window.requestAnimationFrame(tick); }
        else { window.setTimeout(function () { el.classList.remove('is-typing'); el.style.minWidth = ''; }, 350); }
      })(start);
    });
  }

  /* panels enter with a short tick flash (the corner ticks turn the key colour for ~150 ms) */
  function flash(scope) {
    if (reduce) { return; }
    var els = scope.matches('.panel') ? [scope] : Array.prototype.slice.call(scope.querySelectorAll('.panel'));
    els.forEach(function (p, i) {
      window.setTimeout(function () {
        p.classList.add('is-flash');
        window.setTimeout(function () { p.classList.remove('is-flash'); }, 150);
      }, 120 + i * 60);
    });
  }

  /* ---------- parallax (JS fallback; scroll-driven CSS takes over when supported) ---------- */
  var plx = Array.prototype.slice.call(document.querySelectorAll('[data-parallax]'));
  var ticking = false;
  function onScroll() {
    if (ticking) { return; }
    ticking = true;
    window.requestAnimationFrame(function () {
      var vh = window.innerHeight;
      var doc = root.scrollHeight - vh;
      if (bar) { bar.style.transform = 'scaleX(' + (doc > 0 ? window.scrollY / doc : 0) + ')'; }
      if (!reduce && !sda) {
        plx.forEach(function (el) {
          var r = el.getBoundingClientRect();
          if (r.bottom < -200 || r.top > vh + 200) { return; }
          var f = parseFloat(el.getAttribute('data-parallax')) || 0.1;
          var y = el.classList.contains('hero__photo') ? window.scrollY * f : ((r.top + r.height / 2) - vh / 2) * -f;
          el.style.setProperty('--py', y.toFixed(1) + 'px');
        });
      }
      ticking = false;
    });
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll);
  onScroll();

  /* mouse tilt on the hero photo (pointer devices only) */
  var mouseEl = document.querySelector('[data-mouse]');
  if (mouseEl && hero && fine && !reduce) {
    hero.addEventListener('mousemove', function (e) {
      var r = hero.getBoundingClientRect();
      var x = (e.clientX - r.left) / r.width - 0.5;
      var y = (e.clientY - r.top) / r.height - 0.5;
      mouseEl.style.setProperty('--mx', (x * -14).toFixed(1));
      mouseEl.style.setProperty('--my', (y * -10).toFixed(1));
    });
    hero.addEventListener('mouseleave', function () {
      mouseEl.style.setProperty('--mx', '0');
      mouseEl.style.setProperty('--my', '0');
    });
  }

  /* ---------- generic "ler mais" / "+ n" toggles ---------- */
  document.querySelectorAll('[data-toggle]').forEach(function (b) {
    var target = document.getElementById(b.getAttribute('data-toggle'));
    if (!target) { return; }
    var labels = (b.getAttribute('data-labels') || '').split('|');
    b.addEventListener('click', function () {
      var open = b.getAttribute('aria-expanded') !== 'true';
      b.setAttribute('aria-expanded', String(open));
      target.classList.toggle('is-open', open);
      if (open) { target.removeAttribute('hidden'); settle(target); } else { window.setTimeout(function () { if (!target.classList.contains('is-open')) { target.setAttribute('hidden', ''); } }, reduce ? 0 : 500); }
      if (labels.length === 2 && b.querySelector('span')) { b.querySelector('span').textContent = open ? labels[1] : labels[0]; }
      var row = b.closest('.panel');
      if (row) { row.classList.toggle('is-active', open); }
    });
  });

  /* ---------- inline sheets (products: accordion or tabs; also reused for athlete tabs) ---------- */
  function initSheet(sheet) {
    var mode = sheet.getAttribute('data-mode') || 'accordion';
    var products = Array.prototype.slice.call(sheet.querySelectorAll('.product'));
    var ids = products.map(function (p) { return p.getAttribute('data-id'); });
    var btns = Array.prototype.slice.call(document.querySelectorAll('[data-product]')).filter(function (b) { return ids.indexOf(b.getAttribute('data-product')) !== -1; });
    var current = null;
    function scrollToSheet(btn) {
      var navH = parseFloat(getComputedStyle(root).getPropertyValue('--nav-h')) || 60;
      var top = sheet.getBoundingClientRect().top + window.scrollY - navH - 12;
      var tileTop = btn.getBoundingClientRect().top + window.scrollY - navH - 12;
      if (window.innerWidth < 720) { window.scrollTo({ top: Math.min(top, tileTop + window.innerHeight * 0.4), behavior: reduce ? 'auto' : 'smooth' }); }
    }
    function set(id, btn, viaUser) {
      btns.forEach(function (b) {
        var on = b.getAttribute('data-product') === id;
        b.setAttribute('aria-expanded', String(on));
        var holder = b.closest('.tile, .panel');
        if (holder) { holder.classList.toggle('is-active', on); }
      });
      products.forEach(function (p) {
        var on = p.getAttribute('data-id') === id;
        p.classList.toggle('is-active', on);
        if (on) { p.removeAttribute('hidden'); } else { p.setAttribute('hidden', ''); }
      });
      current = id;
      sheet.classList.toggle('is-open', !!id);
      sheet.setAttribute('aria-hidden', id ? 'false' : 'true');
      if (id && viaUser) {
        var p = sheet.querySelector('.product.is-active');
        flash(p); settle(p);
        if (btn) { scrollToSheet(btn); }
        if (sheet.getAttribute('data-group') !== 'athletes' && history.replaceState) { history.replaceState(null, '', '#p-' + id); }
      } else if (!id && history.replaceState && /^#p-/.test(window.location.hash)) { history.replaceState(null, '', window.location.pathname + window.location.search); }
    }
    function focusBtn(id) {
      var t = btns.filter(function (x) { return x.getAttribute('data-product') === id; })[0];
      if (t) { t.focus(); }
      return t;
    }
    btns.forEach(function (b) {
      b.addEventListener('click', function () {
        var id = b.getAttribute('data-product');
        if (mode === 'accordion' && current === id) { set(null, b, true); b.focus(); return; }
        set(id, b, true);
      });
    });
    sheet.querySelectorAll('[data-close-product]').forEach(function (b) {
      b.addEventListener('click', function () {
        if (mode === 'tabs') { return; }
        var id = current;
        set(null, null, true);
        var t = focusBtn(id);
        if (t) { t.scrollIntoView({ block: 'center', behavior: reduce ? 'auto' : 'smooth' }); }
      });
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && mode === 'accordion' && current && !document.querySelector('dialog[open]') && !root.classList.contains('menu-open')) {
        var id = current;
        set(null, null, true);
        focusBtn(id);
      }
    });
    /* thumbnails crossfade the main image */
    products.forEach(function (p) {
      var main = p.querySelector('[data-main] img');
      var link = p.querySelector('[data-main-link]');
      var thumbs = p.querySelectorAll('.thumbs button');
      thumbs.forEach(function (b) {
        b.addEventListener('click', function () {
          if (!main) { return; }
          thumbs.forEach(function (o) { o.removeAttribute('aria-current'); });
          b.setAttribute('aria-current', 'true');
          var fig = main.parentNode;
          fig.classList.add('is-swapping');
          window.setTimeout(function () {
            main.src = b.getAttribute('data-src');
            main.alt = b.getAttribute('data-alt') || '';
            main.classList.toggle('pos-top', b.querySelector('img').classList.contains('pos-top'));
            if (link) { link.href = b.getAttribute('data-full'); }
            main.addEventListener('load', function done() { fig.classList.remove('is-swapping'); main.removeEventListener('load', done); });
            window.setTimeout(function () { fig.classList.remove('is-swapping'); }, 600);
          }, reduce ? 0 : 200);
        });
      });
    });
    /* initial state: deep link #p-kit, else tabs open the first item, accordion stays closed */
    var deep = /^#p-(.+)$/.exec(window.location.hash);
    var initial = null;
    if (deep && ids.indexOf(deep[1]) !== -1) { initial = deep[1]; }
    else if (mode === 'tabs' && ids.length) { initial = ids[0]; }
    sheet.style.transition = 'none';
    set(initial, null, false);
    window.setTimeout(function () { sheet.style.transition = ''; }, 50);
  }
  document.querySelectorAll('.sheet').forEach(initSheet);

  /* ---------- gallery dialog: "ver galeria completa" clones the product's full thumbnail set ---------- */
  var gallery = document.getElementById('galeria');
  var supportsDialog = typeof HTMLDialogElement === 'function';
  var lastTrigger = null;
  function closeGallery() {
    if (!gallery) { return; }
    if (supportsDialog && gallery.open) { gallery.close(); } else { gallery.removeAttribute('open'); }
  }
  if (gallery) {
    var grid = gallery.querySelector('.modal__grid');
    var title = gallery.querySelector('[data-gallery-title]');
    document.querySelectorAll('[data-gallery]').forEach(function (b) {
      b.addEventListener('click', function () {
        var p = b.closest('.product');
        if (!p || !grid) { return; }
        grid.innerHTML = '';
        p.querySelectorAll('.thumbs button').forEach(function (t) {
          var li = document.createElement('li');
          var a = document.createElement('a');
          a.href = t.getAttribute('data-full');
          a.setAttribute('rel', 'noopener');
          var f = document.createElement('span'); f.className = 'photo';
          var im = t.querySelector('img').cloneNode(false);
          im.alt = t.getAttribute('data-alt') || '';
          im.loading = 'lazy';
          f.appendChild(im); a.appendChild(f); li.appendChild(a); grid.appendChild(li);
        });
        if (title) { title.textContent = p.querySelector('.product__name').textContent; }
        lastTrigger = b;
        if (supportsDialog) { gallery.showModal(); } else { gallery.setAttribute('open', ''); }
        root.classList.add('modal-open');
        gallery.scrollTop = 0;
        var first = gallery.querySelector('[data-close]');
        if (first) { first.focus({ preventScroll: true }); }
      });
    });
    gallery.querySelectorAll('[data-close]').forEach(function (b) { b.addEventListener('click', closeGallery); });
    gallery.addEventListener('click', function (e) { if (e.target === gallery) { closeGallery(); } });
    gallery.addEventListener('close', function () { root.classList.remove('modal-open'); if (lastTrigger) { lastTrigger.focus({ preventScroll: true }); lastTrigger = null; } });
  }
})();
