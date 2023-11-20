class Status:
    def __init__(
        self,
        name: str,
        id: int | None = None,
    ) -> None:
        self.id = id
        self.name = name
