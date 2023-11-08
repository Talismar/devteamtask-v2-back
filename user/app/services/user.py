from typing import TypedDict

from app.configs.local import settings
from app.repositories.user_repository import UserRepository
from app.utils.data_storage import get_url_media, save_file
from app.utils.hash_password import hash_password
from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError
from starlette.datastructures import UploadFile

from ..models import UserModel


class RequestGithubDTO(TypedDict):
    login: str
    id: int
    avatar_url: int
    email: None | str


class UserService:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def list_all(self):
        return self.user_repository.list_all()

    def create_by_github(self, auth_provider_name: str, data: RequestGithubDTO):
        try:
            return self.user_repository.create(data, auth_provider_name)
        except IntegrityError:
            raise Exception(detail="Account already exists")

    def create(self, data):
        if data.password != data.password_confirm:
            raise HTTPException(
                status_code=400,
                detail="Passwords do not match",
            )

        del data.password_confirm

        data.password = hash_password(data.password)

        try:
            return self.user_repository.create(data)
        except IntegrityError:
            raise HTTPException(
                status_code=409,
                detail="Account already exists",
            )

    def me(self, user_instance: UserModel):
        user_instance.avatar_url = get_url_media(user_instance.avatar_url)
        return user_instance

    def delete(self, id):
        try:
            self.user_repository.delete(id)
            return Response(status_code=204)
        except:
            raise HTTPException(status_code=400, detail="Error deleting account")

    def get_one(self, id):
        user_instance = self.user_repository.get_by_id(id)
        user_instance.avatar_url = get_url_media(user_instance.avatar_url)
        return user_instance

    def partial_update(self, id, data):
        user_instance = self.get_one(id)

        if user_instance is None:
            raise HTTPException(404)

        if isinstance(data.avatar_url, UploadFile):
            filename = save_file(data.avatar_url, user_instance.avatar_url)
            data.avatar_url = filename

        user_instance_updated = self.user_repository.partial_update(
            id, user_instance, {"avatar_url": data.avatar_url}
        )

        if isinstance(user_instance_updated.avatar_url, str):
            user_instance_updated.avatar_url = (
                settings.BASE_URL.unicode_string()
                + "api/user/static/images/users/"
                + user_instance_updated.avatar_url
            )

        return user_instance_updated
