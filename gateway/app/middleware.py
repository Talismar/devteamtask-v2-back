import httpx
from fastapi.responses import RedirectResponse
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse, Response


class GatewayMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, services):
        super().__init__(app)
        self.services = services

    async def dispatch(self, request: Request, call_next):
        if request["type"] != "http":
            return await call_next(request)

        path = request.url.path
        query = request.url.query

        service = None
        if path.startswith("/api/project"):
            service = self.services["project"]
        elif path.startswith("/api/user"):
            service = self.services["user"]

        if service:
            destination_url = (
                f"{service['url']}{path}{'?' + query if len(query) > 0 else ''}"
            )

            async with httpx.AsyncClient() as client:
                try:
                    response = await client.request(
                        request.method,
                        destination_url,
                        headers=dict(request.headers),
                        data=await request.body(),
                    )
                except httpx.ConnectError as connection_error:
                    return JSONResponse(
                        content={"detail": connection_error.__str__()}, status_code=500
                    )

            if response.status_code == 307:
                return RedirectResponse(response.url)

            if response.status_code == 204:
                return Response(
                    content="",
                    status_code=response.status_code,
                    headers=response.headers,
                )

            content_type = response.headers.get("content-type", None)

            return Response(
                content=response.content,
                headers=response.headers,
                status_code=response.status_code,
                media_type=content_type,
            )

        return await call_next(request)
