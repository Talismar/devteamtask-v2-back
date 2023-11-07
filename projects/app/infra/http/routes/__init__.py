from .project_route import router as project_router
from .sprint_route import router as sprint_router
from .status_route import router as status_router
from .tag_route import router as tag_router
from .task_route import router as task_router

api_routes = [project_router, status_router, task_router, tag_router, sprint_router]
