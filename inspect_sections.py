from bs4 import BeautifulSoup
import re

for ver, path in [('v1', r'C:\Users\ESMIS 2601\.gemini\antigravity\scratch\proptii-30day-motion\src\design-partner-one-pager.html'),
                  ('v2', r'C:\Users\ESMIS 2601\.gemini\antigravity\scratch\proptii-30day-motion\src\design-partner-one-pager-v2.html')]:
    print(f"=== {ver} ===")
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    for tag in soup.find_all(['h1', 'h2', 'h3', 'section']):
        text = tag.get_text(strip=True)[:60]
        classes = tag.get('class', [])
        tag_id = tag.get('id', '')
        print(f"<{tag.name} id='{tag_id}' class='{classes}'> {text}")
