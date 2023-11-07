from datetime import datetime

from pydantic import BaseModel


class NotificationBaseSchema(BaseModel):
    title: str
    description: str


class NotificationSchema(NotificationBaseSchema):
    id: int
    created_at: datetime
    updated_at: datetime


class NotificationCreateSchema(NotificationBaseSchema):
    user_id: int
