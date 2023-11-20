from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class DailyBaseSchema(BaseModel):
    note: Optional[str]


class DailySchema(DailyBaseSchema):
    id: int
    event_notes_id: int
    created_at: datetime
    updated_at: datetime


class DailyPostRequestSchema(DailyBaseSchema):
    sprint_id: int
    note: str | None


class DailyPartialUpdateRequestSchema(BaseModel):
    note: Optional[str] = None
