from typing import Annotated

from app.application.use_cases import (
    NotificationCreateUseCase,
    NotificationGetAllActiveByUserUseCase,
    NotificationMarkAsReadUseCase,
)
from app.domain.errors import AppBaseException
from app.infra.factories.make_notification_use_cases import (
    make_notification_create_use_case,
    make_notification_get_all_active_by_user_use_case,
    make_notification_mark_as_read_use_case,
)
from app.infra.http.dependencies.get_user_id_dependency import get_user_id_dependency
from app.infra.schemas.notification_schemas import NotificationCreateSchema
from app.infra.websocket_connection_manager import websocket_connection_manager
from fastapi import Depends, HTTPException, WebSocket, WebSocketDisconnect


async def create(
    data: NotificationCreateSchema,
    use_case: NotificationCreateUseCase = Depends(make_notification_create_use_case),
):
    try:
        dict_data = data.model_dump()
        notification = use_case.execute(dict_data)  # type: ignore

        await websocket_connection_manager.send_data(
            {
                "id": notification["id"],
                "title": notification["title"],
                "description": notification["description"],
            },
            notification["user_id"],
        )

        return notification
    except AppBaseException as exception:
        raise HTTPException(detail=exception.message, status_code=exception.status_code)


def get_all_by_user(
    user_id: Annotated[int, Depends(get_user_id_dependency)],
    use_case: NotificationGetAllActiveByUserUseCase = Depends(
        make_notification_get_all_active_by_user_use_case
    ),
):
    return use_case.execute(user_id)


def mark_as_read(
    id: int,
    use_case: NotificationMarkAsReadUseCase = Depends(
        make_notification_mark_as_read_use_case
    ),
):
    try:
        return use_case.execute(id)
    except AppBaseException as exception:
        raise HTTPException(detail=exception.message, status_code=exception.status_code)


async def websocket_notifications(
    websocket: WebSocket,
    client_id: int,
    use_case: NotificationGetAllActiveByUserUseCase = Depends(
        make_notification_get_all_active_by_user_use_case
    ),
):
    await websocket_connection_manager.connect(client_id, websocket)
    try:
        results = use_case.execute(client_id)
        notifications = [
            {
                "id": item["id"],
                "title": item["title"],
                "description": item["description"],
            }
            for item in results
        ]

        await websocket_connection_manager.send_data(
            notifications,
            client_id,
        )
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        websocket_connection_manager.disconnect(websocket)
