from .app_base_exception import AppBaseException


class UnauthorizedException(AppBaseException):
    def __init__(self, message: str = "Account already exists") -> None:
        super().__init__(message, 401)
