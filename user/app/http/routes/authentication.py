from app.schemas.authentication import AuthenticationTokenPostResponseSchema
from fastapi import APIRouter, Depends

from ..controllers import authentication

router = APIRouter(prefix="/api/user/authentication", tags=["authentication"])

router.add_api_route(
    "/token",
    authentication.authentication_token,
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
    authentication.refresh_token,
    response_model=AuthenticationTokenPostResponseSchema,
    methods=["POST"],
)
