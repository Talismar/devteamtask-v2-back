from pathlib import Path

from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType

from app.infra.configs.local import settings

TEMPLATE_FOLDER_PATH = Path().absolute() / "templates"

conf = ConnectionConfig(
    MAIL_USERNAME=settings.EMAIL_USERNAME,
    MAIL_PASSWORD=settings.EMAIL_PASSWORD,
    MAIL_FROM=settings.EMAIL_USERNAME,
    MAIL_PORT=settings.EMAIL_PORT,
    MAIL_SERVER=settings.EMAIL_HOST,
    MAIL_FROM_NAME="Talismar Fernandes Costa",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
    TEMPLATE_FOLDER=TEMPLATE_FOLDER_PATH,
)


def send_email_config(
    emails: list[str],
    subject: str,
    html: str | None = None,
    redirect_url: str | None = None,
):
    if isinstance(html, str):
        message = MessageSchema(
            subject=subject,
            recipients=emails,
            body=html,
            subtype=MessageType.html,
        )

    else:
        message = MessageSchema(
            subject=subject,
            recipients=emails,
            template_body={"redirect_url": redirect_url},
            subtype=MessageType.html,
        )

    fast_mail = FastMail(conf)

    return fast_mail, message
