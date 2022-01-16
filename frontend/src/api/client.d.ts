import type {
  OpenAPIClient,
  Parameters,
  UnknownParamsObject,
  OperationResponse,
  AxiosRequestConfig,
} from 'openapi-client-axios'; 

declare namespace Components {
    namespace Schemas {
        /**
         * CardInSchema
         */
        export interface CardInSchema {
            /**
             * Tile 1
             */
            tile_1: string;
            /**
             * Tile 2
             */
            tile_2: string;
            /**
             * Tile 3
             */
            tile_3: string;
            /**
             * Tile 4
             */
            tile_4: string;
            /**
             * Tile 5
             */
            tile_5: string;
            /**
             * Tile 6
             */
            tile_6: string;
            /**
             * Tile 7
             */
            tile_7: string;
            /**
             * Tile 8
             */
            tile_8: string;
            /**
             * Tile 9
             */
            tile_9: string;
            /**
             * Tile 10
             */
            tile_10: string;
            /**
             * Tile 11
             */
            tile_11: string;
            /**
             * Tile 12
             */
            tile_12: string;
            /**
             * Tile 13
             */
            tile_13: string;
            /**
             * Tile 14
             */
            tile_14: string;
            /**
             * Tile 15
             */
            tile_15: string;
            /**
             * Tile 16
             */
            tile_16: string;
            /**
             * Tile 17
             */
            tile_17: string;
            /**
             * Tile 18
             */
            tile_18: string;
            /**
             * Tile 19
             */
            tile_19: string;
            /**
             * Tile 20
             */
            tile_20: string;
            /**
             * Tile 21
             */
            tile_21: string;
            /**
             * Tile 22
             */
            tile_22: string;
            /**
             * Tile 23
             */
            tile_23: string;
            /**
             * Tile 24
             */
            tile_24: string;
            /**
             * Tile 25
             */
            tile_25: string;
            /**
             * Id
             */
            id?: number;
            /**
             * Name
             */
            name: string;
            category: /* IDSchema */ IDSchema;
        }
        /**
         * CardOutSchema
         */
        export interface CardOutSchema {
            /**
             * Tile 1
             */
            tile_1: string;
            /**
             * Tile 2
             */
            tile_2: string;
            /**
             * Tile 3
             */
            tile_3: string;
            /**
             * Tile 4
             */
            tile_4: string;
            /**
             * Tile 5
             */
            tile_5: string;
            /**
             * Tile 6
             */
            tile_6: string;
            /**
             * Tile 7
             */
            tile_7: string;
            /**
             * Tile 8
             */
            tile_8: string;
            /**
             * Tile 9
             */
            tile_9: string;
            /**
             * Tile 10
             */
            tile_10: string;
            /**
             * Tile 11
             */
            tile_11: string;
            /**
             * Tile 12
             */
            tile_12: string;
            /**
             * Tile 13
             */
            tile_13: string;
            /**
             * Tile 14
             */
            tile_14: string;
            /**
             * Tile 15
             */
            tile_15: string;
            /**
             * Tile 16
             */
            tile_16: string;
            /**
             * Tile 17
             */
            tile_17: string;
            /**
             * Tile 18
             */
            tile_18: string;
            /**
             * Tile 19
             */
            tile_19: string;
            /**
             * Tile 20
             */
            tile_20: string;
            /**
             * Tile 21
             */
            tile_21: string;
            /**
             * Tile 22
             */
            tile_22: string;
            /**
             * Tile 23
             */
            tile_23: string;
            /**
             * Tile 24
             */
            tile_24: string;
            /**
             * Tile 25
             */
            tile_25: string;
            /**
             * Name
             */
            name: string;
            author: /* UserSchema */ UserSchema;
            /**
             * Hashtags
             */
            hashtags: /* HashtagSchema */ HashtagSchema[];
            /**
             * Created At
             */
            created_at: string; // date-time
            /**
             * Edited At
             */
            edited_at: string; // date-time
            /**
             * Best
             */
            best: number;
            /**
             * Hot
             */
            hot: number;
            /**
             * Score
             */
            score: number;
            /**
             * Upvoted
             */
            upvoted?: boolean;
        }
        /**
         * CategoryInSchema
         */
        export interface CategoryInSchema {
            /**
             * Name
             */
            name: string;
            /**
             * Description
             */
            description: string;
            /**
             * Icon Url
             */
            icon_url: string; // uri
            /**
             * Banner Url
             */
            banner_url: string; // uri
        }
        /**
         * CategoryOutSchema
         */
        export interface CategoryOutSchema {
            /**
             * Name
             */
            name: string;
            /**
             * Description
             */
            description: string;
            /**
             * Icon Url
             */
            icon_url: string; // uri
            /**
             * Banner Url
             */
            banner_url: string; // uri
            /**
             * Id
             */
            id: number;
            author: /* UserSchema */ UserSchema;
            /**
             * Created At
             */
            created_at: string; // date-time
        }
        /**
         * CreateFollowSchema
         */
        export interface CreateFollowSchema {
            /**
             * Followed Id
             */
            followed_id: number;
        }
        /**
         * HashtagSchema
         */
        export interface HashtagSchema {
            /**
             * Name
             */
            name: string;
        }
        /**
         * IDSchema
         */
        export interface IDSchema {
            /**
             * Id
             */
            id: number;
        }
        /**
         * Schema
         */
        export interface Schema {
        }
        /**
         * SubscriptionSchema
         */
        export interface SubscriptionSchema {
            /**
             * Category Id
             */
            category_id: number;
            /**
             * User Id
             */
            user_id?: number;
        }
        /**
         * TokenObtainPairOutput
         */
        export interface TokenObtainPairOutput {
            /**
             * Refresh
             */
            refresh: string;
            /**
             * Access
             */
            access: string;
            /**
             * Username
             */
            username: string;
        }
        /**
         * TokenObtainPairSerializer
         */
        export interface TokenObtainPairSerializer {
            /**
             * Password
             */
            password: string;
            /**
             * Username
             * Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
             */
            username: string;
        }
        /**
         * TokenRefreshSchema
         */
        export interface TokenRefreshSchema {
            /**
             * Refresh
             */
            refresh: string;
        }
        /**
         * TokenRefreshSerializer
         */
        export interface TokenRefreshSerializer {
            /**
             * Refresh
             */
            refresh: string;
            /**
             * Access
             */
            access?: string;
        }
        /**
         * TokenVerifySerializer
         */
        export interface TokenVerifySerializer {
            /**
             * Token
             */
            token: string;
        }
        /**
         * UserInSchema
         */
        export interface UserInSchema {
            /**
             * Email
             */
            email: string; // email
            /**
             * Username
             */
            username: string;
            /**
             * Password
             */
            password: string;
        }
        /**
         * UserOutSchema
         */
        export interface UserOutSchema {
            /**
             * Id
             */
            id?: number;
            /**
             * Username
             */
            username: string;
            /**
             * Score
             */
            score?: number;
            /**
             * Created At
             */
            created_at: string; // date-time
            /**
             * Followers
             */
            followers: /* UserSchema */ UserSchema[];
            /**
             * Following
             */
            following: /* UserSchema */ UserSchema[];
        }
        /**
         * UserSchema
         */
        export interface UserSchema {
            /**
             * Id
             */
            id?: number;
            /**
             * Username
             */
            username: string;
            /**
             * Score
             */
            score?: number;
            /**
             * Created At
             */
            created_at: string; // date-time
        }
        /**
         * VoteSchema
         */
        export interface VoteSchema {
            /**
             * User Id
             */
            user_id?: number;
            /**
             * Card Id
             */
            card_id: number;
            /**
             * Up
             */
            up: boolean;
        }
    }
}
declare namespace Paths {
    namespace $3e73e3feControllerVerifyToken {
        export type RequestBody = /* TokenVerifySerializer */ Components.Schemas.TokenVerifySerializer;
        namespace Responses {
            export type $200 = /* Schema */ Components.Schemas.Schema;
        }
    }
    namespace $9aa91fa7ControllerRefreshToken {
        export type RequestBody = /* TokenRefreshSchema */ Components.Schemas.TokenRefreshSchema;
        namespace Responses {
            export type $200 = /* TokenRefreshSerializer */ Components.Schemas.TokenRefreshSerializer;
        }
    }
    namespace C3eaa48fControllerObtainToken {
        export type RequestBody = /* TokenObtainPairSerializer */ Components.Schemas.TokenObtainPairSerializer;
        namespace Responses {
            export type $200 = /* TokenObtainPairOutput */ Components.Schemas.TokenObtainPairOutput;
        }
    }
    namespace CardApiCreateCard {
        export type RequestBody = /* CardInSchema */ Components.Schemas.CardInSchema;
        namespace Responses {
            export type $200 = /* CardInSchema */ Components.Schemas.CardInSchema;
        }
    }
    namespace CardApiCreateVote {
        export type RequestBody = /* VoteSchema */ Components.Schemas.VoteSchema;
        namespace Responses {
            export interface $200 {
            }
        }
    }
    namespace CardApiGetCard {
        namespace Parameters {
            /**
             * Card Id
             */
            export type CardId = number;
        }
        export interface PathParameters {
            card_id: /* Card Id */ Parameters.CardId;
        }
        namespace Responses {
            export type $200 = /* CardOutSchema */ Components.Schemas.CardOutSchema;
        }
    }
    namespace CardApiListCards {
        namespace Parameters {
            /**
             * Hashtags
             */
            export type Hashtags = string;
            /**
             * Page
             */
            export type Page = number;
        }
        export interface QueryParameters {
            hashtags?: /* Hashtags */ Parameters.Hashtags;
            page?: /* Page */ Parameters.Page;
        }
        namespace Responses {
            /**
             * Response
             */
            export type $200 = /* CardOutSchema */ Components.Schemas.CardOutSchema[];
        }
    }
    namespace CategoryApiCreateCategory {
        export type RequestBody = /* CategoryInSchema */ Components.Schemas.CategoryInSchema;
        namespace Responses {
            export type $200 = /* CategoryOutSchema */ Components.Schemas.CategoryOutSchema;
        }
    }
    namespace CategoryApiCreateSubscription {
        export type RequestBody = /* SubscriptionSchema */ Components.Schemas.SubscriptionSchema;
        namespace Responses {
            export type $200 = /* SubscriptionSchema */ Components.Schemas.SubscriptionSchema;
        }
    }
    namespace CategoryApiGetCategory {
        namespace Parameters {
            /**
             * Category Id
             */
            export type CategoryId = number;
        }
        export interface PathParameters {
            category_id: /* Category Id */ Parameters.CategoryId;
        }
        namespace Responses {
            export type $200 = /* CategoryOutSchema */ Components.Schemas.CategoryOutSchema;
        }
    }
    namespace CategoryApiListCategories {
        namespace Parameters {
            /**
             * Page
             */
            export type Page = number;
        }
        export interface QueryParameters {
            page?: /* Page */ Parameters.Page;
        }
        namespace Responses {
            /**
             * Response
             */
            export type $200 = /* CategoryOutSchema */ Components.Schemas.CategoryOutSchema[];
        }
    }
    namespace UserApiCreateUser {
        export type RequestBody = /* UserInSchema */ Components.Schemas.UserInSchema;
        namespace Responses {
            export type $200 = /* UserOutSchema */ Components.Schemas.UserOutSchema;
        }
    }
    namespace UserApiFollowUser {
        export type RequestBody = /* CreateFollowSchema */ Components.Schemas.CreateFollowSchema;
        namespace Responses {
            export type $200 = /* CreateFollowSchema */ Components.Schemas.CreateFollowSchema;
        }
    }
    namespace UserApiGetUser {
        namespace Parameters {
            /**
             * User Id
             */
            export type UserId = number;
        }
        export interface PathParameters {
            user_id: /* User Id */ Parameters.UserId;
        }
        namespace Responses {
            export type $200 = /* UserOutSchema */ Components.Schemas.UserOutSchema;
        }
    }
    namespace UserApiIsLoggedIn {
        namespace Responses {
            export interface $200 {
            }
        }
    }
    namespace UserApiListUsers {
        namespace Parameters {
            /**
             * Page
             */
            export type Page = number;
        }
        export interface QueryParameters {
            page?: /* Page */ Parameters.Page;
        }
        namespace Responses {
            /**
             * Response
             */
            export type $200 = /* UserSchema */ Components.Schemas.UserSchema[];
        }
    }
}

export interface OperationMethods {
  /**
   * 3e73e3fe_controller_verify_token - Verify Token
   */
  '3e73e3fe_controller_verify_token'(
    parameters?: Parameters<UnknownParamsObject> | null,
    data?: Paths.$3e73e3feControllerVerifyToken.RequestBody,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.$3e73e3feControllerVerifyToken.Responses.$200>
  /**
   * c3eaa48f_controller_obtain_token - Obtain Token
   */
  'c3eaa48f_controller_obtain_token'(
    parameters?: Parameters<UnknownParamsObject> | null,
    data?: Paths.C3eaa48fControllerObtainToken.RequestBody,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.C3eaa48fControllerObtainToken.Responses.$200>
  /**
   * 9aa91fa7_controller_refresh_token - Refresh Token
   */
  '9aa91fa7_controller_refresh_token'(
    parameters?: Parameters<UnknownParamsObject> | null,
    data?: Paths.$9aa91fa7ControllerRefreshToken.RequestBody,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.$9aa91fa7ControllerRefreshToken.Responses.$200>
  /**
   * user_api_get_user - Get User
   */
  'user_api_get_user'(
    parameters?: Parameters<Paths.UserApiGetUser.PathParameters> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.UserApiGetUser.Responses.$200>
  /**
   * user_api_list_users - List Users
   */
  'user_api_list_users'(
    parameters?: Parameters<Paths.UserApiListUsers.QueryParameters> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.UserApiListUsers.Responses.$200>
  /**
   * user_api_create_user - Create User
   */
  'user_api_create_user'(
    parameters?: Parameters<UnknownParamsObject> | null,
    data?: Paths.UserApiCreateUser.RequestBody,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.UserApiCreateUser.Responses.$200>
  /**
   * user_api_follow_user - Follow User
   */
  'user_api_follow_user'(
    parameters?: Parameters<UnknownParamsObject> | null,
    data?: Paths.UserApiFollowUser.RequestBody,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.UserApiFollowUser.Responses.$200>
  /**
   * user_api_is_logged_in - Is Logged In
   */
  'user_api_is_logged_in'(
    parameters?: Parameters<UnknownParamsObject> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.UserApiIsLoggedIn.Responses.$200>
  /**
   * category_api_get_category - Get Category
   */
  'category_api_get_category'(
    parameters?: Parameters<Paths.CategoryApiGetCategory.PathParameters> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.CategoryApiGetCategory.Responses.$200>
  /**
   * category_api_list_categories - List Categories
   */
  'category_api_list_categories'(
    parameters?: Parameters<Paths.CategoryApiListCategories.QueryParameters> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.CategoryApiListCategories.Responses.$200>
  /**
   * category_api_create_category - Create Category
   */
  'category_api_create_category'(
    parameters?: Parameters<UnknownParamsObject> | null,
    data?: Paths.CategoryApiCreateCategory.RequestBody,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.CategoryApiCreateCategory.Responses.$200>
  /**
   * category_api_create_subscription - Create Subscription
   */
  'category_api_create_subscription'(
    parameters?: Parameters<UnknownParamsObject> | null,
    data?: Paths.CategoryApiCreateSubscription.RequestBody,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.CategoryApiCreateSubscription.Responses.$200>
  /**
   * card_api_get_card - Get Card
   */
  'card_api_get_card'(
    parameters?: Parameters<Paths.CardApiGetCard.PathParameters> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.CardApiGetCard.Responses.$200>
  /**
   * card_api_list_cards - List Cards
   */
  'card_api_list_cards'(
    parameters?: Parameters<Paths.CardApiListCards.QueryParameters> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.CardApiListCards.Responses.$200>
  /**
   * card_api_create_card - Create Card
   */
  'card_api_create_card'(
    parameters?: Parameters<UnknownParamsObject> | null,
    data?: Paths.CardApiCreateCard.RequestBody,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.CardApiCreateCard.Responses.$200>
  /**
   * card_api_create_vote - Create Vote
   */
  'card_api_create_vote'(
    parameters?: Parameters<UnknownParamsObject> | null,
    data?: Paths.CardApiCreateVote.RequestBody,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.CardApiCreateVote.Responses.$200>
}

export interface PathsDictionary {
  ['/api/token/verify']: {
    /**
     * 3e73e3fe_controller_verify_token - Verify Token
     */
    'post'(
      parameters?: Parameters<UnknownParamsObject> | null,
      data?: Paths.$3e73e3feControllerVerifyToken.RequestBody,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.$3e73e3feControllerVerifyToken.Responses.$200>
  }
  ['/api/token/pair']: {
    /**
     * c3eaa48f_controller_obtain_token - Obtain Token
     */
    'post'(
      parameters?: Parameters<UnknownParamsObject> | null,
      data?: Paths.C3eaa48fControllerObtainToken.RequestBody,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.C3eaa48fControllerObtainToken.Responses.$200>
  }
  ['/api/token/refresh']: {
    /**
     * 9aa91fa7_controller_refresh_token - Refresh Token
     */
    'post'(
      parameters?: Parameters<UnknownParamsObject> | null,
      data?: Paths.$9aa91fa7ControllerRefreshToken.RequestBody,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.$9aa91fa7ControllerRefreshToken.Responses.$200>
  }
  ['/api/user/{user_id}']: {
    /**
     * user_api_get_user - Get User
     */
    'get'(
      parameters?: Parameters<Paths.UserApiGetUser.PathParameters> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.UserApiGetUser.Responses.$200>
  }
  ['/api/user/']: {
    /**
     * user_api_list_users - List Users
     */
    'get'(
      parameters?: Parameters<Paths.UserApiListUsers.QueryParameters> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.UserApiListUsers.Responses.$200>
    /**
     * user_api_create_user - Create User
     */
    'post'(
      parameters?: Parameters<UnknownParamsObject> | null,
      data?: Paths.UserApiCreateUser.RequestBody,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.UserApiCreateUser.Responses.$200>
  }
  ['/api/user/follow']: {
    /**
     * user_api_follow_user - Follow User
     */
    'post'(
      parameters?: Parameters<UnknownParamsObject> | null,
      data?: Paths.UserApiFollowUser.RequestBody,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.UserApiFollowUser.Responses.$200>
  }
  ['/api/user/is_logged_in']: {
    /**
     * user_api_is_logged_in - Is Logged In
     */
    'get'(
      parameters?: Parameters<UnknownParamsObject> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.UserApiIsLoggedIn.Responses.$200>
  }
  ['/api/category/{category_id}']: {
    /**
     * category_api_get_category - Get Category
     */
    'get'(
      parameters?: Parameters<Paths.CategoryApiGetCategory.PathParameters> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.CategoryApiGetCategory.Responses.$200>
  }
  ['/api/category/']: {
    /**
     * category_api_list_categories - List Categories
     */
    'get'(
      parameters?: Parameters<Paths.CategoryApiListCategories.QueryParameters> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.CategoryApiListCategories.Responses.$200>
    /**
     * category_api_create_category - Create Category
     */
    'post'(
      parameters?: Parameters<UnknownParamsObject> | null,
      data?: Paths.CategoryApiCreateCategory.RequestBody,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.CategoryApiCreateCategory.Responses.$200>
  }
  ['/api/category/subscribe']: {
    /**
     * category_api_create_subscription - Create Subscription
     */
    'post'(
      parameters?: Parameters<UnknownParamsObject> | null,
      data?: Paths.CategoryApiCreateSubscription.RequestBody,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.CategoryApiCreateSubscription.Responses.$200>
  }
  ['/api/card/{card_id}']: {
    /**
     * card_api_get_card - Get Card
     */
    'get'(
      parameters?: Parameters<Paths.CardApiGetCard.PathParameters> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.CardApiGetCard.Responses.$200>
  }
  ['/api/card/']: {
    /**
     * card_api_list_cards - List Cards
     */
    'get'(
      parameters?: Parameters<Paths.CardApiListCards.QueryParameters> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.CardApiListCards.Responses.$200>
    /**
     * card_api_create_card - Create Card
     */
    'post'(
      parameters?: Parameters<UnknownParamsObject> | null,
      data?: Paths.CardApiCreateCard.RequestBody,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.CardApiCreateCard.Responses.$200>
  }
  ['/api/card/vote']: {
    /**
     * card_api_create_vote - Create Vote
     */
    'post'(
      parameters?: Parameters<UnknownParamsObject> | null,
      data?: Paths.CardApiCreateVote.RequestBody,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.CardApiCreateVote.Responses.$200>
  }
}

export type Client = OpenAPIClient<OperationMethods, PathsDictionary>
