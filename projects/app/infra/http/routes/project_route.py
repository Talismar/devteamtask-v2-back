from fastapi import APIRouter, Depends

from ...schemas.project import (
    ProjectListResponseSchema,
    ProjectResponseSchema,
    ProjectSchema,
)
from ..controllers import github_integration_controller, project_controller
from ..dependencies.current_user_dependency import CurrentUserDependency

current_user_dependency = CurrentUserDependency()

router = APIRouter(prefix="/project", tags=["project"])

router.add_api_route(
    "",
    project_controller.create,
    methods=["POST"],
    status_code=201,
    response_model=ProjectResponseSchema,
    dependencies=[Depends(current_user_dependency)],
)
router.add_api_route(
    "",
    project_controller.get_all,
    methods=["GET"],
    response_model=ProjectListResponseSchema,
    dependencies=[Depends(current_user_dependency)],
)
router.add_api_route(
    "/add_collaborator",
    project_controller.add_collaborator,
    methods=["GET"],
)
router.add_api_route(
    "/invite_collaborators",
    project_controller.invite_collaborators,
    methods=["POST"],
)
router.add_api_route(
    "/add_product_owner",
    project_controller.add_product_owner,
    methods=["GET"],
)
router.add_api_route(
    "/{id}",
    project_controller.get_by_id,
    methods=["GET"],
    # response_model=ProjectSchema,
    dependencies=[Depends(current_user_dependency)],
)
router.add_api_route(
    "/{id}", project_controller.remove, methods=["DELETE"], status_code=204
)
router.add_api_route(
    "/remove_tag_status/{id}",
    project_controller.remove_tag_status,
    methods=["DELETE"],
)
router.add_api_route(
    "/{id}",
    project_controller.partial_update,
    methods=["PATCH"],
    response_model=ProjectSchema,
    dependencies=[Depends(current_user_dependency)],
)
router.add_api_route(
    "/github/webhooks",
    github_integration_controller.github_webhooks,
    methods=["POST"],
    # include_in_schema=False,
)
