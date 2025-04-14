from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from src.models import Condition
from src.services import ConditionService
from .dependencies import get_condition_service

condition_router = APIRouter(
    prefix="/api/conditions",
    tags=["conditions"],
)

# GET /api/conditions/
@condition_router.get('/')
async def get_conditions(condition_service: ConditionService = Depends(get_condition_service)) -> List[Condition]:
    try:
        conditions = await condition_service.get_all()
        return conditions
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        ) from e