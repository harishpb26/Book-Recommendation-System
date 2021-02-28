import React from "react";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import "../App.css";
import Books from "./Books";
import Home from "./Home";
import NotFound from "./NotFound";
import { BookForm } from "./Add";

class Navbar extends React.Component {

  render() {
    return(
        <div>
            <Router>
              <div className="ui menu" style = {{ position: "fixed", width: "100%", zIndex: "300", overflow: "hidden"}}>
                <div className="header item">The Book Recommenders</div>
                    <Link to="/" className="item">
                      Home
                    </Link>
                    <Link to="/books" className="item">
                      Books
                    </Link>
                    <Link to="/add" className="item">
                      Add Book
                    </Link>
              </div>
              <Switch>
                <Route exact path="/" component={Home} />
                <Route exact path="/books" component={Books} />
                <Route exact path="/add" component={BookForm} />
                <Route component = {NotFound} />
              </Switch>
            </Router>
        </div>
    );
  }
}

export default Navbar;
