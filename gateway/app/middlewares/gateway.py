from httpx import AsyncClient, ConnectError
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse, Response


class GatewayMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, services, public_endpoints=[]):
        super().__init__(app)
        self.services = services
        self.public_endpoints = public_endpoints

    async def dispatch(self, request: Request, call_next):
        if request["type"] != "http":
            return await call_next(request)

        path = request.url.path
        query = request.url.query
        user = request.scope.get("user")

        service = None
        if path.startswith("/api/project"):
            service = self.services["project"]
        elif path.startswith("/api/user"):
            service = self.services["user"]

        if service:
            destination_url = f"{service['url']}{path}{'?' + query if len(query) > 0 else ''}"  # noqa: E501

            try:
                http_client: AsyncClient = request.state.http_client

                raw_body = await request.body()
                headers = {**request.headers}

                if user is not None:
                    headers.update(
                        {
                            "user_id": str(user["id"]),
                            "user_name": user["name"],
                            "user_email": user["email"],
                        }
                    )

                response = await http_client.request(
                    request.method,
                    destination_url,
                    headers=headers,
                    content=raw_body,
                )

                return Response(
                    content=response.content,
                    headers=response.headers,
                    status_code=response.status_code,
                )
            except ConnectError as connection_error:
                return JSONResponse(
                    content={"detail": connection_error.__str__()},
                    status_code=500,  # noqa: E501
                )

        return await call_next(request)
