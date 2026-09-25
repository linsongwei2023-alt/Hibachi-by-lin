from pathlib import Path
import re
p=Path('index.html')
s=p.read_text(encoding='utf-8')
# Keep old sample badges removed and old chef-show module removed.
s=s.replace('<span class="reviewSample">SAMPLE PREVIEW</span>','')
s=re.sub(r'<section class="chefShow" aria-labelledby="chef-show-title">.*?</section>\s*','',s,count=1,flags=re.S)
# Remove the old sample disclaimer now that cards no longer carry sample badges.
s=s.replace('<p class="reviewsNote">Sample preview reviews — these will be replaced with real guest feedback.</p>','')
# Add review pagination dots.
if 'class="reviewDots"' not in s:
    s=s.replace('<p class="reviewHint">Swipe left or right to view more</p>', '<div class="reviewDots" aria-label="Review position"><button class="reviewDot active" type="button" aria-label="Review 1"></button><button class="reviewDot" type="button" aria-label="Review 2"></button><button class="reviewDot" type="button" aria-label="Review 3"></button><button class="reviewDot" type="button" aria-label="Review 4"></button><button class="reviewDot" type="button" aria-label="Review 5"></button></div><p class="reviewHint">Swipe left or right to view more</p>',1)
# Add Event Moments section after reviews. Media slots are intentionally ready for real uploads.
if 'id="event-moments-title"' not in s:
    moments='''<section class="eventMoments" aria-labelledby="event-moments-title"><div class="eventMomentsWrap"><p class="eventMomentsEyebrow">EVENT MOMENTS</p><h2 class="eventMomentsTitle" id="event-moments-title">Moments From The Party</h2><p class="eventMomentsCopy">Real food, fire and fun from our hibachi events.</p><div class="momentsTrack"><div class="momentPlaceholder"><span>PHOTO / VIDEO</span></div><div class="momentPlaceholder"><span>PHOTO / VIDEO</span></div><div class="momentPlaceholder"><span>PHOTO / VIDEO</span></div></div><p class="momentsHint">Swipe to see more</p></div></section>'''
    end='</div></section>\n<section class="how" aria-labelledby="how-title">'
    if end in s:
        s=s.replace(end,'</div></section>\n'+moments+'\n<section class="how" aria-labelledby="how-title">',1)
    else:
        marker='<section class="how" aria-labelledby="how-title">'
        if marker not in s: raise SystemExit('How section marker not found')
        s=s.replace(marker,moments+'\n'+marker,1)
# Styles.
if '.reviewDots{' not in s:
    s=s.replace('.reviewHint{margin:12px 0 0;color:#9f9588;font-size:11px}', '.reviewDots{display:flex;justify-content:center;gap:8px;margin:16px 0 0}.reviewDot{width:7px;height:7px;padding:0;border:0;border-radius:50%;background:#5d554c;transition:.2s}.reviewDot.active{width:19px;border-radius:999px;background:var(--gold2)}.reviewHint{margin:9px 0 0;color:#9f9588;font-size:11px}',1)
if '.eventMoments{' not in s:
    css='''.eventMoments{background:#080706;border-top:1px solid rgba(217,171,74,.18);padding:42px 20px 48px}.eventMomentsWrap{max-width:980px;margin:0 auto;text-align:center}.eventMomentsEyebrow{margin:0 0 8px;color:var(--gold);font-size:13px;font-weight:900;letter-spacing:.18em}.eventMomentsTitle{margin:0;color:#fff;font:700 32px/1.08 Georgia,serif}.eventMomentsCopy{margin:10px auto 22px;color:var(--muted);font-size:14px;line-height:1.6}.momentsTrack{display:flex;gap:12px;overflow-x:auto;scroll-snap-type:x mandatory;-webkit-overflow-scrolling:touch;scrollbar-width:none}.momentsTrack::-webkit-scrollbar{display:none}.momentPlaceholder{flex:0 0 78%;aspect-ratio:4/5;scroll-snap-align:center;display:grid;place-items:center;border:1px dashed rgba(217,171,74,.5);border-radius:14px;background:linear-gradient(180deg,#14110e,#0b0908);color:#9f9588;font-size:11px;font-weight:900;letter-spacing:.12em}.momentsHint{margin:12px 0 0;color:#9f9588;font-size:11px}@media(min-width:760px){.eventMoments{padding:56px 28px 62px}.eventMomentsTitle{font-size:42px}.momentsTrack{justify-content:center;overflow:visible}.momentPlaceholder{flex:0 1 280px;max-width:280px}.momentsHint{display:none}}'''
    s=s.replace('.how{background:',css+'\n.how{background:',1)
# Script updates dots while swiping and lets dots jump to reviews.
if 'reviewDotSync' not in s:
    js='''<script id="reviewDotSync">document.addEventListener('DOMContentLoaded',function(){var t=document.querySelector('.reviewsTrack'),d=[].slice.call(document.querySelectorAll('.reviewDot')),c=[].slice.call(document.querySelectorAll('.reviewCard'));if(!t||!d.length||!c.length)return;function set(i){d.forEach(function(x,j){x.classList.toggle('active',j===i)});}function sync(){var x=t.scrollLeft+t.clientWidth/2,i=0,b=Infinity;c.forEach(function(el,j){var m=el.offsetLeft+el.offsetWidth/2,q=Math.abs(m-x);if(q<b){b=q;i=j;}});set(i);}t.addEventListener('scroll',function(){requestAnimationFrame(sync)},{passive:true});d.forEach(function(x,i){x.addEventListener('click',function(){c[i]&&c[i].scrollIntoView({behavior:'smooth',block:'nearest',inline:'center'});});});sync();});</script>'''
    s=s.replace('</body>',js+'\n</body>',1)
p.write_text(s,encoding='utf-8')
