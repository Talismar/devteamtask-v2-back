from typing import TypedDict

from httpx import Client

from app.domain.errors import BadRequestException
from app.infra.configs.local import settings


class TokensResponseDTO(TypedDict):
    access_token: str
    expires_in: int
    refresh_token: str
    refresh_token_expires_in: int
    token_type: str
    scope: str


class ProfileInfoDTO(TypedDict):
    login: str
    id: int
    avatar_url: int
    name: None | str
    email: None | str


class ClientGithub:
    def __init__(self) -> None:
        self.client = Client(
            base_url="https://github.com", headers={"Accept": "application/json"}
        )

    def get_tokens(self, code: str, state=None) -> TokensResponseDTO:
        response = self.client.post(
            "/login/oauth/access_token",
            data={
                "client_id": settings.GITHUB_CLIENT_ID,
                "client_secret": settings.GITHUB_CLIENT_SECRET,
                "code": code,
                # "state": state,
            },
        )

        dict_response: dict = response.json()
        error = dict_response.get("error", None)

        if isinstance(error, str):
            raise BadRequestException("Bad request")

        return response.json()

    def get_profile_info(self, access_token: str) -> ProfileInfoDTO:
        response = self.client.get(
            "https://api.github.com/user",
            headers={"Authorization": f"Bearer {access_token}"},
        )
        return response.json()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.client.close()
