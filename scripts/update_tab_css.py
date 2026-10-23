with open('static/css/main.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update catalog-tab-btn styles for instant fun pop
old_tabs_css = """.catalog-tab-btn {
  display: inline-flex;
  align-items: center;
  padding: 0.5rem 1.15rem;
  border-radius: var(--radius-full);
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--color-text-main);
  background-color: var(--color-surface);
  border: 1px solid var(--color-border);
  text-decoration: none;
  cursor: pointer;
  transition: all 0.22s var(--ease-spring);
}
.catalog-tab-btn:hover {
  background-color: rgba(49, 92, 55, 0.08);
  border-color: rgba(49, 92, 55, 0.35);
  color: var(--color-primary);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(20, 33, 28, 0.08);
}
.catalog-tab-btn.active {
  background-color: var(--color-primary) !important;
  border-color: var(--color-primary) !important;
  color: #FFFFFF !important;
  box-shadow: 0 4px 14px rgba(49, 92, 55, 0.35);
  transform: translateY(-1px);
}"""

new_tabs_css = """.catalog-tab-btn {
  display: inline-flex;
  align-items: center;
  padding: 0.5rem 1.2rem;
  border-radius: var(--radius-full);
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--color-text-main);
  background-color: var(--color-surface);
  border: 1px solid var(--color-border);
  text-decoration: none;
  cursor: pointer;
  user-select: none;
  transition: transform 0.16s cubic-bezier(0.34, 1.56, 0.64, 1), background-color 0.15s ease, border-color 0.15s ease, box-shadow 0.15s ease;
}
.catalog-tab-btn:hover {
  background-color: rgba(49, 92, 55, 0.08);
  border-color: rgba(49, 92, 55, 0.35);
  color: var(--color-primary);
  transform: translateY(-2px) scale(1.03);
  box-shadow: 0 4px 12px rgba(20, 33, 28, 0.08);
}
.catalog-tab-btn:active,
.catalog-tab-btn.tab-popping {
  transform: scale(0.92) !important;
  box-shadow: 0 1px 4px rgba(49, 92, 55, 0.2) !important;
}
.catalog-tab-btn.active {
  background-color: var(--color-primary) !important;
  border-color: var(--color-primary) !important;
  color: #FFFFFF !important;
  box-shadow: 0 4px 16px rgba(49, 92, 55, 0.4) !important;
  transform: scale(1.05) translateY(-1px);
}

/* Instant Fun Card Pop-In Animation */
.project-card.fun-card-pop {
  animation: funCardSpring 0.22s cubic-bezier(0.2, 0.9, 0.3, 1.1) forwards;
}
@keyframes funCardSpring {
  0% { opacity: 0; transform: scale(0.96) translateY(5px); }
  100% { opacity: 1; transform: scale(1) translateY(0); }
}"""

css_norm = css.replace('\r\n', '\n')
old_tabs_norm = old_tabs_css.replace('\r\n', '\n')
new_tabs_norm = new_tabs_css.replace('\r\n', '\n')

assert old_tabs_norm in css_norm, "old_tabs_css not found"
css_norm = css_norm.replace(old_tabs_norm, new_tabs_norm, 1)

with open('static/css/main.css', 'w', encoding='utf-8') as f:
    f.write(css_norm)

print("SUCCESS: Updated static/css/main.css with tactile tab pop styles!")
