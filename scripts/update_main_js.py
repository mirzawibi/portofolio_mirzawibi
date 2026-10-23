with open('static/js/main.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

# 1. Update DOMContentLoaded
old_dom = """  initSlideDeckPlayer();
  
  // Existing core utilities"""

new_dom = """  initSlideDeckPlayer();
  
  // High-priority interactive enhancements (Software, Timeline, Candle)
  initSoftwarePlaypen();
  initTimelineProgressTracker();
  initCandleInteractions();

  // Existing core utilities"""

assert old_dom in js_content, "old_dom not found"
js_content = js_content.replace(old_dom, new_dom, 1)

# 2. Update initPageTransitions with 12 fun facts
old_transitions = """// --- 1. MRT Train High-Speed Page Transition ---
function initPageTransitions() {
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

      overlay.setAttribute('data-target-href', href);
      overlay.classList.add('active', 'animating');

      // Allow train to glide majestically across the screen before page route occurs
      setTimeout(() => {
        window.location.href = href;
      }, 850);
    });
  });
}"""

new_transitions = """// --- 1. MRT Train High-Speed Page Transition with 12 Mirza Facts ---
const MIRZA_TRANSIT_FACTS = [
  "Tahukah Anda? Mirza memimpin koordinasi lintas 8 divisi strategis sebagai Project Officer Planopolis 2026 di PWK ITS.",
  "Tahukah Anda? Selama magang di Dishub Sidoarjo, Mirza mengolah puluhan trayek angkutan umum menjadi geodatabase terpadu.",
  "Tahukah Anda? Mirza menjabat sebagai Kepala Departemen Media & Desain INI LHO ITS 2026, memimpin publikasi ke puluhan ribu calon mahasiswa.",
  "Tahukah Anda? Mirza adalah Asisten Laboratorium Perencanaan Wilayah PWK ITS, membimbing mahasiswa dalam pemodelan spasial ArcGIS.",
  "Tahukah Anda? Mirza mendirikan LokaSolution, inisiatif konsultasi spasial dan perencanaan kawasan urban mandiri.",
  "Tahukah Anda? Skripsi dan fokus riset Mirza berfokus pada integrasi koridor transit dan walkability perkotaan berkelanjutan.",
  "Tahukah Anda? Mirza menguasai workflow geospasial modern: dari analisis buffer ArcGIS, QGIS, hingga visualisasi 3D SketchUp dan AutoCAD.",
  "Tahukah Anda? Filosofi perencanaan Mirza berakar pada Human-Centered Urbanism: kota yang memuliakan pejalan kaki dan transportasi publik.",
  "Tahukah Anda? Mirza telah menyusun lebih dari 5 dokumen masterplan dan pedoman penataan kawasan komprehensif di Jawa Timur.",
  "Tahukah Anda? Setiap peta tematik yang diproduksi Mirza selalu memenuhi kaidah kartografi SNI BIG dengan akurasi data lapangan.",
  "Tahukah Anda? Dalam perancangan simpul transit, Mirza mengintegrasikan radius aksesibilitas pejalan kaki 400 meter (5 menit jalan kaki).",
  "Tahukah Anda? Selain perangkat GIS, Mirza aktif merancang visual identity dan UI sistem informasi spasial berbasis web."
];

function initPageTransitions() {
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

assert old_transitions in js_content, "old_transitions not found"
js_content = js_content.replace(old_transitions, new_transitions, 1)

# 3. Append the 3 new implementations at the bottom
new_functions = """

// --- 21. Interactive Software Playpen Inspector (User Request 1) ---
function initSoftwarePlaypen() {
  const chips = document.querySelectorAll('#software-chips-playpen .soft-chip');
  const label = document.getElementById('inspector-tool-label');
  const output = document.getElementById('inspector-output-text');
  const inspectorBox = document.getElementById('software-inspector');
  if (!chips.length || !output) return;

  const activateChip = (chip) => {
    chips.forEach(c => c.classList.remove('active'));
    chip.classList.add('active');

    const title = chip.getAttribute('data-title') || chip.textContent.trim();
    const out = chip.getAttribute('data-output') || '';

    if (inspectorBox) {
      inspectorBox.classList.add('inspector-updating');
    }

    if (label) {
      label.textContent = `${title.toUpperCase()} · OUTPUT NYATA:`;
    }
    output.textContent = out;

    setTimeout(() => {
      if (inspectorBox) {
        inspectorBox.classList.remove('inspector-updating');
      }
    }, 180);
  };

  chips.forEach(chip => {
    chip.addEventListener('mouseenter', () => activateChip(chip));
    chip.addEventListener('focus', () => activateChip(chip));
    chip.addEventListener('click', (e) => {
      e.preventDefault();
      activateChip(chip);
    });
  });
}

// --- 22. Interactive Metro Timeline Progress Tracker (User Request 2) ---
function initTimelineProgressTracker() {
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
}

// --- 23. Living Philosophy Candle Interactive Dynamics (User Request 3) ---
function initCandleInteractions() {
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
}
"""

js_content += new_functions

with open('static/js/main.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("SUCCESS: Updated static/js/main.js with all 4 features!")
