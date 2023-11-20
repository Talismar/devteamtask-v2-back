from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, declared_attr, mapped_column


class CommonMixin:
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()[:-5]

    id: Mapped[int] = mapped_column(primary_key=True, unique=True, autoincrement=True)


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        default=func.now(), onupdate=func.now()
    )
