from datetime import datetime
from typing import TypedDict
from uuid import UUID

from starlette.datastructures import UploadFile

from app.domain.enums import AuthProvidersEnum


class UserCreateRequestDTO(TypedDict, total=False):
    name: str
    email: str
    password: str
    password_confirm: str


class UserResetPasswordByTokenRequestDTO(TypedDict, total=False):
    invite_token: UUID
    password: str
    password_confirm: str


class UserChangePasswordRequestDTO(TypedDict, total=False):
    new_password: str
    old_password: str


class UserCreateByProviderRequestDTO(TypedDict):
    id: int
    login: str
    name: str | None
    email: str
    auth_provider: AuthProvidersEnum


class UserPartialUpdateRequestDTO(TypedDict):
    name: str | None
    avatar_url: UploadFile | None


class NotificationCreateRequestDTO(TypedDict):
    title: str
    description: str
    user_id: int


class InviteCreateRequestDTO(TypedDict):
    resource_name: str
    resource_id: str
    expiration_date: datetime


class AuthenticationGenerateTokensResquestDTO(TypedDict):
    email: str
    password: str


class AuthenticationTokensResponseDTO(TypedDict):
    access_token: str
    refresh_token: str
    token_type: str
