const blur = document.getElementById('blur');
const radius = document.getElementById('radius');

const zoom = 11;
const vector = new ol.layer.Heatmap({
  title: "HeatMap",
  source: new ol.source.Vector({
    url: 'dataset.json',
    format: new ol.format.GeoJSON({
      dataProjection: "EPSG:32643",
      featureProjection: "EPSG:32643"
    }),
  }),
  blur: 50,
  radius: 20,
  weight: function (feature) {
    return feature.get("lpoTime");
  },
});


const raster = new ol.layer.Tile({
  title: "OSM",
  source: new ol.source.OSM(),
  opacity: 0.5
});

var view = new ol.View({
  //projection: projection,
  //units: "metric",
  //extent: extent,
  zoom: zoom,
  maxZoom: 13,
  minZoom: zoom - 1,
  center: [ 1028954.9058868944, 5696879.17603661 ],
  //numZoomLevels: 13
});

var map = new ol.Map({
  controls: ol.control.defaults(),
  layers: [raster, vector],
  target: 'map',
  view: view
});

var geocoder = new Geocoder('nominatim', {
  provider: 'osm',
  lang: 'en-US', //en-US, fr-FR
  placeholder: 'Search for ...',
  targetType: 'text-input',
  autoComplete: 2,
  autoCompleteTimeout: 200,
  limit: 5,
  keepOpen: true,
  preventDefault: true
});
map.addControl(geocoder);
geocoder.on('addresschosen', function(evt){
  var feature = evt.feature,
      coord = evt.coordinate;
  map.getView().animate({ zoom: zoom, center: evt.coordinate });
});

/*
const blurHandler = function () {
  vector.setBlur(parseInt(blur.value / map.getView().getZoom(), 10));
};
blur.addEventListener('input', blurHandler);
blur.addEventListener('change', blurHandler);

const radiusHandler = function () {
  vector.setRadius(parseInt(radius.value, 10));
};
radius.addEventListener('input', radiusHandler);
radius.addEventListener('change', radiusHandler);
*/
//map.getView().on("change", blurHandler)