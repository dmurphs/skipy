import React from 'react';

class Map extends React.Component{
  render () {
    return <div ref="map_canvas"></div>;
  }

  componentDidMount() {
    mapOptions = {
        zoom: 10,
        center: new google.maps.LatLng(46.8764708, -114.1582527)
    }

    return new google.maps.Map(refs.map_canvas.getDOMNode(), mapOptions)
  }

}

export default Map;