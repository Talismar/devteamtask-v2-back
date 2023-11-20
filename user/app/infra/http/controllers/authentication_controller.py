from json.decoder import JSONDecodeError

from fastapi import BackgroundTasks, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse

from app.application.use_cases import (
    AuthenticationByProviderUseCase,
    AuthenticationGenerateTokensUseCase,
    AuthenticationRefreshTokenUseCase,
)
from app.domain.errors import (
    AppBaseException,
    BadRequestException,
    UnauthorizedException,
)
from app.infra.background_tasks import authenticated_user_audit
from app.infra.configs.local import settings
from app.infra.factories.make_authentication_use_cases import (
    make_authentication_by_provider_use_case,
    make_authentication_token_use_case,
    make_refresh_token_use_case,
)
from app.infra.schemas.authentication import (
    AuthenticationRefreshTokenPostResponseSchema,
)
from app.infra.utils.client_github import ClientGithub


async def authentication_token(
    request: Request,
    background_tasks: BackgroundTasks,
    use_case: AuthenticationGenerateTokensUseCase = Depends(
        make_authentication_token_use_case
    ),  # noqa: E501
):
    data = {}
    has_error = False

    async with request.form() as form:
        data["email"] = form.get("username", None)
        data["password"] = form.get("password", None)

    email = data.get("email", None)
    password = data.get("password", None)

    if email is None and password is None:
        try:
            data_json: dict = await request.json()
        except JSONDecodeError:
            raise HTTPException(status_code=400)

        try:
            data["email"] = data_json["email"]
            data["password"] = data_json["password"]
        except KeyError:
            has_error = True

    if has_error:
        raise HTTPException(status_code=422, detail="Invalid request data")

    try:
        result = use_case.execute(data)  # type: ignore
        return result
    except UnauthorizedException as exception:
        has_error = True
        raise HTTPException(detail=exception.message, status_code=exception.status_code)
    finally:
        if not has_error and isinstance(email, str):
            background_tasks.add_task(authenticated_user_audit, email)


def refresh_token(
    data: AuthenticationRefreshTokenPostResponseSchema,
    use_case: AuthenticationRefreshTokenUseCase = Depends(make_refresh_token_use_case),
):
    return use_case.execute(data.refresh_token)


def github_auth(
    code: str | None = None,
    state: str | None = None,
    use_case: AuthenticationByProviderUseCase = Depends(
        make_authentication_by_provider_use_case
    ),
):
    response = RedirectResponse(str(settings.FRONT_END_URL) + "login")
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
            result = use_case.execute(
                user_info_response_json["email"], user_info_response_json["id"]
            )

            query_params = f"?access_token={result['access_token']}&refresh_token={result['refresh_token']}"
            return RedirectResponse(
                url=str(settings.FRONT_END_URL) + "/login" + query_params
            )
        except AppBaseException as exception:
            response.set_cookie("error", exception.message)
            return response
