import Cookies from "js-cookie";

export function getCSRFToken() {
    return Cookies.get("csrftoken");
}

export function getRefreshTimestamp() {
    return parseFloat(Cookies.get("logged_in") || "0");
}

export function getAccessTimestamp() {
    return parseFloat(Cookies.get("access") || "0");
}

function timestampIsExpired(timestamp: number): boolean {
    return Date.now() > timestamp;
}

export function refreshIsExpired(): boolean {
    return timestampIsExpired(getRefreshTimestamp());
}

export function accessIsExpired(): boolean {
    return timestampIsExpired(getAccessTimestamp());
}
