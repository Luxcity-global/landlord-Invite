import subprocess
import os
from PIL import Image

cr = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
html_path = r"C:\Users\ESMIS 2601\.gemini\antigravity\scratch\proptii-30day-motion\src\design-partner-one-pager-v2.html"
out_dir = r"C:\Users\ESMIS 2601\.gemini\antigravity\brain\613858a4-7b73-4a34-bfa4-af3bec7a516a\scratch"

for w in [390, 768]:
    out_png = os.path.join(out_dir, f"test_w_{w}.png")
    temp_profile = os.path.join(os.environ.get("TEMP", "C:\\temp"), f"chr_shot_{w}")
    cmd = [
        cr,
        "--headless=new",
        "--disable-gpu",
        f"--user-data-dir={temp_profile}",
        f"--screenshot={out_png}",
        f"--window-size={w},1000",
        "--virtual-time-budget=3000",
        f"file:///{html_path}"
    ]
    subprocess.run(cmd, capture_output=True)
    if os.path.exists(out_png):
        print(f"Width {w}: rendered successfully")
