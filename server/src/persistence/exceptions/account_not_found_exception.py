from fastapi import HTTPException

class AccountNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=404,
            detail='La cuenta del usuario no fue encontrada.',
        )