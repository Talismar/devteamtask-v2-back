from typing import Annotated

from app.application.use_cases import SprintCreateUseCase
from app.domain.errors import BusinessRuleException, ResourceNotFoundException
from app.infra.factories import make_sprint_create
from app.infra.schemas.sprint import SprintPostRequestSchema
from fastapi import Depends, HTTPException, Path, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, Response

from ..dependencies.get_user_id_dependency import get_user_id_dependency


def create(
    user_id: Annotated[int, Depends(get_user_id_dependency)],
    data: SprintPostRequestSchema,
    use_case: SprintCreateUseCase = Depends(make_sprint_create),
):
    try:
        data_to_create = data.model_dump()
        return use_case.execute(user_id, data_to_create)
    except ResourceNotFoundException as error:
        raise HTTPException(status_code=404, detail=error.message)
    except BusinessRuleException as error:
        raise HTTPException(status_code=400, detail=error.message)


# def get_all(use_case: TaskGetAllUseCase = Depends(make_task_get_all)):
#     return use_case.execute()


# def get_by_id(
#     id: Annotated[int, Path(title="The ID of the item to get")],
#     use_case: TaskGetByIdUseCase = Depends(make_task_get_by_id),
# ):
#     try:
#         return use_case.execute(id)
#     except ResourceNotFoundException as error:
#         raise HTTPException(status_code=404, detail=error.message)


# def delete(id: int, use_case: TaskDeleteUseCase = Depends(make_task_delete)):
#     try:
#         success_message = use_case.execute(id)
#         return Response(content="", status_code=204, media_type="application/json")
#     except ResourceNotFoundException as exception:
#         return JSONResponse(content={"detail": exception.message}, status_code=404)


# # TESTING AFTER
# def partial_update(
#     id: int,
#     data: TaskPartialUpdateRequestSchema,
#     use_case: TaskPartialUpdateUseCase = Depends(make_task_partial_update),
# ):
#     return use_case.execute(id, data.model_dump(exclude_unset=True))
