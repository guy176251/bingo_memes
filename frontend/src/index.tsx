import ReactDOM from "react-dom";
import { BrowserRouter as Router, useRoutes } from "react-router-dom";
import { ROUTES } from "./routes";
import "bootstrap/dist/css/bootstrap.min.css";

function App() {
    return useRoutes(ROUTES);
}

ReactDOM.render(
    <Router>
        <App />
    </Router>,
    document.getElementById("root")
);
