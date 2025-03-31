from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from .user_entity import UserEntity

class FacultyEntity(SQLModel, table=True):
    __tablename__ = 'faculties'

    # Attributes
    id: int = Field(default=None, primary_key=True)
    name: str = Field(max_length=25, unique=True, nullable=False)

    # Relations
    users: List['UserEntity'] = Relationship(back_populates='faculty')