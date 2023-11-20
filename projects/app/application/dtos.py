from datetime import datetime
from typing import Any, TypedDict
from uuid import UUID

from starlette.datastructures import UploadFile

from app.domain.enums import StateEnum


class SprintPartialUpdateRequestDTO(TypedDict, total=False):
    name: str
    description: str
    state: StateEnum


class ProjectPartialUpdateRequestDTO(TypedDict, total=False):
    name: None | str
    state: None | str
    logo_url: None | UploadFile
    end_date: None | datetime
    product_owner_email: str
    collaborator_emails: list[str]
    product_owner_id: int


class ProjectCreateRequestDTO(TypedDict, total=False):
    name: str
    end_date: datetime
    leader_id: int
    product_owner_email: str | None
    collaborators_email: list[str] | None
    status: Any


class TagRequestDTO(TypedDict, total=False):
    project_id: UUID
    name: str


class StatusRequestDTO(TypedDict, total=False):
    project_id: UUID
    name: str


class TaskCreateRequestDTO(TypedDict, total=False):
    name: str
    description: str
    project_id: UUID
    priority: int
    status_id: int
    sprint_id: None | int
    tags_ids: list[int]
    created_by_user_id: int
    assigned_to_user_id: None | int
