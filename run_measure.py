import subprocess, re

cr = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html = r'C:\Users\ESMIS 2601\.gemini\antigravity\scratch\proptii-30day-motion\src\design-partner-one-pager-v2.html'
script = '''<script>
window.addEventListener('DOMContentLoaded', () => {
    const wide = [];
    document.querySelectorAll('*').forEach(el => {
        if (el.scrollWidth > 395) {
            wide.push({tag: el.tagName, id: el.id, cls: el.className.slice(0, 30), sw: el.scrollWidth});
        }
    });
    document.title = 'SCROLLWIDE:' + JSON.stringify(wide);
});
</script>'''

with open(html, 'r', encoding='utf-8') as f:
    c = f.read()
c = c.replace('</body>', script + '</body>')
with open(r'C:\Users\ESMIS 2601\.gemini\antigravity\scratch\proptii-30day-motion\temp_measure.html', 'w', encoding='utf-8') as f:
    f.write(c)

res = subprocess.run([cr, '--headless=new', '--disable-gpu', '--virtual-time-budget=2000', '--dump-dom', '--window-size=390,1600', r'file:///C:/Users/ESMIS 2601/.gemini/antigravity/scratch/proptii-30day-motion/temp_measure.html'], capture_output=True, text=True)
m = re.findall(r'SCROLLWIDE:\[.*?\]', res.stdout)
if m:
    print(m[0])
