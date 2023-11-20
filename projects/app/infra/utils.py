from datetime import datetime, timedelta
from os import makedirs
from pathlib import Path as PathlibPath
from shutil import copyfileobj
from uuid import uuid1

from httpx import post as httpx_post
from starlette.datastructures import UploadFile

from app.application import AbstractEmailService, AbstractMediaStorages
from app.main.configuration.local import settings


class FileStorageUtils(AbstractMediaStorages):
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
            fullpath = self.base_url + "/".join(self.relative_path) + "/" + filename
        else:
            return None

        return fullpath


class SendEmailService(AbstractEmailService):
    def __init__(self, resource_name: str) -> None:
        self.api_endpoint = f"{settings.USER_SERVICE_URL}/invite/"
        self.resource_name = resource_name

    def get_expiration_date(self):
        return str(datetime.now() + timedelta(days=3))

    def send(self, emails, resource_id, redirect_path):
        expiration_date = self.get_expiration_date()

        response = httpx_post(
            self.api_endpoint,
            json={
                "resource_name": self.resource_name,
                "resource_id": resource_id,
                "expiration_date": expiration_date,
                "emails": emails,
                "redirect_url": f"{settings.BASE_URL}api/project/project/{redirect_path}",
            },
        )

        if response.status_code != 200:
            raise Exception("Email services error")
