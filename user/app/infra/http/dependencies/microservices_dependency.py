from fastapi import HTTPException, Request

from app.infra.configs.local import settings


class MicroservicesDependency:
    def __init__(self) -> None:
        pass

    async def __call__(
        self,
        request: Request,
    ):
        client_id = request.headers.get("x-client-id", None)

        if client_id != settings.PROJECT_SERVICE_CLIENT_ID:
            raise HTTPException(status_code=401, detail="Not authorized to access")
