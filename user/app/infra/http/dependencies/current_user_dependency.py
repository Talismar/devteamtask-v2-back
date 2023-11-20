from fastapi import Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.infra.database import UserModel
from app.infra.dependencies import database_connection
from app.infra.repositories import UserSqlalchemyRepository
from app.infra.utils.authentication_jwt import authentication_jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/user/authentication/token")


class CurrentUserDependency:
    def __init__(self) -> None:
        pass

    async def __call__(
        self,
        request: Request,
        access_token: str = Depends(oauth2_scheme),
        db_session: Session = Depends(database_connection),
    ):
        user_id: str = authentication_jwt.decode_token(access_token)
        user_repository = UserSqlalchemyRepository(db_session)
        user = user_repository.get_by_id(int(user_id))

        if user is None:
            raise HTTPException(status_code=401, detail="Not authorized to access")

        request.scope["user"] = user
