from abc import ABC, abstractmethod
from typing import TypedDict


class PayloadTypes(TypedDict):
    sub: str


class AbstractAuthJwt(ABC):
    @abstractmethod
    def create_tokens(self, payload: PayloadTypes) -> tuple:
        pass

    @abstractmethod
    def refresh_token(self, refresh_token: str) -> tuple:
        pass
