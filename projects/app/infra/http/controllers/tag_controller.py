from typing import Annotated

from app.application.use_cases import TagCreateUseCase  # TagDeleteUseCase,
from app.application.use_cases import TagGetAllUseCase, TagGetByIdUseCase
from app.domain.errors import ResourceNotFoundException
from app.infra.factories import make_tag_create  # make_task_delete,
from app.infra.factories import make_tag_get_all, make_tag_get_by_id
from app.infra.schemas.tag import TagPostRequestSchema, TagSchema
from fastapi import Depends, Path
from fastapi.exceptions import HTTPException


def create(
    data: TagPostRequestSchema,
    use_case: TagCreateUseCase = Depends(make_tag_create),
):
    try:
        return use_case.execute(data.model_dump())
    except ResourceNotFoundException as error:
        raise HTTPException(status_code=404, detail=error.message)


def get_all(use_case: TagGetAllUseCase = Depends(make_tag_get_all)):
    return use_case.execute()


def get_by_id(
    id: Annotated[int, Path(title="The ID of the item to get")],
    use_case: TagGetByIdUseCase = Depends(make_tag_get_by_id),
) -> TagSchema | None:
    try:
        return use_case.execute(id)
    except ResourceNotFoundException as error:
        raise HTTPException(status_code=404, detail=error.message)


# def delete(id: int, use_case: TagDeleteUseCase = Depends(make_task_delete)):
#     return use_case.execute(id)


# def partial_update(
#     user_id: int,
#     form: UserPartialUpdateRequestSchema,
#     user_service: UserService = Depends(make_user_service),
# ):
#     return user_service.partial_update(user_id, form)
