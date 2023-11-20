from app.infra.http.controllers import notification_controller
from app.infra.http.dependencies import CurrentUserDependency, MicroservicesDependency
from app.infra.schemas.notification_schemas import NotificationSchema
from fastapi import APIRouter, Depends

current_user_dependency = CurrentUserDependency()
microservices_dependency = MicroservicesDependency()

router = APIRouter(
    prefix="/api/user/notification",
    tags=["Notification"],
)

router.add_api_route(
    "/",
    notification_controller.create,
    methods=["POST"],
    dependencies=[Depends(microservices_dependency)],
    response_model=NotificationSchema,
    status_code=201,
)
router.add_api_route(
    "/",
    notification_controller.get_all_by_user,
    dependencies=[Depends(current_user_dependency)],
    response_model=list[NotificationSchema],
    methods=["GET"],
)
router.add_api_route(
    "/mark_as_read/{id}",
    notification_controller.mark_as_read,
    dependencies=[Depends(current_user_dependency)],
    methods=["PATCH"],
    response_model=NotificationSchema,
)
