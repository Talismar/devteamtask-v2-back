from contextlib import asynccontextmanager
from typing import AsyncIterator, TypedDict

from fastapi import FastAPI
from httpx import AsyncClient

from app.configuration import settings
from app.utils import clear_terminal_on_save


class State(TypedDict):
    http_client: AsyncClient


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[State]:
    if settings.ENV == "development":
        clear_terminal_on_save()

    async with AsyncClient(timeout=None) as client:
        yield {"http_client": client}
