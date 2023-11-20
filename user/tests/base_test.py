from app.infra.configs.test import Session, engine
from app.infra.database import BaseModel
from faker import Faker
from sqlalchemy.orm import scoped_session


class BaseTest:
    def setup_method(self, method):
        BaseModel.metadata.create_all(bind=engine)
        self.fake = Faker()
        self.session = scoped_session(Session)

    def teardown_method(self, method):
        BaseModel.metadata.drop_all(bind=engine)
