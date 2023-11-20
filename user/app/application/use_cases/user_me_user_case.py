from app.application.utils.abstract_storage_utils import AbstractStorageUtils
from app.domain.entities.user import User


class UserMeUseCase:
    def __init__(self, storage_utils: AbstractStorageUtils):
        self.storage_utils = storage_utils

    def execute(self, data: User):
        if data["avatar_url"] is not None:
            data["avatar_url"] = self.storage_utils.get_url_media(data["avatar_url"])
        return data
