from .app_base_exception import AppBaseException


class DatabaseException(AppBaseException):
    def __init__(self, message: str, status_code: int = 409) -> None:
        super().__init__(message, status_code)
