from abc import ABC, abstractmethod


class AbstractEmailService(ABC):
    @abstractmethod
    def send(self, emails: list[str], resource_id: str, redirect_path: str):
        pass
