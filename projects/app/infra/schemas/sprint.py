from typing import Any, Optional, Union
from uuid import UUID

from app.infra.database.enums import StateEnum
from fastapi import Form
from pydantic import BaseModel

from .status import StatusSchema


class SprintBaseSchema(BaseModel):
    name: str
    description: str
    state: StateEnum


class SprintSchema(SprintBaseSchema):
    id: int
    # project:
    # event_notes:


class SprintPostRequestSchema(SprintBaseSchema):
    project_id: UUID


class SprintPartialUpdateRequestSchema(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[int] = None


class SprintPartialUpdateParams:
    def __init__(
        self,
        name: Union[str, None] = Form(None),
    ):
        self.name = name
