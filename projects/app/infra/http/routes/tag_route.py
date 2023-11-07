from fastapi import APIRouter, Depends

from ...schemas.tag import TagSchema
from ..controllers import tag_controller
from ..dependencies.current_user_dependency import CurrentUserDependency

current_user_dependency = CurrentUserDependency()

router = APIRouter(
    prefix="/tag", dependencies=[Depends(current_user_dependency)], tags=["tag"]
)

router.add_api_route("", tag_controller.create, methods=["POST"], status_code=201)
router.add_api_route(
    "",
    tag_controller.get_all,
    methods=["GET"],
    response_model=list[TagSchema],
    # dependencies=[Depends(current_user_dependency)],
)
router.add_api_route(
    "/{id}",
    tag_controller.get_by_id,
    methods=["GET"],
    # response_model=,
    # dependencies=[Depends(current_user_dependency)],
)
# router.add_api_route(
#     "/{user_id}",
#     status.delete,
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
