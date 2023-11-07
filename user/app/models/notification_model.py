from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_model import BaseModel
from .mixin import CommonMixin, TimestampMixin


class NotificationModel(CommonMixin, TimestampMixin, BaseModel):
    title: Mapped[str] = mapped_column(String(120))
    description: Mapped[str] = mapped_column(String(120))
    state: Mapped[bool] = mapped_column(default=True)

    user_id: Mapped[int] = mapped_column(ForeignKey(column="users.id"))
    user: Mapped["UserModel"] = relationship(
        back_populates="notifications", cascade="all, delete"
    )
