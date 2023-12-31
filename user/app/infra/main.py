from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy import create_engine

from app.infra.configs.local import Session, engine, settings
from app.infra.database import BaseModel, InviteModel, NotificationModel, UserModel
from app.infra.http.controllers.notification_controller import websocket_notifications
from app.infra.http.middleware import HTTPRequestAuditMiddleware
from app.infra.http.routes import app_routes
from app.infra.utils.clear_terminal import clear_terminal

app = FastAPI(
    docs_url="/api/user/docs",
    servers=[
        {"url": "http://localhost:8000", "description": "Local development server"}
    ],
)
app.mount("/api/user/media", StaticFiles(directory="media"), name="media")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# BaseModel.metadata.drop_all(bind=engine)
# BaseModel.metadata.create_all(bind=engine)

# app.add_middleware(HTTPRequestAuditMiddleware)

for route in app_routes:
    app.include_router(route)

clear_terminal()


app.add_api_websocket_route("/ws/{client_id}", websocket_notifications)


@app.post("/reset_database", include_in_schema=False)
def reset_database(secret: str):
    if settings.USER_TOKEN_FOR_RESET_DB == secret:
        engine = create_engine(
            "postgresql://postgres:password@localhost:5433/TestDevTeamTask"
        )
        Session.configure(bind=engine)

        BaseModel.metadata.drop_all(bind=engine)
        BaseModel.metadata.create_all(bind=engine)
