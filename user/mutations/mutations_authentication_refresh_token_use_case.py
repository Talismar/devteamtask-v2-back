import pytest_mutagen as mg

from app.application.use_cases.authentication_refresh_token_use_case import *

mg.link_to_file("authentication_refresh_token_use_case_integration_test.py")


# hash=8edebd26997c2c99
@mg.mutant_of(
    "AuthenticationRefreshTokenUseCase.execute",
    "AUTHENTICATIONREFRESHTOKENUSECASE.EXECUTE_0",
)
def execute(self, refresh_token: str) -> AuthenticationTokensResponseDTO:
    access_token, refresh_token = None
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }


# hash=1a7ee1d86767fe35
@mg.mutant_of(
    "AuthenticationRefreshTokenUseCase.execute",
    "AUTHENTICATIONREFRESHTOKENUSECASE.EXECUTE_1",
)
def execute(self, refresh_token: str) -> AuthenticationTokensResponseDTO:
    access_token, refresh_token = self.auth_jwt.refresh_token(refresh_token)
    pass
