import OpenAPIClientAxios from "openapi-client-axios";
import axios, { AxiosRequestConfig } from "axios";
import { getCSRFToken, accessIsExpired, refreshIsExpired } from "../storage";
import { Client as APIClient } from "types/apiclient";
import { AccessToken, AccessTokenRotator, AuthClientProps, AxiosRetryError } from "types/api";

// https://datatracker.ietf.org/doc/html/rfc7231
const SAFE_METHODS = [
    "GET",
    "HEAD",
    "OPTIONS",
    "TRACE",
    "get",
    "head",
    "options",
    "trace",
];

async function setBearer(
    config: AxiosRequestConfig,
    token: AccessToken | undefined,
    rotateToken: AccessTokenRotator
) {
    if (!refreshIsExpired() && (accessIsExpired() || !token)) {
        try {
            token = await rotateToken();
        } catch (err) {}
    }
    if (token) {
        config.headers = config.headers || {}
        config.headers.authorization = `Bearer ${token}`;
    }
    return config;
}

function setCSRF(config: AxiosRequestConfig) {
    const isNotSafeMethod = !SAFE_METHODS.includes(config.method || "");
    const csrf = getCSRFToken();

    if (csrf && isNotSafeMethod) {
        config.headers = config.headers || {}
        config.headers["X-CSRFToken"] = csrf;
    }
    return config;
}

export async function getBaseClient() {
    const api = new OpenAPIClientAxios({
        definition: "/static/openapi.json",
        axiosConfigDefaults: {
            withCredentials: true,
            headers: {},
        },
    });

    const client = await api.init<APIClient>();

    if (!getCSRFToken()) {
        await client.get_csrf_token();
    }

    client.interceptors.request.use(setCSRF);
    return client;
}

export async function getAuthClient({ token, rotateToken }: AuthClientProps) {
    // https://www.bezkoder.com/react-refresh-token/
    const requestAuth = async (config: AxiosRequestConfig) => {
        if (!config.headers?.authorization) {
            await setBearer(config, token, rotateToken);
        }
        setCSRF(config);
        return config;
    };

    const responseRetry = async (error: AxiosRetryError) => {
        const config = error.config;
        if (error.response?.status === 401 && !config.hasRetried) {
            config.hasRetried = true;
            await setBearer(config, token, rotateToken);
            return axios(config);
        }
        throw error;
    };

    const client = await getBaseClient();
    client.interceptors.request.use(requestAuth);
    client.interceptors.response.use((response) => {
        return response;
    }, responseRetry);

    return client;
}
