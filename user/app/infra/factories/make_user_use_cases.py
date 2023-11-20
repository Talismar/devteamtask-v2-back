from fastapi import Depends

from app.application.use_cases import (
    UserChangePasswordUseCase,
    UserCreateByProviderUseCase,
    UserCreateUseCase,
    UserForgotPasswordUseCase,
    UserMeUseCase,
    UserPartialUpdateUseCase,
    UserResetPasswordByTokenUseCase,
)
from app.infra.configs.local import settings
from app.infra.dependencies import database_connection
from app.infra.repositories import InviteSqlalchemyRepository, UserSqlalchemyRepository
from app.infra.utils.storages import StorageUtils

storage_utils = StorageUtils(["media", "images", "users"], settings.BASE_URL)


def make_user_create_use_case(session=Depends(database_connection)):
    repository = UserSqlalchemyRepository(session)
    use_case = UserCreateUseCase(repository)
    return use_case


def make_user_change_password_use_case(session=Depends(database_connection)):
    repository = UserSqlalchemyRepository(session)
    use_case = UserChangePasswordUseCase(repository)
    return use_case


def make_user_reset_password_by_token_use_case(session=Depends(database_connection)):
    user_repository = UserSqlalchemyRepository(session)
    invite_respository = InviteSqlalchemyRepository(session)
    use_case = UserResetPasswordByTokenUseCase(user_repository, invite_respository)
    return use_case


def make_user_forgot_password_use_case(session=Depends(database_connection)):
    user_repository = UserSqlalchemyRepository(session)
    invite_respository = InviteSqlalchemyRepository(session)
    use_case = UserForgotPasswordUseCase(user_repository, invite_respository)
    return use_case


def make_user_create_by_provider_use_case(session=Depends(database_connection)):
    repository = UserSqlalchemyRepository(session)
    use_case = UserCreateByProviderUseCase(repository)
    return use_case


def make_user_partial_update_use_case(session=Depends(database_connection)):
    repository = UserSqlalchemyRepository(session)
    use_case = UserPartialUpdateUseCase(repository, storage_utils)
    return use_case


def make_user_me_use_case():
    use_case = UserMeUseCase(storage_utils)
    return use_case
