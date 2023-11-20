from typing import Optional

from starlette.datastructures import UploadFile

from app.application.dtos import UserPartialUpdateRequestDTO
from app.application.repositories.user_repository import UserRepository
from app.application.utils.abstract_storage_utils import AbstractStorageUtils
from app.domain.errors import ResourceNotFoundException


class UserPartialUpdateUseCase:
    def __init__(
        self, user_repository: UserRepository, storage_utils: AbstractStorageUtils
    ):
        self.user_repository = user_repository
        self.storage_utils = storage_utils

    def execute(self, id: int, data: UserPartialUpdateRequestDTO):
        user_storaged = self.user_repository.get_by_id(id)

        if user_storaged is None:
            raise ResourceNotFoundException("User")

        data_to_update = {}

        for key, value in data.items():
            if key == "avatar_url" or value is None:
                continue

            data_to_update[key] = value

        if isinstance(data["avatar_url"], UploadFile):
            filename = self.storage_utils.save_file(
                data["avatar_url"],
                user_storaged["avatar_url"] if user_storaged["avatar_url"] else "",
            )
            data_to_update["avatar_url"] = filename

        user_storaged_updated = self.user_repository.partial_update(id, data_to_update)

        if isinstance(user_storaged_updated["avatar_url"], str):
            user_storaged_updated["avatar_url"] = self.storage_utils.get_url_media(
                user_storaged_updated["avatar_url"]
            )

        return user_storaged_updated
