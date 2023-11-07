from fastapi import Depends, HTTPException
from app.repositories.user_repository import UserRepository
from app.utils.authentication_jwt import authentication_jwt
from app.utils.hash_password import verify_password


class AuthenticationService:
    def __init__(self, user_repository: UserRepository = Depends()):
        self.user_repository = user_repository

    def authenticate_user(self, email: str, password: str):
        user = self.user_repository.get_by_email(email)
        if not user:
            return False
        if not verify_password(password, user.password):
            return False
        if user is None:
            return False
        return user

    def token(self, email: str, password: str):
        user = self.authenticate_user(email, password)

        if not user:
            raise HTTPException(
                status_code=401,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        payload_sub = {"sub": str(user.id)}
        access_token, refresh_token = authentication_jwt.create_tokens(payload_sub)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
        }

    def refresh_token(self, refresh_token: str):
        access_token, refresh_token = authentication_jwt.refresh_token(refresh_token)
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
        }
