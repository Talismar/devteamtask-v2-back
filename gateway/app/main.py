from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

from .configuration import settings
from .middleware import GatewayMiddleware
from .utils import clear_terminal

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


clear_terminal()
# if __name__ == "__main__":
#     import uvicorn

#     uvicorn.run(app, host="http://localhost", port=8000, reload=True)
