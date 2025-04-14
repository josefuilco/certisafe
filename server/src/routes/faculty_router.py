from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from src.models import Faculty
from src.services import FacultyService
from .dependencies import get_faculty_service

faculty_router = APIRouter(
    prefix="/api/faculties",
    tags=["faculties"],
)

# GET /api/faculties/
@faculty_router.get("/")
async def get_faculties(faculty_service: FacultyService = Depends(get_faculty_service)) -> List[Faculty]:
    try:
        faculties = await faculty_service.get_all()
        return faculties
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        ) from e