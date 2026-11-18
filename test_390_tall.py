import subprocess
import os
from PIL import Image

cr = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
html_path = r"C:\Users\ESMIS 2601\.gemini\antigravity\scratch\proptii-30day-motion\src\design-partner-one-pager-v2.html"
out_dir = r"C:\Users\ESMIS 2601\.gemini\antigravity\brain\613858a4-7b73-4a34-bfa4-af3bec7a516a\scratch"

out_png = os.path.join(out_dir, "test_390_tall.png")
temp_profile = os.path.join(os.environ.get("TEMP", "C:\\temp"), "chr_shot_390_tall")
cmd = [
    cr,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={temp_profile}",
    f"--screenshot={out_png}",
    "--window-size=390,1600",
    "--virtual-time-budget=3000",
    f"file:///{html_path}"
]
subprocess.run(cmd, capture_output=True)
if os.path.exists(out_png):
    im = Image.open(out_png)
    crop = im.crop((0, 750, 390, 1250))
    crop.save(os.path.join(out_dir, "crop_390_stage_bottom.png"))
    print("Done")
