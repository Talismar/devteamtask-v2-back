from app.application.dtos import (
    AuthenticationGenerateTokensResquestDTO,
    AuthenticationTokensResponseDTO,
)
from app.application.repositories.user_repository import UserRepository
from app.application.utils.abstract_auth_jwt import AbstractAuthJwt, PayloadTypes
from app.application.utils.cryptography import verify_password
from app.domain.errors import UnauthorizedException


class AuthenticationGenerateTokensUseCase:
    def __init__(self, user_repository: UserRepository, auth_jwt: AbstractAuthJwt):
        self.user_repository = user_repository
        self.auth_jwt = auth_jwt

    def authenticate_user(self, email: str, password: str):
        user = self.user_repository.get_by_email(email)

        if user is None:
            return False

        elif not verify_password(password, user["password"]):
            return False

        return user

    def execute(
        self, data: AuthenticationGenerateTokensResquestDTO
    ) -> AuthenticationTokensResponseDTO:
        email = data["email"]
        password = data["password"]

        user = self.authenticate_user(email, password)

        if not user:
            raise UnauthorizedException()

        payload_sub: PayloadTypes = {"sub": str(user["id"])}
        access_token, refresh_token = self.auth_jwt.create_tokens(payload_sub)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
        }
