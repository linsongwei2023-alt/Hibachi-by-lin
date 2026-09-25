from pathlib import Path
import re
p=Path('index.html')
s=p.read_text(encoding='utf-8')
# Keep review badges removed.
s=s.replace('<span class="reviewSample">SAMPLE PREVIEW</span>','')
# Remove only the standalone LIVE HIBACHI EXPERIENCE / chefShow module.
pattern=r'<section class="chefShow" aria-labelledby="chef-show-title">.*?</section>\s*'
s,n=re.subn(pattern,'',s,count=1,flags=re.S)
if n != 1:
    raise SystemExit('chefShow module not found exactly once')
p.write_text(s,encoding='utf-8')
