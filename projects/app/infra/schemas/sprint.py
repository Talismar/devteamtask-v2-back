from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from app.domain.enums import StateEnum


class SprintBaseSchema(BaseModel):
    name: str
    description: str


class SprintSchema(SprintBaseSchema):
    id: int
    updated_at: datetime
    created_at: datetime
    state: StateEnum
    project_id: UUID

    # project:
    # event_notes:


class SprintPostRequestSchema(SprintBaseSchema):
    project_id: UUID


class SprintPartialUpdateRequestSchema(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    state: Optional[StateEnum] = None
