from app.main.configuration.test import Session


def override_database_connection():
    try:
        session = Session()
        yield session
    finally:
        session.close()
