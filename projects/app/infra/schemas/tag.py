from datetime import datetime
from typing import Any, Optional, Union
from uuid import UUID

from fastapi import File, Form, UploadFile
from pydantic import BaseModel, Field, HttpUrl


class TagBaseSchema(BaseModel):
    name: str


class TagSchema(TagBaseSchema):
    id: int
    name: str


class TagPostRequestSchema(TagBaseSchema):
    project_id: UUID


class TagPartialUpdateRequestSchema(BaseModel):
    name: Optional[str] = None


class TagPartialUpdateParams:
    def __init__(
        self,
        name: Union[str, None] = Form(None),
    ):
        self.name = name
