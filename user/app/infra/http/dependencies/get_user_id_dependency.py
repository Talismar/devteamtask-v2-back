from fastapi import Request

from app.domain.entities.user import User


def get_user_id_dependency(request: Request):
    user_data: User = request.scope.get("user")  # type: ignore
    user_id = user_data["id"]
    return user_id
