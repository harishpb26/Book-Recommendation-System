import React from 'react';
import { Link } from 'react-router-dom';

const NotFound = ({location}) => (
  <div style = {{paddingTop: "100px", margin: "0 auto"}}>
      <div>
          <div>
              <p className="lead">Page not found</p>
              <p className="lead">The requested URL <code>{location.pathname}</code> was not found on this server.
              </p>
              <button className="btn btn-default"><Link to="/">Home</Link></button>
          </div>
     </div>
  </div>
);

export default NotFound;
