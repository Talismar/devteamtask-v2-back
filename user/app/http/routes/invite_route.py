from app.http.dependencies.current_user_dependency import CurrentUserDependency
from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse

from ...schemas.invite_schemas import InviteSchema
from ..controllers import invite_controller

current_user_dependency = CurrentUserDependency()

router = APIRouter(
    prefix="/api/user/invite",
    tags=["invite"],
)

router.add_api_route(
    "/",
    invite_controller.create_and_send_email,
    methods=["POST"],
    status_code=201,
    # dependencies=[Depends(current_user_dependency)],
)
router.add_api_route(
    "/{token}",
    invite_controller.validate_invitation_by_token,
    # response_model=InviteSchema,
    methods=["GET"],
)
# router.add_api_route(
#     "/me",
#     user.me,
#     methods=["GET"],
#     response_model=UserSchema,
#     dependencies=[Depends(current_user_dependency)],
# )
# router.add_api_route(
#     "/{user_id}",
#     user.get_one,
#     methods=["GET"],
#     response_model=UserSchema,
#     dependencies=[Depends(current_user_dependency)],
# )
# router.add_api_route(
#     "/{user_id}",
#     user.delete,
#     methods=["DELETE"],
#     status_code=204,
#     dependencies=[Depends(current_user_dependency)],
# )
# router.add_api_route(
#     "/{user_id}",
#     user.partial_update,
#     methods=["PATCH"],
#     response_model=UserSchema,
#     dependencies=[Depends(current_user_dependency)],
# )
