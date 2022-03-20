import ReactDOM from "react-dom";
import { BrowserRouter as Router, Link, Route, useRoutes } from "react-router-dom";
import { ProvideAuth, useAuth } from "./auth";

function App() {
    return <></>;
}

ReactDOM.render(
    <Router>
        <ProvideAuth>
            <App />
        </ProvideAuth>
    </Router>,
    document.getElementById("root")
);
