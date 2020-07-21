import React from 'react';
import {BrowserRouter} from 'react-router-dom';
import Main from '../src/main';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <div>
          <Main/>
        </div>
      </BrowserRouter>
    </div>
  );
}

export default App;