from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from app.main.configuration.local import settings

engine = create_engine(settings.DATABASE_URL)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
