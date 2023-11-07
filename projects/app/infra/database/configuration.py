from app.main.configuration.local import settings
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

engine = create_engine(settings.DATABASE_URL)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# with engine.connect() as connection:
#     result = connection.execute(text("select * from users"))
#     for row in result:
#         print("username:", row)
