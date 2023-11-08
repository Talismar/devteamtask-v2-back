from json.decoder import JSONDecodeError

from app.background_tasks import authenticated_user_audit
from app.schemas.authentication import AuthenticationRefreshTokenPostResponseSchema
from app.services.authentication import AuthenticationService
from app.services.factories.make_authentication_service import (
    make_authentication_service,
)
from app.utils.client_github import ClientGithub
from fastapi import BackgroundTasks, Depends, HTTPException, Request
from starlette.datastructures import UploadFile


async def authentication_token(
    request: Request,
    background_tasks: BackgroundTasks,
    authentication_service: AuthenticationService = Depends(
        make_authentication_service
    ),
):
    email: None | str | UploadFile = None
    password: None | str | UploadFile = None

    async with request.form() as form:
        email = form.get("username", None)
        password = form.get("password", None)

    if email is None and password is None:
        try:
            data_json: dict = await request.json()
        except JSONDecodeError as json_decode_error:
            raise HTTPException(status_code=400)

        email = data_json["email"]
        password = data_json["password"]

    hasError = False
    try:
        return authentication_service.token(email, password)
    except HTTPException as error:
        hasError = True
        raise error
    finally:
        if not hasError:
            background_tasks.add_task(authenticated_user_audit, email)


def refresh_token(
    data: AuthenticationRefreshTokenPostResponseSchema,
    authentication_service: AuthenticationService = Depends(
        make_authentication_service
    ),
):
    return authentication_service.refresh_token(data.refresh_token)


def github_auth(code: str | None = None, state: str | None = None):
    print(code, state)
    with ClientGithub() as github_client:
        oauth_response_json = github_client.get_tokens(code)
        user_info_response_json = github_client.get_profile_info(
            oauth_response_json["access_token"]
        )

    return "asdasd"
