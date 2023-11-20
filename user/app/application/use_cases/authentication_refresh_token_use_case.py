from app.application.dtos import AuthenticationTokensResponseDTO
from app.application.utils.abstract_auth_jwt import AbstractAuthJwt


class AuthenticationRefreshTokenUseCase:
    def __init__(self, auth_jwt: AbstractAuthJwt):
        self.auth_jwt = auth_jwt

    def execute(self, refresh_token: str) -> AuthenticationTokensResponseDTO:
        access_token, refresh_token = self.auth_jwt.refresh_token(refresh_token)
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
        }
