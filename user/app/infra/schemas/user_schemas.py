from datetime import datetime
from typing import Optional, Union
from uuid import UUID

from fastapi import Form, UploadFile
from pydantic import BaseModel, EmailStr, Field


class UserBaseSchema(BaseModel):
    name: str
    email: EmailStr


class UserSchema(UserBaseSchema):
    id: int
    created_at: datetime
    updated_at: datetime
    avatar_url: Optional[str]
    auth_provider: Optional[str]
    notification_state: bool


class UserPostRequestSchema(UserBaseSchema):
    password: str = Field(
        description="Password of the user", min_length=6, max_length=8
    )
    password_confirm: str = Field(
        description="Confirm password", min_length=6, max_length=8
    )


class UserResetPasswortByTokenRequestSchema(BaseModel):
    invite_token: UUID
    password: str = Field(
        description="Password of the user", min_length=6, max_length=8
    )
    password_confirm: str = Field(
        description="Confirm password", min_length=6, max_length=8
    )


class UserChangePasswordRequestSchema(BaseModel):
    old_password: str = Field(
        description="Password of the user", min_length=6, max_length=8
    )
    new_password: str = Field(
        description="Confirm password", min_length=6, max_length=8
    )


class UserLoginPostRequestSchema(BaseModel):
    password: str = Field(
        description="Password of the user", min_length=6, max_length=8
    )
    email: EmailStr


class UserPartialUpdateRequestSchema(BaseModel):
    name: Optional[str] = None


class UserPartialUpdateParams:
    def __init__(
        self,
        avatar_url: Union[UploadFile, None] = None,
        name: Union[str, None] = Form(None),
    ):
        self.name = name
        self.avatar_url = avatar_url
