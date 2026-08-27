from pathlib import Path
import re

path = Path('quote.html')
s = path.read_text()
replacement = """    const m=calc();
    const proteinRows=(Array.isArray(proteins)?proteins:['Chicken','Steak','Shrimp','Salmon']).filter(n=>((p.adultProteins?.[n]||0)+(p.childProteins?.[n]||0))>0).length;
    const addonRows=addons.filter(([n])=>(p.extras?.[n]||0)>0).length+((+p.filetUpgrade||0)>0?1:0);
    const logicalW=1200,logicalH=Math.max(1650,1440+(proteinRows+addonRows)*52);
    const c=document.createElement('canvas'),scale=2/3;c.width=Math.round(logicalW*scale);c.height=Math.round(logicalH*scale);
    const x=c.getContext('2d');if(!x)throw new Error('Canvas unavailable');x.scale(scale,scale);
    x.fillStyle='#f7f2e8';x.fillRect(0,0,logicalW,logicalH);
    x.fillStyle='#15120f';x.fillRect(0,0,logicalW,170);
    x.fillStyle='#f4b942';x.font='700 58px Georgia';x.fillText('HIBACHI BY LIN',65,82);
    x.fillStyle='#fff';x.font='26px Arial';x.fillText('ITEMIZED EVENT QUOTE',68,130);x.textAlign='right';x.fillText(p.reference||'QUOTE',1130,98);x.textAlign='left';
    let y=220;
    const fit=(text,maxWidth,font)=>{x.font=font;let t=String(text||'—');if(x.measureText(t).width<=maxWidth)return t;while(t.length>1&&x.measureText(t+'…').width>maxWidth)t=t.slice(0,-1);return t+'…'};
    const line=(l,v)=>{x.fillStyle='#6b6258';x.font='24px Arial';x.fillText(l,70,y);x.fillStyle='#15120f';const f='700 27px Arial';x.font=f;x.fillText(fit(v,800,f),315,y);y+=49};
    line('Event',`${p.date||''} ${p.time||''}`);line('Customer',p.name||'');line('Phone',p.phone||'');line('Email',p.email||'');line('Location',p.address||'');line('Guests',`${p.adults||0} adults · ${p.children||0} children · ${p.toddlers||0} age 3 & under`);
    y+=18;x.fillStyle='#ee5428';x.fillRect(65,y,1070,5);y+=54;x.fillStyle='#15120f';x.font='700 32px Georgia';x.fillText('MENU DETAILS',70,y);y+=49;
    const menu=(n,v,a='')=>{const f='24px Arial';x.font=f;x.fillStyle='#15120f';x.fillText(fit(n,470,f),75,y);x.textAlign='center';x.fillText(fit(v,300,f),760,y);x.textAlign='right';x.font='700 24px Arial';x.fillText(a,1125,y);x.textAlign='left';y+=45};
    menu('Food package',`${p.adults||0} adults / ${p.children||0} children`,money(m.food));
    (Array.isArray(proteins)?proteins:['Chicken','Steak','Shrimp','Salmon']).forEach(n=>{const a=p.adultProteins?.[n]||0,ch=p.childProteins?.[n]||0;if(a+ch){const qty=a+ch,isFilet=n==='Upgrade to Filet Mignon +$5',isLobster=n==='Upgrade to Lobster Tail +$10',label=(isFilet||isLobster)?n:`${n} protein`,amount=isFilet?money(qty*5):isLobster?money(qty*10):'Included';menu(label,`${a} adult + ${ch} child`,amount)}});
    addons.filter(([n])=>(p.extras?.[n]||0)>0).forEach(([n,price])=>menu(n,`${p.extras[n]} order(s)`,money(p.extras[n]*price)));
    if((+p.filetUpgrade||0)>0)menu('Filet Mignon Upgrade',`${p.filetUpgrade} portion(s)`,money(p.filetUpgrade*5));
    y+=12;x.fillStyle='#d6cab9';x.fillRect(65,y,1070,2);y+=43;menu('Travel fee','',money(travel));menu('Tax','',money(m.tax));
    y+=4;x.fillStyle='#15120f';x.fillRect(65,y,1070,68);x.fillStyle='#fff';x.font='700 29px Arial';x.fillText('TOTAL PRICE',85,y+44);x.textAlign='right';x.font='700 31px Arial';x.fillText(money(m.total),1115,y+44);x.textAlign='left';y+=108;
    x.fillStyle='#ee5428';x.font='700 32px Georgia';x.fillText('SUGGESTED GRATUITY',70,y);y+=50;
    [.2,.25,.3].forEach(r=>{const tip=m.foodSubtotal*r;menu(`${r*100}% tip`,money(tip),`Total: ${money(m.total+tip)}`)});
    y+=18;x.fillStyle='#15120f';x.font='700 25px Arial';x.fillText('Food allergies',70,y);x.font='23px Arial';x.fillText(fit(p.allergies||'None reported',820,'23px Arial'),285,y);y+=51;
    x.font='700 25px Arial';x.fillText('Notes',70,y);x.font='23px Arial';x.fillText(fit(notes||'—',900,'23px Arial'),285,y);y+=78;
    x.fillStyle='#6b6258';x.font='21px Arial';x.fillText('Total price = food + add-ons + travel fee + tax.',70,y);y+=35;x.fillText('Suggested gratuity is based on food subtotal only; travel and tax excluded.',70,y);
    stage='encode JPG';"""
pattern = r"    const m=calc\(\),c=document\.createElement\('canvas'\),w=800,h=1100;.*?\n    stage='encode JPG';"
new_s, count = re.subn(pattern, replacement, s, count=1, flags=re.S)
if count != 1:
    raise SystemExit(f'Expected one quote canvas block, replaced {count}')
path.write_text(new_s)
print('Updated quote canvas layout')
