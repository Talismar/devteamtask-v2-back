from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from app.infra.database.base_model import BaseModel
from app.infra.database.models import *

engine = create_engine("postgresql://postgres:password@localhost:5433/TestDevTeamTask")
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

BaseModel.metadata.drop_all(bind=engine)
# BaseModel.metadata.create_all(bind=engine)


session = scoped_session(Session)

# model = StatusModel(name="status")
# session.add(model)
# session.commit()
# session.refresh(model)

# print(model.id)
from typing import TypedDict

from typing_extensions import Unpack


class TTTTest(TypedDict, total=False):
    name: str


def ttttest(**kwargs: Unpack[TTTTest]):
    dic = {"name": "Talismar", **kwargs}

    print(dic)


ttttest(name="Fernandes")
