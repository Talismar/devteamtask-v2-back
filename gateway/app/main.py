from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

from app.configuration import settings
from app.lifespan import lifespan
from app.middleware import GatewayMiddleware

app = FastAPI(lifespan=lifespan)


app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(GatewayMiddleware, services=settings.MICROSERVICES_URLS)


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
