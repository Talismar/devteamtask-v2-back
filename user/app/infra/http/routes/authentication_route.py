from fastapi import APIRouter

from app.infra.http.controllers import authentication_controller
from app.infra.schemas.authentication import AuthenticationTokenPostResponseSchema

router = APIRouter(prefix="/api/user/authentication", tags=["authentication"])

router.add_api_route(
    "/token",
    authentication_controller.authentication_token,
    response_model=AuthenticationTokenPostResponseSchema,
    methods=["POST"],
    status_code=200,
    openapi_extra={
        "requestBody": {
            "content": {
                "application/json": {
                    "schema": {
                        "required": ["email", "password"],
                        "type": "object",
                        "properties": {
                            "email": {"type": "string"},
                            "password": {"type": "string"},
                        },
                    }
                }
            },
            "required": True,
        },
    },
)
router.add_api_route(
    "/refresh_token",
    authentication_controller.refresh_token,
    response_model=AuthenticationTokenPostResponseSchema,
    methods=["POST"],
)
router.add_api_route(
    "/github_auth", authentication_controller.github_auth, methods=["GET"]
)
