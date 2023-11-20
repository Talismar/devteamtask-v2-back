from typing import Annotated

from fastapi import Depends, HTTPException, Path
from fastapi.responses import JSONResponse, Response

from app.application.use_cases import (
    StatusCreateUseCase,
    StatusDeleteUseCase,
    StatusGetAllUseCase,
    StatusGetByIdUseCase,
)
from app.domain.errors import ResourceNotFoundException
from app.infra.factories import (
    make_status_create,
    make_status_delete,
    make_status_get_all,
    make_status_get_by_id,
)
from app.infra.schemas.status import StatusPostRequestSchema


def create(
    data: StatusPostRequestSchema,
    use_case: StatusCreateUseCase = Depends(make_status_create),
):
    dict_data = data.model_dump()
    return use_case.execute(dict_data)


def get_all(use_case: StatusGetAllUseCase = Depends(make_status_get_all)):
    return use_case.execute()


def get_by_id(
    id: Annotated[int, Path(title="The ID of the item to get")],
    use_case: StatusGetByIdUseCase = Depends(make_status_get_by_id),
):
    try:
        return use_case.execute(id)
    except ResourceNotFoundException as error:
        raise HTTPException(status_code=404, detail=error.message)


def delete(id: int, use_case: StatusDeleteUseCase = Depends(make_status_delete)):
    try:
        success_message = use_case.execute(id)
        return Response(content="", status_code=204, media_type="application/json")
    except ResourceNotFoundException as exception:
        return JSONResponse(content={"detail": exception.message}, status_code=404)


# def partial_update(
#     user_id: int,
#     form: UserPartialUpdateRequestSchema,
#     user_service: UserService = Depends(make_user_service),
# ):
#     return user_service.partial_update(user_id, form)
