from fastapi import APIRouter, FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.endpoints import HTTPEndpoint

from app.infra.configs.local import engine, settings
from app.infra.database import BaseModel, InviteModel, NotificationModel, UserModel
from app.infra.http.controllers.notification_controller import websocket_notifications
from app.infra.http.middleware import HTTPRequestAuditMiddleware
from app.infra.http.routes import app_routes
from app.infra.utils.clear_terminal import clear_terminal

app = FastAPI(docs_url="/api/user/docs")
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
