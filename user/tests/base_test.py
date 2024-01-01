from faker import Faker

from app.infra.configs.test import Session, engine
from app.infra.database import BaseModel


class BaseTest:
    def setup_method(self, method):
        BaseModel.metadata.create_all(bind=engine)
        self.faker = Faker()
        self.session = Session()

    def teardown_method(self, method):
        BaseModel.metadata.drop_all(bind=engine)
