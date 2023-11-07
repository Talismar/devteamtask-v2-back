from uuid import UUID


class Task:
    def __init__(self, id: UUID, name: str, description: str) -> None:
        self.__id = id
        self.name = name
        self.description = description
