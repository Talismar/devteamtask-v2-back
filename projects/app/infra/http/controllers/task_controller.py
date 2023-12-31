from typing import Annotated
from uuid import UUID

from fastapi import BackgroundTasks, Depends, HTTPException, Path, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, Response
from httpx import AsyncClient

from app.application.use_cases import (
    TaskCreateUseCase,
    TaskDashboardDataUseCase,
    TaskDeleteUseCase,
    TaskGetAllUseCase,
    TaskGetByIdUseCase,
    TaskPartialUpdateUseCase,
)
from app.domain.errors import ResourceNotFoundException
from app.infra.factories import (
    make_task_create,
    make_task_dashboard_data,
    make_task_delete,
    make_task_get_all,
    make_task_get_by_id,
    make_task_partial_update,
)
from app.infra.schemas.task import TaskPartialUpdateRequestSchema, TaskPostRequestSchema
from app.main.configuration.local import settings

from ..dependencies.get_user_id_dependency import get_user_id_dependency


async def create(
    request: Request,
    user_id: Annotated[int, Depends(get_user_id_dependency)],
    background_task: BackgroundTasks,
    data: TaskPostRequestSchema,
    use_case: TaskCreateUseCase = Depends(make_task_create),
):
    try:
        http_client: AsyncClient = request.state.http_client

        data_to_create = data.model_dump(exclude_unset=True)
        data_to_create["created_by_user_id"] = user_id

        result = use_case.execute(data_to_create)  # type: ignore

        if result["assigned_to_user_id"] is not None:
            notification = {
                "title": "New task assignment for you",
                "description": result["name"],
                "user_id": result["assigned_to_user_id"],
            }
            notification_create_url = f"{settings.USER_SERVICE_URL}/notification/"
            background_task.add_task(
                http_client.post, url=notification_create_url, json=notification
            )

        return result
    except ResourceNotFoundException as error:
        raise HTTPException(status_code=404, detail=error.message)


def get_all_by_project_id(
    project_id: UUID,
    task_name: None | str = None,
    use_case: TaskGetAllUseCase = Depends(make_task_get_all),
):
    return use_case.execute(project_id, task_name)


def get_by_id(
    id: Annotated[int, Path(title="The ID of the item to get")],
    use_case: TaskGetByIdUseCase = Depends(make_task_get_by_id),
):
    try:
        return use_case.execute(id)
    except ResourceNotFoundException as error:
        raise HTTPException(status_code=404, detail=error.message)


def dashboard_data(
    user_id: Annotated[int, Depends(get_user_id_dependency)],
    use_case: TaskDashboardDataUseCase = Depends(make_task_dashboard_data),
):
    return use_case.execute(user_id)


def delete(id: int, use_case: TaskDeleteUseCase = Depends(make_task_delete)):
    try:
        use_case.execute(id)
        return Response(content="", status_code=204, media_type="application/json")
    except ResourceNotFoundException as exception:
        return JSONResponse(content={"detail": exception.message}, status_code=404)


# TESTING AFTER
def partial_update(
    id: int,
    data: TaskPartialUpdateRequestSchema,
    use_case: TaskPartialUpdateUseCase = Depends(make_task_partial_update),
):
    try:
        return use_case.execute(id, data.model_dump(exclude_unset=True))
    except ResourceNotFoundException as exception:
        return JSONResponse(content={"detail": exception.message}, status_code=404)
