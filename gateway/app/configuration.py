from functools import lru_cache

from pydantic import AnyHttpUrl
from pydantic_core import Url
from pydantic_settings import BaseSettings


class AppBaseSettings(BaseSettings):
    SECRET_KEY: str = "asdasdasdasdasdacascasc"
    BASE_URL: AnyHttpUrl

    BACKEND_CORS_ORIGINS: list[Url] = [
        Url("http://localhost"),
        Url("http://localhost:8080"),
    ]


@lru_cache()
def get_settings():
    return AppBaseSettings(_env_file=(".env",))


settings = get_settings()
