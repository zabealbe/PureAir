const blur = document.getElementById('blur');
const radius = document.getElementById('radius');

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

var map = new ol.Map({
  layers: [raster, vector],
  target: 'map',
  view: new ol.View({
    //projection: projection,
    units: "metric",
    //extent: extent,
    zoom: 6,
    maxZoom: 13,
    minZoom: 3,
    maxResolution: 6000,
    center: [ 1028954.9058868944, 5696879.17603661 ],
    //numZoomLevels: 13
  })
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