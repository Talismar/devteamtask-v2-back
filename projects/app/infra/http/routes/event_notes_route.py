from fastapi import APIRouter, Depends

from app.infra.http.controllers import event_notes_controller
from app.infra.http.dependencies.current_user_dependency import CurrentUserDependency
from app.infra.schemas.event_notes import EventNotesSchema

current_user_dependency = CurrentUserDependency()

router = APIRouter(
    prefix="/event_notes",
    dependencies=[Depends(current_user_dependency)],
    tags=["Event Notes"],
)

router.add_api_route(
    "/{sprint_id}",
    event_notes_controller.get_by_sprint_id,
    response_model=EventNotesSchema,
    methods=["GET"],
)
router.add_api_route(
    "/{id}",
    event_notes_controller.partial_update,
    response_model=EventNotesSchema,
    methods=["PATCH"],
)
