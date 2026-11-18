from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

opts = Options()
opts.add_argument('--headless')
opts.add_argument('--window-size=1440,950')
driver = webdriver.Chrome(options=opts)
driver.get('file:///C:/Users/ESMIS 2601/.gemini/antigravity/scratch/proptii-30day-motion/src/design-partner-one-pager-v2.html')
script = """
  const stage = document.querySelector('.hero-stage').getBoundingClientRect();
  const wrap = document.querySelector('.hero-photo-wrap').getBoundingClientRect();
  const photo = document.querySelector('.hero-photo').getBoundingClientRect();
  return {
    stage: {top: stage.top, bottom: stage.bottom, height: stage.height},
    wrap: {top: wrap.top, bottom: wrap.bottom, height: wrap.height},
    photo: {top: photo.top, bottom: photo.bottom, height: photo.height}
  };
"""
res = driver.execute_script(script)
print(json.dumps(res, indent=2))
driver.save_screenshot('check_v2_bottom.png')
driver.quit()
