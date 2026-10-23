with open('static/css/main.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update mrt carriage dimensions to avoid clipping
old_carriage_css = """.mrt-train-carriage {
  position: absolute;
  top: -72px;
  left: -460px;
  width: 380px;
  height: 90px;
  transform: translate3d(0, 0, 0);
  filter: drop-shadow(0 0 35px rgba(132, 169, 80, 0.85));
  overflow: visible;
}

.mrt-train-svg {
  width: 380px;
  height: 90px;
  display: block;
}"""

new_carriage_css = """.transit-cinematic-stage {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100vw;
  overflow: visible !important;
  position: relative;
  min-height: 180px;
}

.transit-speed-tunnel {
  position: absolute;
  left: 0;
  right: 0;
  height: 120px;
  top: 50%;
  transform: translateY(-50%);
  background: radial-gradient(ellipse at 50% 50%, rgba(132, 169, 80, 0.18) 0%, rgba(20, 33, 28, 0) 75%);
  pointer-events: none;
  z-index: 1;
}

.transit-track-line {
  position: relative;
  width: 100vw;
  height: 12px;
  background: linear-gradient(90deg, rgba(132, 169, 80, 0.1) 0%, rgba(132, 169, 80, 0.95) 50%, rgba(132, 169, 80, 0.1) 100%);
  margin-bottom: 2.5rem;
  overflow: visible !important;
  box-shadow: 0 0 35px rgba(132, 169, 80, 0.6);
  z-index: 2;
}

.mrt-train-carriage {
  position: absolute;
  top: -95px;
  left: -520px;
  width: 440px;
  height: 115px;
  transform: translate3d(0, 0, 0);
  filter: drop-shadow(0 0 35px rgba(132, 169, 80, 0.85));
  overflow: visible !important;
  z-index: 10;
}

.mrt-train-svg {
  width: 440px;
  height: 115px;
  display: block;
  overflow: visible !important;
}"""

css_norm = css.replace('\r\n', '\n')
old_carr_norm = old_carriage_css.replace('\r\n', '\n')
new_carr_norm = new_carriage_css.replace('\r\n', '\n')

assert old_carr_norm in css_norm, "old_carriage_css not found"
css_norm = css_norm.replace(old_carr_norm, new_carr_norm, 1)

# 2. Add full high-clarity Sliding Bar CSS and Candle Rework at the end of static/css/main.css
additional_block = """

/* =========================================================================
   HIGH-CLARITY SIMPLE SLIDING BAR SYSTEM (User Request: Rombak Jelas & Rapi)
   ========================================================================= */
.transit-metro-timeline {
  position: relative;
  padding-left: 96px;
  margin: 3.5rem 0;
}

/* Dedicated Clearly Visible Vertical Rail */
.metro-timeline-rail-system {
  position: absolute;
  left: 36px;
  top: 24px;
  bottom: 48px;
  width: 6px;
  pointer-events: none;
  z-index: 2;
}
.metro-rail-track-line {
  position: relative;
  width: 100%;
  height: 100%;
  background: rgba(255, 255, 255, 0.14);
  border-radius: 999px;
  box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.6);
}
.metro-rail-fill-bar {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 0%;
  background: linear-gradient(180deg, #84A950 0%, #315C37 45%, #D97736 100%);
  border-radius: 999px;
  box-shadow: 0 0 12px rgba(132, 169, 80, 0.75);
  transition: height 0.08s linear;
}

/* Clearly Visible Sliding Commuter Beacon Capsule */
.metro-sliding-capsule {
  position: absolute;
  top: 0;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: #14211C;
  border: 2.5px solid #FEF08A;
  box-shadow: 0 0 16px rgba(254, 240, 138, 0.95), 0 2px 8px rgba(0, 0, 0, 0.8);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 5;
  transition: transform 0.08s linear;
}
.capsule-core {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: #FEF08A;
}
.capsule-beacon {
  position: absolute;
  inset: -4px;
  border-radius: 50%;
  border: 1.5px solid #FEF08A;
  animation: beaconWave 1.6s infinite ease-out;
}
@keyframes beaconWave {
  0% { transform: scale(0.85); opacity: 0.9; }
  100% { transform: scale(2.2); opacity: 0; }
}

/* High-Contrast Clear Station Points */
.metro-station-badge-node {
  position: absolute;
  left: -96px;
  top: 1rem;
  width: 78px;
  display: flex;
  flex-direction: column;
  align-items: center;
  z-index: 4;
}
.metro-badge-core {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background: #0E1713;
  border: 2.5px solid rgba(132, 169, 80, 0.5);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform 0.25s var(--ease-spring), border-color 0.25s ease, box-shadow 0.25s ease;
}
.metro-timeline-item.station-active .metro-badge-core {
  border-color: #FEF08A !important;
  box-shadow: 0 0 22px rgba(254, 240, 138, 0.75), 0 4px 16px rgba(0, 0, 0, 0.8) !important;
  transform: scale(1.08) !important;
}
.station-code-pill {
  font-family: var(--font-mono, monospace);
  font-size: 0.725rem;
  font-weight: 800;
  color: #FEF08A;
  letter-spacing: 0.02em;
}

/* =========================================================================
   REWORKED CANDLE: DEEP REALISM & SEAMLESS REVELATION (User Request)
   ========================================================================= */
.sculpted-candle-pillar {
  position: relative;
  width: 38px;
  height: 92px;
  background: linear-gradient(90deg, #CBB794 0%, #E8DCC4 22%, #FFFDF8 50%, #E8DCC4 78%, #C1AC88 100%);
  border-radius: 6px 6px 3px 3px;
  box-shadow: inset -3px 0 8px rgba(0, 0, 0, 0.28), inset 3px 0 8px rgba(255, 255, 255, 0.6), 0 12px 28px rgba(0, 0, 0, 0.7);
  z-index: 3;
}

.living-candle-flame {
  position: absolute;
  top: -46px;
  left: 50%;
  transform: translateX(-50%);
  width: 22px;
  height: 46px;
  transform-origin: center bottom;
  animation: seamlessLivingFlame 2.6s ease-in-out infinite;
  z-index: 6;
  filter: drop-shadow(0 0 18px rgba(245, 158, 11, 0.85)) drop-shadow(0 -4px 10px rgba(254, 240, 138, 0.65));
  transition: transform 0.16s ease-out, filter 0.25s ease;
}
.grand-candle-interactive-zone:hover .living-candle-flame,
.grand-candle-interactive-zone.candle-active .living-candle-flame {
  transform: translateX(-50%) scale(1.22, 1.25);
  filter: drop-shadow(0 0 32px rgba(245, 158, 11, 0.98)) drop-shadow(0 -6px 18px rgba(254, 240, 138, 0.95));
}

.candle-revelation-message {
  margin-top: 1.25rem;
  background: rgba(14, 23, 19, 0.96);
  border: 1.5px solid #FEF08A;
  border-radius: var(--radius-full);
  padding: 0.6rem 1.6rem;
  font-size: 0.95rem;
  font-weight: 800;
  color: #FEF08A;
  letter-spacing: 0.02em;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.8), 0 0 25px rgba(254, 240, 138, 0.45);
  display: flex;
  align-items: center;
  gap: 0.6rem;
  opacity: 0;
  pointer-events: none;
  transform: translateY(14px) scale(0.95);
  transition: opacity 0.3s cubic-bezier(0.34, 1.56, 0.64, 1), transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.3s ease;
  z-index: 10;
}
.grand-candle-interactive-zone:hover .candle-revelation-message,
.grand-candle-interactive-zone.candle-active .candle-revelation-message {
  opacity: 1 !important;
  pointer-events: auto !important;
  transform: translateY(0) scale(1) !important;
  box-shadow: 0 12px 35px rgba(0, 0, 0, 0.9), 0 0 35px rgba(254, 240, 138, 0.7) !important;
}

.candle-hover-hint {
  font-size: 0.775rem;
  color: var(--color-hero-muted, #9BB0A3);
  margin-top: 0.85rem;
  display: flex;
  align-items: center;
  gap: 0.45rem;
  opacity: 0.85;
  transition: opacity 0.25s ease;
}
.grand-candle-interactive-zone:hover .candle-hover-hint,
.grand-candle-interactive-zone.candle-active .candle-hover-hint {
  opacity: 0;
  pointer-events: none;
}
"""

css_norm += additional_block

with open('static/css/main.css', 'w', encoding='utf-8') as f:
    f.write(css_norm)

print("SUCCESS: Updated static/css/main.css with carriage unclipped styles, high-clarity sliding rail, and reworked candle!")
