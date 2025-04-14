from fastapi import APIRouter, Depends, HTTPException, status, Response
from uuid import uuid4
from src.models import User, Faculty, Condition
from src.services import AuthService, JWTService
from src.enums import Role
from .dtos import UserAuthDto, CreateUserDto
from .dependencies import get_auth_service, get_jwt_service
from .presenters import SuccessfulPresenter

auth_router = APIRouter(
    prefix='/api/auth',
    tags=['auth'],
)

# POST /api/auth/sign-in
@auth_router.post('/sign-in')
async def sign_in(authentication: UserAuthDto):
    return authentication

# post /api/auth/sign-up
@auth_router.post('/sign-up')
async def sign_up(
    create_user_dto: CreateUserDto,
    response: Response,
    auth_service: AuthService = Depends(get_auth_service),
    jwt_service: JWTService = Depends(get_jwt_service)
) -> SuccessfulPresenter:
    try:
        new_user = User(
            id=str(uuid4()),
            dni=create_user_dto.dni,
            names=create_user_dto.names,
            surnames=create_user_dto.surnames,
            email=create_user_dto.email,
            cellphone=create_user_dto.cellphone,
            faculty=Faculty(id=create_user_dto.faculty),
            condition=Condition(id=create_user_dto.condition)
        )
        new_account = await auth_service.create_account(
            user=new_user,
            role=Role.ATTENDER
        )
        response.headers['x-api-token'] = jwt_service.encode({
            'user_id': new_user.id,
            'role_id': new_account.role_id,
            'exp': 4 * 60 * 60,
        })
        
        return SuccessfulPresenter(
            message=f'Usuario con número de documento: {new_account.dni} - Registrado.'
        )
    except HTTPException as e:
        raise HTTPException(
            status_code=e.status_code,
            detail=e.detail
        ) from e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        ) from e
