from datetime import date as datetime_date
from typing import Any, Optional, Union
from uuid import UUID

from fastapi import File, Form, UploadFile
from pydantic import BaseModel, Field, HttpUrl

from .status import StatusSchema
from .tag import TagSchema


class TaskBaseSchema(BaseModel):
    name: str
    description: Optional[str] = None
    priority: int


class TaskSchema(TaskBaseSchema):
    id: int
    status: StatusSchema
    tags: list[TagSchema]
    created_by_user_id: int
    assigned_to_user_id: Optional[int]


class TaskPostRequestSchema(TaskBaseSchema):
    status_id: int
    tags_ids: list[int]
    sprint_id: Optional[int] = None
    assigned_to_user_id: Optional[int]
    project_id: UUID


class TaskPartialUpdateRequestSchema(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[int] = None
    sprint_id: Optional[int] = None
    status_id: Optional[int] = None
    tags_ids: Optional[list[int]] = None
    assigned_to_user_id: Optional[int] = None


class TotalCompletedByDaySchema(BaseModel):
    amount: int
    date: datetime_date


class TaskDashboardDataSchema(BaseModel):
    total_completed: int
    total_assigned: int
    total_scheduled: int
    total_task_in_last_7_days: int
    total_pending_in_last_7_days: int
    total_completed_by_day_in_last_7_days: list[TotalCompletedByDaySchema]


class TaskPartialUpdateParams:
    def __init__(
        self,
        name: Union[str, None] = Form(None),
    ):
        self.name = name
