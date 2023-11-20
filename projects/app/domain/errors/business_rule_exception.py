from . import AppBaseException


class BusinessRuleException(AppBaseException):
    def __init__(self, message="Error") -> None:
        super().__init__(message, 400)
