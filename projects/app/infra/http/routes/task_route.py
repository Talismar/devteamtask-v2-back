from fastapi import APIRouter, Depends, Response

from ...schemas.task import TaskDashboardDataSchema, TaskSchema
from ..controllers import task_controller
from ..dependencies.current_user_dependency import CurrentUserDependency

current_user_dependency = CurrentUserDependency()

router = APIRouter(
    prefix="/task",
    dependencies=[Depends(current_user_dependency)],
    tags=["task"],
)

router.add_api_route("", task_controller.create, methods=["POST"], status_code=201)
router.add_api_route(
    "/dashboard_data",
    task_controller.dashboard_data,
    methods=["GET"],
    response_model=TaskDashboardDataSchema,
)
router.add_api_route(
    "/{project_id}",
    task_controller.get_all_by_project_id,
    methods=["GET"],
    response_model=list[TaskSchema],
)
router.add_api_route(
    "/{id}",
    task_controller.get_by_id,
    methods=["GET"],
    response_model=TaskSchema,
)
router.add_api_route(
    "/{id}",
    task_controller.delete,
    methods=["DELETE"],
    response_class=Response,
    # responses={204: {"model": None}}
    # dependencies=[Depends(current_user_dependency)],
)
router.add_api_route(
    "/{id}",
    task_controller.partial_update,
    methods=["PATCH"],
    response_model=TaskSchema,
    # dependencies=[Depends(current_user_dependency)],
)
