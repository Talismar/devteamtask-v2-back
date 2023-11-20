from abc import ABC, abstractmethod


class TagRepository(ABC):
    @abstractmethod
    def get_or_create(self, data):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, id: int):
        pass

    @abstractmethod
    def delete(self, id: int):
        pass
