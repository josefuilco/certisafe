from fastapi import Depends
from src.configuration.database import get_async_session
from src.persistence.repositories import ConditionRepository
from src.services import ConditionService

def get_condition_service(session=Depends(get_async_session)) -> ConditionService:
    condition_repository = ConditionRepository(session=session)
    return ConditionService(condition_repository=condition_repository)