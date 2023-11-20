from datetime import datetime
from typing import Set, TypedDict

from app.domain.entities.notification import Notification
from app.domain.enums import AuthProvidersEnum


class User(TypedDict, total=False):
    id: int
    name: str
    email: str
    password: str
    auth_provider: AuthProvidersEnum | None
    avatar_url: str | None
    notification_state: bool
    notifications: Set[Notification]
    created_at: datetime
    updated_at: datetime

    # phone_number: str | None


# class User:
#     def __init__(
#         self,
#         name: str,
#         email: str,
#         password: str,
#         id: int = None,
#         created_at: datetime = datetime.now(),
#         updated_at: datetime = datetime.now(),
#         notifications: list[Notification] = [],
#         auth_provider: AuthProvidersEnum | None = None,
#         notification_state: bool = True,
#     ) -> None:
#         self.id = id
#         self.name = name
#         self.email = email
#         self.password = password
#         self.auth_provider = auth_provider
#         self.notification_state = notification_state
#         self.notifications = notifications
#         self.created_at = created_at
#         self.updated_at = updated_at

#     @property
#     def password(self):
#         return self.password

#     @password.setter
#     def password(self, value: str):
#         if self.auth_provider is None:
#             self.password = value
