from functools import lru_cache
from pydantic import computed_field, TypeAdapter
from pydantic_core import Url
from pydantic_settings import BaseSettings

class AppBaseSettings(BaseSettings):
    SECRET_KEY: str = "asdasdasdasdasdacascasc"
    BASE_URL: Url
    ENV: str = "development"
    
    SERVICE_PROJECT_URL: Url
    SERVICE_USER_URL: Url

    @computed_field
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
