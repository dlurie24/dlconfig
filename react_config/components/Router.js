import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

export default () => {
  return (
    <>
      <Router>
        <Switch>
          <Route to="/">
            <div>Hello World!</div>
          </Route>
        </Switch>
      </Router>
    </>
  );
};
