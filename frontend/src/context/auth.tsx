import { useContext, useState, createContext } from "react";
import { getAuthClient, getBaseClient } from "api/client";
import { AccessToken } from "types/api";
import { AuthData } from "types/auth";

/**
 * Token is only stored in memory.
 * https://stackoverflow.com/questions/68777033/storing-jwt-token-into-httponly-cookies
 */
export function useProvideAuth(): AuthData {
    const [token, setToken] = useState<AccessToken>(null);
    const isLoggedIn = Boolean(token);

    const rotateToken = async () => {
        const client = await getBaseClient();
        try {
            const resp = await client.token_refresh();
            if (resp.status === 200) {
                setToken(resp.data.access);
                return resp.data.access;
            }
        } catch (err) {}
    };

    return {
        isLoggedIn,
        async login(credentials) {
            const client = await getBaseClient();
            const resp = await client.token_obtain_pair(null, credentials);
            if (resp.status === 200) {
                setToken(resp.data.access);
            }
        },
        async logout() {
            setToken(null);
            const client = await getBaseClient();
            await client.token_unpair();
        },
        async getClient() {
            return await getAuthClient({ token, rotateToken });
        },
        doIfAuth(fn: () => void) {
            if (isLoggedIn) {
                fn();
            } else {
                /// redirect to login
                alert("write a thing to redirect to login screen");
            }
        },
    };
}

export const AuthContext = createContext<AuthData>({
    isLoggedIn: false,
    async login(credentials) {},
    async logout() {},
    async getClient() {
        return await getBaseClient();
    },
    doIfAuth(fn: () => void) {},
});

export function ProvideAuth({ children }: { children: any }) {
    const authData = useProvideAuth();
    return <AuthContext.Provider value={authData}>{children}</AuthContext.Provider>;
}

export function useAuth() {
    return useContext(AuthContext);
}
