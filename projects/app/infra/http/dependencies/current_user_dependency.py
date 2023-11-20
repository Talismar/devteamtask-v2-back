from app.main.configuration.local import settings
from fastapi import Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer
from httpx import AsyncClient

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/user/authentication/token")


class CurrentUserDependency:
    async def __call__(
        self,
        request: Request,
        access_token: str = Depends(oauth2_scheme),
    ):
        user_service_url = f"{settings.USER_SERVICE_URL}/user/me"
        headers = {"Authorization": f"Bearer {access_token}"}

        http_client: AsyncClient = request.state.http_client

        response = await http_client.request(
            method="GET", url=user_service_url, headers=headers, timeout=None
        )

        if response.status_code == 200:
            user_data = response.json()
            request.scope["user"] = user_data
        else:
            raise HTTPException(
                status_code=response.status_code, detail=response.json()["detail"]
            )
