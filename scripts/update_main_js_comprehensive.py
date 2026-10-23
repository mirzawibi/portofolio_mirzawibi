with open('static/js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Ensure initTimelineProgressTracker is in DOMContentLoaded
if 'initTimelineProgressTracker();' not in js:
    js = js.replace('  initSoftwarePlaypen();\n', '  initSoftwarePlaypen();\n  initTimelineProgressTracker();\n')

# 2. Update initCatalogFilters for instant tactile pop
old_cat_fn = """// --- 14. Project Catalog Pure Card-to-Card Transition (User Request 7) ---
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

new_cat_fn = """// --- 14. Project Catalog Instant Fun Tactile Pop Filter (User Request) ---
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

  const applyInstantCardFilter = (category, query) => {
    query = (query || '').toLowerCase().trim();
    category = (category || 'semua').toLowerCase();

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
        card.classList.remove('fun-card-pop');
        void card.offsetWidth; // force reflow for snappy animation restart
        card.classList.add('fun-card-pop');
        visibleCount++;
      } else {
        card.style.display = 'none';
        card.classList.remove('fun-card-pop');
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
  };

  // Wire Tab Buttons for Instant Fun Pop Action
  tabBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const href = btn.getAttribute('href');
      const targetUrl = new URL(href, window.location.origin);
      const cat = targetUrl.searchParams.get('kategori') || 'semua';

      // Fun tactile bounce on clicked button
      btn.classList.add('tab-popping');
      setTimeout(() => btn.classList.remove('tab-popping'), 160);

      tabBtns.forEach(b => {
        b.classList.remove('active');
        b.setAttribute('aria-selected', 'false');
      });
      btn.classList.add('active');
      btn.setAttribute('aria-selected', 'true');

      currentCategory = cat;
      const q = searchInput ? searchInput.value : '';
      applyInstantCardFilter(cat, q);

      if (window.history && window.history.pushState) {
        window.history.pushState(null, '', href);
      }
    });
  });

  // Wire Search Input for Instant Filtering
  if (searchInput) {
    searchInput.addEventListener('input', () => {
      applyInstantCardFilter(currentCategory, searchInput.value);
    });
  }
}"""

js_norm = js.replace('\r\n', '\n')
old_cat_norm = old_cat_fn.replace('\r\n', '\n')
new_cat_norm = new_cat_fn.replace('\r\n', '\n')

assert old_cat_norm in js_norm, "old_cat_fn not found"
js_norm = js_norm.replace(old_cat_norm, new_cat_norm, 1)

# 3. Add initTimelineProgressTracker and update candle interactions
new_timeline_and_candle = """// --- 22. Interactive Metro Timeline Progress Tracker (Rombak Jelas & Simple) ---
function initTimelineProgressTracker() {
  const container = document.getElementById('metro-timeline-container');
  const progressFill = document.getElementById('metro-progress-fill');
  const capsule = document.getElementById('metro-sliding-capsule');
  const items = document.querySelectorAll('.metro-timeline-item');
  if (!container || !progressFill || !capsule) return;

  const onScroll = () => {
    const rect = container.getBoundingClientRect();
    const windowH = window.innerHeight;
    
    // Viewport-relative vertical progress calculation
    const startY = rect.top;
    const totalH = rect.height;
    const currentY = (windowH * 0.45) - startY;
    const progress = Math.min(Math.max(currentY / totalH, 0), 1);

    // Update fill height & clearly visible sliding capsule
    const percent = progress * 100;
    progressFill.style.height = `${percent.toFixed(2)}%`;
    capsule.style.top = `${percent.toFixed(2)}%`;

    // Highlight clearly visible station points as the capsule reaches them
    items.forEach((item) => {
      const itemRect = item.getBoundingClientRect();
      if (itemRect.top <= windowH * 0.55) {
        item.classList.add('station-active');
      } else {
        item.classList.remove('station-active');
      }
    });
  };

  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
}

// --- 23. Reworked Living Philosophy Candle (Organic Flame & Hover Revelation) ---
function initCandleInteractions() {
  const zone = document.getElementById('candle-interactive-zone');
  const flame = document.getElementById('realistic-candle-flame');
  const halo = document.getElementById('candle-ambient-halo');
  if (!zone || !flame) return;

  const reveal = () => {
    zone.classList.add('candle-active');
    flame.classList.add('flame-ignited');
    if (halo) halo.style.opacity = '1';
  };

  const conceal = () => {
    zone.classList.remove('candle-active');
    flame.classList.remove('flame-ignited');
    flame.style.transform = '';
    if (halo) halo.style.opacity = '';
  };

  // Organic living flame reacts to cursor position like a real gentle breeze
  zone.addEventListener('mousemove', (e) => {
    reveal();
    const rect = zone.getBoundingClientRect();
    const centerX = rect.left + rect.width / 2;
    const diffX = e.clientX - centerX;
    const tilt = Math.min(Math.max((diffX / (rect.width / 2)) * 6, -6), 6);
    flame.style.transform = `translateX(-50%) rotate(${tilt.toFixed(1)}deg) scale(1.18, 1.22)`;
  });

  zone.addEventListener('mouseenter', reveal);
  zone.addEventListener('mouseleave', conceal);
  zone.addEventListener('focus', reveal);
  zone.addEventListener('blur', conceal);
  
  // Interactive Click: Flare up and spark burst!
  zone.addEventListener('click', () => {
    zone.classList.add('candle-active');
    flame.classList.add('flame-ignited');
    flame.style.transform = 'translateX(-50%) scale(1.3, 1.35)';
    if (halo) halo.style.opacity = '1';

    setTimeout(() => {
      flame.style.transform = '';
      setTimeout(conceal, 3500);
    }, 450);
  });
}
"""

# Replace the existing candle interaction block at the bottom
old_bottom = """// --- 22. Living Philosophy Candle Interactive Dynamics (Reveals on Hover Only) ---
function initCandleInteractions() {
  const zone = document.getElementById('candle-interactive-zone');
  const flame = document.getElementById('realistic-candle-flame');
  const halo = document.getElementById('candle-ambient-halo');
  const message = document.getElementById('candle-revelation-message');
  const hint = document.getElementById('candle-hover-hint');
  if (!zone || !flame) return;

  // Strict initial hidden state
  if (message) {
    message.style.opacity = '0';
    message.style.visibility = 'hidden';
    message.style.pointerEvents = 'none';
  }

  const reveal = () => {
    flame.classList.add('flame-ignited');
    if (halo) halo.style.opacity = '1';
    if (message) {
      message.style.opacity = '1';
      message.style.visibility = 'visible';
      message.style.pointerEvents = 'auto';
      message.style.transform = 'translateY(0) scale(1)';
    }
    if (hint) hint.style.opacity = '0';
  };

  const conceal = () => {
    flame.classList.remove('flame-ignited');
    flame.style.transform = '';
    if (halo) halo.style.opacity = '';
    if (message) {
      message.style.opacity = '0';
      message.style.visibility = 'hidden';
      message.style.pointerEvents = 'none';
      message.style.transform = 'translateY(14px) scale(0.95)';
    }
    if (hint) hint.style.opacity = '0.8';
  };

  // Organic flame physics tracking cursor breeze (User Request 5)
  zone.addEventListener('mousemove', (e) => {
    reveal();
    const rect = zone.getBoundingClientRect();
    const centerX = rect.left + rect.width / 2;
    const diffX = e.clientX - centerX;
    const tilt = Math.min(Math.max((diffX / (rect.width / 2)) * 6, -6), 6);
    flame.style.transform = `translateX(-50%) rotate(${tilt.toFixed(1)}deg) scale(1.15, 1.2)`;
  });

  zone.addEventListener('mouseenter', reveal);
  zone.addEventListener('mouseleave', conceal);
  zone.addEventListener('focus', reveal);
  zone.addEventListener('blur', conceal);
  
  // Mobile touch toggle
  zone.addEventListener('click', () => {
    if (message && message.style.visibility === 'visible') {
      conceal();
    } else {
      reveal();
      setTimeout(conceal, 3500);
    }
  });
}"""

old_bot_norm = old_bottom.replace('\r\n', '\n')
new_tl_norm = new_timeline_and_candle.replace('\r\n', '\n')

assert old_bot_norm in js_norm, "old_bottom not found"
js_norm = js_norm.replace(old_bot_norm, new_tl_norm, 1)

with open('static/js/main.js', 'w', encoding='utf-8') as f:
    f.write(js_norm)

print("SUCCESS: Updated static/js/main.js with instant pop filters, sliding rail tracker, and reworked candle interactions!")
