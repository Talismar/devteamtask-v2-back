from fastapi import APIRouter, Depends

from app.infra.http.controllers import daily_controller

from ...schemas.daily import DailySchema
from ..dependencies.current_user_dependency import CurrentUserDependency

current_user_dependency = CurrentUserDependency()

router = APIRouter(
    prefix="/daily", dependencies=[Depends(current_user_dependency)], tags=["daily"]
)

router.add_api_route("", daily_controller.create, methods=["POST"], status_code=201)
router.add_api_route(
    "",
    daily_controller.get_all,
    methods=["GET"],
    response_model=list[DailySchema],
)
router.add_api_route(
    "/{id}",
    daily_controller.get_by_id,
    methods=["GET"],
    response_model=DailySchema,
)
# router.add_api_route(
#     "/{user_id}",
#     status.delete,
#     methods=["DELETE"],
#     status_code=204,
#     dependencies=[Depends(current_user_dependency)],
# )
router.add_api_route(
    "/{id}",
    daily_controller.partial_update,
    methods=["PATCH"],
    response_model=DailySchema,
)
