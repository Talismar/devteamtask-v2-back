from enum import Enum
from typing import Optional, Set

from sqlalchemy import Enum as SQLAlchemyEnum
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..associations import TaskTagModel
from ..base_model import BaseModel
from ..mixins import CommonMixin, TimestampMixin


class TaskModel(CommonMixin, TimestampMixin, BaseModel):
    name: Mapped[str] = mapped_column(String(length=120))
    description: Mapped[str] = mapped_column(nullable=True)
    priority: Mapped[int]

    # Relationships
    status_id: Mapped[int] = mapped_column(ForeignKey(column="status.id"))
    status: Mapped["StatusModel"] = relationship(back_populates="tasks")

    project_id: Mapped[int] = mapped_column(
        ForeignKey(column="project.id", ondelete="CASCADE")
    )
    project: Mapped["ProjectModel"] = relationship(back_populates="tasks")

    sprint_id: Mapped[Optional[int]] = mapped_column(ForeignKey(column="sprint.id"))
    sprint: Mapped["SprintModel"] = relationship()

    created_by_user_id: Mapped[int]
    assigned_to_user_id: Mapped[Optional[int]]

    # many to many
    tags: Mapped[Set["TagModel"]] = relationship(secondary=TaskTagModel)

    def __str__(self):
        return f"{self.id} - {self.name}"
