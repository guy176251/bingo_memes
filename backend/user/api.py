from ninja import Router, NinjaAPI
from ninja.pagination import PageNumberPagination, paginate

from .models import AuthUser, Profile
from .schema import FollowSchema, UserCreateSchema, UserDetailSchema, UserListSchema

user_router = Router()


def add_user_exceptions(api: NinjaAPI):
    @api.exception_handler(Profile.DoesNotExist)
    def user_not_exist(request, exc):
        return api.create_response(
            request,
            {"detail": "Not a valid user id."},
            status=422,
        )


@user_router.get("{int:user_id}", response=UserDetailSchema, operation_id="user_get")
def user_get(request, user_id: int):
    return Profile.objects.outgoing(user=request.user).get(pk=user_id)


@user_router.get("", response=list[UserListSchema], operation_id="user_list")
@paginate(PageNumberPagination)
def user_list(request, **kwargs):
    return Profile.objects.outgoing(user=request.user)


@user_router.post("follow", operation_id="follow_user")
def user_follow(request, payload: FollowSchema):
    Profile.objects.follow(
        follower_id=request.user.profile.id,
        followed_id=payload.followed_id,
    )


@user_router.post("", auth=None, operation_id="user_create", url_name="user_create")
def user_create(request, payload: UserCreateSchema):
    AuthUser.objects.create_user(
        email=payload.email,
        username=payload.username,
        password=payload.password.get_secret_value(),
    )


@user_router.get("is_logged_in", operation_id="check_logged_in")
def is_logged_in(request):
    token_user = request.user
    return {
        "detail": "You're logged in!",
        "user": {
            "id": token_user.id,
            "username": token_user.username,
        },
    }
