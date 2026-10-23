with open('static/css/main.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Replace the timeline sliding indicator block
old_timeline_spine = """.timeline-sliding-indicator {
  position: absolute;
  top: 0;
  left: 50%;
  transform: translate(-50%, 0);
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: #14211C;
  border: 2px solid #84A950;
  box-shadow: 0 0 16px rgba(132, 169, 80, 0.65), 0 2px 8px rgba(0,0,0,0.4);
  display: flex;
  align-items: center;
  justify-content: center;
  will-change: transform;
  transition: transform 0.1s linear, border-color 0.2s ease;
  z-index: 4;
}
.timeline-sliding-indicator .scroller-pulse {
  position: absolute;
  inset: -4px;
  border-radius: 50%;
  border: 1.5px solid #84A950;
  animation: scrollerBeaconPulse 2s infinite ease-out;
}
@keyframes scrollerBeaconPulse {
  0% { transform: scale(0.9); opacity: 0.85; }
  100% { transform: scale(1.45); opacity: 0; }
}
.timeline-sliding-indicator .scroller-badge {
  font-size: 0.625rem;
  font-weight: 800;
  font-family: var(--font-mono, monospace);
  color: #FEF08A;
  letter-spacing: 0.02em;
}"""

new_timeline_spine = """.timeline-sliding-indicator {
  position: absolute;
  top: 0;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 14px;
  height: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  pointer-events: none;
  z-index: 4;
  will-change: transform;
  transition: transform 0.08s linear;
}
.timeline-slider-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: #FEF08A;
  border: 2px solid #14211C;
  box-shadow: 0 0 8px #FEF08A, 0 0 12px #84A950;
}
.timeline-slider-pulse {
  position: absolute;
  inset: -3px;
  border-radius: 50%;
  border: 1.5px solid #84A950;
  animation: timelineDotPulse 1.8s infinite ease-out;
}
@keyframes timelineDotPulse {
  0% { transform: scale(0.85); opacity: 0.9; }
  100% { transform: scale(2.2); opacity: 0; }
}"""

css_norm = css.replace('\r\n', '\n')
old_tl_norm = old_timeline_spine.replace('\r\n', '\n')
new_tl_norm = new_timeline_spine.replace('\r\n', '\n')

assert old_tl_norm in css_norm, "old_timeline_spine not found"
css_norm = css_norm.replace(old_tl_norm, new_tl_norm, 1)

# 2. Neutralize the two duplicate 2.2s !important rules so speed is dynamic
css_norm = css_norm.replace(
    "animation: mrtCinematicGlideSlower 2.2s cubic-bezier(0.25, 1, 0.35, 1) forwards !important;",
    "animation: mrtCinematicGlide var(--mrt-speed, 0.85s) cubic-bezier(0.2, 0.8, 0.25, 1) forwards !important;"
)

# 3. Add train liveries, candle hover revelation, and card-to-card transition styles at the end
additional_rules = """

/* --- Dynamic Multi-Livery Train Styling (User Request 6) --- */
.mrt-train-carriage.livery-krl #svg-train-body { fill: url(#trainBodyGradKRL); stroke: #A7C66A; }
.mrt-train-carriage.livery-krl #svg-train-stripe { fill: #D97736; }

.mrt-train-carriage.livery-metro #svg-train-body { fill: url(#trainBodyGradMetro); stroke: #38BDF8; }
.mrt-train-carriage.livery-metro #svg-train-stripe { fill: #38BDF8; }

.mrt-train-carriage.livery-lrt #svg-train-body { fill: url(#trainBodyGradLRT); stroke: #F87171; }
.mrt-train-carriage.livery-lrt #svg-train-stripe { fill: #FEF08A; }

/* --- Candle Revelation on Hover Only (User Request 5) --- */
.candle-revelation-message {
  opacity: 0 !important;
  transform: translateY(14px) scale(0.96) !important;
  pointer-events: none !important;
  transition: opacity 0.35s ease, transform 0.35s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.35s ease !important;
}
.grand-candle-interactive-zone:hover .candle-revelation-message,
.grand-candle-interactive-zone:focus-within .candle-revelation-message,
.grand-candle-interactive-zone.active .candle-revelation-message {
  opacity: 1 !important;
  transform: translateY(0) scale(1) !important;
  pointer-events: auto !important;
  border-color: #FFFFFF !important;
  box-shadow: 0 12px 35px rgba(0, 0, 0, 0.9), 0 0 30px rgba(254, 240, 138, 0.6) !important;
}

.candle-hover-hint {
  font-size: 0.75rem;
  color: var(--color-hero-muted, #9BB0A3);
  margin-top: 0.85rem;
  display: flex;
  align-items: center;
  gap: 0.4rem;
  opacity: 0.8;
  transition: opacity 0.3s ease;
}
.grand-candle-interactive-zone:hover .candle-hover-hint,
.grand-candle-interactive-zone:focus-within .candle-hover-hint,
.grand-candle-interactive-zone.active .candle-hover-hint {
  opacity: 0;
  pointer-events: none;
}
.hint-pulse {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #FEF08A;
  box-shadow: 0 0 6px #FEF08A;
  animation: hintBlink 1.5s infinite alternate;
}
@keyframes hintBlink {
  0% { opacity: 0.35; transform: scale(0.9); }
  100% { opacity: 1; transform: scale(1.25); }
}

/* --- Card-to-card Smooth In-Page Transition (User Request 7) --- */
.project-card.card-fading {
  opacity: 0 !important;
  transform: scale(0.96) translateY(8px) !important;
  transition: opacity 0.16s ease-out, transform 0.16s ease-out !important;
}
.project-card.card-entering {
  opacity: 1 !important;
  transform: scale(1) translateY(0) !important;
  transition: opacity 0.25s var(--ease-spring), transform 0.25s var(--ease-spring) !important;
}
"""

css_norm += additional_rules

with open('static/css/main.css', 'w', encoding='utf-8') as f:
    f.write(css_norm)

print("SUCCESS: Updated static/css/main.css with simplified timeline, liveries, candle hover, and card transitions!")
