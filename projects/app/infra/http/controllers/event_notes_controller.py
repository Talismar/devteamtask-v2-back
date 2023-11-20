from fastapi import Depends, HTTPException

from app.application.use_cases import (
    EventNotesGetByIdUseCase,
    EventNotesPartialUpdateUseCase,
)
from app.domain.errors import ResourceNotFoundException
from app.infra.factories import (
    make_event_notes_get_by_id,
    make_event_notes_partial_update,
)
from app.infra.schemas.event_notes import EventNotesPartialUpdateRequestSchema


def get_by_sprint_id(
    sprint_id: int,
    use_case: EventNotesGetByIdUseCase = Depends(make_event_notes_get_by_id),
):
    try:
        return use_case.execute(sprint_id)
    except ResourceNotFoundException as exception:
        raise HTTPException(status_code=404, detail=exception.message)


def partial_update(
    id: int,
    data: EventNotesPartialUpdateRequestSchema,
    use_case: EventNotesPartialUpdateUseCase = Depends(make_event_notes_partial_update),
):
    try:
        dict_data = data.model_dump(exclude_unset=True)
        return use_case.execute(id, dict_data)  # type: ignore
    except ResourceNotFoundException as exception:
        raise HTTPException(status_code=404, detail=exception.message)
