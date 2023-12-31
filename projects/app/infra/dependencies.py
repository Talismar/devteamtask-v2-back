from .database.configuration import Session


def database_connection():
    db = Session()
    try:
        yield db
    finally:
        db.close()
