from datetime import datetime
from typing import TypedDict
from uuid import UUID


class Invite(TypedDict, total=False):
    id: int
    resource_name: str
    resource_id: str
    expiration_date: datetime
    token: UUID
    email: str
    created_at: datetime
    updated_at: datetime
