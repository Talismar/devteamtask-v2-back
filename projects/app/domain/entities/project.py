from datetime import datetime
from uuid import UUID

from ..enums import StateEnum
from .status import Status
from .types import ProjectBaseTypes, SprintTypes, StatusTypes, TagTypes, TaskTypes


class Project(ProjectBaseTypes, total=False):
    sprints: list[SprintTypes]
    current_sprint: SprintTypes | None
    tasks: list[TaskTypes]
    tags: list[TagTypes]
    status: list[StatusTypes]
