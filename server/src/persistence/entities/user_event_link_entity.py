from sqlmodel import SQLModel, Field, Relationship

class UserEventLinkEntity(SQLModel, table=True):
    __tablename__ = "user_event_link"
    
    user_id: str = Field(foreign_key="users.id", primary_key=True)
    event_id: int = Field(foreign_key="events.id", primary_key=True)
    attended: bool = Field(default=False, nullable=False)
    