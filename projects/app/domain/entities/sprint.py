from datetime import datetime
from typing import TypedDict
from uuid import UUID

from app.domain.enums import StateEnum


class Sprint(TypedDict, total=False):
    id: int
    name: str
    description: str
    state: StateEnum
    project_id: UUID
    created_at: datetime
    updated_at: datetime
