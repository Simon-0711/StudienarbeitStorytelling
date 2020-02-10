mapboxgl.accessToken = 'pk.eyJ1Ijoic2ltb24tMDgxNSIsImEiOiJjazJrd3RuY3MwMHhvM29vejViazBkZGttIn0.GImDQgrwRkS_XRsyTYcGUw';

var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v11'
});

map.on('load', function () {
    map.loadImage('https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Cat_silhouette.svg/400px-Cat_silhouette.svg.png', function (error, image) {
        if (error) throw error;
        map.addImage('cat', image);
        map.addLayer({
            "id": "points",
            "type": "symbol",
            "source": {
                "type": "geojson",
                "data": {
                    "type": "FeatureCollection",
                    "features": [{
                        "type": "Feature",
                        "geometry": {
                            "type": "Point",
                            "coordinates": [4.385127,45.459961]
                        }
                    }]
                }
            },
            "layout": {
                "icon-image": "finishFlag",
                "icon-size": 0.25
            }
        });
    });
});