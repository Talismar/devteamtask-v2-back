from typing import TypedDict

from app.configs.local import settings
from httpx import Client


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
