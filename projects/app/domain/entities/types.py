import typing
from datetime import datetime
from uuid import UUID

from app.domain.enums import StateEnum


class StatusTypes(typing.TypedDict):
    id: int
    name: str


class TagTypes(typing.TypedDict):
    id: int
    name: str


class TaskTypes(typing.TypedDict, total=False):
    id: int
    name: str
    description: str
    priority: int
    created_at: datetime
    updated_at: datetime
    status_id: int
    status: StatusTypes
    tags: list[TagTypes]
    project_id: UUID
    sprint_id: int | None
    created_by_user_id: int
    assigned_to_user_id: int | None


class ProjectBaseTypes(typing.TypedDict, total=False):
    id: UUID
    name: str
    start_date: datetime
    end_date: datetime
    state: StateEnum
    logo_url: str | None
    leader_id: int
    product_owner_id: int | None
    collaborators_ids: set[int]


class SprintTypes(typing.TypedDict, total=False):
    id: int
    name: str
    description: str
    state: StateEnum
    project_id: UUID
    created_at: datetime
    updated_at: datetime
