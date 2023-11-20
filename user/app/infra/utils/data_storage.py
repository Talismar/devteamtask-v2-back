from os import makedirs
from pathlib import Path as PathlibPath
from shutil import copyfileobj
from uuid import uuid1

from starlette.datastructures import UploadFile

from ..configs.local import settings


def save_file(new_file: UploadFile, original_filename: str | None = None):
    upload_dir = PathlibPath().absolute() / "static" / "images" / "users"

    if not upload_dir.exists():
        makedirs(upload_dir)

    file_search = (
        PathlibPath().absolute() / original_filename
        if original_filename is not None
        else ""
    )
    # print(new_file.filename, original_filename)
    if isinstance(file_search, PathlibPath):
        print("File search", file_search.exists())
        if file_search.exists() and not file_search.is_dir():
            file_search.unlink()
            # raise Exception("File already exists")

    dest = PathlibPath(upload_dir) / new_file.filename

    with open(dest, "wb") as buffer:
        copyfileobj(new_file.file, buffer)

    return new_file.filename


def get_url_media(filename: str):
    fullpath = ""

    if isinstance(filename, str):
        fullpath = (
            settings.BASE_URL.unicode_string()
            + "api/user/static/images/users/"
            + filename
        )
    else:
        return None

    return fullpath
