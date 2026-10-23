import re

with open('static/js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Add initTimelineProgressTracker(); to DOMContentLoaded
if 'initTimelineProgressTracker();' not in js:
    js = js.replace('  initSoftwarePlaypen();\n', '  initSoftwarePlaypen();\n  initTimelineProgressTracker();\n')

# 2. Replace initCatalogFilters with instant fun tactile pop filter
cat_start = js.find('// --- 14. Project Catalog Pure Card-to-Card Transition')
cat_end = js.find('// --- 15.', cat_start)

new_cat_section = """// --- 14. Project Catalog Instant Fun Tactile Pop Filter (User Request) ---
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
      const title = (card.getAttribute('data-title') || '').toLowerCase();
      const cats = (card.getAttribute('data-categories') || '').toLowerCase();
      const tools = (card.getAttribute('data-tools') || '').toLowerCase();
      const summary = (card.getAttribute('data-summary') || '').toLowerCase();

      const matchesCat = (category === 'semua' || cats.includes(category));
      const matchesQuery = !query || title.includes(query) || cats.includes(query) || tools.includes(query) || summary.includes(query);

      if (matchesCat && matchesQuery) {
        card.style.display = '';
        // Fun pop animation trigger
        card.classList.remove('fun-card-pop');
        void card.offsetWidth; // trigger reflow
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

  // Fun tactile button bounce on tab switch
  tabBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const href = btn.getAttribute('href');
      const targetUrl = new URL(href, window.location.origin);
      const cat = targetUrl.searchParams.get('kategori') || 'semua';

      tabBtns.forEach(b => {
        b.classList.remove('active', 'tab-popping');
        b.setAttribute('aria-selected', 'false');
      });
      btn.classList.add('active', 'tab-popping');
      btn.setAttribute('aria-selected', 'true');

      currentCategory = cat;
      const q = searchInput ? searchInput.value : '';
      applyInstantCardFilter(cat, q);

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
        applyInstantCardFilter(currentCategory, searchInput.value);
      }, 80);
    });
  }
}

"""

js = js[:cat_start] + new_cat_section + js[cat_end:]

# 3. Replace Candle section with Timeline Sliding Rail Tracker + Reworked Candle
candle_start = js.find('// --- 22. Living Philosophy Candle')

new_timeline_and_candle = """// --- 22. Enhanced Timeline Station & Sliding Capsule Tracker (Simple & Clear Rail) ---
function initTimelineProgressTracker() {
  const container = document.getElementById('metro-timeline-container');
  const fillBar = document.getElementById('metro-progress-fill');
  const capsule = document.getElementById('metro-sliding-capsule');
  const stations = document.querySelectorAll('.metro-timeline-item');
  if (!container || !fillBar) return;

  const onScroll = () => {
    const rect = container.getBoundingClientRect();
    const windowH = window.innerHeight;
    const totalH = rect.height;

    // Start tracking when top enters 65% viewport, finish when bottom reaches 35% viewport
    const startOffset = windowH * 0.65;
    const currentY = startOffset - rect.top;
    let progress = currentY / (totalH + startOffset * 0.3);
    progress = Math.max(0, Math.min(1, progress));

    const percent = (progress * 100).toFixed(1);
    fillBar.style.height = `${percent}%`;
    if (capsule) {
      capsule.style.top = `${percent}%`;
      capsule.setAttribute('aria-valuenow', Math.round(progress * 100));
    }

    // Activate stations as capsule / scroll reaches them
    stations.forEach(item => {
      const itemRect = item.getBoundingClientRect();
      if (itemRect.top <= windowH * 0.58) {
        item.classList.add('station-active');
      } else {
        item.classList.remove('station-active');
      }
    });
  };

  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
}

// --- 23. Reworked Living Philosophy Candle (Organic Flame & Hover-Only Revelation) ---
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
    flame.style.transform = 'translateX(-50%) scale(1.35, 1.4)';
    if (halo) halo.style.opacity = '1';

    setTimeout(() => {
      flame.style.transform = '';
      setTimeout(conceal, 3800);
    }, 450);
  });
}
"""

js = js[:candle_start] + new_timeline_and_candle

with open('static/js/main.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("SUCCESS: main.js updated perfectly!")
