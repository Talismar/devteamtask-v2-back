from typing import Set

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..associations import ProjectStatusModel
from ..base_model import BaseModel
from ..mixins import CommonMixin


class StatusModel(CommonMixin, BaseModel):
    name: Mapped[str] = mapped_column(String(length=24))
    order: Mapped[int]

    projects: Mapped[Set["ProjectModel"]] = relationship(
        secondary=ProjectStatusModel,
        back_populates="status",
        passive_deletes=True,
    )

    # References
    tasks: Mapped[Set["TaskModel"]] = relationship(back_populates="status")
