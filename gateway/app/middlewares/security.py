from httpx import AsyncClient
from starlette.datastructures import URL
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse


class SecurityMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, service_user_url, public_endpoints=[]):
        super().__init__(app)
        self.service_user_url = service_user_url
        self.public_endpoints = public_endpoints

    async def fetch_user_data_by_access_token(
        self, authorization_value: str, request: Request
    ):
        user_me_url = f"{self.service_user_url}api/user/user/me"
        headers = {"Authorization": authorization_value}

        http_client: AsyncClient = request.state.http_client

        response = await http_client.request(
            method="GET", url=user_me_url, headers=headers
        )

        if response.status_code == 200:
            user_data = response.json()
            return user_data
        else:
            return response.status_code, response.json()["detail"]

    async def dispatch(self, request: Request, call_next):
        if request["type"] != "http":
            return await call_next(request)

        if request.method not in ["POST", "GET", "PUT", "DELETE"]:
            return await call_next(request)

        authorization_value = request.headers.get("Authorization")

        url = URL(scope=request.scope)

        if self.is_public_endpoint(url.path, request.method) is None:
            if authorization_value is None:
                return JSONResponse(
                    content={"detail": "Not authenticated."}, status_code=401
                )

            user_data = await self.fetch_user_data_by_access_token(
                authorization_value, request
            )

            if not isinstance(user_data, dict):
                return JSONResponse(content=user_data[1], status_code=user_data[0])

            if url.path == "/api/user/user/me":
                return JSONResponse(content=user_data)

            request.scope["user"] = user_data

        return await call_next(request)

    def is_public_endpoint(self, path: str, method: str):
        for item in self.public_endpoints:
            if path == item["path"] and method in item["methods"]:
                return True
