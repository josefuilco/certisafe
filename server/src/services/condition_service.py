from src.persistence.repositories import ConditionRepository

class ConditionService:
    def __init__(self, condition_repository: ConditionRepository):
        self._condition_repository = condition_repository

    async def get_all(self):
        return await self._condition_repository.get_all()