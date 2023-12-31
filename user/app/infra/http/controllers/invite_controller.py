from uuid import UUID

from fastapi import BackgroundTasks, Depends
from fastapi.responses import JSONResponse, RedirectResponse
from pydantic import AnyHttpUrl

from app.application.use_cases import InviteCreateUseCase, InviteValidateByTokenUseCase
from app.domain.errors import AppBaseException
from app.infra.configs.local import settings
from app.infra.factories.make_invite_use_cases import (
    make_invite_create_use_case,
    make_invite_validate_by_token_use_case,
)
from app.infra.schemas.invite_schemas import InvitePostRequestSchema
from app.infra.utils.send_email import send_email_config


def create_and_send_email(
    data: InvitePostRequestSchema,
    background_tasks: BackgroundTasks,
    use_case: InviteCreateUseCase = Depends(make_invite_create_use_case),
):
    emails = data.emails
    project_service_redirect_url = data.redirect_url
    del data.emails
    del data.redirect_url

    dict_data: dict = data.model_dump()

    invities = use_case.execute(dict_data, emails)  # type: ignore

    for invite in invities:
        redirect_url = f"{settings.BASE_URL}api/user/invite/{invite['token']}?redirect_url={project_service_redirect_url}"
        fast_mail, message = send_email_config(
            emails=[invite["email"]],
            subject="DevTeamTask | Joining the project",
            redirect_url=str(redirect_url),
        )

        background_tasks.add_task(
            fast_mail.send_message, message, template_name="join_the_project.html"
        )

    return JSONResponse(status_code=200, content={"message": "Email has been sent"})


def validate_invitation_by_token(
    token: UUID,
    redirect_url: AnyHttpUrl,
    use_case: InviteValidateByTokenUseCase = Depends(
        make_invite_validate_by_token_use_case
    ),
):
    response = RedirectResponse(settings.FRONT_END_URL)
    try:
        result = use_case.execute(token)
    except AppBaseException:
        response.set_cookie(
            "error",
            "Please create your registration in the system to proceed with the operation",
        )
        return response

    if result["invite"]["resource_name"] == "Project":
        return RedirectResponse(
            f"{redirect_url}?user_id={result['user']['id']}&project_id={result['invite']['resource_id']}"
        )

    if result["invite"]["resource_name"] == "User":
        return RedirectResponse(
            f"{redirect_url}?token={result['invite']['token']}&user_email={result['user']['email']}"
        )

    response.set_cookie("error", "Error")
    return response
