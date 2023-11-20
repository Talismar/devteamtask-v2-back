import json

from faker import Faker
from sqlalchemy import text
from sqlalchemy.orm import scoped_session

from app.infra.database.base_model import BaseModel
from app.infra.database.models import *
from app.main.configuration.test import Session, engine


class BaseTest:
    def setup_method(self, method):
        BaseModel.metadata.create_all(bind=engine)
        self.fake = Faker()
        self.session = scoped_session(Session)

        sql = text(
            """
                create table if not exists users
                (
                    id                 serial
                        primary key,
                    name               varchar(120) not null,
                    email              varchar(120) not null
                        unique,
                    password           varchar      not null,
                    avatar_url         varchar,
                    created_at         timestamp    not null,
                    updated_at         timestamp    not null
                )
            """
        )

        self.session.execute(sql)
        self.session.commit()
        self.session.close()

    def teardown_method(self, method):
        self.session.close()
        BaseModel.metadata.drop_all(bind=engine)
        self.session.commit()
        self.session.close()

        self.session.execute(text("DROP TABLE IF EXISTS users"))
        self.session.commit()

    def fprint(self, data: dict):
        print()
        pretty = json.dumps(data, indent=2)
        print(pretty)
