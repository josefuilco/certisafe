from fastapi import Depends
from src.configuration import get_async_session
from src.persistence.repositories import FacultyRepository
from src.services import FacultyService

def get_faculty_service(session=Depends(get_async_session)) -> FacultyService:
    faculty_repository = FacultyRepository(session=session)
    return FacultyService(faculty_repository=faculty_repository)