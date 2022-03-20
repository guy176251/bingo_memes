from typing import Optional

from email_validator import EmailNotValidError, caching_resolver, validate_email
from ninja import ModelSchema, Schema
from ninja.errors import ValidationError
from pydantic import EmailStr, SecretStr, validator

from .models import AuthUser, Profile

resolver = caching_resolver(timeout=10)


class UserListSchema(ModelSchema):
    class Config:
        model = Profile
        model_fields = ["id", "username", "created_at"]


class UserDetailSchema(UserListSchema):
    followers: list[UserListSchema]
    following: list[UserListSchema]
    is_following: Optional[bool]


class UserCreateSchema(Schema):
    email: EmailStr
    username: str
    password: SecretStr

    @validator("email")
    def validate_email_field(cls, email):
        try:
            validate_email(email, dns_resolver=resolver)
        except EmailNotValidError:
            raise ValidationError([{"detail": "Invalid email."}])
        return email

    @validator("username")
    def check_username_length(cls, username):
        if len(username) > AuthUser.USERNAME_LENGTH:
            raise ValidationError([{"detail": "Username too long."}])
        return username


class FollowSchema(Schema):
    followed_id: int
