from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse

from app.infra.http.controllers import invite_controller
from app.infra.http.dependencies.current_user_dependency import CurrentUserDependency

current_user_dependency = CurrentUserDependency()

router = APIRouter(prefix="/api/user/invite", tags=["invite"])

router.add_api_route(
    "/",
    invite_controller.create_and_send_email,
    methods=["POST"],
    status_code=201,
)
router.add_api_route(
    "/{token}",
    invite_controller.validate_invitation_by_token,
    methods=["GET"],
    status_code=307,
)
