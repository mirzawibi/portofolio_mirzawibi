with open('static/css/main.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

additional_css = """

/* --- Polished Interactive Software Live Inspector --- */
.software-live-inspector {
  transition: transform 0.2s var(--ease-spring), border-color 0.2s ease, box-shadow 0.2s ease;
}
.software-live-inspector.inspector-updating {
  transform: translateY(-2px);
  border-color: var(--color-primary) !important;
  box-shadow: 0 8px 24px rgba(49, 92, 55, 0.16) !important;
}

/* --- Timeline Active Station Glow --- */
.metro-timeline-item.station-active-glow .metro-station-badge-node {
  transform: scale(1.05);
  box-shadow: 0 0 20px rgba(132, 169, 80, 0.4);
}
.metro-timeline-item.station-active-glow .station-code-pill {
  background: var(--color-primary);
  color: #FFFFFF;
  border-color: var(--color-primary);
}

/* --- Badges & Executive CV Polishing (User Request 6) --- */
.badge-accent {
  background: rgba(217, 119, 54, 0.12) !important;
  color: #B45309 !important;
  border: 1px solid rgba(217, 119, 54, 0.3) !important;
  font-size: 0.72rem;
  font-weight: 700;
  padding: 0.2rem 0.55rem;
  border-radius: var(--radius-full);
  display: inline-flex;
  align-items: center;
  gap: 0.3rem;
  white-space: nowrap;
}

.badge-transit {
  background: rgba(49, 92, 55, 0.09) !important;
  color: var(--color-primary) !important;
  border: 1px solid rgba(49, 92, 55, 0.22) !important;
  font-size: 0.72rem;
  font-weight: 600;
  padding: 0.2rem 0.55rem;
  border-radius: var(--radius-full);
  display: inline-flex;
  align-items: center;
  gap: 0.3rem;
  white-space: nowrap;
}

/* Polished CV Accordion & Typography */
.cv-card {
  border-left: 3.5px solid transparent !important;
  transition: all 0.22s var(--ease-spring);
}
.cv-card:hover {
  border-left-color: var(--color-primary) !important;
  transform: translateY(-2px);
}
.cv-card.open {
  border-color: rgba(49, 92, 55, 0.28) !important;
  border-left-color: var(--color-primary) !important;
}

.cv-bullets-list li::before {
  content: "▸" !important;
  position: absolute;
  left: 0;
  top: 0;
  color: var(--color-primary);
  font-weight: 800;
  font-size: 1rem;
}

/* Clean CV Subject Tab Strip */
.cv-subject-nav .transit-tabs-wrapper {
  scrollbar-width: none;
  -ms-overflow-style: none;
}
.cv-subject-nav .transit-tabs-wrapper::-webkit-scrollbar {
  display: none;
}
"""

if "/* --- Polished Interactive Software Live Inspector --- */" not in css_content:
    css_content += additional_css
    with open('static/css/main.css', 'w', encoding='utf-8') as f:
        f.write(css_content)
    print("SUCCESS: Appended polished CV and inspector styles to static/css/main.css")
else:
    print("INFO: Styles already present")
