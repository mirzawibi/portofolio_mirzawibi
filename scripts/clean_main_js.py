with open('static/js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Remove initTimelineProgressTracker from DOMContentLoaded
js = js.replace('  initTimelineProgressTracker();\n', '')

# 2. Remove initTimelineProgressTracker function and replace initCandleInteractions
old_section = """// --- 22. Interactive Metro Timeline Progress Tracker (User Request 2) ---
function initTimelineProgressTracker() {
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

new_section = """// --- 22. Living Philosophy Candle Interactive Dynamics (Reveals on Hover Only) ---
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

js_norm = js.replace('\r\n', '\n')
old_sec_norm = old_section.replace('\r\n', '\n')
new_sec_norm = new_section.replace('\r\n', '\n')

assert old_sec_norm in js_norm, "old_section not found in static/js/main.js"
js_norm = js_norm.replace(old_sec_norm, new_sec_norm, 1)

with open('static/js/main.js', 'w', encoding='utf-8') as f:
    f.write(js_norm)

print("SUCCESS: Removed initTimelineProgressTracker and updated initCandleInteractions in static/js/main.js")
