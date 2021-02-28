/*
import React from "react";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import "./App.css";
import Books from "./components/Books";
import Home from "./components/Home";
import NotFound from "./components/NotFound";
import { Menu } from "semantic-ui-react";

function App() {

  return (
      <div>
    <Router>
      <div>
        <Menu>
          <Menu.Item link>
            <Link to="/">Home</Link>
          </Menu.Item>
          <Menu.Item link>
            <Link to="/books">Books</Link>
          </Menu.Item>
        </Menu>

        <Route exact path="/" render={() => <Home />} />
        <Route exact path="/books" render={() => <Books />} />
      </div>
    </Router>
    </div>
  );
}
export default App;
*/


import React from "react";
import "./App.css";
import Navbar from "./components/Navbar";


function App() {
  return (
    <div>
      <Navbar />
    </div>
  );
}
export default App;
