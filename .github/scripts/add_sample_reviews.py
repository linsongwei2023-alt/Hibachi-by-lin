from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')
css='''
.reviews{background:#0b0908;border-top:1px solid rgba(217,171,74,.18);padding:42px 20px 48px}.reviewsWrap{max-width:760px;margin:0 auto;text-align:center}.reviewsEyebrow{margin:0 0 8px;color:var(--gold);font-size:13px;font-weight:900;letter-spacing:.18em}.reviewsTitle{margin:0;color:#fff;font:700 32px/1.08 Georgia,serif}.reviewsNote{margin:9px auto 20px;color:var(--muted);font-size:12px;line-height:1.5}.reviewsTrack{display:flex;gap:12px;overflow-x:auto;scroll-snap-type:x mandatory;-webkit-overflow-scrolling:touch;scrollbar-width:none;padding:1px}.reviewsTrack::-webkit-scrollbar{display:none}.reviewCard{flex:0 0 100%;scroll-snap-align:center;padding:22px 20px;border:1px solid rgba(217,171,74,.36);border-radius:12px;background:linear-gradient(180deg,#14110e,#0c0a08);text-align:left}.reviewSample{display:inline-block;margin-bottom:11px;padding:3px 7px;border:1px solid rgba(217,171,74,.34);border-radius:999px;color:var(--gold2);font-size:9px;font-weight:900;letter-spacing:.12em}.reviewStars{color:var(--gold2);font-size:17px;letter-spacing:.08em}.reviewName{margin:8px 0 0;color:#fff;font-size:15px;font-weight:900}.reviewText{margin:12px 0 0;color:var(--muted);font-size:14px;line-height:1.65}.reviewHint{margin:12px 0 0;color:#9f9588;font-size:11px}@media(min-width:760px){.reviews{padding:56px 28px 62px}.reviewsTitle{font-size:42px}.reviewCard{padding:26px 28px}.reviewText{font-size:15px}}
'''
html='''
<section class="reviews" aria-labelledby="reviews-title"><div class="reviewsWrap"><p class="reviewsEyebrow">REVIEWS</p><h2 class="reviewsTitle" id="reviews-title">What Guests Say</h2><p class="reviewsNote">Sample preview reviews — these will be replaced with real guest feedback.</p><div class="reviewsTrack" aria-label="Sample guest reviews">
<article class="reviewCard"><span class="reviewSample">SAMPLE PREVIEW</span><div class="reviewStars" aria-label="5 out of 5 stars">★★★★★</div><p class="reviewName">Jessica · Fremont, CA</p><p class="reviewText">We booked hibachi for my husband's birthday and everyone had such a good time. The fire show was a hit, the chef kept everyone laughing, and dinner felt really fresh and fun.</p></article>
<article class="reviewCard"><span class="reviewSample">SAMPLE PREVIEW</span><div class="reviewStars" aria-label="5 out of 5 stars">★★★★★</div><p class="reviewName">Amanda · San Jose, CA</p><p class="reviewText">Super easy from booking to the actual party. We had adults and kids together and the kids loved watching the cooking. Steak and shrimp were our favorites.</p></article>
<article class="reviewCard"><span class="reviewSample">SAMPLE PREVIEW</span><div class="reviewStars" aria-label="5 out of 5 stars">★★★★★</div><p class="reviewName">Kevin · Palo Alto, CA</p><p class="reviewText">We wanted something different for a small backyard get-together and this worked perfectly. Everything was set up right at the house and we didn't have to worry about going anywhere.</p></article>
<article class="reviewCard"><span class="reviewSample">SAMPLE PREVIEW</span><div class="reviewStars" aria-label="5 out of 5 stars">★★★★★</div><p class="reviewName">Michelle · Oakland, CA</p><p class="reviewText">The food was great, but the interaction made the night. Everyone was taking videos during the fire part and the whole group stayed around the grill until dinner was finished.</p></article>
<article class="reviewCard"><span class="reviewSample">SAMPLE PREVIEW</span><div class="reviewStars" aria-label="5 out of 5 stars">★★★★★</div><p class="reviewName">Daniel · Los Angeles, CA</p><p class="reviewText">Booked for a family celebration at home. Communication was simple, the setup was smooth, and it felt more personal than regular catering. We'd definitely do hibachi at home again.</p></article>
</div><p class="reviewHint">Swipe left or right to view more</p></div></section>
'''
if '.reviews{' not in s:
    s=s.replace('\n.serviceAreas{','\n'+css+'\n.serviceAreas{',1)
if 'aria-labelledby="reviews-title"' not in s:
    marker='<section class="how" aria-labelledby="how-title">'
    if marker not in s: raise SystemExit('how section marker not found')
    s=s.replace(marker,html+marker,1)
p.write_text(s,encoding='utf-8')
# Triggered after the workflow exists so the homepage update runs automatically.
