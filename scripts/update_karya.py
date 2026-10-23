with open('templates/karya.html', 'r', encoding='utf-8') as f:
    c = f.read()

target = """        <!-- Category Filter Pills with Gliding Rail -->
        <div class="transit-tabs-wrapper" style="flex-wrap:wrap;">
          <div class="transit-gliding-pill"></div>
          {% for cat in categories %}
          <a href="/karya?kategori={{ cat.id }}{% if search_query %}&q={{ search_query }}{% endif %}" 
             class="transit-tab-link {% if selected_category == cat.id %}active{% endif %}">
            <span>{{ cat.label }}</span>
          </a>
          {% endfor %}
        </div>"""

replacement = """        <!-- Category Filter Pills (Glitch-Free Smooth Buttons) -->
        <div class="catalog-category-tabs" role="tablist" aria-label="Kategori Karya">
          {% for cat in categories %}
          <a href="/karya?kategori={{ cat.id }}{% if search_query %}&q={{ search_query }}{% endif %}" 
             class="catalog-tab-btn {% if selected_category == cat.id %}active{% endif %}"
             role="tab"
             aria-selected="{% if selected_category == cat.id %}true{% else %}false{% endif %}">
            <span>{{ cat.label }}</span>
          </a>
          {% endfor %}
        </div>"""

c_norm = c.replace('\r\n', '\n')
target_norm = target.replace('\r\n', '\n')
replacement_norm = replacement.replace('\r\n', '\n')

if target_norm in c_norm:
    c_norm = c_norm.replace(target_norm, replacement_norm, 1)
    with open('templates/karya.html', 'w', encoding='utf-8') as f:
        f.write(c_norm)
    print("SUCCESS: Updated templates/karya.html")
else:
    print("WARNING: Target not found in templates/karya.html")
