from json import loads
from os import mkdir
from pathlib import Path

from app.infra.database.base_model import BaseModel
from app.infra.database.configuration import Session, engine
from app.infra.database.models import *
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy import create_engine

from .configuration.local import settings
from .lifespan import lifespan
from .make_routes import router

# BaseModel.metadata.drop_all(bind=engine)
# BaseModel.metadata.create_all(bind=engine)

app = FastAPI(
    docs_url="/api/project/docs",
    lifespan=lifespan,
    title="DTT: Project API",
    servers=[
        {"url": "http://localhost:8000", "description": "Local development server"}
    ],
)

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


@app.post("/integration/github/installation")
async def github_app_webhooks(
    request: Request,
    code: str | None = None,
    state: str | None = None,
    installation_id: int | None = None,
):
    print(request.scope)
    async with request.form() as form:
        data: str = str(form.get("payload", ""))
        data_dict = loads(data)
        print(data_dict)

    # Se todos os repositorios foram liberados, retorne a lista de repositorio para o usuario

    return {"status": "ok"}


@app.post("/reset_database", include_in_schema=False)
def reset_database(secret: str):
    if settings.USER_TOKEN_FOR_RESET_DB == secret:
        engine = create_engine(
            "postgresql://postgres:password@localhost:5433/TestDevTeamTask"
        )

        Session.configure(bind=engine)

        BaseModel.metadata.drop_all(bind=engine)
        BaseModel.metadata.create_all(bind=engine)
