from contextlib import asynccontextmanager
from os import system
from threading import Thread
from typing import AsyncIterator, TypedDict

from fastapi import FastAPI
from httpx import AsyncClient

from app.main.configuration.local import settings


class State(TypedDict):
    http_client: AsyncClient


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[State]:
    if settings.ENV == "development":

        def clear_terminal():
            system("clear")

        Thread(None, target=clear_terminal).start()

    headers = {"X-Client-ID": "DevTeamTask-Project-Service"}

    async with AsyncClient(headers=headers) as client:
        yield {"http_client": client}
