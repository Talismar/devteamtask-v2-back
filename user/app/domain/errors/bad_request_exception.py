from .app_base_exception import AppBaseException


class BadRequestException(AppBaseException):
    def __init__(self, message: str) -> None:
        super().__init__(message, 400)
