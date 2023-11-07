from uuid import UUID

from fastapi import BackgroundTasks, Depends
from fastapi.responses import JSONResponse, RedirectResponse
from pydantic import AnyHttpUrl

from ...schemas.invite_schemas import InvitePostRequestSchema
from ...services.factories.make_invite_service import make_invite_service
from ...services.invite_service import InviteService
from ...utils.send_email import send_email_config


def create_and_send_email(
    data: InvitePostRequestSchema,
    background_tasks: BackgroundTasks,
    invite_service: InviteService = Depends(make_invite_service),
):
    emails = data.emails[0]
    del data.emails
    redirect_url = data.redirect_url
    del data.redirect_url

    invite_instance = invite_service.create(data.model_dump())

    html = f"""
        <p>Hi this test mail, thanks for using Fastapi-mail
            <a href="http://localhost:8000/api/user/invite/{invite_instance.token}?redirect_url={redirect_url}" >Test</a>
        </p> """

    fast_mail, message = send_email_config(emails, html)

    background_tasks.add_task(fast_mail.send_message, message)

    return JSONResponse(status_code=200, content={"message": "email has been sent"})


def validate_invitation_by_token(
    token: UUID,
    redirect_url: AnyHttpUrl,
    invite_service: InviteService = Depends(make_invite_service),
):
    invite_data = invite_service.validate_invitation_by_token(token)

    return RedirectResponse(
        f"{redirect_url}?validation_state=success&project_id={invite_data.token}"
    )
