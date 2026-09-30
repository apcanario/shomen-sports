/* Shomen HUD — Phase 2 script.
   1. Mobile navigation overlay toggle.
   2. Restrained motion: load stagger for [data-reveal="load"], one-time scroll reveal
      for [data-reveal="scroll"]. prefers-reduced-motion disables all of it.
   Nothing else. No parallax, no marquee, no counters, no typewriter. */
(function () {
  'use strict';
  var root = document.documentElement;
  root.classList.add('js');

  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- navigation ---------- */
  var toggle = document.querySelector('.nav__toggle');
  var menu = document.getElementById('nav-menu');
  if (toggle && menu) {
    var setOpen = function (open) {
      toggle.setAttribute('aria-expanded', String(open));
      menu.classList.toggle('is-open', open);
      root.classList.toggle('menu-open', open);
      toggle.querySelector('.nav__toggle-label').textContent = open ? 'Fechar' : 'Menu';
    };
    toggle.addEventListener('click', function () {
      setOpen(toggle.getAttribute('aria-expanded') !== 'true');
    });
    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
        setOpen(false);
        toggle.focus();
      }
    });
    menu.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () { setOpen(false); });
    });
  }

  /* ---------- reveal ---------- */
  var loadEls = document.querySelectorAll('[data-reveal="load"]');
  var scrollEls = document.querySelectorAll('[data-reveal="scroll"]');
  var showAll = function () {
    loadEls.forEach(function (el) { el.classList.add('is-in'); });
    scrollEls.forEach(function (el) { el.classList.add('is-in'); });
  };

  if (reduce || !('IntersectionObserver' in window)) {
    showAll();
    return;
  }

  loadEls.forEach(function (el, i) {
    el.style.transitionDelay = (i * 120) + 'ms';
  });
  window.requestAnimationFrame(function () {
    window.requestAnimationFrame(function () {
      loadEls.forEach(function (el) { el.classList.add('is-in'); });
    });
  });

  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-in');
        io.unobserve(entry.target);
      }
    });
  }, { threshold: 0.2, rootMargin: '0px 0px -5% 0px' });
  scrollEls.forEach(function (el) { io.observe(el); });
})();
