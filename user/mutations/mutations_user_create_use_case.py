import pytest_mutagen as mg

from app.application.use_cases import user_create_use_case
from app.application.use_cases.user_create_use_case import UserCreateUseCase

# mg.link_to_file(mg.APPLY_TO_ALL)
mg.link_to_file("user_create_use_case_unit_test.py")


@mg.mutant_of("UserCreateUseCase.execute", "USERCREATEUSECASE.EXECUTE_0")
def execute(self, data):
    if not (data["password"] != data["password_confirm"]):
        raise user_create_use_case.BadRequestException("Passwords do not match")

    data.pop("password_confirm")

    data["password"] = user_create_use_case.hash_password(data["password"])

    return self.user_repository.create(data)


@mg.mutant_of("UserCreateUseCase.execute", "USERCREATEUSECASE.EXECUTE_1")
def execute_2(self, data):
    if data["password"] == data["password_confirm"]:
        raise user_create_use_case.BadRequestException("Passwords do not match")

    data.pop("password_confirm")

    data["password"] = user_create_use_case.hash_password(data["password"])

    return self.user_repository.create(data)
