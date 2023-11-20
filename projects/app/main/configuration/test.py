from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:password@localhost:5433/TestDevTeamTask")
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
