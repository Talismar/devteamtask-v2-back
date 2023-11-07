from jose import (
    JWTError,
    jwt,
    ExpiredSignatureError,
)
from fastapi import HTTPException
from datetime import datetime, timedelta
from app.configs.local import settings


class AuthenticationJWT:
    def __init__(self):
        self.secret = settings.SECRET_KEY
        self.algorithm = settings.AUTHJWT_ALGORITHM

    def create_access_token(self, payload_sub: dict):
        payload = payload_sub.copy()

        expire = datetime.utcnow() + timedelta(
            minutes=settings.AUTHJWT_ACCESS_TOKEN_EXPIRE_MINUTES
        )

        payload.update(
            {
                "exp": expire,
                "type": "access_token",
            }
        )

        return self.encode_token(payload)

    def encode_token(self, payload: dict):
        payload_copy = payload.copy()
        payload_copy["iat"] = datetime.utcnow()
        return jwt.encode(payload_copy, self.secret, algorithm=self.algorithm)

    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.secret, algorithms=[self.algorithm])

            if payload["type"] == "access_token":
                return payload["sub"]
            raise HTTPException(
                status_code=401, detail="Scope for the token is invalid"
            )
        except ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token expired")
        except JWTError:
            raise HTTPException(status_code=401, detail="Invalid token")

    def create_refresh_token(self, payload_sub):
        payload = payload_sub.copy()

        expire = datetime.utcnow() + timedelta(
            days=settings.AUTHJWT_REFRESH_TOKEN_EXPIRE_DAYS
        )

        payload.update(
            {
                "exp": expire,
                "type": "refresh_token",
            }
        )

        return self.encode_token(payload)

    def create_tokens(self, payload_sub):
        access_token = self.create_access_token(payload_sub)
        refresh_token = self.create_refresh_token(payload_sub)
        return access_token, refresh_token

    def refresh_token(self, refresh_token):
        try:
            payload = jwt.decode(
                refresh_token, self.secret, algorithms=[self.algorithm]
            )
            if payload["type"] == "refresh_token":
                payload_sub = {"sub": payload["sub"]}

                new_access_token, new_refresh_token = self.create_tokens(payload_sub)

                return new_access_token, new_refresh_token

            raise HTTPException(status_code=401, detail="Invalid scope for token")
        except ExpiredSignatureError as error:
            print("1 ", error)
            raise HTTPException(status_code=401, detail="Refresh token expired")
        except JWTError as error:
            print(error)
            raise HTTPException(status_code=401, detail="Invalid refresh token")


authentication_jwt = AuthenticationJWT()
