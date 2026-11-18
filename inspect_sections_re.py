import re

for ver, path in [('v1', r'C:\Users\ESMIS 2601\.gemini\antigravity\scratch\proptii-30day-motion\src\design-partner-one-pager.html'),
                  ('v2', r'C:\Users\ESMIS 2601\.gemini\antigravity\scratch\proptii-30day-motion\src\design-partner-one-pager-v2.html')]:
    print(f"\n=== {ver} ({path}) ===")
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for idx, line in enumerate(lines):
        if re.search(r'<(h1|h2|h3|section|header|footer)\b', line, re.IGNORECASE) or 'class="section' in line or 'class="deal' in line:
            print(f"L{idx+1}: {line.strip()[:100]}")
