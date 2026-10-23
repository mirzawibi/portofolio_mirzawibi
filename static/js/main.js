/**
 * PORTOFOLIO MUHAMMAD MIRZA WIBISONO
 * Advanced Urban Transit Interaction & Motion System
 */

document.addEventListener('DOMContentLoaded', () => {
  initPageTransitions();
  initMetroScrollTracker();
  initScrollReveal();
  initCounterAnimations();
  initBeforeAfterSliders();
  initCard3DTilt();
  initGlidingTabIndicator();
  initPillarTabs();
  initSlideDeckPlayer();
  
  // High-priority interactive enhancements (Software, Timeline, Candle)
  initSoftwarePlaypen();
  initTimelineProgressTracker();
  initCandleInteractions();

  // Existing core utilities
  initReducedMotion();
  initToast();
  initCopyEmail();
  initScenarioSwitcher();
  initModalViewer();
  initCvAccordion();
  initCvSubjectFilter();
  initCvExperienceFilter();
  initHalteIntroListener();
  initCatalogFilters();
  initMobileNav();
});

// --- 1. MRT Train High-Speed Page Transition with 12 Mirza Facts ---
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

    // EXCLUDE CATALOG FILTER TABS & QUERY LINKS ON /karya (User Request 7)
    // Filter clicks must do card-to-card transitions, NOT full MRT train transitions
    if (link.classList.contains('catalog-tab-btn') || 
        link.closest('.catalog-category-tabs') ||
        (href && (href.includes('?kategori=') || href.includes('?filter='))) ||
        (window.location.pathname.includes('karya') && (href.includes('karya?') || href.startsWith('?') || href.startsWith('./?')))) {
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
      if (href === '/' || href === './' || href === '../' || href === '../../' || href === '') {
        destText = 'Stasiun Beranda';
      } else if (href.includes('cv')) {
        destText = 'Stasiun CV Interaktif';
      } else if (href.includes('karya')) {
        if (href.endsWith('karya') || href.endsWith('karya/') || href.endsWith('karya/?') || href.includes('?kategori=')) {
          destText = 'Stasiun Katalog Karya';
        } else {
          destText = 'Stasiun Studi Kasus';
        }
      } else if (href.includes('admin')) {
        destText = 'Stasiun Panel Admin';
      }

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
}

// --- 2. Top Metro Scroll Progress Tracker with Dynamic Transit Vehicle ---
function initMetroScrollTracker() {
  const progressBar = document.getElementById('metro-scroll-progress');
  const vehicle = document.getElementById('metro-transit-vehicle');
  if (!progressBar) return;

  let lastScrollY = window.scrollY;

  const updateScroll = () => {
    const totalHeight = document.documentElement.scrollHeight - window.innerHeight;
    if (totalHeight <= 0) return;
    const progress = Math.min(Math.max(window.scrollY / totalHeight, 0), 1) * 100;
    progressBar.style.width = `${progress}%`;

    const currentScrollY = window.scrollY;
    if (vehicle) {
      if (currentScrollY > lastScrollY + 2) {
        vehicle.style.transform = 'translate3d(0, 0, 0) scaleX(1)';
      } else if (currentScrollY < lastScrollY - 2) {
        vehicle.style.transform = 'translate3d(0, 0, 0) scaleX(-1)';
      }
    }
    lastScrollY = currentScrollY;
  };

  window.addEventListener('scroll', updateScroll, { passive: true });
  updateScroll();
}

// --- 3. Scroll-Driven Reveal System ---
function initScrollReveal() {
  const revealElements = document.querySelectorAll('.reveal');
  if (!revealElements.length) return;

  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries, obs) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('reveal-visible');
          obs.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.1,
      rootMargin: '0px 0px -40px 0px'
    });

    revealElements.forEach(el => observer.observe(el));
  } else {
    // Fallback
    revealElements.forEach(el => el.classList.add('reveal-visible'));
  }
}

// --- 4. Live Counter Number Animations ---
function initCounterAnimations() {
  const counters = document.querySelectorAll('[data-counter], [data-target]');
  if (!counters.length) return;

  const animateCounter = (el) => {
    const targetStr = el.getAttribute('data-counter') || el.getAttribute('data-target');
    const target = parseInt(targetStr, 10);
    if (isNaN(target)) return;

    let current = 0;
    const step = Math.max(Math.floor(target / 35), 1);
    const duration = 1100;
    const intervalTime = Math.max(Math.floor(duration / (target / step)), 16);

    el.textContent = '0';
    const timer = setInterval(() => {
      current += step;
      if (current >= target) {
        current = target;
        clearInterval(timer);
      }
      el.textContent = current;
    }, intervalTime);
  };

  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries, obs) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          animateCounter(entry.target);
          obs.unobserve(entry.target);
        }
      });
    }, { threshold: 0.25 });

    counters.forEach(c => observer.observe(c));
  } else {
    counters.forEach(c => animateCounter(c));
  }
}

// --- 5. Interactive Before / After Comparison Map Slider ---
function initBeforeAfterSliders() {
  const sliders = document.querySelectorAll('.before-after-slider');
  sliders.forEach(slider => {
    const afterImg = slider.querySelector('.slider-img-after');
    const handle = slider.querySelector('.slider-handle');
    if (!afterImg || !handle) return;

    let isDragging = false;
    let currentPercent = 50;

    const setPercent = (percent) => {
      currentPercent = Math.min(Math.max(percent, 0), 100);
      afterImg.style.clipPath = `polygon(0 0, ${currentPercent}% 0, ${currentPercent}% 100%, 0 100%)`;
      handle.style.left = `${currentPercent}%`;
      slider.setAttribute('aria-valuenow', Math.round(currentPercent));
    };

    const setPosition = (xPos) => {
      const rect = slider.getBoundingClientRect();
      const percent = ((xPos - rect.left) / rect.width) * 100;
      setPercent(percent);
    };

    slider.addEventListener('mousedown', (e) => {
      isDragging = true;
      setPosition(e.clientX);
    });

    window.addEventListener('mousemove', (e) => {
      if (!isDragging) return;
      setPosition(e.clientX);
    });

    window.addEventListener('mouseup', () => {
      isDragging = false;
    });

    slider.addEventListener('touchstart', (e) => {
      isDragging = true;
      if (e.touches[0]) setPosition(e.touches[0].clientX);
    }, { passive: true });

    window.addEventListener('touchmove', (e) => {
      if (!isDragging || !e.touches[0]) return;
      setPosition(e.touches[0].clientX);
    }, { passive: true });

    window.addEventListener('touchend', () => {
      isDragging = false;
    });

    // Keyboard Accessibility (UI UX Pro Max & WCAG 2.2 AA)
    slider.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowLeft' || e.key === 'ArrowDown') {
        e.preventDefault();
        setPercent(currentPercent - 5);
      } else if (e.key === 'ArrowRight' || e.key === 'ArrowUp') {
        e.preventDefault();
        setPercent(currentPercent + 5);
      } else if (e.key === 'Home') {
        e.preventDefault();
        setPercent(0);
      } else if (e.key === 'End') {
        e.preventDefault();
        setPercent(100);
      }
    });
  });
}

// --- 6. 3D Card Perspective Tilt Effect ---
function initCard3DTilt() {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  const cards = document.querySelectorAll('.project-card');
  cards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
      if (document.body.classList.contains('reduced-motion')) return;
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;

      const rotateX = ((y - centerY) / centerY) * -5;
      const rotateY = ((x - centerX) / centerX) * 5;

      card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-4px)`;
    });

    card.addEventListener('mouseleave', () => {
      card.style.transform = '';
    });
  });
}

// --- 7. Gliding Active Tab Indicator ---
function initGlidingTabIndicator() {
  const tabWrappers = document.querySelectorAll('.transit-tabs-wrapper');
  tabWrappers.forEach(wrapper => {
    const pill = wrapper.querySelector('.transit-gliding-pill');
    const tabs = wrapper.querySelectorAll('.transit-tab-link');
    if (!pill || !tabs.length) return;

    const movePill = (activeTab) => {
      pill.style.left = `${activeTab.offsetLeft}px`;
      pill.style.width = `${activeTab.offsetWidth}px`;
    };

    const activeTab = wrapper.querySelector('.transit-tab-link.active') || tabs[0];
    if (activeTab) movePill(activeTab);

    tabs.forEach(tab => {
      tab.addEventListener('mouseenter', () => movePill(tab));
      tab.addEventListener('click', () => {
        tabs.forEach(t => t.classList.remove('active'));
        tab.classList.add('active');
        movePill(tab);
      });
    });

    wrapper.addEventListener('mouseleave', () => {
      const currentActive = wrapper.querySelector('.transit-tab-link.active');
      if (currentActive) movePill(currentActive);
    });
  });
}

// --- 8. Reduced Motion Preference ---
function initReducedMotion() {
  const toggleBtn = document.getElementById('motion-toggle');
  const storedPref = localStorage.getItem('pref-reduced-motion');
  const systemPref = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  
  if (storedPref === 'true' || (storedPref === null && systemPref)) {
    document.body.classList.add('reduced-motion');
    if (toggleBtn) updateMotionButton(toggleBtn, true);
  }
  
  if (toggleBtn) {
    toggleBtn.addEventListener('click', () => {
      const isReduced = document.body.classList.toggle('reduced-motion');
      localStorage.setItem('pref-reduced-motion', isReduced);
      updateMotionButton(toggleBtn, isReduced);
      showToast(isReduced ? 'Animasi dinonaktifkan (Reduced Motion)' : 'Animasi transportasi diaktifkan kembali');
    });
  }
}

function updateMotionButton(btn, isReduced) {
  btn.setAttribute('aria-pressed', isReduced);
  btn.title = isReduced ? 'Aktifkan Animasi' : 'Kurangi Animasi';
  const label = btn.querySelector('.motion-label');
  if (label) label.textContent = isReduced ? 'Animasi: Nonaktif' : 'Kurangi Animasi';
}

// --- 9. Toast Notifications ---
function initToast() {
  if (!document.getElementById('toast-container')) {
    const container = document.createElement('div');
    container.id = 'toast-container';
    container.className = 'toast-container';
    document.body.appendChild(container);
  }
}

function showToast(message, duration = 3000) {
  const container = document.getElementById('toast-container');
  if (!container) return;
  
  const toast = document.createElement('div');
  toast.className = 'toast';
  toast.innerHTML = `
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: #A7C66A">
      <polyline points="20 6 9 17 4 12"></polyline>
    </svg>
    <span>${message}</span>
  `;
  container.appendChild(toast);
  
  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateY(8px)';
    toast.style.transition = 'all 0.2s ease';
    setTimeout(() => toast.remove(), 200);
  }, duration);
}

// --- 10. Copy Email to Clipboard ---
function initCopyEmail() {
  document.querySelectorAll('[data-copy-email]').forEach(btn => {
    btn.addEventListener('click', async (e) => {
      e.preventDefault();
      const email = btn.getAttribute('data-copy-email') || 'mirzawibi@gmail.com';
      try {
        if (navigator.clipboard && window.isSecureContext) {
          await navigator.clipboard.writeText(email);
        } else {
          const textArea = document.createElement('textarea');
          textArea.value = email;
          document.body.appendChild(textArea);
          textArea.select();
          document.execCommand('copy');
          document.body.removeChild(textArea);
        }
        showToast(`Alamat email ${email} berhasil disalin ke clipboard!`);
      } catch (err) {
        showToast(`Email: ${email}`);
      }
    });
  });
}

// --- 11. Interactive Scenario Switcher ---
function initScenarioSwitcher() {
  const switchers = document.querySelectorAll('.scenario-switcher-card');
  switchers.forEach(card => {
    const tabBtns = card.querySelectorAll('.scenario-tab-btn');
    const panels = card.querySelectorAll('.scenario-panel');
    
    tabBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const targetId = btn.getAttribute('data-scenario-target');
        
        tabBtns.forEach(b => b.classList.remove('active'));
        panels.forEach(p => p.classList.remove('active'));
        
        btn.classList.add('active');
        const activePanel = card.querySelector(`#panel-${targetId}`);
        if (activePanel) {
          activePanel.classList.add('active');
          activePanel.style.animation = 'panelFadeIn 0.3s ease forwards';
        }
      });
    });
  });
}

// --- 12. High-Res Modal Viewer ---
function initModalViewer() {
  let modal = document.getElementById('map-modal');
  if (!modal) {
    modal = document.createElement('div');
    modal.id = 'map-modal';
    modal.className = 'modal-overlay';
    modal.innerHTML = `
      <div class="modal-dialog">
        <button class="modal-close-btn" id="modal-close" aria-label="Tutup Pratinjau">&times;</button>
        <div class="modal-img-container">
          <img id="modal-image" src="" alt="Pratinjau Resolusi Penuh" />
        </div>
      </div>
    `;
    document.body.appendChild(modal);
    
    modal.addEventListener('click', (e) => {
      if (e.target === modal || e.target.id === 'modal-close') {
        closeModal();
      }
    });
    
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && modal.classList.contains('active')) {
        closeModal();
      }
    });
  }
  
  document.querySelectorAll('[data-zoom-img]').forEach(el => {
    el.addEventListener('click', () => {
      const src = el.getAttribute('data-zoom-img');
      const modalImg = document.getElementById('modal-image');
      if (modalImg && src) {
        modalImg.src = src;
        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
      }
    });
  });
}

function closeModal() {
  const modal = document.getElementById('map-modal');
  if (modal) {
    modal.classList.remove('active');
    document.body.style.overflow = '';
  }
}

// --- 13. CV Accordion & Filter ---
function initCvAccordion() {
  document.querySelectorAll('.cv-card-header').forEach(header => {
    header.addEventListener('click', () => {
      const card = header.closest('.cv-card');
      if (card) {
        card.classList.toggle('open');
      }
    });
  });
  
  const openAllBtn = document.getElementById('cv-open-all');
  const closeAllBtn = document.getElementById('cv-close-all');
  
  if (openAllBtn) {
    openAllBtn.addEventListener('click', () => {
      document.querySelectorAll('.cv-card').forEach(c => c.classList.add('open'));
    });
  }
  
  if (closeAllBtn) {
    closeAllBtn.addEventListener('click', () => {
      document.querySelectorAll('.cv-card').forEach(c => c.classList.remove('open'));
    });
  }
}

// --- 14. Project Catalog Instant Fun Tactile Pop Filter (User Request) ---
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
      const targetUrl = new URL(href, window.location.href);
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

// --- 15. Mobile Navigation Drawer ---
function initMobileNav() {
  const menuBtn = document.getElementById('mobile-menu-toggle');
  const navDrawer = document.getElementById('mobile-nav-drawer');
  
  if (menuBtn && navDrawer) {
    menuBtn.addEventListener('click', () => {
      const isOpen = navDrawer.classList.toggle('open');
      menuBtn.setAttribute('aria-expanded', isOpen);
    });
  }
}

// --- 16. Interactive Capability Pillars Console ---
function initPillarTabs() {
  const btns = document.querySelectorAll('.pillar-nav-btn');
  const panels = document.querySelectorAll('.pillar-panel');
  if (!btns.length || !panels.length) return;

  btns.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetId = btn.getAttribute('data-pillar-tab');
      btns.forEach(b => b.classList.remove('active'));
      panels.forEach(p => p.classList.remove('active'));

      btn.classList.add('active');
      const targetPanel = document.getElementById(targetId);
      if (targetPanel) {
        targetPanel.classList.add('active');
        const fills = targetPanel.querySelectorAll('.skill-fill');
        fills.forEach(fill => {
          const targetW = fill.style.width;
          fill.style.width = '0%';
          setTimeout(() => { fill.style.width = targetW; }, 60);
        });
      }
    });
  });
}

// --- 17. Interactive Slide Deck Explorer (User Request 6) ---
function initSlideDeckPlayer() {
  const container = document.querySelector('.slide-deck-container');
  if (!container) return;

  const frames = container.querySelectorAll('.slide-frame');
  const thumbs = container.querySelectorAll('.slide-thumb-btn');
  const counter = container.querySelector('#slide-deck-counter');
  const prevBtn = container.querySelector('#btn-slide-prev');
  const nextBtn = container.querySelector('#btn-slide-next');

  if (!frames.length) return;

  let currentIndex = 0;
  const total = frames.length;

  const goToSlide = (index) => {
    if (index < 0) index = total - 1;
    if (index >= total) index = 0;
    currentIndex = index;

    frames.forEach((f, i) => {
      f.classList.toggle('active', i === currentIndex);
    });

    thumbs.forEach((t, i) => {
      t.classList.toggle('active', i === currentIndex);
      if (i === currentIndex) {
        t.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
      }
    });

    if (counter) {
      counter.textContent = `Slide ${currentIndex + 1} dari ${total}`;
    }
  };

  if (prevBtn) prevBtn.addEventListener('click', () => goToSlide(currentIndex - 1));
  if (nextBtn) nextBtn.addEventListener('click', () => goToSlide(currentIndex + 1));

  thumbs.forEach((t, i) => {
    t.addEventListener('click', () => goToSlide(i));
  });

  document.addEventListener('keydown', (e) => {
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
    if (e.key === 'ArrowLeft') {
      goToSlide(currentIndex - 1);
    } else if (e.key === 'ArrowRight') {
      goToSlide(currentIndex + 1);
    }
  });
}

// --- 18. Interactive CV Subject Navigator (User Request 9) ---
function initCvSubjectFilter() {
  const tabs = document.querySelectorAll('[data-cv-subject]');
  const blocks = document.querySelectorAll('.cv-section-block');
  if (!tabs.length || !blocks.length) return;

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      const target = tab.getAttribute('data-cv-subject');
      tabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');

      if (target === 'all') {
        blocks.forEach(b => {
          b.style.display = 'block';
          b.classList.add('reveal-visible');
        });
      } else {
        blocks.forEach(b => {
          if (b.id === `subjek-${target}`) {
            b.style.display = 'block';
            b.classList.add('reveal-visible');
            b.scrollIntoView({ behavior: 'smooth', block: 'start' });
          } else {
            b.style.display = 'none';
          }
        });
      }
    });
  });
}

// --- 19. Halte Menuju Dunia Saya - Canvas Intro Listener ---
function initHalteIntroListener() {
  window.addEventListener('halte-intro:done', () => {
    document.querySelectorAll('.hero-section .reveal').forEach(el => {
      el.classList.add('reveal-visible');
    });
  });
}

// --- 20. Interactive CV Experience Category Filter (PRD Section 5.2 / 7.2) ---
function initCvExperienceFilter() {
  const filterBtns = document.querySelectorAll('.cv-filter-btn');
  const expCards = document.querySelectorAll('.cv-experience-card');
  const countEl = document.getElementById('cv-active-count');
  if (!filterBtns.length || !expCards.length) return;

  filterBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const filterId = btn.getAttribute('data-filter-id');
      const rawTags = btn.getAttribute('data-filter-tags') || '';
      const filterTags = rawTags ? rawTags.split(',').map(t => t.trim().toLowerCase()).filter(Boolean) : [];

      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      let visibleCount = 0;
      expCards.forEach(card => {
        const cardTags = (card.getAttribute('data-tags') || '').toLowerCase().split(' ');
        let matches = false;

        if (filterId === 'semua' || filterTags.length === 0) {
          matches = true;
        } else {
          matches = filterTags.some(t => cardTags.includes(t));
        }

        if (matches) {
          card.style.display = '';
          visibleCount++;
        } else {
          card.style.display = 'none';
        }
      });

      if (countEl) {
        if (filterId === 'semua') {
          countEl.textContent = `Menampilkan seluruh ${visibleCount} pengalaman`;
        } else {
          countEl.textContent = `Menampilkan ${visibleCount} dari ${expCards.length} pengalaman (${btn.textContent.trim()})`;
        }
      }

      if (window.history && window.history.replaceState) {
        const url = new URL(window.location.href);
        if (filterId === 'semua') {
          url.searchParams.delete('filter');
        } else {
          url.searchParams.set('filter', filterId);
        }
        window.history.replaceState(null, '', url.toString());
      }
    });
  });
}


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

// --- 22. Enhanced Timeline Station & Sliding Capsule Tracker (Simple & Clear Rail) ---
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
