from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING, Optional, List
from datetime import date, time
from .user_event_link_entity import UserEventLinkEntity

if TYPE_CHECKING:
    from .user_entity import UserEntity

class EventEntity(SQLModel, table=True):
    __tablename__ = 'events'

    # Attributes
    id: str = Field(max_length=36, primary_key=True)
    name: str = Field(max_length=50, nullable=False)
    capacity: int = Field(default=0, nullable=False)
    description: Optional[str] = Field(max_length=250, nullable=True)
    day: date = Field(nullable=False)
    start: time = Field(nullable=False)
    end: time = Field(nullable=False)
    have_certificate: bool = Field(default=False, nullable=False)

    # Relations
    users: List['UserEntity'] = Relationship(back_populates='events', link_model=UserEventLinkEntity)