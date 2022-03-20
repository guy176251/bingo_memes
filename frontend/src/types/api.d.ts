import type { OperationResponse } from "openapi-client-axios";
import type { AxiosRequestConfig, AxiosError } from "axios";

declare type AccessToken = string | null;
declare type AccessTokenRotator = () => Promise<string | undefined>;
declare type APICall<T> = (...args: any[]) => OperationResponse<T>;

declare interface AuthClientProps {
    token: AccessToken;
    rotateToken: AccessTokenRotator;
}

declare interface AxiosRetryError<T = any> extends AxiosError<T> {
    config: AxiosRequestConfig & { hasRetried?: boolean };
}
