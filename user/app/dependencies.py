from app.configs.local import Session
from sqlalchemy.orm import scoped_session


def get_db_connection():
    db = scoped_session(Session)
    try:
        yield db
    finally:
        print("DB disconnect")
        db.close()
