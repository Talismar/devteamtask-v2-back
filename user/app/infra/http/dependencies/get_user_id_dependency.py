from fastapi import Request

from app.domain.entities.user import User


def get_user_id_dependency(request: Request):
    user_id = request.headers.get("user_id")

    if isinstance(user_id, str):
        user_id = int(user_id)

    return user_id
