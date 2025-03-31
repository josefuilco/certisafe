from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING, Optional, List
from .user_event_link_entity import UserEventLinkEntity

if TYPE_CHECKING:
    from .user_entity import UserEntity

class EventEntity(SQLModel, table=True):
    __tablename__ = 'events'

    # Attributes
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=50, nullable=False)
    description: Optional[str] = Field(max_length=250, nullable=True)
    start_date: str = Field(nullable=False)
    end_date: str = Field(nullable=False)

    # Relations
    users: List['UserEntity'] = Relationship(back_populates='events', link_model=UserEventLinkEntity)