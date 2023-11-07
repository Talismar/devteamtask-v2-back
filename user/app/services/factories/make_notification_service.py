from app.dependencies import get_db_connection
from app.repositories.sqlalchemy import SqlalchemyNotificationRepository
from fastapi import Depends

from ..notification_service import NotificationService


def make_notification_service(session=Depends(get_db_connection)):
    repository = SqlalchemyNotificationRepository(session)
    return NotificationService(repository)
