from os import mkdir
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from httpx import post as httpx_post
from starlette.datastructures import UploadFile

from app.infra.database.base_model import BaseModel
from app.infra.database.configuration import Session, engine
from app.infra.database.models import *

from .configuration.local import settings
from .lifespan import lifespan
from .load_initial_data import create_initial_project, create_status_initial
from .make_routes import router

# BaseModel.metadata.drop_all(bind=engine)
# BaseModel.metadata.create_all(bind=engine)

app = FastAPI(docs_url="/api/project/docs", lifespan=lifespan)

try:
    app.mount("/api/project/media", StaticFiles(directory="media"), name="media")
except RuntimeError as e:
    if "'media' does not exist" in e.args[0]:
        path_to_create = Path().absolute().__truediv__("media")
        mkdir(path_to_create)


app.include_router(router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# create_status_initial()
# create_initial_project()


@app.post("/api/user/authentication/token", include_in_schema=False)
async def get_token(request: Request):
    email: None | str | UploadFile = None
    password: None | str | UploadFile = None

    async with request.form() as form:
        email = form.get("username", None)
        password = form.get("password", None)

    content_json = {"email": email, "password": password}
    user_service_url = f"{settings.USER_SERVICE_URL}/authentication/token"
    response = httpx_post(user_service_url, json=content_json)

    return response.json()
