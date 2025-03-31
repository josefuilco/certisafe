from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING, Optional, List

if TYPE_CHECKING:
    from .account_entity import AccountEntity

class RoleEntity(SQLModel, table=True):
    __tablename__ = 'roles'

    # Attributes
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=25, unique=True, nullable=False)

    # Relations
    accounts: List['AccountEntity'] = Relationship(back_populates='role')