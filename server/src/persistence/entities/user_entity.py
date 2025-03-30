from sqlmodel import SQLModel, Field
from typing import Optional

class UserEntity(SQLModel, table=True):
    __tablename__ = 'users'
    id: Optional[int] = Field(default=None, primary_key=True)
    names: str = Field(max_length=25, nullable=False)
    lastnames: str = Field(max_length=25, nullable=False)
    email: str = Field(max_length=80, unique=True, nullable=False)
    cellphone: str = Field(max_length=9, unique=True, nullable=False)
    dni: str = Field(max_length=8, unique=True, nullable=False)