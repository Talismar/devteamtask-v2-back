from fastapi import APIRouter, Depends

from app.infra.http.controllers import user_controller
from app.infra.http.dependencies.current_user_dependency import CurrentUserDependency
from app.infra.schemas.user_schemas import UserSchema

current_user_dependency = CurrentUserDependency()

router = APIRouter(prefix="/api/user/user", tags=["user"])

router.add_api_route(
    "/",
    user_controller.create,
    methods=["POST"],
    status_code=201,
    response_model=UserSchema,
)
router.add_api_route("/github", user_controller.github_create, methods=["GET"])
router.add_api_route(
    "/forgot_password",
    user_controller.forgot_password,
    response_model=None,
    status_code=200,
    methods=["POST"],
)
router.add_api_route(
    "/me",
    user_controller.me,
    methods=["GET"],
    response_model=UserSchema,
    dependencies=[Depends(current_user_dependency)],
)
router.add_api_route(
    "/change_password",
    user_controller.change_password,
    methods=["PUT"],
    response_model=UserSchema,
    dependencies=[Depends(current_user_dependency)],
)
router.add_api_route(
    "/reset_password_by_token",
    user_controller.reset_password_by_token,
    methods=["PUT"],
    response_model=UserSchema,
)
router.add_api_route(
    "/{user_id}",
    user_controller.partial_update,
    methods=["PATCH"],
    response_model=UserSchema,
    dependencies=[Depends(current_user_dependency)],
)
