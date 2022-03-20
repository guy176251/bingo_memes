import type { Client as APIClient, Components } from "types/apiclient";

declare type LoginProps = Components.Schemas.TokenObtainPairSerializer;

declare interface AuthData {
    isLoggedIn: boolean;
    login: (credentials: LoginProps) => Promise<void>;
    logout: () => Promise<void>;
    getClient: () => Promise<APIClient>;
    doIfAuth: (fn: () => void) => void;
}

export { LoginProps, AuthData };
