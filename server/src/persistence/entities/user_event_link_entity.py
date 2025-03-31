from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

class UserEventLinkEntity(SQLModel, table=True):
    __tablename__ = "user_event_link"
    
    user_id: int = Field(foreign_key="users.id", primary_key=True)
    event_id: int = Field(foreign_key="events.id", primary_key=True)
    