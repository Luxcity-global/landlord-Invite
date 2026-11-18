import subprocess
import os

html_path = r"C:\Users\ESMIS 2601\.gemini\antigravity\scratch\proptii-30day-motion\src\design-partner-one-pager-v2.html"
cr = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

probe = """
<script>
window.addEventListener('load', () => {
  setTimeout(() => {
    const stage = document.querySelector('.hero-stage').getBoundingClientRect();
    const wrap = document.querySelector('.hero-photo-wrap').getBoundingClientRect();
    const photo = document.querySelector('.hero-photo').getBoundingClientRect();
    const copy = document.querySelector('.hero-copy').getBoundingClientRect();
    const data = JSON.stringify({
      stage: {top: stage.top, bottom: stage.bottom, height: stage.height},
      wrap: {top: wrap.top, bottom: wrap.bottom, height: wrap.height},
      photo: {top: photo.top, bottom: photo.bottom, height: photo.height},
      copy: {top: copy.top, bottom: copy.bottom, height: copy.height}
    });
    document.title = 'RESULT:' + data;
  }, 100);
});
</script>
"""

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

temp_html = r"C:\Users\ESMIS 2601\.gemini\antigravity\scratch\proptii-30day-motion\temp_measure.html"
with open(temp_html, "w", encoding="utf-8") as f:
    f.write(content.replace("</body>", probe + "</body>"))

cmd = [
    cr,
    "--headless=new",
    "--disable-gpu",
    "--window-size=1440,950",
    "--virtual-time-budget=2000",
    "--dump-dom",
    f"file:///{temp_html}"
]
res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
for line in res.stdout.splitlines():
    if "RESULT:" in line:
        print(line)
