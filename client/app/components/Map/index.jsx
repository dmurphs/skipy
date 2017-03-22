import React from 'react';

class Map extends React.Component{


  render () {
    return <div ref="map_canvas" style={{"height" : "100%", "width": "100%"}}></div>;
  }

  componentDidMount() {
    let mapCanvas = this.refs.map_canvas;

    let mapOptions = {
          zoom: 10,
          center: new google.maps.LatLng(46.8764708, -114.1582527),
          mapTypeId: 'terrain'
      }

    this.map = new google.maps.Map(mapCanvas, mapOptions)

    this.addMarker(46.8764708, -114.1582527);
  }

  addMarker(latitude,longitude){
    var latLon = {lat: latitude, lng: longitude};

    var marker = new google.maps.Marker({
      position: latLon,
      map: this.map,
      title: 'Hello World!'
    });
  }

}

export default Map;
