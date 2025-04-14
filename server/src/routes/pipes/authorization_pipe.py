from fastapi import Depends, Request, HTTPException, status
from src.services import JWTService
from ..dependencies import get_jwt_service
from src.services.dtos import AuthenticationDto

def use_authorization_pipe(
    request: Request,
    jwt_service: JWTService = Depends(get_jwt_service)
) -> AuthenticationDto:
    auth_header = request.headers['Authorization']
    # Validations
    if not auth_header or not auth_header.startswith('Bearer '):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='No se ha proporcionado un token de autorización.'
        )
    # Extract the token from the header
    token = auth_header.split(' ')[1]
    # Decode the token
    jwt_dict = jwt_service.decode(token)
    # Map the JWT dictionary to the AuthenticationDto
    auth_dto = AuthenticationDto(
        user_id=jwt_dict['user_id'],
        role_id=jwt_dict['role_id']
    )
    return auth_dto