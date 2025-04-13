from typing import List
from src.persistence.repositories import ConditionRepository
from src.models import Condition

class ConditionService:
    def __init__(self, condition_repository: ConditionRepository):
        self._condition_repository = condition_repository

    async def get_all(self) -> List[Condition]:
        return await self._condition_repository.get_all()