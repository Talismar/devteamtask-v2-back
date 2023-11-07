from typing import Annotated

from fastapi import Depends
from fastapi.responses import JSONResponse

from ...schemas.notification_schemas import NotificationCreateSchema, NotificationSchema
from ...services.factories.make_notification_service import make_notification_service
from ...services.notification_service import NotificationService
from ..dependencies.get_user_id_dependency import get_user_id_dependency


def create(
    data: NotificationCreateSchema,
    notification_service: NotificationService = Depends(make_notification_service),
):
    notification_data = notification_service.create(data.model_dump())
    return notification_data


def get_all_by_user(
    user_id: Annotated[int, Depends(get_user_id_dependency)],
    notification_service: NotificationService = Depends(make_notification_service),
):
    return notification_service.get_all(user_id)


def mark_as_read(
    id: int,
    notification_service: NotificationService = Depends(make_notification_service),
):
    try:
        notification_service.mark_as_read(id)
    except Exception as e:
        return JSONResponse(
            content={"detail": "Error marking as read"}, status_code=400
        )
