const blur = document.getElementById('blur');
const radius = document.getElementById('radius');

const vector = new ol.layer.Heatmap({
  source: new ol.source.Vector({
    url: '2012_Earthquakes_Mag5.kml',
    format: new ol.format.KML({
      extractStyles: false,
    }),
  }),
  blur: parseInt(blur.value, 10),
  radius: parseInt(radius.value, 10),
  weight: function (feature) {
    // 2012_Earthquakes_Mag5.kml stores the magnitude of each earthquake in a
    // standards-violating <magnitude> tag in each Placemark.  We extract it from
    // the Placemark's name instead.
    const name = feature.get('name');
    const magnitude = parseFloat(name.substr(2));
    return magnitude - 5;
  },
});

const raster = new ol.layer.Tile({
  source: new ol.source.Stamen({
    layer: 'toner',
  }),
});

new ol.Map({
  layers: [raster, vector],
  target: 'map',
  view: new ol.View({
    center: [0, 0],
    zoom: 2,
  }),
});

const blurHandler = function () {
  vector.setBlur(parseInt(blur.value, 10));
};
blur.addEventListener('input', blurHandler);
blur.addEventListener('change', blurHandler);

const radiusHandler = function () {
  vector.setRadius(parseInt(radius.value, 10));
};
radius.addEventListener('input', radiusHandler);
radius.addEventListener('change', radiusHandler);
