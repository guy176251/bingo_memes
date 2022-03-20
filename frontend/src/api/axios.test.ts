import { getAPIClient } from "./axios";
import axios from "axios";

test("auth api client", async () => {
    process.env.TEST_BACKEND_URL = "http://127.0.0.1:8000";
    process.env.TEST_OPENAPI_DEFINITION = "public/static/openapi.json";
    Object.defineProperty(window.document, "cookie", {
        writable: true,
        value: "myCookie=omnomnom",
    });
    axios.defaults.adapter = require("axios/lib/adapters/http");
    console.log("test start");

    let token: string | null = null;
    const setToken = (s: string | null) => {
        token = s;
    };
    const rotateToken = async () => {
        const client = await getAPIClient();
        const resp = await client.token_refresh();
        setToken(resp.data.access);
    };

    const client = await getAPIClient();
    const resp_1 = await client.token_obtain_pair(null, {
        username: "gabriel28",
        password: "pass",
    });
    console.log("logged in");
    /*
    setToken(resp_1.data.access);
    const resp_2 = await client.vote_card(null, { card_id: 13, up: true });
    console.log("voted on card");
    console.log(resp_2);
    */
});
