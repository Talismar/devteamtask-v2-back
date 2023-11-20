from typing import Optional

from pydantic import BaseModel


class EventNotesBaseSchema(BaseModel):
    planning: Optional[str]
    review: Optional[str]
    retrospective: Optional[str]


class EventNotesSchema(EventNotesBaseSchema):
    id: int
    sprint_id: int


class EventNotesPartialUpdateRequestSchema(BaseModel):
    planning: Optional[str] = None
    review: Optional[str] = None
    retrospective: Optional[str] = None
