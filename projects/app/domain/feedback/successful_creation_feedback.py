class SuccessFulCreationFeedback:
    def __init__(
        self, resource_name: str, message: str = " created successfully"
    ) -> None:
        self.message = resource_name + message
