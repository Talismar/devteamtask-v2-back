from app.schemas.user import (
    UserLoginPostRequestSchema,
    UserPartialUpdateParams,
    UserPostRequestSchema,
)
from app.services.factories.make_user_service import make_user_service
from app.services.user import UserService
from app.utils.client_github import ClientGithub
from fastapi import Depends, Request
from fastapi.responses import RedirectResponse


def list_all(user_service: UserService = Depends(make_user_service)):
    return user_service.list_all()


def get_one(user_id: int, user_service: UserService = Depends(make_user_service)):
    return user_service.get_one(user_id)


def me(request: Request, user_service: UserService = Depends(make_user_service)):
    return user_service.me(request.scope["user"])


def create(
    data: UserPostRequestSchema, user_service: UserService = Depends(make_user_service)
):
    return user_service.create(data)


def github_create(
    code: str | None = None,
    state: str | None = None,
    user_service: UserService = Depends(make_user_service),
):
    with ClientGithub() as github_client:
        oauth_response_json = github_client.get_tokens(code)
        user_info_response_json = github_client.get_profile_info(
            oauth_response_json["access_token"]
        )
        if user_info_response_json["email"] is None:
            response.set_cookie(
                "error", "Email not visible make it visible to continue"
            )
            return response

        print(oauth_response_json)
        # response = RedirectResponse("http://127.0.0.1:3000/signup")
        # response.set_cookie(
        #     "success",
        #     "User created successfully",
        # )
        return RedirectResponse("http://127.0.0.1:3000/signup")
        # try:
        #     # user_service.create_by_github("GITHUB", user_info_response_json)
        #     # print(oauth_response_json)
        #     response.set_cookie(
        #         "success",
        #         "User created successfully",
        #     )
        #     return response
        # except Exception as e:
        #     response.set_cookie(
        #         "error",
        #         "User already exists. Please try again with another email address",
        #     )
        #     return response

        # print(e)
        # response.set_cookie("error", "Error creating")
        # return response


def delete(user_id: int, user_service: UserService = Depends(make_user_service)):
    return user_service.delete(user_id)


def partial_update(
    user_id: int,
    form: UserPartialUpdateParams = Depends(UserPartialUpdateParams),
    user_service: UserService = Depends(make_user_service),
):
    return user_service.partial_update(user_id, form)
