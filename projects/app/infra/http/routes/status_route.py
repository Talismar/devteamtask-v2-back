from fastapi import APIRouter, Depends

from ...schemas.status import StatusSchema
from ..controllers import status_controller
from ..dependencies.current_user_dependency import CurrentUserDependency

current_user_dependency = CurrentUserDependency()

router = APIRouter(
    prefix="/status", dependencies=[Depends(current_user_dependency)], tags=["status"]
)

router.add_api_route("", status_controller.create, methods=["POST"], status_code=201)
router.add_api_route(
    "",
    status_controller.get_all,
    methods=["GET"],
    response_model=list[StatusSchema],
)
router.add_api_route(
    "/{id}",
    status_controller.get_by_id,
    methods=["GET"],
    response_model=StatusSchema,
)
# router.add_api_route(
#     "/{id}",
#     status.delete,
#     methods=["DELETE"],
#     status_code=204,
#     # dependencies=[Depends(current_user_dependency)],
# )
# router.add_api_route(
#     "/{user_id}",
#     user.partial_update,
#     methods=["PATCH"],
#     response_model=UserSchema,
#     dependencies=[Depends(current_user_dependency)],
# )
