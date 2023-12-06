from datetime import datetime
from enum import Enum
from typing import Optional, Set
from uuid import UUID, uuid1

from sqlalchemy import Enum as SQLAlchemyEnum
from sqlalchemy import String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.domain.enums import StateEnum

from ..associations import ProjectStatusModel, ProjectTagModel
from ..base_model import BaseModel
from ..mixins import CommonMixin


class ProjectModel(CommonMixin, BaseModel):
    id: Mapped[UUID] = mapped_column(primary_key=True, unique=True, default=uuid1)  # type: ignore
    name: Mapped[str] = mapped_column(String(length=120))
    start_date: Mapped[datetime] = mapped_column(default=func.now())
    end_date: Mapped[datetime]
    state: Mapped[Enum] = mapped_column(
        SQLAlchemyEnum(StateEnum), default=StateEnum.IN_PROGRESS
    )
    logo_url: Mapped[Optional[str]] = mapped_column(String(length=120))
    leader_id: Mapped[int]
    product_owner_id: Mapped[int] = mapped_column(nullable=True)
    collaborators_ids: Mapped[Set["ProjectCollaboratorModel"]] = relationship()  # type: ignore

    # Relationships
    status: Mapped[Set["StatusModel"]] = relationship(  # type: ignore
        secondary=ProjectStatusModel,
        back_populates="projects",
        # order_by="StatusModel.id"
    )
    tags: Mapped[Set["TagModel"]] = relationship(  # type: ignore
        secondary=ProjectTagModel, back_populates="projects"
    )

    # References
    tasks: Mapped[Set["TaskModel"]] = relationship(  # type: ignore
        back_populates="project", cascade="all, delete-orphan"
    )
    sprints: Mapped[Set["SprintModel"]] = relationship(  # type: ignore
        back_populates="project", cascade="all, delete-orphan"
    )
