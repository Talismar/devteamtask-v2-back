from datetime import datetime
from enum import Enum
from typing import Annotated
from uuid import UUID

from app.application.use_cases import (
    ProjectCreateUseCase,
    ProjectDeleteUseCase,
    ProjectGetAllUseCase,
    ProjectGetByIdUseCase,
    ProjectPartialUpdateUseCase,
    ProjectRemoveTagStatusUseCase,
)
from app.domain.errors import ResourceNotFoundException
from app.infra.factories import (
    make_project_create,
    make_project_delete,
    make_project_get_all,
    make_project_get_by_id,
    make_project_partial_update,
    make_project_remove_tag_status,
)
from app.infra.http.dependencies.get_user_id_dependency import get_user_id_dependency
from app.infra.schemas.project import (
    ProjectPartialUpdateParams,
    ProjectPostRequestSchema,
)
from fastapi import Depends, HTTPException, Path, Query, Request
from starlette.datastructures import UploadFile


class ResourceNameEnum(str, Enum):
    Tag = "Tag"
    Status = "Status"


def create(
    user_id: Annotated[int, Depends(get_user_id_dependency)],
    data: ProjectPostRequestSchema,
    use_case: ProjectCreateUseCase = Depends(make_project_create),
):
    return use_case.execute(
        {
            "leader_id": user_id,
            **data.model_dump(exclude_unset=True),
        }
    )


def get_all(
    request: Request, use_case: ProjectGetAllUseCase = Depends(make_project_get_all)
):
    user_id = request.scope.get("user")["id"]
    # print(user_id)
    return use_case.execute(user_id)


def get_by_id(
    id: Annotated[UUID, Path(title="The ID of the item to get")],
    use_case: ProjectGetByIdUseCase = Depends(make_project_get_by_id),
):
    try:
        return use_case.execute(id)
    except ResourceNotFoundException as error:
        raise HTTPException(status_code=404, detail=error.message)


def remove(id: UUID, use_case: ProjectDeleteUseCase = Depends(make_project_delete)):
    try:
        use_case.execute(id)
    except ResourceNotFoundException as error:
        raise HTTPException(status_code=404, detail=error.message)


def partial_update(
    id: Annotated[UUID, Path(title="The ID of the item to get")],
    form: ProjectPartialUpdateParams = Depends(ProjectPartialUpdateParams),
    use_case: ProjectPartialUpdateUseCase = Depends(make_project_partial_update),
):
    data = {}
    if isinstance(form.logo_url, UploadFile):
        data["logo_url"] = form.logo_url
    if isinstance(form.name, str):
        data["name"] = form.name
    if isinstance(form.end_date, datetime):
        data["end_date"] = form.end_date
    if isinstance(form.state, str):
        data["state"] = form.state
    if isinstance(form.product_owner_email, str):
        data["product_owner_email"] = form.product_owner_email

    try:
        return use_case.execute(id, data)
    except ResourceNotFoundException as error:
        raise HTTPException(status_code=404, detail=error.message)


def remove_tag_status(
    id: UUID,
    resource_name: ResourceNameEnum,
    resource_id: int,
    use_case: ProjectRemoveTagStatusUseCase = Depends(make_project_remove_tag_status),
):
    try:
        return use_case.execute(id, resource_name, resource_id)
    except ResourceNotFoundException as error:
        raise HTTPException(status_code=404, detail=error.message)


def add_collaborator(
    project_id: UUID,
    validation_state: str,
    # use_case: ProjectRemoveTagStatusUseCase = Depends(make_project_remove_tag_status),
):
    try:
        print(project_id, validation_state)
        return validation_state
    except ResourceNotFoundException as error:
        raise HTTPException(status_code=404, detail=error.message)
