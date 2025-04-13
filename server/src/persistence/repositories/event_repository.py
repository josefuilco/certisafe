from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from sqlmodel import select
from uuid import uuid4
from ..exceptions import CreationConflictException
from ..entities import EventEntity
from ...models import Event

class EventRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def create(self, event: Event) -> Event:
        try:
            # Generate a unique ID for the event
            event.id = str(uuid4())

            # Create an EventEntity instance and add it to the session
            event_entity = EventEntity(
                id=event.id,
                name=event.name,
                description=event.description,
                day=event.day,
                start=event.start,
                end=event.end,
                capacity=event.capacity,
                have_certificate=event.have_certificate,
            )
            self._session.add(event_entity)
            await self._session.commit()
            await self._session.refresh(event_entity)

            return event
        except SQLAlchemyError:
            self._session.rollback()
            raise CreationConflictException('El evento ya se encuentra registrado.')