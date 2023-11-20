from . import AppBaseException


class ResourceNotFoundException(AppBaseException):
    def __init__(self, resource_name: str) -> None:
        super().__init__(resource_name + " not found", 404)
