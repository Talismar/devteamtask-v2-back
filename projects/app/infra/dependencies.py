from sqlalchemy.orm import scoped_session

from .database.configuration import Session


def database_connection():
    db = scoped_session(Session)
    try:
        yield db
    finally:
        db.close()
