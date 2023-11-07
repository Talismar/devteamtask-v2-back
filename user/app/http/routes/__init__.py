from .authentication import router as authentication_router
from .invite_route import router as invite_route
from .notification_route import router as notification_router
from .user import router as user_router

app_routes = [user_router, authentication_router, invite_route, notification_router]
