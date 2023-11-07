from typing import Optional, Union
from uuid import UUID

from fastapi import Form
from pydantic import BaseModel

# from .task import TaskSchema


class StatusBaseSchema(BaseModel):
    name: str


class StatusSchema(StatusBaseSchema):
    id: int
    # tasks: list[TaskSchema]
    # projects: set


class StatusPostRequestSchema(StatusBaseSchema):
    project_id: UUID


class StatusPartialUpdateRequestSchema(BaseModel):
    name: Optional[str] = None


class StatusPartialUpdateParams:
    def __init__(
        self,
        name: Union[str, None] = Form(None),
    ):
        self.name = name
