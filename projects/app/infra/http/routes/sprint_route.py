from fastapi import APIRouter, Depends

from app.infra.schemas.sprint import SprintSchema

from ..controllers import sprint_controller
from ..dependencies.current_user_dependency import CurrentUserDependency

current_user_dependency = CurrentUserDependency()

router = APIRouter(
    prefix="/sprint", dependencies=[Depends(current_user_dependency)], tags=["Sprint"]
)

router.add_api_route(
    "",
    sprint_controller.create,
    response_model=SprintSchema,
    methods=["POST"],
    status_code=201,
)

router.add_api_route(
    "/{id}",
    sprint_controller.partial_update,
    response_model=SprintSchema,
    methods=["PATCH"],
)
