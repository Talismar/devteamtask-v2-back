from enum import Enum
from typing import Set

from sqlalchemy import Enum as SqlAlchemyEnum
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.domain.enums import AuthProvidersEnum

from ..base_model import BaseModel
from ..mixins import TimestampMixin


class UserModel(TimestampMixin, BaseModel):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, unique=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(length=120))
    email: Mapped[str] = mapped_column(String(length=120), unique=True)
    password: Mapped[str]
    avatar_url: Mapped[str] = mapped_column(nullable=True)
    notification_state: Mapped[bool] = mapped_column(default=True)
    auth_provider: Mapped[Enum] = mapped_column(
        SqlAlchemyEnum(AuthProvidersEnum), nullable=True
    )

    notifications: Mapped[Set["NotificationModel"]] = relationship()

    # phone_number: Mapped[str] = mapped_column(String(32), nullable=True)
