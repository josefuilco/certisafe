from fastapi import HTTPException

class CreationConflictException(HTTPException):
    def __init__(self, message: str):
        super().__init__(
            status_code=409,
            detail=message,
        )