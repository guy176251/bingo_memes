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
         * AccessTokenOutput
         */
        export interface AccessTokenOutput {
            /**
             * Access
             */
            access: string;
        }
        /**
         * CardCreateSchema
         */
        export interface CardCreateSchema {
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
             * Title
             */
            title: string;
            /**
             * Id
             */
            id?: number;
            /**
             * Category Id
             */
            category_id: number;
        }
        /**
         * CardDetailSchema
         */
        export interface CardDetailSchema {
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
            id: number;
            /**
             * Title
             */
            title: string;
            author: /* UserListSchema */ UserListSchema;
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
             * Is Upvoted
             */
            is_upvoted?: boolean;
            category: /* CategoryListSchema */ CategoryListSchema;
        }
        /**
         * CardListSchema
         */
        export interface CardListSchema {
            /**
             * Id
             */
            id: number;
            /**
             * Title
             */
            title: string;
            author: /* UserListSchema */ UserListSchema;
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
             * Is Upvoted
             */
            is_upvoted?: boolean;
            category: /* CategoryListSchema */ CategoryListSchema;
        }
        /**
         * CardUpdateSchema
         */
        export interface CardUpdateSchema {
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
             * Title
             */
            title: string;
        }
        /**
         * CategoryCreateSchema
         */
        export interface CategoryCreateSchema {
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
         * CategoryDetailSchema
         */
        export interface CategoryDetailSchema {
            /**
             * Id
             */
            id: number;
            /**
             * Name
             */
            name: string;
            /**
             * Created At
             */
            created_at: string; // date-time
            /**
             * Description
             */
            description: string;
            /**
             * Icon Url
             */
            icon_url: string; // uri
            /**
             * Is Subscribed
             */
            is_subscribed?: boolean;
            author: /* UserListSchema */ UserListSchema;
            /**
             * Banner Url
             */
            banner_url: string; // uri
            /**
             * Hashtags
             */
            hashtags: /* HashtagSchema */ HashtagSchema[];
        }
        /**
         * CategoryListSchema
         */
        export interface CategoryListSchema {
            /**
             * Id
             */
            id: number;
            /**
             * Name
             */
            name: string;
            /**
             * Created At
             */
            created_at: string; // date-time
            /**
             * Description
             */
            description: string;
            /**
             * Icon Url
             */
            icon_url: string; // uri
            /**
             * Is Subscribed
             */
            is_subscribed?: boolean;
        }
        /**
         * FollowSchema
         */
        export interface FollowSchema {
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
         * SubscriptionSchema
         */
        export interface SubscriptionSchema {
            /**
             * Category Id
             */
            category_id: number;
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
         * UserCreateSchema
         */
        export interface UserCreateSchema {
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
            password: string; // password
        }
        /**
         * UserDetailSchema
         */
        export interface UserDetailSchema {
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
            followers: /* UserListSchema */ UserListSchema[];
            /**
             * Following
             */
            following: /* UserListSchema */ UserListSchema[];
            /**
             * Is Following
             */
            is_following?: boolean;
        }
        /**
         * UserListSchema
         */
        export interface UserListSchema {
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
    namespace CardCreate {
        export type RequestBody = /* CardCreateSchema */ Components.Schemas.CardCreateSchema;
        namespace Responses {
            export type $200 = /* CardCreateSchema */ Components.Schemas.CardCreateSchema;
        }
    }
    namespace CardGet {
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
            export type $200 = /* CardDetailSchema */ Components.Schemas.CardDetailSchema;
        }
    }
    namespace CardList {
        namespace Parameters {
            /**
             * Hashtags
             */
            export type Hashtags = string[];
            /**
             * Page
             */
            export type Page = number;
            /**
             * Sort
             */
            export type Sort = string;
        }
        export interface QueryParameters {
            sort?: /* Sort */ Parameters.Sort;
            hashtags?: /* Hashtags */ Parameters.Hashtags;
            page?: /* Page */ Parameters.Page;
        }
        namespace Responses {
            /**
             * Response
             */
            export type $200 = /* CardListSchema */ Components.Schemas.CardListSchema[];
        }
    }
    namespace CardUpdate {
        namespace Parameters {
            /**
             * Card Id
             */
            export type CardId = number;
        }
        export interface PathParameters {
            card_id: /* Card Id */ Parameters.CardId;
        }
        export type RequestBody = /* CardUpdateSchema */ Components.Schemas.CardUpdateSchema;
        namespace Responses {
            export type $200 = /* CardUpdateSchema */ Components.Schemas.CardUpdateSchema;
        }
    }
    namespace CategoryCreate {
        export type RequestBody = /* CategoryCreateSchema */ Components.Schemas.CategoryCreateSchema;
        namespace Responses {
            export type $200 = /* CategoryDetailSchema */ Components.Schemas.CategoryDetailSchema;
        }
    }
    namespace CategoryGet {
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
            export type $200 = /* CategoryDetailSchema */ Components.Schemas.CategoryDetailSchema;
        }
    }
    namespace CategoryList {
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
            export type $200 = /* CategoryListSchema */ Components.Schemas.CategoryListSchema[];
        }
    }
    namespace CheckLoggedIn {
        namespace Responses {
            export interface $200 {
            }
        }
    }
    namespace FollowUser {
        export type RequestBody = /* FollowSchema */ Components.Schemas.FollowSchema;
        namespace Responses {
            export interface $200 {
            }
        }
    }
    namespace GetCsrfToken {
        namespace Responses {
            export interface $200 {
            }
        }
    }
    namespace SubscribeCategory {
        export type RequestBody = /* SubscriptionSchema */ Components.Schemas.SubscriptionSchema;
        namespace Responses {
            export interface $200 {
            }
        }
    }
    namespace TokenObtainPair {
        export type RequestBody = /* TokenObtainPairSerializer */ Components.Schemas.TokenObtainPairSerializer;
        namespace Responses {
            export type $200 = /* AccessTokenOutput */ Components.Schemas.AccessTokenOutput;
        }
    }
    namespace TokenRefresh {
        namespace Responses {
            export type $200 = /* AccessTokenOutput */ Components.Schemas.AccessTokenOutput;
        }
    }
    namespace TokenUnpair {
        namespace Responses {
            export interface $200 {
            }
        }
    }
    namespace UserCreate {
        export type RequestBody = /* UserCreateSchema */ Components.Schemas.UserCreateSchema;
        namespace Responses {
            export type $200 = /* UserDetailSchema */ Components.Schemas.UserDetailSchema;
        }
    }
    namespace UserGet {
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
            export type $200 = /* UserDetailSchema */ Components.Schemas.UserDetailSchema;
        }
    }
    namespace UserList {
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
            export type $200 = /* UserListSchema */ Components.Schemas.UserListSchema[];
        }
    }
    namespace VoteCard {
        export type RequestBody = /* VoteSchema */ Components.Schemas.VoteSchema;
        namespace Responses {
            export interface $200 {
            }
        }
    }
}

export interface OperationMethods {
  /**
   * user_get - User Get
   */
  'user_get'(
    parameters?: Parameters<Paths.UserGet.PathParameters> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.UserGet.Responses.$200>
  /**
   * user_list - User List
   */
  'user_list'(
    parameters?: Parameters<Paths.UserList.QueryParameters> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.UserList.Responses.$200>
  /**
   * user_create - User Create
   */
  'user_create'(
    parameters?: Parameters<UnknownParamsObject> | null,
    data?: Paths.UserCreate.RequestBody,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.UserCreate.Responses.$200>
  /**
   * follow_user - User Follow
   */
  'follow_user'(
    parameters?: Parameters<UnknownParamsObject> | null,
    data?: Paths.FollowUser.RequestBody,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.FollowUser.Responses.$200>
  /**
   * check_logged_in - Is Logged In
   */
  'check_logged_in'(
    parameters?: Parameters<UnknownParamsObject> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.CheckLoggedIn.Responses.$200>
  /**
   * category_get - Get Category
   */
  'category_get'(
    parameters?: Parameters<Paths.CategoryGet.PathParameters> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.CategoryGet.Responses.$200>
  /**
   * category_list - List Categories
   */
  'category_list'(
    parameters?: Parameters<Paths.CategoryList.QueryParameters> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.CategoryList.Responses.$200>
  /**
   * category_create - Create Category
   */
  'category_create'(
    parameters?: Parameters<UnknownParamsObject> | null,
    data?: Paths.CategoryCreate.RequestBody,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.CategoryCreate.Responses.$200>
  /**
   * subscribe_category - Create Subscription
   */
  'subscribe_category'(
    parameters?: Parameters<UnknownParamsObject> | null,
    data?: Paths.SubscribeCategory.RequestBody,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.SubscribeCategory.Responses.$200>
  /**
   * card_get - Get Card
   */
  'card_get'(
    parameters?: Parameters<Paths.CardGet.PathParameters> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.CardGet.Responses.$200>
  /**
   * card_update - Update Card
   */
  'card_update'(
    parameters?: Parameters<Paths.CardUpdate.PathParameters> | null,
    data?: Paths.CardUpdate.RequestBody,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.CardUpdate.Responses.$200>
  /**
   * card_list - List Cards
   */
  'card_list'(
    parameters?: Parameters<Paths.CardList.QueryParameters> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.CardList.Responses.$200>
  /**
   * card_create - Create Card
   */
  'card_create'(
    parameters?: Parameters<UnknownParamsObject> | null,
    data?: Paths.CardCreate.RequestBody,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.CardCreate.Responses.$200>
  /**
   * vote_card - Create Vote
   */
  'vote_card'(
    parameters?: Parameters<UnknownParamsObject> | null,
    data?: Paths.VoteCard.RequestBody,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.VoteCard.Responses.$200>
  /**
   * token_obtain_pair - Obtain Token
   */
  'token_obtain_pair'(
    parameters?: Parameters<UnknownParamsObject> | null,
    data?: Paths.TokenObtainPair.RequestBody,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.TokenObtainPair.Responses.$200>
  /**
   * token_refresh - Refresh Token
   */
  'token_refresh'(
    parameters?: Parameters<UnknownParamsObject> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.TokenRefresh.Responses.$200>
  /**
   * get_csrf_token - Give Csrf Token
   */
  'get_csrf_token'(
    parameters?: Parameters<UnknownParamsObject> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.GetCsrfToken.Responses.$200>
  /**
   * token_unpair - Unpair Token
   */
  'token_unpair'(
    parameters?: Parameters<UnknownParamsObject> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.TokenUnpair.Responses.$200>
}

export interface PathsDictionary {
  ['/api/user/{user_id}']: {
    /**
     * user_get - User Get
     */
    'get'(
      parameters?: Parameters<Paths.UserGet.PathParameters> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.UserGet.Responses.$200>
  }
  ['/api/user/']: {
    /**
     * user_list - User List
     */
    'get'(
      parameters?: Parameters<Paths.UserList.QueryParameters> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.UserList.Responses.$200>
    /**
     * user_create - User Create
     */
    'post'(
      parameters?: Parameters<UnknownParamsObject> | null,
      data?: Paths.UserCreate.RequestBody,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.UserCreate.Responses.$200>
  }
  ['/api/user/follow']: {
    /**
     * follow_user - User Follow
     */
    'post'(
      parameters?: Parameters<UnknownParamsObject> | null,
      data?: Paths.FollowUser.RequestBody,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.FollowUser.Responses.$200>
  }
  ['/api/user/is_logged_in']: {
    /**
     * check_logged_in - Is Logged In
     */
    'get'(
      parameters?: Parameters<UnknownParamsObject> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.CheckLoggedIn.Responses.$200>
  }
  ['/api/category/{category_id}']: {
    /**
     * category_get - Get Category
     */
    'get'(
      parameters?: Parameters<Paths.CategoryGet.PathParameters> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.CategoryGet.Responses.$200>
  }
  ['/api/category/']: {
    /**
     * category_list - List Categories
     */
    'get'(
      parameters?: Parameters<Paths.CategoryList.QueryParameters> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.CategoryList.Responses.$200>
    /**
     * category_create - Create Category
     */
    'post'(
      parameters?: Parameters<UnknownParamsObject> | null,
      data?: Paths.CategoryCreate.RequestBody,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.CategoryCreate.Responses.$200>
  }
  ['/api/category/subscribe']: {
    /**
     * subscribe_category - Create Subscription
     */
    'post'(
      parameters?: Parameters<UnknownParamsObject> | null,
      data?: Paths.SubscribeCategory.RequestBody,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.SubscribeCategory.Responses.$200>
  }
  ['/api/card/{card_id}']: {
    /**
     * card_get - Get Card
     */
    'get'(
      parameters?: Parameters<Paths.CardGet.PathParameters> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.CardGet.Responses.$200>
    /**
     * card_update - Update Card
     */
    'put'(
      parameters?: Parameters<Paths.CardUpdate.PathParameters> | null,
      data?: Paths.CardUpdate.RequestBody,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.CardUpdate.Responses.$200>
  }
  ['/api/card/']: {
    /**
     * card_list - List Cards
     */
    'get'(
      parameters?: Parameters<Paths.CardList.QueryParameters> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.CardList.Responses.$200>
    /**
     * card_create - Create Card
     */
    'post'(
      parameters?: Parameters<UnknownParamsObject> | null,
      data?: Paths.CardCreate.RequestBody,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.CardCreate.Responses.$200>
  }
  ['/api/card/vote']: {
    /**
     * vote_card - Create Vote
     */
    'post'(
      parameters?: Parameters<UnknownParamsObject> | null,
      data?: Paths.VoteCard.RequestBody,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.VoteCard.Responses.$200>
  }
  ['/api/token/pair']: {
    /**
     * token_obtain_pair - Obtain Token
     */
    'post'(
      parameters?: Parameters<UnknownParamsObject> | null,
      data?: Paths.TokenObtainPair.RequestBody,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.TokenObtainPair.Responses.$200>
  }
  ['/api/token/refresh']: {
    /**
     * token_refresh - Refresh Token
     */
    'post'(
      parameters?: Parameters<UnknownParamsObject> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.TokenRefresh.Responses.$200>
  }
  ['/api/token/check_in']: {
    /**
     * get_csrf_token - Give Csrf Token
     */
    'get'(
      parameters?: Parameters<UnknownParamsObject> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.GetCsrfToken.Responses.$200>
  }
  ['/api/token/unpair']: {
    /**
     * token_unpair - Unpair Token
     */
    'post'(
      parameters?: Parameters<UnknownParamsObject> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.TokenUnpair.Responses.$200>
  }
}

export type Client = OpenAPIClient<OperationMethods, PathsDictionary>
