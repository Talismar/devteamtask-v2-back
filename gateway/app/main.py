from os import system

import httpx
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse, Response

from .configuration import settings

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
            print(destination_url)
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


# Microservices URLs
services_urls = {
    "project": {
        "url": "http://127.0.0.1:8001",
    },
    "user": {
        "url": "http://127.0.0.1:8002",
    },
}

app.add_middleware(GatewayMiddleware, services=services_urls)


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "service_project_url": services_urls["project"]["url"]
            + "/api/project/docs",
            "service_user_url": services_urls["user"]["url"] + "/api/user/docs",
        },
    )


system("clear")
# if __name__ == "__main__":
#     import uvicorn

#     uvicorn.run(app, host="http://localhost", port=8000, reload=True)
