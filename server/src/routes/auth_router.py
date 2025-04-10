from fastapi import APIRouter
from .dtos import UserAuthDto

auth_router = APIRouter(
    prefix='/api/auth',
    tags=['auth'],
)

# POST /auth/login
@auth_router.post('/sign-in')
async def sign_in(authentication: UserAuthDto):
    return authentication