import subprocess
import os
import sys
from PIL import Image

cr = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
out_dir = r"C:\Users\ESMIS 2601\.gemini\antigravity\brain\613858a4-7b73-4a34-bfa4-af3bec7a516a\scratch"
out_png = os.path.join(out_dir, "v2_full.png")
url = "file:///C:/Users/ESMIS 2601/.gemini/antigravity/scratch/proptii-30day-motion/src/design-partner-one-pager-v2.html"

temp_profile = os.path.join(os.environ.get("TEMP", "C:\\temp"), "chr_shot")

cmd = [
    cr,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={temp_profile}",
    f"--screenshot={out_png}",
    "--window-size=1440,950",
    "--virtual-time-budget=3000",
    url
]
print("Running chrome...")
res = subprocess.run(cmd, capture_output=True, text=True)
print("Returncode:", res.returncode)
if os.path.exists(out_png):
    print("Screenshot captured, size:", os.path.getsize(out_png))
    im = Image.open(out_png)
    print("Dimensions:", im.size)
    crop = im.crop((100, 150, 1340, 850))
    crop_path = os.path.join(out_dir, "v2_hero_crop_current.png")
    crop.save(crop_path)
    print("Saved crop:", crop_path)
else:
    print("Screenshot failed to save")
