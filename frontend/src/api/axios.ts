import OpenAPIClientAxios from "openapi-client-axios";
import { Client as APIClient } from "./client";

export const getAPIClient = async () => {
    const api = new OpenAPIClientAxios({ definition: "/static/openapi.json" });
    return await api.init<APIClient>();
};
