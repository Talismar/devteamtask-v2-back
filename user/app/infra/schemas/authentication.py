from pydantic import BaseModel


class AuthenticationTokenPostResponseSchema(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str


class AuthenticationRefreshTokenPostResponseSchema(BaseModel):
    refresh_token: str
