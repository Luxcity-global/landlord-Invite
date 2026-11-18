import subprocess
import os
from PIL import Image

cr = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
out_dir = r"C:\Users\ESMIS 2601\.gemini\antigravity\brain\613858a4-7b73-4a34-bfa4-af3bec7a516a\scratch"

for ver, filename in [("v1", "design-partner-one-pager.html"), ("v2", "design-partner-one-pager-v2.html")]:
    url = f"file:///C:/Users/ESMIS 2601/.gemini/antigravity/scratch/proptii-30day-motion/src/{filename}"
    out_png = os.path.join(out_dir, f"fullpage_{ver}.png")
    temp_profile = os.path.join(os.environ.get("TEMP", "C:\\temp"), f"chr_{ver}_full")
    cmd = [
        cr,
        "--headless=new",
        "--disable-gpu",
        f"--user-data-dir={temp_profile}",
        f"--screenshot={out_png}",
        "--window-size=1440,3200",
        "--virtual-time-budget=4000",
        url
    ]
    subprocess.run(cmd, capture_output=True)
    if os.path.exists(out_png):
        im = Image.open(out_png)
        print(f"{ver}: fullpage captured, size={im.size}")
        # Crop sections:
        # Deal section (y: 800 to 1800)
        crop_deal = im.crop((100, 800, 1340, 1750))
        crop_deal.save(os.path.join(out_dir, f"deal_section_{ver}.png"))
        # How section (y: 1750 to 2400)
        crop_how = im.crop((100, 1750, 1340, 2450))
        crop_how.save(os.path.join(out_dir, f"how_section_{ver}.png"))
        # Who + Final section (y: 2450 to 3200)
        crop_who = im.crop((100, 2450, 1340, 3150))
        crop_who.save(os.path.join(out_dir, f"who_section_{ver}.png"))
        print(f"{ver}: all crops saved")
