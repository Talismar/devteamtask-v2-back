from app.schemas.user import (
    UserLoginPostRequestSchema,
    UserPartialUpdateParams,
    UserPostRequestSchema,
)
from app.services.factories.make_user_service import make_user_service
from app.services.user import UserService
from fastapi import Depends, Request


def list_all(user_service: UserService = Depends(make_user_service)):
    return user_service.list_all()


def get_one(user_id: int, user_service: UserService = Depends(make_user_service)):
    return user_service.get_one(user_id)


def me(request: Request, user_service: UserService = Depends(make_user_service)):
    return user_service.me(request.scope["user"])


def create(
    data: UserPostRequestSchema, user_service: UserService = Depends(make_user_service)
):
    return user_service.create(data)


def delete(user_id: int, user_service: UserService = Depends(make_user_service)):
    return user_service.delete(user_id)


def partial_update(
    user_id: int,
    form: UserPartialUpdateParams = Depends(UserPartialUpdateParams),
    user_service: UserService = Depends(make_user_service),
):
    return user_service.partial_update(user_id, form)
