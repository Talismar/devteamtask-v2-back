from app.http.middleware import HTTPRequestAuditMiddleware
from app.http.routes import app_routes
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .configs.local import engine, settings
from .models import BaseModel, InviteModel, NotificationModel, UserModel
from .utils.clear_terminal import clear_terminal

app = FastAPI(docs_url="/api/user/docs")
app.mount("/api/user/static", StaticFiles(directory="static"), name="static")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# BaseModel.metadata.drop_all(bind=engine)
# BaseModel.metadata.create_all(bind=engine)

app.add_middleware(HTTPRequestAuditMiddleware)

for route in app_routes:
    app.include_router(route)

clear_terminal()
