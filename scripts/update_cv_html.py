with open('templates/cv.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Change Uraian Kontribusi Nyata: to Kontribusi:
c = c.replace(
    '<div style="font-size:0.8rem;font-weight:700;color:var(--color-text-light);text-transform:uppercase;margin-bottom:0.4rem;">Uraian Kontribusi Nyata:</div>',
    '<div style="font-size:0.825rem;font-weight:700;color:var(--color-primary);text-transform:uppercase;letter-spacing:0.04em;margin-bottom:0.5rem;">Kontribusi:</div>'
)

# 2. Update Education section with clean, executive layout
old_edu_chunk = """      <div style="display:flex;flex-direction:column;gap:1.25rem;">
        {% for edu in education %}
        <div style="background:var(--color-surface);border:1px solid var(--color-border);border-radius:var(--radius-lg);padding:1.5rem;box-shadow:var(--shadow-sm);">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:0.75rem;margin-bottom:0.5rem;">
            <div>
              <div style="display:flex;align-items:center;gap:0.6rem;flex-wrap:wrap;margin-bottom:0.25rem;">
                <h3 style="font-size:1.15rem;font-weight:700;color:var(--color-text-main);margin:0;">{{ edu.institution }}</h3>
                {% if edu.degree %}
                <span class="badge badge-primary" style="font-size:0.7rem;">{{ edu.degree }}</span>
                {% endif %}
              </div>
              <div style="font-size:0.95rem;font-weight:600;color:var(--color-primary);">
                {{ edu.field }}
              </div>
            </div>
            <span class="cv-card-period">{{ edu.period }}</span>
          </div>

          {% if edu.gpa %}
          <div style="margin-top:0.75rem;display:inline-flex;align-items:center;gap:0.5rem;background:rgba(49,92,55,0.08);border:1px solid rgba(49,92,55,0.2);border-radius:var(--radius-full);padding:0.35rem 0.85rem;">
            <span style="font-size:0.8rem;font-weight:700;color:var(--color-primary);">Indeks Prestasi Kumulatif (IPK):</span>
            <span style="font-size:0.9rem;font-weight:800;color:var(--color-primary);">{{ edu.gpa }}</span>
            <span style="font-size:0.75rem;color:var(--color-text-light);">/ 4.00</span>
          </div>
          {% endif %}

          {% if edu.highlights %}
          <ul class="cv-bullets-list" style="margin-top:1rem;">
            {% for h in edu.highlights %}
            <li>{{ h }}</li>
            {% endfor %}
          </ul>
          {% endif %}
        </div>
        {% endfor %}
      </div>"""

new_edu_chunk = """      <div style="display:flex;flex-direction:column;gap:1.25rem;">
        {% for edu in education %}
        <div style="background:var(--color-surface);border:1px solid var(--color-border);border-left:3.5px solid var(--color-primary);border-radius:var(--radius-lg);padding:1.6rem;box-shadow:var(--shadow-sm);transition:transform 0.2s ease, box-shadow 0.2s ease;">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:0.75rem;margin-bottom:0.6rem;">
            <div>
              <div style="display:flex;align-items:center;gap:0.6rem;flex-wrap:wrap;margin-bottom:0.3rem;">
                <h3 style="font-size:1.15rem;font-weight:700;color:var(--color-text-main);margin:0;">{{ edu.institution }}</h3>
                {% if edu.degree %}
                <span class="badge badge-primary" style="font-size:0.72rem;">{{ edu.degree }}</span>
                {% endif %}
              </div>
              <div style="font-size:0.95rem;font-weight:600;color:var(--color-primary);">
                {{ edu.program or edu.field }}
              </div>
              {% if edu.location %}
              <div style="font-size:0.825rem;color:var(--color-text-muted);margin-top:0.25rem;">
                📍 {{ edu.location }}
              </div>
              {% endif %}
            </div>
            <span class="cv-card-period">{{ edu.period }}</span>
          </div>

          {% if edu.gpa %}
          <div style="margin-top:0.6rem;margin-bottom:0.85rem;display:inline-flex;align-items:center;gap:0.45rem;background:rgba(49,92,55,0.08);border:1px solid rgba(49,92,55,0.22);border-radius:var(--radius-full);padding:0.3rem 0.85rem;">
            <span style="font-size:0.8rem;font-weight:700;color:var(--color-primary);">
              {% if '100' in edu.gpa_scale|string %}Nilai Rata-rata Ujian:{% else %}Indeks Prestasi Kumulatif (IPK):{% endif %}
            </span>
            <span style="font-size:0.875rem;font-weight:800;color:var(--color-primary);">{{ edu.gpa }}</span>
            <span style="font-size:0.75rem;color:var(--color-text-light);">/ {{ edu.gpa_scale or '4.00' }}</span>
          </div>
          {% endif %}

          {% if edu.highlights %}
          <div style="font-size:0.8rem;font-weight:700;color:var(--color-text-light);text-transform:uppercase;letter-spacing:0.04em;margin-top:0.4rem;margin-bottom:0.4rem;">Pencapaian & Fokus Keilmuan:</div>
          <ul class="cv-bullets-list">
            {% if edu.highlights is string %}
            <li>{{ edu.highlights }}</li>
            {% else %}
              {% for h in edu.highlights %}
              <li>{{ h }}</li>
              {% endfor %}
            {% endif %}
          </ul>
          {% endif %}
        </div>
        {% endfor %}
      </div>"""

c_norm = c.replace('\r\n', '\n')
old_edu_norm = old_edu_chunk.replace('\r\n', '\n')
new_edu_norm = new_edu_chunk.replace('\r\n', '\n')

assert old_edu_norm in c_norm, "old_edu_chunk not found in templates/cv.html"
c_norm = c_norm.replace(old_edu_norm, new_edu_norm, 1)

with open('templates/cv.html', 'w', encoding='utf-8') as f:
    f.write(c_norm)

print("SUCCESS: Updated templates/cv.html (Kontribusi and tidy Education)!")
