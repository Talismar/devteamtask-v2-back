from datetime import datetime
from typing import TypedDict


class Daily(TypedDict, total=False):
    id: int
    note: str | None
    event_notes_id: int
    created_at: datetime
    updated_at: datetime
