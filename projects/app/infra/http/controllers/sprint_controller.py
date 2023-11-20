from typing import Annotated

from fastapi import Depends, HTTPException

from app.application.use_cases import SprintCreateUseCase, SprintPartialUpdateUseCase
from app.domain.errors import BusinessRuleException, ResourceNotFoundException
from app.infra.factories import make_sprint_create, make_sprint_partial_update
from app.infra.schemas.sprint import (
    SprintPartialUpdateRequestSchema,
    SprintPostRequestSchema,
)

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


def partial_update(
    id: int,
    data: SprintPartialUpdateRequestSchema,
    use_case: SprintPartialUpdateUseCase = Depends(make_sprint_partial_update),
):
    try:
        dict_data = data.model_dump(exclude_unset=True)
        return use_case.execute(id, dict_data)  # type: ignore
    except ResourceNotFoundException as exception:
        raise HTTPException(status_code=404, detail=exception.message)
