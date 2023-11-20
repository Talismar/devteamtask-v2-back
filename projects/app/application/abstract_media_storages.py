from abc import ABC, abstractmethod

from starlette.datastructures import UploadFile


class AbstractMediaStorages(ABC):
    @abstractmethod
    def save_file(self, new_file: UploadFile, original_filename: str | None = None):
        pass

    @abstractmethod
    def get_url_media(self, filename: str):
        pass
