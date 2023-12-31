from datetime import datetime
from enum import Enum
from typing import Annotated
from uuid import UUID

from fastapi import Depends, HTTPException, Path
from fastapi.responses import RedirectResponse
from starlette.datastructures import UploadFile

from app.application.use_cases import (
    ProjectAddCollaboratorUseCase,
    ProjectCreateUseCase,
    ProjectDeleteUseCase,
    ProjectGetAllUseCase,
    ProjectGetByIdUseCase,
    ProjectPartialUpdateUseCase,
    ProjectRemoveTagStatusUseCase,
)
from app.domain.errors import ResourceNotFoundException
from app.infra.factories import (
    make_project_add_collaborator,
    make_project_create,
    make_project_delete,
    make_project_get_all,
    make_project_get_by_id,
    make_project_partial_update,
    make_project_remove_tag_status,
)
from app.infra.http.dependencies.get_user_id_dependency import get_user_id_dependency
from app.infra.schemas.project import (
    ProjectInviteCollaboratorsSchema,
    ProjectPartialUpdateParams,
    ProjectPostRequestSchema,
)
from app.main.configuration.local import settings


def create(
    user_id: Annotated[int, Depends(get_user_id_dependency)],
    data: ProjectPostRequestSchema,
    use_case: ProjectCreateUseCase = Depends(make_project_create),
):
    dict_data = {"leader_id": user_id, **data.model_dump(exclude_unset=True)}
    return use_case.execute(dict_data)  # type: ignore


def get_all(
    user_id: Annotated[int, Depends(get_user_id_dependency)],
    use_case: ProjectGetAllUseCase = Depends(make_project_get_all),
):
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
        data["name"] = form.name  # type: ignore
    if isinstance(form.end_date, datetime):
        data["end_date"] = form.end_date  # type: ignore
    if isinstance(form.state, str):
        data["state"] = form.state  # type: ignore
    if isinstance(form.product_owner_email, str):
        data["product_owner_email"] = form.product_owner_email  # type: ignore

    if len(data.keys()) == 0:
        raise HTTPException(status_code=400)

    try:
        return use_case.execute(id, data)  # type: ignore
    except ResourceNotFoundException as error:
        raise HTTPException(status_code=404, detail=error.message)
    except Exception as exception:
        raise HTTPException(status_code=500, detail="Service email error")


def invite_collaborators(
    data: ProjectInviteCollaboratorsSchema,
    use_case: ProjectPartialUpdateUseCase = Depends(make_project_partial_update),
):
    try:
        return use_case.execute(data.project_id, {"collaborator_emails": data.emails})
    except ResourceNotFoundException as error:
        raise HTTPException(status_code=404, detail=error.message)
    except Exception as exception:
        raise HTTPException(status_code=500, detail=exception.args[0])


class ResourceNameEnum(str, Enum):
    Tag = "Tag"
    Status = "Status"


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


def add_product_owner(
    project_id: UUID,
    user_id: int,
    use_case: ProjectPartialUpdateUseCase = Depends(make_project_partial_update),
):
    response = RedirectResponse(settings.FRONT_END_URL)

    try:
        use_case.execute(project_id, {"product_owner_id": user_id})
    except Exception:
        response.set_cookie("error", "Error")

    return response


def add_collaborator(
    project_id: UUID,
    user_id: int,
    use_case: ProjectAddCollaboratorUseCase = Depends(make_project_add_collaborator),
):
    response = RedirectResponse(settings.FRONT_END_URL)
    try:
        use_case.execute(project_id, user_id)
        return response
    except ResourceNotFoundException as error:
        response.set_cookie("error", error.message)

    return response
