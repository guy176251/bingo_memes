import ReactDOM from "react-dom";
import { BrowserRouter as Router, useRoutes } from "react-router-dom";
import { ROUTES } from "./routes";
import { ProvideAuth } from "./context/auth";
import "bootstrap/dist/css/bootstrap.min.css";
import "./scss/main.scss";
import { ProvideTiles } from "context/tiles";

function App() {
    return useRoutes(ROUTES);
}

ReactDOM.render(
    <ProvideAuth>
        <ProvideTiles>
            <Router>
                <App />
            </Router>
        </ProvideTiles>
    </ProvideAuth>,
    document.getElementById("root")
);
