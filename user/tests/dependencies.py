from app.configs.test import Session


def override_get_db():
    try:
        db = Session()
        yield db
    finally:
        db.close()
