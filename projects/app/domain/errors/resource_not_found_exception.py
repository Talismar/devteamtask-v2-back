class ResourceNotFoundException(Exception):
    def __init__(self, resource_name: str) -> None:
        self.message = resource_name + " not found"
        self.status_code = 401
