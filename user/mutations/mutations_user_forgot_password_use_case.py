import pytest_mutagen as mg

from app.application.use_cases.user_forgot_password_use_case import *

mg.link_to_file("user_forgot_password_use_case_integration_test.py")


# hash=9edc5ce2752506bb
@mg.mutant_of(
    "UserForgotPasswordUseCase.execute", "USERFORGOTPASSWORDUSECASE.EXECUTE_0"
)
def execute(self, email: str):
    user_storaged = None

    if user_storaged is None:
        raise ResourceNotFoundException("User")

    current_date = datetime.now()
    one_day = timedelta(days=1)
    expiration_date = current_date + one_day

    invite = self.invite_repository.create(
        {
            "resource_name": "User",
            "resource_id": str(user_storaged["id"]),
            "expiration_date": expiration_date,
            "email": email,
        }
    )

    return invite


# hash=a7954e3a7d62949b
@mg.mutant_of(
    "UserForgotPasswordUseCase.execute", "USERFORGOTPASSWORDUSECASE.EXECUTE_1"
)
def execute(self, email: str):
    user_storaged = self.user_repository.get_by_email(email)

    if not (user_storaged is None):
        raise ResourceNotFoundException("User")

    current_date = datetime.now()
    one_day = timedelta(days=1)
    expiration_date = current_date + one_day

    invite = self.invite_repository.create(
        {
            "resource_name": "User",
            "resource_id": str(user_storaged["id"]),
            "expiration_date": expiration_date,
            "email": email,
        }
    )

    return invite


# hash=e5716bba3b7a40be
@mg.mutant_of(
    "UserForgotPasswordUseCase.execute", "USERFORGOTPASSWORDUSECASE.EXECUTE_2"
)
def execute(self, email: str):
    user_storaged = self.user_repository.get_by_email(email)

    if user_storaged is None:
        raise ResourceNotFoundException("User")

    current_date = None
    one_day = timedelta(days=1)
    expiration_date = current_date + one_day

    invite = self.invite_repository.create(
        {
            "resource_name": "User",
            "resource_id": str(user_storaged["id"]),
            "expiration_date": expiration_date,
            "email": email,
        }
    )

    return invite


# hash=65f0d3039935e514
@mg.mutant_of(
    "UserForgotPasswordUseCase.execute", "USERFORGOTPASSWORDUSECASE.EXECUTE_3"
)
def execute(self, email: str):
    user_storaged = self.user_repository.get_by_email(email)

    if user_storaged is None:
        raise ResourceNotFoundException("User")

    current_date = datetime.now()
    one_day = None
    expiration_date = current_date + one_day

    invite = self.invite_repository.create(
        {
            "resource_name": "User",
            "resource_id": str(user_storaged["id"]),
            "expiration_date": expiration_date,
            "email": email,
        }
    )

    return invite


# hash=e7a3c8bba710298f
@mg.mutant_of(
    "UserForgotPasswordUseCase.execute", "USERFORGOTPASSWORDUSECASE.EXECUTE_4"
)
def execute(self, email: str):
    user_storaged = self.user_repository.get_by_email(email)

    if user_storaged is None:
        raise ResourceNotFoundException("User")

    current_date = datetime.now()
    one_day = timedelta(days=None)
    expiration_date = current_date + one_day

    invite = self.invite_repository.create(
        {
            "resource_name": "User",
            "resource_id": str(user_storaged["id"]),
            "expiration_date": expiration_date,
            "email": email,
        }
    )

    return invite


# hash=ec9212a7cea53ec1
@mg.mutant_of(
    "UserForgotPasswordUseCase.execute", "USERFORGOTPASSWORDUSECASE.EXECUTE_5"
)
def execute(self, email: str):
    user_storaged = self.user_repository.get_by_email(email)

    if user_storaged is None:
        raise ResourceNotFoundException("User")

    current_date = datetime.now()
    one_day = timedelta(days=2)
    expiration_date = current_date + one_day

    invite = self.invite_repository.create(
        {
            "resource_name": "User",
            "resource_id": str(user_storaged["id"]),
            "expiration_date": expiration_date,
            "email": email,
        }
    )

    return invite


# hash=2234f6bb2d37dca8
@mg.mutant_of(
    "UserForgotPasswordUseCase.execute", "USERFORGOTPASSWORDUSECASE.EXECUTE_6"
)
def execute(self, email: str):
    user_storaged = self.user_repository.get_by_email(email)

    if user_storaged is None:
        raise ResourceNotFoundException("User")

    current_date = datetime.now()
    one_day = timedelta(days=1)
    expiration_date = None

    invite = self.invite_repository.create(
        {
            "resource_name": "User",
            "resource_id": str(user_storaged["id"]),
            "expiration_date": expiration_date,
            "email": email,
        }
    )

    return invite


# hash=2ae258e8dbca66e0
@mg.mutant_of(
    "UserForgotPasswordUseCase.execute", "USERFORGOTPASSWORDUSECASE.EXECUTE_7"
)
def execute(self, email: str):
    user_storaged = self.user_repository.get_by_email(email)

    if user_storaged is None:
        raise ResourceNotFoundException("User")

    current_date = datetime.now()
    one_day = timedelta(days=1)
    expiration_date = current_date - one_day

    invite = self.invite_repository.create(
        {
            "resource_name": "User",
            "resource_id": str(user_storaged["id"]),
            "expiration_date": expiration_date,
            "email": email,
        }
    )

    return invite


# hash=26c961b37781493a
@mg.mutant_of(
    "UserForgotPasswordUseCase.execute", "USERFORGOTPASSWORDUSECASE.EXECUTE_8"
)
def execute(self, email: str):
    user_storaged = self.user_repository.get_by_email(email)

    if user_storaged is None:
        raise ResourceNotFoundException("User")

    current_date = datetime.now()
    one_day = timedelta(days=1)
    expiration_date = current_date + one_day

    invite = None

    return invite
