import pytest_mutagen as mg

from app.infra.repositories.user_sqlalchemy_repository import *

mg.link_to_file("user_repository_integration_test.py")


# hash=7bdd61f9ee7ab776
@mg.mutant_of(
    "UserSqlalchemyRepository.__init__", "USERSQLALCHEMYREPOSITORY.__INIT___0"
)
def __init__(self, session: Session) -> None:
    self.session = None


# hash=bb5a078a7cebfc4b
@mg.mutant_of(
    "UserSqlalchemyRepository.list_all", "USERSQLALCHEMYREPOSITORY.LIST_ALL_0"
)
def list_all(self):
    user_models = None
    return [UserSqlalchemyMapper.toDomain(row) for row in user_models]


# hash=5d1ad11d2b1f0391
@mg.mutant_of(
    "UserSqlalchemyRepository.list_all", "USERSQLALCHEMYREPOSITORY.LIST_ALL_1"
)
def list_all(self):
    user_models = self.session.query(UserModel).all()
    pass


# hash=b61d4543665a772a
@mg.mutant_of("UserSqlalchemyRepository.create", "USERSQLALCHEMYREPOSITORY.CREATE_0")
def create(self, data):
    user_model = None

    try:
        self.session.add(user_model)
        self.session.commit()
        self.session.refresh(user_model)
    except IntegrityError:
        raise DatabaseException("Account already exists", 409)

    return UserSqlalchemyMapper.toDomain(user_model)


# hash=38b833f0f3320bed
@mg.mutant_of("UserSqlalchemyRepository.create", "USERSQLALCHEMYREPOSITORY.CREATE_1")
def create(self, data):
    user_model = UserSqlalchemyMapper.toSqlAlchemy(data)

    try:
        self.session.add(user_model)
        self.session.commit()
        self.session.refresh(user_model)
    except IntegrityError:
        raise DatabaseException("Account already exists", 410)

    return UserSqlalchemyMapper.toDomain(user_model)


# hash=392d5ddf733d2872
@mg.mutant_of("UserSqlalchemyRepository.create", "USERSQLALCHEMYREPOSITORY.CREATE_2")
def create(self, data):
    user_model = UserSqlalchemyMapper.toSqlAlchemy(data)

    try:
        self.session.add(user_model)
        self.session.commit()
        self.session.refresh(user_model)
    except IntegrityError:
        raise DatabaseException("Account already exists", 409)

    pass


# hash=98aeebe487b00cb2
@mg.mutant_of(
    "UserSqlalchemyRepository.get_by_id", "USERSQLALCHEMYREPOSITORY.GET_BY_ID_0"
)
def get_by_id(self, id):
    user_model = None

    if user_model is not None:
        return UserSqlalchemyMapper.toDomain(user_model)

    return None


# hash=e300a4cd17f746e2
@mg.mutant_of(
    "UserSqlalchemyRepository.get_by_id", "USERSQLALCHEMYREPOSITORY.GET_BY_ID_1"
)
def get_by_id(self, id):
    user_model = self.session.query(UserModel).filter_by(id=None).first()

    if user_model is not None:
        return UserSqlalchemyMapper.toDomain(user_model)

    return None


# hash=894275d3bf938860
@mg.mutant_of(
    "UserSqlalchemyRepository.get_by_id", "USERSQLALCHEMYREPOSITORY.GET_BY_ID_2"
)
def get_by_id(self, id):
    user_model = self.session.query(UserModel).filter_by(id=id).first()

    if not (user_model is not None):
        return UserSqlalchemyMapper.toDomain(user_model)

    return None


# hash=d925beafdeb74bfb
@mg.mutant_of(
    "UserSqlalchemyRepository.get_by_id", "USERSQLALCHEMYREPOSITORY.GET_BY_ID_3"
)
def get_by_id(self, id):
    user_model = self.session.query(UserModel).filter_by(id=id).first()

    if user_model is not None:
        pass

    return None


# hash=1a24227f35497ecc
@mg.mutant_of(
    "UserSqlalchemyRepository.get_by_id", "USERSQLALCHEMYREPOSITORY.GET_BY_ID_4"
)
def get_by_id(self, id):
    user_model = self.session.query(UserModel).filter_by(id=id).first()

    if user_model is not None:
        return UserSqlalchemyMapper.toDomain(user_model)

    pass


# hash=2640288b6d930b48
@mg.mutant_of(
    "UserSqlalchemyRepository.get_by_email", "USERSQLALCHEMYREPOSITORY.GET_BY_EMAIL_0"
)
def get_by_email(self, email):
    user_model = None

    if user_model is not None:
        return UserSqlalchemyMapper.toDomain(user_model)

    return None


# hash=4f5f792d7bd97aa2
@mg.mutant_of(
    "UserSqlalchemyRepository.get_by_email", "USERSQLALCHEMYREPOSITORY.GET_BY_EMAIL_1"
)
def get_by_email(self, email):
    user_model = self.session.query(UserModel).filter_by(email=None).first()

    if user_model is not None:
        return UserSqlalchemyMapper.toDomain(user_model)

    return None


# hash=facaf9f13c43bced
@mg.mutant_of(
    "UserSqlalchemyRepository.get_by_email", "USERSQLALCHEMYREPOSITORY.GET_BY_EMAIL_2"
)
def get_by_email(self, email):
    user_model = self.session.query(UserModel).filter_by(email=email).first()

    if not (user_model is not None):
        return UserSqlalchemyMapper.toDomain(user_model)

    return None


# hash=71336a2d9abeead8
@mg.mutant_of(
    "UserSqlalchemyRepository.get_by_email", "USERSQLALCHEMYREPOSITORY.GET_BY_EMAIL_3"
)
def get_by_email(self, email):
    user_model = self.session.query(UserModel).filter_by(email=email).first()

    if user_model is not None:
        pass

    return None


# hash=f48452acd55fdc7d
@mg.mutant_of(
    "UserSqlalchemyRepository.get_by_email", "USERSQLALCHEMYREPOSITORY.GET_BY_EMAIL_4"
)
def get_by_email(self, email):
    user_model = self.session.query(UserModel).filter_by(email=email).first()

    if user_model is not None:
        return UserSqlalchemyMapper.toDomain(user_model)

    pass
