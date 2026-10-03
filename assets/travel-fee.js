(function(){
  const ORIGINS={southCA:'451 N Gerona Ave, San Gabriel, CA 91775',northCA:'43281 Gallegos Ave, Fremont, CA 94539',midwest:'5332 N Cumberland Ave, Chicago, IL 60656'};
  const SLO_LAT=35.2828, SB_LAT=34.4208;
  let state={status:'waiting',fee:'',miles:'',origin:''};

  function region(components,lat){
    const get=t=>(components||[]).find(c=>(c.types||[]).includes(t));
    const st=(get('administrative_area_level_1')?.shortText||get('administrative_area_level_1')?.short_name||'').toUpperCase();
    if(['IL','WI','IN','MI'].includes(st)) return {origin:ORIGINS.midwest};
    if(st==='CA'){
      const y=Number(lat);
      if(y>=SLO_LAT)return {origin:ORIGINS.northCA};
      if(y<=SB_LAT)return {origin:ORIGINS.southCA};
    }
    return {manual:true};
  }

  function panel(){
    let el=document.getElementById('travelFeeAuto');
    const address=document.getElementById('eventAddress');
    if(!address)return null;
    if(!el){el=document.createElement('div');el.id='travelFeeAuto';el.className='contactHint';address.closest('label').insertAdjacentElement('afterend',el)}
    if(state.status==='calculated')el.innerHTML='<b>Estimated Travel Fee: $'+state.fee+'</b><br>'+state.miles+' driving miles · $1/mile';
    else if(state.status==='calculating')el.innerHTML='<b>Calculating Travel Fee…</b><br>Using driving distance from our service base.';
    else if(state.status==='manual')el.innerHTML='<b>Travel Fee: Manual Review</b><br>We’ll confirm the travel fee before your booking is finalized.';
    else el.innerHTML='<b>Travel Fee</b><br>Select your full event address to calculate it automatically.';
    return el;
  }

  function syncFields(){
    const form=document.getElementById('bookingForm');if(!form)return;
    [['Travel fee',state.status==='calculated'?'$'+state.fee:'Manual Review'],['Travel distance',state.status==='calculated'?state.miles+' mi':'Manual Review'],['Travel fee origin',state.origin||'Manual Review']].forEach(([name,value])=>{
      let input=form.querySelector('input[name="'+name+'"]');if(!input){input=document.createElement('input');input.type='hidden';input.name=name;form.appendChild(input)}input.value=value;
    });
  }

  async function calculate(destination,components,lat){
    const r=region(components,lat);state={status:'calculating',fee:'',miles:'',origin:r.origin||''};panel();
    if(r.manual){state.status='manual';panel();syncFields();return}
    try{
      const svc=new google.maps.DistanceMatrixService();
      const res=await svc.getDistanceMatrix({origins:[r.origin],destinations:[destination],travelMode:google.maps.TravelMode.DRIVING,unitSystem:google.maps.UnitSystem.IMPERIAL});
      const item=res&&res.rows&&res.rows[0]&&res.rows[0].elements&&res.rows[0].elements[0];
      if(!item||item.status!=='OK'||!item.distance||!item.distance.value)throw new Error('route unavailable');
      state.miles=Math.round(item.distance.value/1609.344);state.fee=state.miles;state.status='calculated';
    }catch(e){console.error('Travel fee:',e);state={status:'manual',fee:'',miles:'',origin:r.origin}}
    panel();syncFields();
  }

  window.hblTravelFee={calculate,state:()=>({...state}),mount:panel,sync:syncFields};
  const observer=new MutationObserver(()=>{panel();syncFields()});
  observer.observe(document.body,{childList:true,subtree:true});
  panel();
})();