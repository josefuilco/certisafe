from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from sqlmodel import select
from ..entities import ConditionEntity
from ...models import Condition

class ConditionRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_all(self) -> List[Condition]:
        statement = select(ConditionEntity)
        result = await self._session.execute(statement)
        condition_entities = result.scalars().all()

        conditions: List[Condition] = []
        for condition_entity in condition_entities:
            condition = Condition(
                id=condition_entity.id,
                name=condition_entity.name
            )
            conditions.append(condition)

        return conditions