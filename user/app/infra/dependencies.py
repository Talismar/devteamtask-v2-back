from sqlalchemy.orm import scoped_session

from app.infra.configs.local import Session


def database_connection():
    session = scoped_session(Session)
    try:
        yield session
    finally:
        session.close()
