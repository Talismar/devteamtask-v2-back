from typing import Any

from faker import Faker, providers


class Test:
    def name(self):
        return "Method Name"

    def __getattr__(self, __name: str) -> str:
        return "Method not found"

    # def __getattribute__(self, __name: str) -> Any:
    #     print("GETATTRIBUTE")
    #     return super().__getattribute__(__name)


class Test2:
    def test(self):
        print(self.name())


class Children(Test, Test2):
    pass


user = Children()
user.test()

# fake = Faker()

# print(fake.name())
# print(fake.email())
# print(fake.address())
# print(fake.random_int())
