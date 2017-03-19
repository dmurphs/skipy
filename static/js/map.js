var map;

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 46.8764708, lng: -114.1582527},
        zoom: 8,
        mapTypeId: 'terrain',
    });
}
