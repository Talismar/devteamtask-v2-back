from functools import lru_cache

from pydantic import computed_field
from pydantic_core import Url
from pydantic_settings import BaseSettings


class AppBaseSettings(BaseSettings):
    SECRET_KEY: str = "asdasdasdasdasdacascasc"
    BASE_URL: Url
    ENV: str = "development"

    SERVICE_PROJECT_URL: Url
    SERVICE_USER_URL: Url
    PUBLIC_ENDPOINTS: list[dict[str, str | list[str]]] = [
        {"path": "/api/user/authentication/token", "methods": ["POST"]},
        {"path": "/api/user/authentication/refresh_token", "methods": ["POST"]},
        {"path": "/api/user/user/forgot_password", "methods": ["POST"]},
        {"path": "/api/user/user/", "methods": ["POST"]},
        {"path": "/api/user/user/reset_password_by_token", "methods": ["PUT"]},
        {"path": "/api/user/user/github", "methods": ["GET"]},
        {"path": "/api/user/authentication/github_auth", "methods": ["GET"]},
        {"path": "/", "methods": ["GET"]},
        {"path": "/static/styles.css", "methods": ["GET"]},
        {"path": "/favicon.ico", "methods": ["GET"]},
    ]

    @computed_field  # type: ignore
    @property
    def MICROSERVICES_URLS(self) -> dict:
        return {
            "project": {
                "url": str(self.SERVICE_PROJECT_URL)[:-1],
            },
            "user": {
                "url": str(self.SERVICE_USER_URL)[:-1],
            },
        }

    BACKEND_CORS_ORIGINS: list[Url] = [
        Url("http://localhost"),
        Url("http://localhost:8080"),
    ]


@lru_cache()
def get_settings():
    return AppBaseSettings(_env_file=(".env",))


settings = get_settings()
