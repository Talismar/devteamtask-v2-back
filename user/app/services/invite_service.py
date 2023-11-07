from datetime import datetime
from typing import TypedDict
from uuid import UUID

from app.repositories.invite_repository import InviteRepository
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError


class InviteCreateDTO(TypedDict):
    resource_name: str
    resource_id: int
    expiration_date: datetime


class InviteService:
    def __init__(self, invite_repository: InviteRepository) -> None:
        self.__invite_repository = invite_repository

    def validate_invitation_by_token(self, token: UUID):
        try:
            invite_instance = self.__invite_repository.get_by_token(token)
            if invite_instance is None:
                raise HTTPException(status_code=200, detail="Token invalid")
            return invite_instance
        except:
            raise HTTPException(status_code=200, detail="Token invalid")

    def create(self, data: InviteCreateDTO):
        try:
            return self.__invite_repository.create(data)
        except IntegrityError:
            # TODO: handle this error after
            raise HTTPException(
                status_code=500,
                detail="Error creating invite",
            )
