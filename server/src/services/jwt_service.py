import jwt
from fastapi import HTTPException, status
from src.configuration import env

class JWTService:
    def __init__(self):
        self.secret_key = env.JWT_SECRET
        self.algorithm = 'HS256'

    def encode(self, payload: dict) -> str:
        return jwt.encode(
            payload,
            self.secret_key,
            algorithm=self.algorithm
        )

    def decode(self, token: str) -> dict:
        try:
            return jwt.decode(
                token,
                self.secret_key,
                algorithms=[self.algorithm]
            )
        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='El token ha expirado',
            )
        except jwt.InvalidTokenError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='El token es inválido',
            )