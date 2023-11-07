from fastapi import APIRouter, Depends, Response

from ...schemas.sprint import SprintSchema
from ..controllers import sprint_controller
from ..dependencies.current_user_dependency import CurrentUserDependency

current_user_dependency = CurrentUserDependency()

router = APIRouter(
    prefix="/sprint", dependencies=[Depends(current_user_dependency)], tags=["Sprint"]
)

router.add_api_route("", sprint_controller.create, methods=["POST"], status_code=201)
# router.add_api_route(
#     "",
#     task_controller.get_all,
#     methods=["GET"],
#     response_model=list[TaskSchema],
#     # dependencies=[Depends(current_user_dependency)],
# )
# router.add_api_route(
#     "/{id}",
#     task_controller.get_by_id,
#     methods=["GET"],
#     response_model=TaskSchema,
#     # dependencies=[Depends(current_user_dependency)],
# )
# router.add_api_route(
#     "/{id}",
#     task_controller.delete,
#     methods=["DELETE"],
#     response_class=Response,
#     # responses={204: {"model": None}}
#     # dependencies=[Depends(current_user_dependency)],
# )
# router.add_api_route(
#     "/{id}",
#     task_controller.partial_update,
#     methods=["PATCH"],
#     response_model=TaskSchema,
#     # dependencies=[Depends(current_user_dependency)],
# )
