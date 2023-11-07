from uuid import UUID

from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import BaseModel

ProjectStatusModel = Table(
    "projectstatus",
    BaseModel.metadata,
    Column("project_id", ForeignKey("project.id"), primary_key=True),
    Column("status_id", ForeignKey("status.id"), primary_key=True),
)

ProjectTagModel = Table(
    "projecttag",
    BaseModel.metadata,
    Column("project_id", ForeignKey("project.id"), primary_key=True),
    Column("tag_id", ForeignKey("tag.id"), primary_key=True),
)

# ProjectCollaborator = Table(
#     "projectcollaborator",
#     BaseModel.metadata,
#     Column("project_id", ForeignKey("project.id"), primary_key=True),
#     Column("user_id", Integer),
# )


class ProjectCollaboratorModel(BaseModel):
    project_id: Mapped[UUID] = mapped_column(ForeignKey("project.id"), primary_key=True)
    user_id: Mapped[int]


TaskTagModel = Table(
    "tasktag",
    BaseModel.metadata,
    Column("task_id", ForeignKey("task.id"), primary_key=True),
    Column("tag_id", ForeignKey("tag.id"), primary_key=True),
)
# class TaskTagModel(BaseModel):
#     task_id: Mapped[int] = mapped_column(ForeignKey("task.id"), primary_key=True)
#     tag_id: Mapped[int] = mapped_column(ForeignKey("tag.id"), primary_key=True)
