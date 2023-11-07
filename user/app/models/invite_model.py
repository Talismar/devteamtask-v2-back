from datetime import datetime
from uuid import UUID, uuid1

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import BaseModel
from .mixin import CommonMixin, TimestampMixin


class InviteModel(CommonMixin, TimestampMixin, BaseModel):
    resource_name: Mapped[str] = mapped_column(String(32))
    resource_id: Mapped[str]
    expiration_date: Mapped[datetime]
    token: Mapped[UUID] = mapped_column(default=uuid1())
