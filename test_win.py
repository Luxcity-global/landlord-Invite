import subprocess, re, os

cr = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
with open('test_win.html', 'w') as f:
    f.write('<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width, initial-scale=1"></head><body><script>document.title = "INNER:" + window.innerWidth;</script></body></html>')

res = subprocess.run([cr, '--headless=new', '--disable-gpu', '--virtual-time-budget=1000', '--window-size=390,1600', '--dump-dom', 'test_win.html'], capture_output=True, text=True)
print(re.findall(r'INNER:\d+', res.stdout))
os.remove('test_win.html')
