from os import path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

from app.configuration import settings
from app.lifespan import lifespan
from app.middlewares.gateway import GatewayMiddleware
from app.middlewares.security import SecurityMiddleware

app = FastAPI(lifespan=lifespan)


app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


app.add_middleware(GatewayMiddleware, services=settings.MICROSERVICES_URLS)
app.add_middleware(
    SecurityMiddleware,
    service_user_url=settings.SERVICE_USER_URL,
    public_endpoints=settings.PUBLIC_ENDPOINTS,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/favicon.ico")
async def favicon():
    file_name = "favicon.ico"
    file_path = path.join(app.root_path, "static", file_name)
    return FileResponse(
        path=file_path,
        headers={"Content-Disposition": "attachment; filename=" + file_name},
    )


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "service_project_url": settings.MICROSERVICES_URLS["project"][
                "url"
            ]  # noqa: E501
            + "/api/project/docs",
            "service_user_url": settings.MICROSERVICES_URLS["user"]["url"]
            + "/api/user/docs",
        },
    )
