from app.routers.auth import registr_router
from app.routers.chat import chat_router
from app.routers.project import project_router


list_of_routes = [
    registr_router,
    chat_router,
    project_router,
]

__all__ = [
    "list_of_routes",
]
