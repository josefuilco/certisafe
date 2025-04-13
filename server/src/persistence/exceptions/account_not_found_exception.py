from fastapi import HTTPException, status

class AccountNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='La cuenta del usuario no fue encontrada.',
        )