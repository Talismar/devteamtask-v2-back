from os import mkdir, system
from pathlib import Path
from threading import Thread

from app.infra.database.base_model import BaseModel
from app.infra.database.configuration import Session, engine
from app.infra.database.models import *
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from httpx import post as httpx_post
from sqlalchemy import text

from .configuration.local import settings
from .load_initial_data import create_initial_project, create_status_initial
from .make_routes import router

# BaseModel.metadata.drop_all(bind=engine)
# BaseModel.metadata.create_all(bind=engine)

app = FastAPI(docs_url="/api/project/docs")
# try:
app.mount("/api/project/media", StaticFiles(directory="media"), name="media")
# except RuntimeError as e:
#     print(Path(__file__))
#     print(e)

app.include_router(router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# print(Path().absolute().__truediv__("media"))

# create_status_initial()
# create_initial_project()


@app.post("/api/user/authentication/token", include_in_schema=False)
async def get_token(request: Request):
    email: None | str = None
    password: None | str = None

    async with request.form() as form:
        email = form.get("username", None)
        password = form.get("password", None)

    content_json = {"email": email, "password": password}
    user_service_url = f"{settings.USER_SERVICE_URL}/authentication/token"
    response = httpx_post(user_service_url, json=content_json)

    return response.json()


# statement = text("SELECT name FROM user;")
# with engine.connect() as conn:
#     results = conn.execute("SELECT * FROM user")
#     [print(row) for row in results]
# session = Session()
# results = session.execute(text("SELECT * FROM project"))
# for row in results:
#     print(row)
def clear_terminal():
    system("clear")
    # Consulta SQL "raw"
    # sql_query = text("SELECT * FROM sua_tabela WHERE coluna = :valor")

    # # Parâmetros para a consulta
    # params = {"valor": "algum_valor"}

    # # Executa a consulta SQL
    # result = engine.execute(sql_query, params)

    # # Itera sobre o resultado
    # for row in result:
    #     print(row)


Thread(None, target=clear_terminal).start()
