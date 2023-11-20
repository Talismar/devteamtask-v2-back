from datetime import datetime
from uuid import UUID

from pydantic import AnyHttpUrl, BaseModel, EmailStr


class InviteBaseSchema(BaseModel):
    resource_name: str
    resource_id: str
    expiration_date: datetime


class InviteSchema(InviteBaseSchema):
    id: int
    created_at: datetime
    updated_at: datetime
    # token: UUID


class InvitePostRequestSchema(InviteBaseSchema):
    emails: list[EmailStr]
    redirect_url: AnyHttpUrl
