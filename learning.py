from typing import Any


class Faker:
    def __getattribute__(self, __name: str) -> Any:
        print(__name)


fake = Faker()
fake.name()
