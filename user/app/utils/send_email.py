from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType

from ..configs.local import settings

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
)


def send_email_config(emails: str, html: str):
    message = MessageSchema(
        subject="Fastapi mail module",
        recipients=[emails],
        body=html,
        subtype=MessageType.html,
    )

    fast_mail = FastMail(conf)

    return fast_mail, message
