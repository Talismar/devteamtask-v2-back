from .authentication_route import router as authentication_router
from .invite_route import router as invite_router
from .notification_route import router as notification_router
from .user_route import router as user_router

app_routes = [user_router, authentication_router, invite_router, notification_router]
