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


# hash=592b7c9af51ff1a9
@mg.mutant_of(
    "UserSqlalchemyRepository.partial_update",
    "USERSQLALCHEMYREPOSITORY.PARTIAL_UPDATE_0",
)
def partial_update(self, id, data_to_update):
    stmt = None
    result = self.session.execute(stmt)
    updated_data = result.fetchone()
    self.session.commit()

    return UserSqlalchemyMapper.toDomain(updated_data[0])


# hash=64a323717567ebac
@mg.mutant_of(
    "UserSqlalchemyRepository.partial_update",
    "USERSQLALCHEMYREPOSITORY.PARTIAL_UPDATE_1",
)
def partial_update(self, id, data_to_update):
    stmt = (
        update(UserModel)
        .where(UserModel.id != id)
        .values(**data_to_update)
        .returning(UserModel)
    )
    result = self.session.execute(stmt)
    updated_data = result.fetchone()
    self.session.commit()

    return UserSqlalchemyMapper.toDomain(updated_data[0])


# hash=5c1b0db86c59c286
@mg.mutant_of(
    "UserSqlalchemyRepository.partial_update",
    "USERSQLALCHEMYREPOSITORY.PARTIAL_UPDATE_2",
)
def partial_update(self, id, data_to_update):
    stmt = (
        update(UserModel)
        .where(UserModel.id == id)
        .values(*data_to_update)
        .returning(UserModel)
    )
    result = self.session.execute(stmt)
    updated_data = result.fetchone()
    self.session.commit()

    return UserSqlalchemyMapper.toDomain(updated_data[0])


# hash=a37d41c0ceb060fd
@mg.mutant_of(
    "UserSqlalchemyRepository.partial_update",
    "USERSQLALCHEMYREPOSITORY.PARTIAL_UPDATE_3",
)
def partial_update(self, id, data_to_update):
    stmt = (
        update(UserModel)
        .where(UserModel.id == id)
        .values(**data_to_update)
        .returning(UserModel)
    )
    result = None
    updated_data = result.fetchone()
    self.session.commit()

    return UserSqlalchemyMapper.toDomain(updated_data[0])


# hash=59dd504f8f01a91b
@mg.mutant_of(
    "UserSqlalchemyRepository.partial_update",
    "USERSQLALCHEMYREPOSITORY.PARTIAL_UPDATE_4",
)
def partial_update(self, id, data_to_update):
    stmt = (
        update(UserModel)
        .where(UserModel.id == id)
        .values(**data_to_update)
        .returning(UserModel)
    )
    result = self.session.execute(stmt)
    updated_data = None
    self.session.commit()

    return UserSqlalchemyMapper.toDomain(updated_data[0])


# hash=bc6b85fba51eaf8f
@mg.mutant_of(
    "UserSqlalchemyRepository.partial_update",
    "USERSQLALCHEMYREPOSITORY.PARTIAL_UPDATE_5",
)
def partial_update(self, id, data_to_update):
    stmt = (
        update(UserModel)
        .where(UserModel.id == id)
        .values(**data_to_update)
        .returning(UserModel)
    )
    result = self.session.execute(stmt)
    updated_data = result.fetchone()
    self.session.commit()

    pass


# hash=6bef99caa6bf6ffa
@mg.mutant_of(
    "UserSqlalchemyRepository.partial_update",
    "USERSQLALCHEMYREPOSITORY.PARTIAL_UPDATE_6",
)
def partial_update(self, id, data_to_update):
    stmt = (
        update(UserModel)
        .where(UserModel.id == id)
        .values(**data_to_update)
        .returning(UserModel)
    )
    result = self.session.execute(stmt)
    updated_data = result.fetchone()
    self.session.commit()

    return UserSqlalchemyMapper.toDomain(updated_data[1])


# hash=1dc5cb7f868f5e20
@mg.mutant_of("UserSqlalchemyRepository.delete", "USERSQLALCHEMYREPOSITORY.DELETE_0")
def delete(self, id):
    user_mode = None

    if user_mode is not None:
        raise ResourceNotFoundException("User")

    self.session.delete(user_mode)
    self.session.commit()


# hash=33818f4f5da5a7f7
@mg.mutant_of("UserSqlalchemyRepository.delete", "USERSQLALCHEMYREPOSITORY.DELETE_1")
def delete(self, id):
    user_mode = self.session.get(UserModel, id)

    if not (user_mode is not None):
        raise ResourceNotFoundException("User")

    self.session.delete(user_mode)
    self.session.commit()
