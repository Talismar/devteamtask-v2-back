from fastapi import Depends

from app.application.use_cases import (
    NotificationCreateUseCase,
    NotificationGetAllActiveByUserUseCase,
    NotificationMarkAsReadUseCase,
)
from app.infra.dependencies import database_connection
from app.infra.repositories import NotificationSqlalchemyRepository


def make_notification_create_use_case(session=Depends(database_connection)):
    repository = NotificationSqlalchemyRepository(session)
    return NotificationCreateUseCase(repository)


def make_notification_mark_as_read_use_case(session=Depends(database_connection)):
    repository = NotificationSqlalchemyRepository(session)
    return NotificationMarkAsReadUseCase(repository)


def make_notification_get_all_active_by_user_use_case(
    session=Depends(database_connection),
):
    repository = NotificationSqlalchemyRepository(session)
    return NotificationGetAllActiveByUserUseCase(repository)
