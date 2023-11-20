from typing import TypedDict

from app.domain.entities import daily, sprint


class EventNotes(TypedDict, total=False):
    id: int
    planning: str | None
    review: str | None
    retrospective: str | None
    sprint_id: int

    # sprint: sprint.Sprint
    # daily: set[daily.Daily]
