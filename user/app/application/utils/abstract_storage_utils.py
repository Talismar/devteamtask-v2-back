from abc import ABC, abstractmethod
from typing import BinaryIO

from starlette.datastructures import UploadFile


class AbstractFile(ABC):
    @property
    @abstractmethod
    def file(self) -> BinaryIO:
        pass

    @property
    @abstractmethod
    def filename(self) -> str:
        pass


class AbstractStorageUtils(ABC):
    @abstractmethod
    def get_url_media(self, filename: str) -> str:
        pass

    @abstractmethod
    def save_file(self, file: UploadFile, original_filename: str | None = None):
        pass
