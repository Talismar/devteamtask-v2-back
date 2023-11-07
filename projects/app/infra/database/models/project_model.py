from datetime import datetime
from enum import Enum
from typing import Any, List, Optional, Set
from uuid import UUID, uuid1

from sqlalchemy import Enum as SQLAlchemyEnum
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..associations import ProjectCollaboratorModel, ProjectStatusModel, ProjectTagModel
from ..base_model import BaseModel
from ..enums import StateEnum
from ..mixins import CommonMixin


class ProjectModel(CommonMixin, BaseModel):
    id: Mapped[UUID] = mapped_column(primary_key=True, unique=True, default=uuid1)
    name: Mapped[str] = mapped_column(String(length=120))
    start_date: Mapped[datetime]
    end_date: Mapped[datetime]
    state: Mapped[Enum] = mapped_column(
        SQLAlchemyEnum(StateEnum), default=StateEnum.IN_PROGRESS
    )
    logo_url: Mapped[Optional[str]] = mapped_column(String(length=120))
    leader_id: Mapped[int]
    product_owner_id: Mapped[int] = mapped_column(nullable=True)
    collaborators_ids: Mapped[Set["ProjectCollaboratorModel"]] = relationship()

    # Relationships
    status: Mapped[Set["StatusModel"]] = relationship(
        secondary=ProjectStatusModel, back_populates="projects"
    )
    tags: Mapped[Set["TagModel"]] = relationship(
        secondary=ProjectTagModel, back_populates="projects"
    )

    # References
    tasks: Mapped[Set["TaskModel"]] = relationship(  # type: ignore # noqa: F821
        back_populates="project", cascade="all, delete-orphan"
    )
    sprints: Mapped[Set["SprintModel"]] = relationship(  # type: ignore # noqa: F821
        back_populates="project", cascade="all, delete-orphan"
    )


# class Project(Model):
#     leader = ForeignKey(User, on_delete=CASCADE, related_name="leader")
#     product_owner = ForeignKey(
#         User, on_delete=SET_NULL, null=True, blank=True, related_name="product_owner"
#     )
#     collaborators = ManyToManyField(User, related_name="collaborators", blank=True)
