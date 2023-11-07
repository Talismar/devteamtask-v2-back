from abc import ABC, abstractmethod


class SprintRepository(ABC):
    @abstractmethod
    def create(self, data):
        pass

    # @abstractmethod
    # def get_all(self):
    #     pass

    # @abstractmethod
    # def get_by_id(self, id: int):
    #     pass

    # @abstractmethod
    # def partial_update(self, id: int, data):
    #     pass

    # @abstractmethod
    # def delete(self, id: int):
    #     pass
