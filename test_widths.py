import subprocess
import os
from PIL import Image

cr = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
html_path = r"C:\Users\ESMIS 2601\.gemini\antigravity\scratch\proptii-30day-motion\src\design-partner-one-pager-v2.html"
out_dir = r"C:\Users\ESMIS 2601\.gemini\antigravity\brain\613858a4-7b73-4a34-bfa4-af3bec7a516a\scratch"

widths = [1024, 1200, 1280, 1366, 1536, 1600, 1920]

for w in widths:
    out_png = os.path.join(out_dir, f"test_w_{w}.png")
    temp_profile = os.path.join(os.environ.get("TEMP", "C:\\temp"), f"chr_shot_{w}")
    cmd = [
        cr,
        "--headless=new",
        "--disable-gpu",
        f"--user-data-dir={temp_profile}",
        f"--screenshot={out_png}",
        f"--window-size={w},900",
        "--virtual-time-budget=3000",
        f"file:///{html_path}"
    ]
    subprocess.run(cmd, capture_output=True)
    if os.path.exists(out_png):
        im = Image.open(out_png)
        # Check center of image around hero stage bottom
        # Let's save a crop around the bottom of .hero-stage
        crop = im.crop((int(w * 0.4), 450, int(w * 0.95), 850))
        crop.save(os.path.join(out_dir, f"crop_w_{w}.png"))
        print(f"Width {w}: rendered successfully")
