from fastapi import HTTPException, status

class EventNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='El evento buscado no fue encontrado.',
        )