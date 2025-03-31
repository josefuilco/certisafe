from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .user_entity import UserEntity

class AccountEntity(SQLModel, table=True):
    __tablename__ = 'accounts'

    # Attributes
    id: str = Field(max_length=36, primary_key=True)
    password: str = Field(max_length=64, nullable=False)
    active: bool = Field(default=True, nullable=False)

    # Foreign key
    user_id: int = Field(nullable=False, foreign_key='users.id')

    # Relation
    user: Optional['UserEntity'] = Relationship(back_populates='account')


