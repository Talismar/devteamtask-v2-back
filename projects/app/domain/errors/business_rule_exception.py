class BusinessRuleException(Exception):
    def __init__(self, message="Error") -> None:
        self.message = message
        self.status_code = 401
