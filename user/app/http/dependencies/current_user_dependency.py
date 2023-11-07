from app.dependencies import get_db_connection
from app.models.user import UserModel
from app.utils.authentication_jwt import authentication_jwt
from fastapi import Depends, Request
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/authentication/token")


class CurrentUserDependency:
    def __init__(self) -> None:
        pass

    async def __call__(
        self,
        request: Request,
        access_token: str = Depends(oauth2_scheme),
        db_session: Session = Depends(get_db_connection),
    ):
        user_id: str = authentication_jwt.decode_token(access_token)
        user = db_session.get(UserModel, int(user_id))
        db_session.commit()

        request.scope["user"] = user
