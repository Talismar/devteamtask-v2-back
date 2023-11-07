from enum import Enum

from sqlalchemy import Enum as SqlAlchemyEnum
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_model import BaseModel
from .enums import AuthProvidersEnum
from .mixin import CommonMixin, TimestampMixin


class UserModel(TimestampMixin, BaseModel):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, unique=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(length=120))
    email: Mapped[str] = mapped_column(String(length=120), unique=True)
    password: Mapped[str]
    phone_number: Mapped[str] = mapped_column(String(32), nullable=True)
    avatar_url: Mapped[str] = mapped_column(nullable=True)
    notification_state: Mapped[bool] = mapped_column(default=True)
    auth_provider: Mapped[Enum] = mapped_column(
        SqlAlchemyEnum(AuthProvidersEnum), nullable=True
    )

    notifications: Mapped["NotificationModel"] = relationship()
