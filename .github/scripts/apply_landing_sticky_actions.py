from pathlib import Path
import re

ROOT = Path('.')
CSS_LINK = '<link rel="stylesheet" href="/landing-sticky-actions.css">'
BAR = '<nav class="mobileBar" aria-label="Quick actions"><a href="/menu">VIEW MENU</a><a href="/book">BOOK NOW</a></nav>'

# Service-area index plus every SEO/service landing page. Leave index/menu/book/quote/review alone.
files = [ROOT/'areas-we-serve.html']
files += sorted(ROOT.glob('hibachi-*.html'))

for path in files:
    if not path.exists():
        continue
    text = path.read_text(encoding='utf-8')

    # Load the common override even on older standalone landing pages with their own inline CSS.
    if 'landing-sticky-actions.css' not in text:
        if '</head>' in text:
            text = text.replace('</head>', CSS_LINK + '</head>', 1)

    # Guarantee a single persistent View Menu / Book Now bar.
    if 'class="mobileBar"' not in text:
        text = text.replace('</body>', BAR + '</body>', 1)

    path.write_text(text, encoding='utf-8')
    print(path)
