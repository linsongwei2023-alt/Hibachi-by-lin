(function () {
'use strict';
var origins = {
  southCA: '451 N Gerona Ave, San Gabriel, CA 91775',
  northCA: '43281 Gallegos Ave, Fremont, CA 94539',
  midwest: '5332 N Cumberland Ave, Chicago, IL 60656'
};
var result = { status: 'waiting', fee: '', miles: '', origin: '' };

function componentValue(components, type, shortValue) {
  var list = components || [];
  for (var i = 0; i < list.length; i++) {
    var types = list[i].types || [];
    if (types.indexOf(type) !== -1) {
      if (shortValue) return list[i].shortText || list[i].short_name || '';
      return list[i].longText || list[i].long_name || '';
    }
  }
  return '';
}
function chooseOrigin(components, latitude) {
  var state = componentValue(components, 'administrative_area_level_1', true).toUpperCase();
  if (state === 'IL' || state === 'WI' || state === 'IN' || state === 'MI') return origins.midwest;
  if (state === 'CA') {
    var lat = Number(latitude);
    if (lat >= 35.2828) return origins.northCA;
    if (lat <= 34.4208) return origins.southCA;
  }
  return '';
}
function textValue() {
  if (result.status === 'calculated') return 'Estimated Travel Fee: $' + result.fee + ' (' + result.miles + ' driving miles x $1/mile)';
  if (result.status === 'calculating') return 'Calculating Travel Fee...';
  if (result.status === 'manual') return 'Travel Fee: Manual Review - We will confirm it before your booking is finalized.';
  return 'Travel Fee will be calculated after you select the full address.';
}
function calculate(destination, components, latitude) {
  var origin = chooseOrigin(components, latitude);
  result = { status: origin ? 'calculating' : 'manual', fee: '', miles: '', origin: origin };
  if (!origin) return Promise.resolve(getResult());
  if (!window.google || !google.maps || !google.maps.DistanceMatrixService) {
    result.status = 'manual';
    return Promise.resolve(getResult());
  }
  var service = new google.maps.DistanceMatrixService();
  return service.getDistanceMatrix({
    origins: [origin],
    destinations: [destination],
    travelMode: google.maps.TravelMode.DRIVING,
    unitSystem: google.maps.UnitSystem.IMPERIAL
  }).then(function (response) {
    var item = response && response.rows && response.rows[0] && response.rows[0].elements && response.rows[0].elements[0];
    if (!item || item.status !== 'OK' || !item.distance || !item.distance.value) throw new Error('route unavailable');
    var miles = Math.round(item.distance.value / 1609.344);
    result = { status: 'calculated', fee: String(miles), miles: String(miles), origin: origin };
    return getResult();
  }).catch(function (error) {
    console.error('Travel fee calculation error', error);
    result = { status: 'manual', fee: '', miles: '', origin: origin };
    return getResult();
  });
}
function getResult() {
  return { status: result.status, fee: result.fee, miles: result.miles, origin: result.origin, text: textValue() };
}
window.HBLTravelFee = { calculate: calculate, getResult: getResult };
})();