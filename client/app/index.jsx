import React from 'react';
import {render} from 'react-dom';

import Map from './components/Map'

class App extends React.Component {
  render () {
    return <Map />;
  }
}

render(<App/>, document.getElementById('app'));