import pytest_mutagen as mg

from app.application.use_cases.authentication_generate_tokens_use_case import *

mg.link_to_file("authentication_generate_tokens_use_case_integration_test.py")


# hash=393a578643ce9c7f
@mg.mutant_of(
    "AuthenticationGenerateTokensUseCase.authenticate_user",
    "AUTHENTICATIONGENERATETOKENSUSECASE.AUTHENTICATE_USER_1",
)
def authenticate_user(self, email: str, password: str):
    user = self.user_repository.get_by_email(email)

    if not (user is None):
        return False

    elif not verify_password(password, user["password"]):
        return False

    return user


# hash=c731c9692cdfd84e
@mg.mutant_of(
    "AuthenticationGenerateTokensUseCase.authenticate_user",
    "AUTHENTICATIONGENERATETOKENSUSECASE.AUTHENTICATE_USER_3",
)
def authenticate_user(self, email: str, password: str):
    user = self.user_repository.get_by_email(email)

    if user is None:
        return False

    elif verify_password(password, user["password"]):
        return False

    return user


# hash=33c8c8f71c861f49
@mg.mutant_of(
    "AuthenticationGenerateTokensUseCase.authenticate_user",
    "AUTHENTICATIONGENERATETOKENSUSECASE.AUTHENTICATE_USER_4",
)
def authenticate_user(self, email: str, password: str):
    user = self.user_repository.get_by_email(email)

    if user is None:
        return False

    elif not verify_password(password, user["password"]):
        return False

    pass
