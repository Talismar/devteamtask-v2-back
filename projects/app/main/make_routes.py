from fastapi import APIRouter

from app.infra.http.routes import api_routes

router = APIRouter(prefix="/api/project")

for route in api_routes:
    router.include_router(route)
