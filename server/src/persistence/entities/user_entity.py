from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING, Optional, List
from .user_event_link_entity import UserEventLinkEntity

if TYPE_CHECKING:
    from .condition_entity import ConditionEntity
    from .faculty_entity import FacultyEntity
    from .account_entity import AccountEntity
    from .event_entity import EventEntity    

class UserEntity(SQLModel, table=True):
    __tablename__ = 'users'

    # Attributes
    id: Optional[int] = Field(default=None, primary_key=True)
    names: str = Field(max_length=25, nullable=False)
    surnames: str = Field(max_length=25, nullable=False)
    email: str = Field(max_length=80, unique=True, nullable=False)
    cellphone: str = Field(max_length=9, unique=True, nullable=False)
    dni: str = Field(max_length=8, unique=True, nullable=False)

    # Foreign keys
    condition_id: int = Field(nullable=False, foreign_key='conditions.id')
    faculty_id: int = Field(nullable=False, foreign_key='faculties.id')

    # Relations
    condition: Optional['ConditionEntity'] = Relationship(back_populates='users')
    faculty: Optional['FacultyEntity'] = Relationship(back_populates='users')
    account: Optional['AccountEntity'] = Relationship(back_populates='user')
    events: List['EventEntity'] = Relationship(back_populates='users', link_model=UserEventLinkEntity)
