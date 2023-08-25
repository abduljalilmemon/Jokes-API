from uuid import UUID

from fastapi import Form
from pydantic import BaseModel, Field, SecretStr


class UserAuth(BaseModel):
    email: str = Field(..., description="user email")
    name: str = Field(..., description="user name")
    password: SecretStr = Form(..., min_length=5, max_length=24,
                               description="user password")


class UserLogin(BaseModel):
    email: str = Field(..., description="user email")
    password: SecretStr = Form(..., min_length=5, max_length=24,
                               description="user password")


class JokeSchema(BaseModel):
    joke: str = Field(default="write your joke here")
    category: str = Field(default="category")
