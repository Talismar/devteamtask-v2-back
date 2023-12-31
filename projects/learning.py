# print(model.id)
from typing import TypedDict
from uuid import UUID

from sqlalchemy import select, text
from sqlalchemy.orm import joinedload
from typing_extensions import Unpack

from app.infra.database.base_model import BaseModel
from app.infra.database.configuration import Session, engine
from app.infra.database.models import *

# engine = create_engine("postgresql://postgres:password@localhost:5432/DevTeamTask")
# Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# BaseModel.metadata.drop_all(bind=engine)
# BaseModel.metadata.create_all(bind=engine)

# with engine.connect() as connection:
#     result = connection.execute(
#         text("select * from projects where id == 5485df06-a0f5-11ee-89d5-f09e4ac22c2f")
#     )
#     for row in result:
#         print("username:", row)

# session = Session()


# model = session().query(ProjectModel).get(UUID("5485df06-a0f5-11ee-89d5-f09e4ac22c2f"))
# # session.commit()
# print(model)
# session.add(model)
# session.refresh(model)


# class TTTTest(TypedDict, total=False):
#     name: str


# def ttttest(**kwargs: Unpack[TTTTest]):
#     dic = {"name": "Talismar", **kwargs}

#     print(dic)


# ttttest(name="Fernandes")


session = Session()
project = (
    session.query(ProjectModel)
    .filter_by(id=UUID("f0590162-a265-11ee-8b83-f09e4ac22c2f"))
    .options(joinedload(ProjectModel.tasks))
    .first()
)

# Filtra as tarefas diretamente na relação (InstrumentedSet)
filtered_tasks_set = set(
    task for task in project.tasks if "1".lower() in task.name.lower()
)

# Atualiza a coleção no projeto com a nova InstrumentedSet filtrada
project.tasks = filtered_tasks_set

# Agora, project.tasks conterá apenas as tarefas filtradas
for task in project.tasks:
    print(task)

# task = (
#     session.query(TaskModel)
#     .filter_by(
#         project_id=UUID("f0590162-a265-11ee-8b83-f09e4ac22c2f"), name.ilike="tas"
#     )
#     .all()
# )
# for i in task:
#     print(i.project_id)

stmt = (
    select(ProjectModel)
    .join(ProjectModel.tasks)
    .where(TaskModel.name.ilike(f"%as%"))
    .where(ProjectModel.id == UUID("f0590162-a265-11ee-8b83-f09e4ac22c2f"))
)

print(stmt)

for task in session.scalars(stmt).first().tasks:
    print(task)

# # for status in sorted(
# #     session.query(ProjectModel).first().status, key=lambda status: status.id
# # ):
# #     print(status.id)
