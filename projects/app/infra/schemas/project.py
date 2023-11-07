from datetime import datetime
from typing import Optional, Union
from uuid import UUID

from fastapi import Form, UploadFile
from pydantic import BaseModel, EmailStr

from .sprint import SprintSchema
from .status import StatusSchema
from .tag import TagSchema
from .task import TaskSchema


class ProjectBaseSchema(BaseModel):
    name: str
    # "name": "Project Two",
    start_date: datetime
    # "start_date": "2023-10-29T19:37:39.931000",
    end_date: datetime
    # "end_date": "2023-10-29T19:37:39.931000",


class ProjectResponseSchema(ProjectBaseSchema):
    id: UUID
    # "id": "0bd2dec2-7c0a-11ee-8a1e-f09e4ac22c2f",
    logo_url: Optional[str]
    # "logo_url": null,
    state: str
    # "state": "IN PROGRESS",
    # "leader_id": 1,
    # "product_owner_id": null,
    # "collaborators_ids": [],
    leader_id: int
    product_owner_id: Optional[str]
    collaborators_ids: list[int]
    tasks: list[TaskSchema]
    status: list[StatusSchema]
    tags: list[TagSchema]
    sprints: list[SprintSchema]


class ProjectPostRequestSchema(ProjectBaseSchema):
    product_owner_email: Optional[EmailStr] = None
    collaborators_email: Optional[list[EmailStr]] = None


class UserSchema(BaseModel):
    id: int
    name: str
    avatar_url: Optional[str]


class ProjectSchema(BaseModel):
    project_data: ProjectResponseSchema
    users: list[UserSchema]


class ProjectListResponseSchema(BaseModel):
    projects: list[ProjectResponseSchema]
    users: list[UserSchema]


class ProjectPartialUpdateRequestSchema(BaseModel):
    name: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    state: Optional[str] = None


class ProjectPartialUpdateParams:
    def __init__(
        self,
        name: Union[str, None] = Form(None),
        end_date: Union[datetime, None] = Form(None),
        logo_url: Union[UploadFile, None] = Form(None),
        state: Union[str, None] = Form(None),
        product_owner_email: Union[EmailStr, None] = Form(None),
    ):
        self.name = name
        self.logo_url = logo_url
        self.end_date = end_date
        self.state = state
        self.product_owner_email = product_owner_email

    def __str__(self) -> str:
        return f"name: {self.name}\nlogo_ur: {self.logo_url}\nend_data: {self.end_date}\nstate: {self.state}"
