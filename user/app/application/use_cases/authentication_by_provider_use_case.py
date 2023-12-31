from app.application.dtos import AuthenticationTokensResponseDTO
from app.application.repositories import UserRepository
from app.application.utils.abstract_auth_jwt import AbstractAuthJwt, PayloadTypes
from app.domain.errors import BadRequestException, ResourceNotFoundException


class AuthenticationByProviderUseCase:
    def __init__(self, user_repository: UserRepository, auth_jwt: AbstractAuthJwt):
        self.user_repository = user_repository
        self.auth_jwt = auth_jwt

    def execute(self, email: str) -> AuthenticationTokensResponseDTO:
        user_storaged = self.user_repository.get_by_email(email)

        if user_storaged is None:
            raise ResourceNotFoundException("User")

        if user_storaged["email"] != email:
            raise BadRequestException("Bad request")

        payload_sub: PayloadTypes = {"sub": str(user_storaged["id"])}
        access_token, refresh_token = self.auth_jwt.create_tokens(payload_sub)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
        }
