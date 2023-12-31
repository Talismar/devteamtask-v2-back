from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class StatusBaseSchema(BaseModel):
    name: str
    order: int


class StatusSchema(BaseModel):
    id: int
    name: str
    order: int


class StatusPostRequestSchema(StatusBaseSchema):
    project_id: UUID


class StatusPartialUpdateRequestSchema(BaseModel):
    name: Optional[str] = None
