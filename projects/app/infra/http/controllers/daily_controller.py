from typing import Annotated

from fastapi import Depends, HTTPException, Path, Query

from app.application.use_cases import (
    DailyCreateUseCase,
    DailyGetAllBySprintIdUseCase,
    DailyGetByIdUseCase,
    DailyPartialUpdateUseCase,
)
from app.domain.errors import AppBaseException
from app.infra.factories import (
    make_daily_create,
    make_daily_get_all_by_sprint_id,
    make_daily_get_by_id,
    make_daily_partial_update,
)
from app.infra.schemas.daily import (
    DailyPartialUpdateRequestSchema,
    DailyPostRequestSchema,
)


def create(
    data: DailyPostRequestSchema,
    use_case: DailyCreateUseCase = Depends(make_daily_create),
):
    try:
        return use_case.execute(data.sprint_id, {"note": data.note})
    except AppBaseException as exception:
        raise HTTPException(status_code=404, detail=exception.message)


def get_all(
    sprint_id: Annotated[int, Query()],
    use_case: DailyGetAllBySprintIdUseCase = Depends(make_daily_get_all_by_sprint_id),
):
    try:
        return use_case.execute(sprint_id)
    except AppBaseException as exception:
        raise HTTPException(status_code=exception.status_code, detail=exception.message)


def get_by_id(
    id: Annotated[int, Path(title="The ID of the item to get")],
    use_case: DailyGetByIdUseCase = Depends(make_daily_get_by_id),
):
    try:
        print("Getting")
        return use_case.execute(id)
    except AppBaseException as error:
        raise HTTPException(status_code=404, detail=error.message)


def partial_update(
    id: Annotated[int, Path(title="The ID of the item to get")],
    data: DailyPartialUpdateRequestSchema,
    use_case: DailyPartialUpdateUseCase = Depends(make_daily_partial_update),
):
    return use_case.execute(id, data.model_dump(exclude_unset=True))  # type: ignore
