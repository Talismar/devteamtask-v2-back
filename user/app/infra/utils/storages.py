from os import makedirs
from pathlib import Path as PathlibPath
from shutil import copyfileobj
from uuid import uuid1

from starlette.datastructures import UploadFile

from app.application.utils.abstract_storage_utils import AbstractStorageUtils


class StorageUtils(AbstractStorageUtils):
    def __init__(self, relative_path: list[str], base_url: str) -> None:
        self.relative_path = relative_path
        self.base_url = base_url

    def generate_filename(self, raw_filename: str):
        return f"{uuid1()}-{raw_filename}"

    def get_upload_dir(self):
        upload_dir = PathlibPath().absolute()

        for path in self.relative_path:
            upload_dir = upload_dir.__truediv__(path)

        return upload_dir

    def save_file(self, new_file: UploadFile, original_filename: str | None = None):
        upload_dir = self.get_upload_dir()

        if not upload_dir.exists():
            makedirs(upload_dir)

        file_search = (
            upload_dir / original_filename if original_filename is not None else ""
        )

        if isinstance(file_search, PathlibPath):
            if file_search.exists() and not file_search.is_dir():
                file_search.unlink()

        new_filename = self.generate_filename(str(new_file.filename))
        dest = upload_dir / new_filename

        with open(dest, "wb") as buffer:
            copyfileobj(new_file.file, buffer)

        return new_filename

    def get_url_media(self, filename: str):
        fullpath = ""

        if isinstance(filename, str):
            fullpath = (
                str(self.base_url)
                + "api/user/media/"
                + "/".join(self.relative_path[1:])
                + "/"
                + filename
            )
        else:
            return None

        return fullpath


# class StorageUtils(AbstractStorageUtils):
#     def __init__(self, relative_path: list[str], base_url: str) -> None:
#         self.relative_path = relative_path
#         self.base_url = base_url

#     def get_upload_dir(self):
#         upload_dir = PathlibPath().absolute()

#         for path in self.relative_path:
#             upload_dir = upload_dir.__truediv__(path)

#         return upload_dir

#     def save_file(self, new_file: UploadFile, original_filename: str | None = None):
#         upload_dir = self.get_upload_dir()

#         if not upload_dir.exists():
#             makedirs(upload_dir)

#         file_search = (
#             PathlibPath().absolute() / original_filename
#             if original_filename is not None
#             else ""
#         )
#         # print(new_file.filename, original_filename)
#         if isinstance(file_search, PathlibPath):
#             print("File search", file_search.exists())
#             if file_search.exists() and not file_search.is_dir():
#                 file_search.unlink()
#                 # raise Exception("File already exists")

#         dest = PathlibPath(upload_dir) / new_file.filename

#         with open(dest, "wb") as buffer:
#             copyfileobj(new_file.file, buffer)

#         return new_file.filename

#     def get_url_media(self, filename: str):
#         fullpath = ""

#         if isinstance(filename, str):
#             fullpath = (
#                 str(self.base_url)
#                 + "api/user/"
#                 + "/".join(self.relative_path)
#                 + "/"
#                 + filename
#             )
#         else:
#             return None

#         return fullpath
