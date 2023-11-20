from datetime import datetime
from typing import TypedDict


class Notification(TypedDict, total=True):
    id: int
    title: str
    state: bool
    user_id: int
    description: str
    created_at: datetime
    updated_at: datetime
