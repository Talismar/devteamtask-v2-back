from typing import Annotated

from fastapi import BackgroundTasks, Depends, HTTPException, Request
from fastapi.responses import JSONResponse, RedirectResponse

from app.application.use_cases import (
    AuthenticationByProviderUseCase,
    UserChangePasswordUseCase,
    UserCreateByProviderUseCase,
    UserCreateUseCase,
    UserDeleteUseCase,
    UserForgotPasswordUseCase,
    UserMeUseCase,
    UserPartialUpdateUseCase,
    UserResetPasswordByTokenUseCase,
)
from app.domain.enums import AuthProvidersEnum
from app.domain.errors import AppBaseException
from app.infra.configs.local import settings
from app.infra.factories.make_authentication_use_cases import (
    make_authentication_by_provider_use_case,
)
from app.infra.factories.make_user_use_cases import (
    make_user_change_password_use_case,
    make_user_create_by_provider_use_case,
    make_user_create_use_case,
    make_user_delete_use_case,
    make_user_forgot_password_use_case,
    make_user_me_use_case,
    make_user_partial_update_use_case,
    make_user_reset_password_by_token_use_case,
)
from app.infra.http.dependencies import get_user_id_dependency
from app.infra.schemas.base import EmailSchema
from app.infra.schemas.user_schemas import (
    UserChangePasswordRequestSchema,
    UserPartialUpdateParams,
    UserPostRequestSchema,
    UserResetPasswortByTokenRequestSchema,
)
from app.infra.utils.client_github import ClientGithub
from app.infra.utils.send_email import send_email_config


def create(
    data: UserPostRequestSchema,
    use_case: UserCreateUseCase = Depends(make_user_create_use_case),
):
    try:
        dict_data = data.model_dump()
        result = use_case.execute(dict_data)  # type: ignore
        return result
    except AppBaseException as exception:
        raise HTTPException(detail=exception.message, status_code=exception.status_code)


def me(request: Request, use_case: UserMeUseCase = Depends(make_user_me_use_case)):
    dict_data = request.scope["user"]
    return use_case.execute(dict_data)


def github_create(
    code: str | None = None,
    state: str | None = None,
    use_case: UserCreateByProviderUseCase = Depends(
        make_user_create_by_provider_use_case
    ),
    auth_use_case: AuthenticationByProviderUseCase = Depends(
        make_authentication_by_provider_use_case
    ),
):
    response = RedirectResponse(str(settings.FRONT_END_URL) + "/signup")
    with ClientGithub() as github_client:
        try:
            oauth_response_json = github_client.get_tokens(code)
        except AppBaseException as exception:
            response.set_cookie("error", exception.message)
            return response

        user_info_response_json = github_client.get_profile_info(
            oauth_response_json["access_token"]
        )

        if user_info_response_json["email"] is None:
            response.set_cookie(
                "error", "Email not visible make it visible to continue"
            )
            return response

        try:
            use_case.execute(
                {
                    "auth_provider": AuthProvidersEnum.GITHUB,
                    "email": user_info_response_json["email"],
                    "login": user_info_response_json["login"],
                    "name": user_info_response_json["name"],
                }
            )

            result = auth_use_case.execute(user_info_response_json["email"])

            query_params = f"?access_token={result['access_token']}&refresh_token={result['refresh_token']}"
            response = RedirectResponse(
                url=str(settings.FRONT_END_URL) + "/signup" + query_params
            )
            response.set_cookie(
                "success",
                "User created successfully",
            )
            return response
        except AppBaseException as exception:
            response.set_cookie(
                "error",
                exception.message,
            )
            return response


def partial_update(
    user_id: int,
    form: UserPartialUpdateParams = Depends(UserPartialUpdateParams),
    use_case: UserPartialUpdateUseCase = Depends(make_user_partial_update_use_case),
):
    dict_data = {
        "avatar_url": form.avatar_url,
        "name": form.name,
        "notification_state": form.notification_state,
    }

    if form.is_active is not None:
        dict_data["is_active"] = form.is_active

    try:
        return use_case.execute(user_id, dict_data)  # type: ignore
    except AppBaseException as exception:
        raise HTTPException(status_code=exception.status_code, detail=exception.message)


def forgot_password(
    data: EmailSchema,
    background_tasks: BackgroundTasks,
    use_case: UserForgotPasswordUseCase = Depends(make_user_forgot_password_use_case),
):
    try:
        invite = use_case.execute(data.email)

        front_end_redirect_url = f"{settings.FRONT_END_URL}reset-password"
        redirect_url = f"{settings.BASE_URL}api/user/invite/{invite['token']}?redirect_url={front_end_redirect_url}"

        fast_mail, message = send_email_config(
            emails=[invite["email"]],
            subject="DevTeamTask | Reset password",
            redirect_url=redirect_url,
        )

        background_tasks.add_task(
            fast_mail.send_message, message, template_name="reset_password.html"
        )

        return JSONResponse(status_code=200, content={"detail": "Email has been sent"})
    except AppBaseException as exception:
        raise HTTPException(status_code=exception.status_code, detail=exception.message)


def change_password(
    user_id: Annotated[int, Depends(get_user_id_dependency)],
    data: UserChangePasswordRequestSchema,
    use_case: UserChangePasswordUseCase = Depends(make_user_change_password_use_case),
):
    try:
        return use_case.execute(
            {"old_password": data.old_password, "new_password": data.new_password},
            user_id,
        )
    except AppBaseException as exception:
        raise HTTPException(status_code=exception.status_code, detail=exception.message)


def reset_password_by_token(
    data: UserResetPasswortByTokenRequestSchema,
    use_case: UserResetPasswordByTokenUseCase = Depends(
        make_user_reset_password_by_token_use_case
    ),
):
    try:
        dict_data = data.model_dump()
        return use_case.execute(dict_data)  # type: ignore
    except AppBaseException as exception:
        raise HTTPException(status_code=exception.status_code, detail=exception.message)


def delete(
    user_id: int, use_case: UserDeleteUseCase = Depends(make_user_delete_use_case)
):
    try:
        return use_case.execute(user_id)
    except AppBaseException as exception:
        return HTTPException(
            status_code=exception.status_code, detail=exception.message
        )
