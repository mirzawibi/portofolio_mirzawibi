import urllib.request

endpoints = ['/', '/karya', '/cv']
for ep in endpoints:
    url = f'http://127.0.0.1:8000{ep}'
    with urllib.request.urlopen(url) as res:
        assert res.status == 200
        html = res.read().decode('utf-8')
        print(f"Verified {ep}: 200 OK, length {len(html)}")
        if ep == '/':
            assert 'metro-timeline-rail-system' in html
            assert 'metro-progress-fill' in html
            assert 'metro-sliding-capsule' in html
            assert 'candle-interactive-zone' in html
            assert '0 -18 440 115' in html # unclipped train viewBox
        if ep == '/karya':
            assert 'catalog-tab-btn' in html
            assert 'catalog-projects-grid' in html

print("ALL LIVE ENDPOINTS AND ELEMENTS VERIFIED SUCCESSFULLY!")
