from PIL import Image

im = Image.open(r'C:\Users\ESMIS 2601\.gemini\antigravity\brain\613858a4-7b73-4a34-bfa4-af3bec7a516a\scratch\v2_full.png')
# Find the exact Y coordinate where the dark blue background starts at the bottom of .hero-stage
# Column x=600 is in the middle of .hero-stage
for y in range(630, 720):
    rgb = im.getpixel((600, y))
    print(f'x=600, y={y}: rgb={rgb}')
