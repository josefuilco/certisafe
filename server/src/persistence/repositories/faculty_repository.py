from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from sqlmodel import select
from ..entities import FacultyEntity
from ...models import Faculty

class FacultyRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_all(self) -> List[Faculty]:
        statement = select(FacultyEntity)
        result = await self._session.execute(statement)
        faculty_entities = result.scalars().all()

        faculties: List[Faculty] = []
        for faculty_entity in faculty_entities:
            faculty = Faculty(
                id=faculty_entity.id,
                name=faculty_entity.name
            )
            faculties.append(faculty)

        return faculties