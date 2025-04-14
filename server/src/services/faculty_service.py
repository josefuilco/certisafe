from typing import List
from src.persistence.repositories import FacultyRepository
from src.models import Faculty

class FacultyService:
    def __init__(self, faculty_repository: FacultyRepository):
        self._faculty_repository = faculty_repository

    async def get_all(self) -> List[Faculty]:
        return await self._faculty_repository.get_all()