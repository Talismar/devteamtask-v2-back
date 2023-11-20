from enum import Enum
from uuid import UUID

from sqlalchemy import Enum as SQLAlchemyEnum
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.domain.enums import StateEnum

from ..base_model import BaseModel
from ..mixins import CommonMixin, TimestampMixin


class SprintModel(CommonMixin, TimestampMixin, BaseModel):
    name: Mapped[str] = mapped_column(String(length=120))
    description: Mapped[str]
    state: Mapped[Enum] = mapped_column(
        SQLAlchemyEnum(StateEnum), default=StateEnum.IN_PROGRESS
    )

    # Relationships
    project_id: Mapped[UUID] = mapped_column(
        ForeignKey(column="project.id", ondelete="CASCADE")
    )

    # References
    event_notes: Mapped["EventNotesModel"] = relationship(back_populates="sprint")
    project: Mapped["ProjectModel"] = relationship(back_populates="sprints")  # type: ignore
