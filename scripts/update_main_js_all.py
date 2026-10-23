with open('static/js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Update initPageTransitions
old_transitions = """function initPageTransitions() {
  const overlay = document.getElementById('page-transition-overlay');
  if (!overlay) return;

  // On page load arrival: fade out overlay smoothly
  overlay.classList.remove('active', 'animating');

  // Handle bfcache page restore (Back/Forward navigation)
  window.addEventListener('pageshow', (event) => {
    overlay.classList.remove('active', 'animating');
  });

  // Allow clicking overlay to skip transition immediately
  overlay.addEventListener('click', () => {
    const pendingHref = overlay.getAttribute('data-target-href');
    if (pendingHref) window.location.href = pendingHref;
  });

  // Intercept internal links for seamless MRT transition
  document.querySelectorAll('a[href]').forEach(link => {
    const href = link.getAttribute('href');
    const target = link.getAttribute('target');
    
    // Ignore external links, downloads, anchors on the same page, or special links
    if (!href || href.startsWith('http') || href.startsWith('#') || href.startsWith('mailto:') || href.startsWith('tel:') || target === '_blank' || link.hasAttribute('download')) {
      return;
    }

    link.addEventListener('click', (e) => {
      // Check reduced motion preference
      if (document.body.classList.contains('reduced-motion')) {
        return; // Allow instant default navigation
      }

      // Allow middle click or ctrl/cmd click to open in new tab
      if (e.metaKey || e.ctrlKey || e.button !== 0) return;

      e.preventDefault();

      // Determine destination label
      let destText = 'Perjalanan Berikutnya';
      if (href === '/') destText = 'Stasiun Beranda';
      else if (href.startsWith('/karya/')) destText = 'Stasiun Studi Kasus';
      else if (href.startsWith('/karya')) destText = 'Stasiun Katalog Karya';
      else if (href.startsWith('/cv')) destText = 'Stasiun CV Interaktif';
      else if (href.startsWith('/admin')) destText = 'Stasiun Panel Admin';

      const board = overlay.querySelector('.mrt-dest-name');
      if (board) board.textContent = destText;

      // Update dynamic fun fact from Mirza's authentic profile
      const factEl = overlay.querySelector('#mrt-fact-text') || overlay.querySelector('.mrt-fact-text');
      if (factEl && MIRZA_TRANSIT_FACTS.length) {
        const randomIndex = Math.floor(Math.random() * MIRZA_TRANSIT_FACTS.length);
        factEl.textContent = MIRZA_TRANSIT_FACTS[randomIndex];
      }

      overlay.setAttribute('data-target-href', href);
      overlay.classList.add('active', 'animating');

      // Allow train to glide majestically across the screen before page route occurs
      setTimeout(() => {
        window.location.href = href;
      }, 850);
    });
  });
}"""

new_transitions = """function initPageTransitions() {
  const overlay = document.getElementById('page-transition-overlay');
  if (!overlay) return;

  // On page load arrival: fade out overlay smoothly
  overlay.classList.remove('active', 'animating');

  // Handle bfcache page restore (Back/Forward navigation)
  window.addEventListener('pageshow', (event) => {
    overlay.classList.remove('active', 'animating');
  });

  // Allow clicking overlay to skip transition immediately
  overlay.addEventListener('click', () => {
    const pendingHref = overlay.getAttribute('data-target-href');
    if (pendingHref) window.location.href = pendingHref;
  });

  // Intercept internal links for seamless MRT transition
  document.querySelectorAll('a[href]').forEach(link => {
    const href = link.getAttribute('href');
    const target = link.getAttribute('target');
    
    // Ignore external links, downloads, anchors on the same page, or special links
    if (!href || href.startsWith('http') || href.startsWith('#') || href.startsWith('mailto:') || href.startsWith('tel:') || target === '_blank' || link.hasAttribute('download')) {
      return;
    }

    // EXCLUDE CATALOG FILTER TABS & QUERY LINKS ON /karya (User Request 7)
    // Filter clicks must do card-to-card transitions, NOT full MRT train transitions
    if (link.classList.contains('catalog-tab-btn') || 
        link.closest('.catalog-category-tabs') ||
        (window.location.pathname === '/karya' && href.startsWith('/karya?')) ||
        (window.location.pathname === '/karya' && href === '/karya')) {
      return;
    }

    link.addEventListener('click', (e) => {
      // Check reduced motion preference
      if (document.body.classList.contains('reduced-motion')) {
        return; // Allow instant default navigation
      }

      // Allow middle click or ctrl/cmd click to open in new tab
      if (e.metaKey || e.ctrlKey || e.button !== 0) return;

      e.preventDefault();

      // Determine destination label
      let destText = 'Perjalanan Berikutnya';
      if (href === '/') destText = 'Stasiun Beranda';
      else if (href.startsWith('/karya/')) destText = 'Stasiun Studi Kasus';
      else if (href.startsWith('/karya')) destText = 'Stasiun Katalog Karya';
      else if (href.startsWith('/cv')) destText = 'Stasiun CV Interaktif';
      else if (href.startsWith('/admin')) destText = 'Stasiun Panel Admin';

      const board = overlay.querySelector('.mrt-dest-name');
      if (board) board.textContent = destText;

      // Update dynamic fun fact from Mirza's authentic profile
      const factEl = overlay.querySelector('#mrt-fact-text') || overlay.querySelector('.mrt-fact-text');
      if (factEl && MIRZA_TRANSIT_FACTS.length) {
        const randomIndex = Math.floor(Math.random() * MIRZA_TRANSIT_FACTS.length);
        factEl.textContent = MIRZA_TRANSIT_FACTS[randomIndex];
      }

      // MULTI-LIVERY & VARIED DYNAMIC SPEED (User Request 6)
      const liveries = [
        { cls: 'livery-krl', callsign: 'KRL-SURABAYA', baseSpeed: 0.82 },
        { cls: 'livery-metro', callsign: 'MRT-JAKARTA', baseSpeed: 0.72 },
        { cls: 'livery-lrt', callsign: 'LRT-PLANOPOLIS', baseSpeed: 0.90 }
      ];
      const selected = liveries[Math.floor(Math.random() * liveries.length)];
      const randomSpeed = Math.max(0.68, Math.min(0.98, selected.baseSpeed + (Math.random() * 0.16 - 0.08)));

      const carriage = overlay.querySelector('.mrt-train-carriage');
      if (carriage) {
        carriage.className = 'mrt-train-carriage ' + selected.cls;
        carriage.style.setProperty('--mrt-speed', `${randomSpeed.toFixed(2)}s`);
        carriage.style.animationDuration = `${randomSpeed.toFixed(2)}s`;
      }

      const callsignEl = overlay.querySelector('#mrt-loco-callsign');
      if (callsignEl) callsignEl.textContent = selected.callsign;

      overlay.setAttribute('data-target-href', href);
      overlay.classList.add('active', 'animating');

      // Sync page navigation exactly to dynamic animation duration
      const routeDelay = Math.round(randomSpeed * 1000 - 80);
      setTimeout(() => {
        window.location.href = href;
      }, routeDelay);
    });
  });
}"""

js_norm = js.replace('\r\n', '\n')
old_trans_norm = old_transitions.replace('\r\n', '\n')
new_trans_norm = new_transitions.replace('\r\n', '\n')

assert old_trans_norm in js_norm, "old_transitions not found"
js_norm = js_norm.replace(old_trans_norm, new_trans_norm, 1)

# 2. Update initCatalogFilters with client-side card-to-card crossfade transitions
old_catalog = """// --- 14. Project Catalog Live Filters ---
function initCatalogFilters() {
  const searchInput = document.getElementById('catalog-search');
  if (!searchInput) return;
  
  let timer;
  searchInput.addEventListener('input', () => {
    clearTimeout(timer);
    timer = setTimeout(() => {
      const form = document.getElementById('catalog-filter-form');
      if (form) form.submit();
    }, 450);
  });
}"""

new_catalog = """// --- 14. Project Catalog Pure Card-to-Card Transition (User Request 7) ---
function initCatalogFilters() {
  const cards = document.querySelectorAll('#catalog-projects-grid .project-card');
  const tabBtns = document.querySelectorAll('.catalog-tab-btn');
  const searchInput = document.getElementById('catalog-search');
  const countNum = document.getElementById('catalog-count-num');
  const statusText = document.getElementById('catalog-status-text');
  if (!cards.length) return;

  let currentCategory = 'semua';
  const urlParams = new URLSearchParams(window.location.search);
  if (urlParams.has('kategori')) currentCategory = urlParams.get('kategori');

  const applyCardFilter = (category, query) => {
    query = (query || '').toLowerCase().trim();
    category = (category || 'semua').toLowerCase();

    // 1. Fade out cards smoothly
    cards.forEach(card => card.classList.add('card-fading'));

    setTimeout(() => {
      let visibleCount = 0;
      cards.forEach(card => {
        const title = card.getAttribute('data-title') || '';
        const cats = card.getAttribute('data-categories') || '';
        const tools = card.getAttribute('data-tools') || '';
        const summary = card.getAttribute('data-summary') || '';

        const matchesCat = (category === 'semua' || cats.includes(category));
        const matchesQuery = !query || title.includes(query) || cats.includes(query) || tools.includes(query) || summary.includes(query);

        if (matchesCat && matchesQuery) {
          card.style.display = '';
          card.classList.remove('card-fading');
          card.classList.add('card-entering');
          visibleCount++;
        } else {
          card.style.display = 'none';
          card.classList.remove('card-fading', 'card-entering');
        }
      });

      if (countNum) countNum.textContent = visibleCount;
      if (statusText) {
        if (category === 'semua' && !query) {
          statusText.innerHTML = `Menampilkan <strong id="catalog-count-num">${visibleCount}</strong> dari ${cards.length} studi kasus`;
        } else {
          statusText.innerHTML = `Menampilkan <strong id="catalog-count-num">${visibleCount}</strong> dari ${cards.length} studi kasus (Kategori: <em>"${category}"</em>${query ? `, Kata kunci: <em>"${query}"</em>` : ''})`;
        }
      }
    }, 150);
  };

  // Wire Tab Buttons for Card-to-Card Transition without Page Reload / Train Overlay
  tabBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const href = btn.getAttribute('href');
      const targetUrl = new URL(href, window.location.origin);
      const cat = targetUrl.searchParams.get('kategori') || 'semua';

      tabBtns.forEach(b => {
        b.classList.remove('active');
        b.setAttribute('aria-selected', 'false');
      });
      btn.classList.add('active');
      btn.setAttribute('aria-selected', 'true');

      currentCategory = cat;
      const q = searchInput ? searchInput.value : '';
      applyCardFilter(cat, q);

      if (window.history && window.history.pushState) {
        window.history.pushState(null, '', href);
      }
    });
  });

  // Wire Search Input for In-Page Instant Filtering
  if (searchInput) {
    let timer;
    searchInput.addEventListener('input', () => {
      clearTimeout(timer);
      timer = setTimeout(() => {
        applyCardFilter(currentCategory, searchInput.value);
      }, 160);
    });
  }
}"""

old_cat_norm = old_catalog.replace('\r\n', '\n')
new_cat_norm = new_catalog.replace('\r\n', '\n')

assert old_cat_norm in js_norm, "old_catalog not found"
js_norm = js_norm.replace(old_cat_norm, new_cat_norm, 1)

# 3. Update initTimelineProgressTracker with clean simple indicator
old_tl_js = """function initTimelineProgressTracker() {
  const container = document.getElementById('metro-timeline-container');
  const progressFill = document.getElementById('timeline-progress-fill');
  const indicator = document.getElementById('timeline-sliding-indicator');
  const dockBadge = document.getElementById('train-dock-badge');
  const items = document.querySelectorAll('.metro-timeline-item');
  if (!container || !progressFill || !indicator) return;

  const onScroll = () => {
    const rect = container.getBoundingClientRect();
    const windowH = window.innerHeight;
    
    // Viewport-relative vertical position
    const startY = rect.top;
    const totalH = rect.height;
    const currentY = (windowH * 0.45) - startY;
    const progress = Math.min(Math.max(currentY / totalH, 0), 1);

    // Update fill height & sliding indicator
    const percent = Math.round(progress * 100);
    progressFill.style.height = `${percent}%`;
    indicator.style.top = `${percent}%`;

    // Detect closest active station
    let activeStationCode = 'ST-01';
    items.forEach((item) => {
      const itemRect = item.getBoundingClientRect();
      if (itemRect.top <= windowH * 0.55) {
        activeStationCode = (item.getAttribute('data-station') || 'st-01').toUpperCase();
        item.classList.add('station-active-glow');
      } else {
        item.classList.remove('station-active-glow');
      }
    });

    if (dockBadge) {
      dockBadge.textContent = activeStationCode;
    }
  };

  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
}"""

new_tl_js = """function initTimelineProgressTracker() {
  const container = document.getElementById('metro-timeline-container');
  const progressFill = document.getElementById('timeline-progress-fill');
  const indicator = document.getElementById('timeline-sliding-indicator');
  const items = document.querySelectorAll('.metro-timeline-item');
  if (!container || !progressFill || !indicator) return;

  const onScroll = () => {
    const rect = container.getBoundingClientRect();
    const windowH = window.innerHeight;
    
    // Viewport-relative vertical position (smooth simple sliding bar)
    const startY = rect.top;
    const totalH = rect.height;
    const currentY = (windowH * 0.45) - startY;
    const progress = Math.min(Math.max(currentY / totalH, 0), 1);

    // Update fill height & sliding indicator dot
    const percent = progress * 100;
    progressFill.style.height = `${percent.toFixed(2)}%`;
    indicator.style.top = `${percent.toFixed(2)}%`;

    // Highlight reached stations
    items.forEach((item) => {
      const itemRect = item.getBoundingClientRect();
      if (itemRect.top <= windowH * 0.55) {
        item.classList.add('station-active-glow');
      } else {
        item.classList.remove('station-active-glow');
      }
    });
  };

  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
}"""

old_tl_js_norm = old_tl_js.replace('\r\n', '\n')
new_tl_js_norm = new_tl_js.replace('\r\n', '\n')

assert old_tl_js_norm in js_norm, "old_tl_js not found"
js_norm = js_norm.replace(old_tl_js_norm, new_tl_js_norm, 1)

# 4. Update initCandleInteractions with dynamic cursor tracking & hover revelation
old_candle_js = """function initCandleInteractions() {
  const zone = document.getElementById('candle-interactive-zone');
  const flame = document.getElementById('realistic-candle-flame');
  const halo = document.getElementById('candle-ambient-halo');
  const message = document.getElementById('candle-revelation-message');
  if (!zone || !flame) return;

  const ignite = () => {
    flame.classList.add('flame-ignited');
    if (halo) halo.style.opacity = '1';
    if (message) {
      message.style.transform = 'scale(1.03)';
      message.style.boxShadow = '0 6px 20px rgba(245, 158, 11, 0.4)';
    }
  };

  const calm = () => {
    flame.classList.remove('flame-ignited');
    if (halo) halo.style.opacity = '';
    if (message) {
      message.style.transform = '';
      message.style.boxShadow = '';
    }
  };

  zone.addEventListener('mouseenter', ignite);
  zone.addEventListener('mouseleave', calm);
  zone.addEventListener('focus', ignite);
  zone.addEventListener('blur', calm);
  zone.addEventListener('click', () => {
    ignite();
    setTimeout(calm, 2800);
  });
}"""

new_candle_js = """function initCandleInteractions() {
  const zone = document.getElementById('candle-interactive-zone');
  const flame = document.getElementById('realistic-candle-flame');
  const halo = document.getElementById('candle-ambient-halo');
  const message = document.getElementById('candle-revelation-message');
  if (!zone || !flame) return;

  const ignite = () => {
    flame.classList.add('flame-ignited');
    if (halo) halo.style.opacity = '1';
  };

  const calm = () => {
    flame.classList.remove('flame-ignited');
    flame.style.transform = '';
    if (halo) halo.style.opacity = '';
  };

  // Organic flame physics tracking cursor breeze (User Request 5)
  zone.addEventListener('mousemove', (e) => {
    ignite();
    const rect = zone.getBoundingClientRect();
    const centerX = rect.left + rect.width / 2;
    const diffX = e.clientX - centerX;
    const tilt = Math.min(Math.max((diffX / (rect.width / 2)) * 5, -5), 5);
    flame.style.transform = `translateX(-50%) rotate(${tilt.toFixed(1)}deg) scale(1.15, 1.2)`;
  });

  zone.addEventListener('mouseenter', ignite);
  zone.addEventListener('mouseleave', calm);
  zone.addEventListener('focus', ignite);
  zone.addEventListener('blur', calm);
  
  // Mobile touch / click toggle
  zone.addEventListener('click', () => {
    zone.classList.toggle('active');
    ignite();
    setTimeout(calm, 3200);
  });
}"""

old_cd_norm = old_candle_js.replace('\r\n', '\n')
new_cd_norm = new_candle_js.replace('\r\n', '\n')

assert old_cd_norm in js_norm, "old_candle_js not found"
js_norm = js_norm.replace(old_cd_norm, new_cd_norm, 1)

with open('static/js/main.js', 'w', encoding='utf-8') as f:
    f.write(js_norm)

print("SUCCESS: Updated static/js/main.js with train liveries, catalog card-to-card transitions, simple timeline slider, and interactive candle!")
