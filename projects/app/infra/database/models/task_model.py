from enum import Enum
from typing import Optional, Set

from sqlalchemy import Enum as SQLAlchemyEnum
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..associations import TaskTagModel
from ..base_model import BaseModel
from ..enums import DefaultStatusEnum
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
    project: Mapped["ProjectModel"] = relationship(back_populates="tasks")  # type: ignore

    # sprint_id = ForeignKey(Sprint, on_delete=CASCADE, null=True, blank=True)

    created_by_user_id: Mapped[int]
    assigned_to_user_id: Mapped[Optional[int]]

    # many to many
    tags: Mapped[Set["TagModel"]] = relationship(secondary=TaskTagModel)


# class Parent(Base):
#     __tablename__ = "parent_table"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     children: Mapped[List["Child"]] = relationship(back_populates="parent")


# class Child(Base):
#     __tablename__ = "child_table"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     parent_id: Mapped[int] = mapped_column(ForeignKey("parent_table.id"))
#     parent: Mapped["Parent"] = relationship(back_populates="children")


# class Tasks(Model):


# def __str__(self):
#     return f"{self.pk} - {self.project_id.name}"

# @classmethod
# def get_total_completed(cls, user: User):
#     status_instance, created = Status.objects.get_or_create(name="Done")
#     return cls.objects.filter(status=status_instance, assigned_to=user).count()

# @classmethod
# def get_total_assigned(cls, user: User):
#     return cls.objects.filter(assigned_to=user).count()

# @classmethod
# def get_total_completed_in_last_7_days(cls, user: User):
#     status_instance, created = Status.objects.get_or_create(name="Done")
#     queryset = cls.objects.filter(
#         assigned_to=user, status=status_instance, updated_at__gte=datetime.now() - timedelta(days=7)
#     )

#     def total_by_date(date: datetime):
#         return cls.objects.filter(
#             assigned_to=user, status=status_instance, updated_at__contains=str(date.date())
#         ).count()

#     data = []
#     for item in queryset:
#         data.append({"date": item.updated_at.date(), "amount": total_by_date(item.updated_at)})

#     return data

# @classmethod
# def get_total_pending_in_last_7_days(cls, user: User):
#     status_instance, created = Status.objects.get_or_create(name="To do")

#     return cls.objects.filter(
#         assigned_to=user, status=status_instance, updated_at__gte=datetime.now() - timedelta(days=7)
#     ).count()

# @staticmethod
# def get_total_task_in_last_7_days(user: User):
#     return Tasks.objects.filter(
#         Q(project_id__leader=user.pk)
#         | Q(project_id__collaborators__pk=user.pk)
#         | Q(project_id__product_owner=user.pk),
#         assigned_to__isnull=True,
#         updated_at__gte=datetime.now() - timedelta(days=7),
#     ).count()

# @staticmethod
# def get_total_scheduled(user: User):
#     return Tasks.objects.filter(
#         Q(project_id__leader=user.pk)
#         | Q(project_id__collaborators__pk=user.pk)
#         | Q(project_id__product_owner=user.pk),
#         assigned_to__isnull=True,
#     ).count()

# class Meta:
#     verbose_name = "Task"
#     verbose_name_plural = "Tasks"
