from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')
# Only remove the visible SAMPLE PREVIEW badges. Keep all other review content and layout unchanged.
s=s.replace('<span class="reviewSample">SAMPLE PREVIEW</span>','')
p.write_text(s,encoding='utf-8')
# Triggered by workflow to update homepage.
