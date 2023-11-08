from secrets import token_urlsafe

from pydantic import AnyHttpUrl, EmailStr
from pydantic_core import Url
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppBaseSettings(BaseSettings):
    SECRET_KEY: str = "asdasdasdasdasdacascasc"
    BASE_URL: AnyHttpUrl

    BACKEND_CORS_ORIGINS: list[Url] = [
        Url("http://localhost"),
        Url("http://localhost:8080"),
    ]

    EMAIL_HOST: str
    EMAIL_PORT: int
    EMAIL_USERNAME: str
    EMAIL_PASSWORD: str
    EMAIL_FROM: EmailStr

    GITHUB_CLIENT_ID: str
    GITHUB_CLIENT_SECRET: str

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)
