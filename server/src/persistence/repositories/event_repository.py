from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from sqlmodel import select
from uuid import uuid4
from ..exceptions import CreationConflictException, EventNotFoundException
from ..entities import EventEntity
from ...models import Event

class EventRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    def _map_event_entity_to_event(self, event_entity: EventEntity) -> Event:
        return Event(
            id=event_entity.id,
            name=event_entity.name,
            description=event_entity.description,
            day=event_entity.day,
            start=event_entity.start,
            end=event_entity.end,
            capacity=event_entity.capacity,
            have_certificate=event_entity.have_certificate,
        )

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
    
    async def get_by_page(self) -> list[Event]:
        statement = select(EventEntity)
        result = await self._session.execute(statement)
        event_entities = result.scalars().all()

        return [self._map_event_entity_to_event(event_entity) for event_entity in event_entities]
    
    async def get_by_id(self, event_id: str) -> Event:
        statement = (
            select(EventEntity)
            .where(EventEntity.id == event_id)
        )
        result = await self._session.execute(statement)
        event_entity = result.scalar_one_or_none()

        if not event_entity:
            raise EventNotFoundException()

        return self._map_event_entity_to_event(event_entity)