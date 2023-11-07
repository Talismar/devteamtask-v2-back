from os import makedirs
from pathlib import Path as PathlibPath
from shutil import copyfileobj
from uuid import UUID, uuid1

from app.main.configuration.local import settings
from httpx import post as httpx_post
from starlette.datastructures import UploadFile

html_invite_project = """
        <p>Hi this test mail, thanks for using Fastapi-mail
            <a href="http://localhost:8000/api/user/invite/f5ece628-79d6-11ee-b00e-f09e4ac22c2f" >Test</a>
        </p> """


class FileStorageUtils:
    def __init__(self, relative_path: list[str], base_url: str) -> None:
        self.relative_path = relative_path
        self.base_url = base_url

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

    def get_url_media(self, filename: str):
        fullpath = ""

        if isinstance(filename, str):
            fullpath = self.base_url + "/".join(self.relative_path) + "/" + filename
        else:
            return None

        return fullpath


class SendEmailService:
    def __init__(self, resource_name: str) -> None:
        self.api_endpoint = f"{settings.USER_SERVICE_URL}/invite/"
        self.resource_name = resource_name

    def send(
        self,
        emails: list[str],
        resource_id: int,
        expiration_date: str = "2023-11-04T02:17:18.877Z",
    ):
        response = httpx_post(
            self.api_endpoint,
            json={
                "resource_name": self.resource_name,
                "resource_id": str(resource_id),
                "expiration_date": expiration_date,
                "emails": emails,
                "redirect_url": f"{settings.BASE_URL}api/project/add_collaborator",
            },
        )
        print(response)
