from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .user_entity import UserEntity
    from .role_entity import RoleEntity

class AccountEntity(SQLModel, table=True):
    __tablename__ = 'accounts'

    # Attributes
    id: Optional[int] = Field(default=None, primary_key=True)
    password: str = Field(max_length=60, nullable=False)
    active: bool = Field(default=True, nullable=False)

    # Foreign key
    user_id: str = Field(nullable=False, foreign_key='users.id')
    role_id: int = Field(nullable=False, foreign_key='roles.id')

    # Relation
    user: Optional['UserEntity'] = Relationship(back_populates='account')
    role: Optional['RoleEntity'] = Relationship(back_populates='accounts')


