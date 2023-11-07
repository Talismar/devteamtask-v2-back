from fastapi import Request


def get_user_id_dependency(request: Request):
    user_data: dict = request.scope.get("user")
    user_id = user_data.get("id")
    return user_id
