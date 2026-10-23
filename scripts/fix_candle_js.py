with open('static/js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

old_candle_fn = """// --- 22. Living Philosophy Candle Interactive Dynamics (Reveals on Hover Only) ---
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

new_candle_fn = """// --- 22. Living Philosophy Candle Interactive Dynamics (Reveals on Hover Only) ---
function initCandleInteractions() {
  const zone = document.getElementById('candle-interactive-zone');
  const flame = document.getElementById('realistic-candle-flame');
  const halo = document.getElementById('candle-ambient-halo');
  const hint = document.getElementById('candle-hover-hint');
  if (!zone || !flame) return;

  const reveal = () => {
    zone.classList.add('candle-revealed');
    flame.classList.add('flame-ignited');
    if (halo) halo.style.opacity = '1';
    if (hint) hint.style.opacity = '0';
  };

  const conceal = () => {
    zone.classList.remove('candle-revealed');
    flame.classList.remove('flame-ignited');
    flame.style.transform = '';
    if (halo) halo.style.opacity = '';
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
  
  // Mobile tap / touch toggle
  zone.addEventListener('click', () => {
    if (zone.classList.contains('candle-revealed')) {
      conceal();
    } else {
      reveal();
      setTimeout(conceal, 3800);
    }
  });
}"""

js_norm = js.replace('\r\n', '\n')
old_fn_norm = old_candle_fn.replace('\r\n', '\n')
new_fn_norm = new_candle_fn.replace('\r\n', '\n')

assert old_fn_norm in js_norm, "old_candle_fn not found"
js_norm = js_norm.replace(old_fn_norm, new_fn_norm, 1)

with open('static/js/main.js', 'w', encoding='utf-8') as f:
    f.write(js_norm)

print("SUCCESS: Updated initCandleInteractions in static/js/main.js")
