from app.http.dependencies.current_user_dependency import CurrentUserDependency
from app.schemas.notification_schemas import NotificationSchema
from fastapi import APIRouter, Depends

from ..controllers import notification_controller

current_user_dependency = CurrentUserDependency()

router = APIRouter(
    prefix="/api/user/notification",
    dependencies=[Depends(current_user_dependency)],
    tags=["Notification"],
)

router.add_api_route(
    "/",
    notification_controller.create,
    methods=["POST"],
    response_model=NotificationSchema,
    status_code=201,
)
router.add_api_route(
    "/",
    notification_controller.get_all_by_user,
    response_model=list[NotificationSchema],
    methods=["GET"],
)
router.add_api_route(
    "/mark_as_read/{id}",
    notification_controller.mark_as_read,
    methods=["PATCH"],
    response_model=None,
)

# router.add_api_route(
#     "/{id}",
#     notification_controller.delete,
#     methods=["DELETE"],
#     status_code=204,
# )
