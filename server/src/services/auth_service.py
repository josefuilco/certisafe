import asyncio
from fastapi import HTTPException, status
from bcrypt import hashpw, gensalt, checkpw
from src.persistence.repositories import UserRepository, AccountRepository
from src.models import User, Account
from src.enums import Role
from .dtos import AuthenticationDto

class AuthService:
    def __init__(self, user_repository: UserRepository, account_repository: AccountRepository):
        self._user_repository = user_repository
        self._account_repository = account_repository

    async def create_account(self, user: User, role: Role) -> Account:
        new_user = await self._user_repository.create(user)
        # Encrypt the password using bcrypt
        encrypted_password = hashpw(
            new_user.dni.encode('utf-8'),
            gensalt(rounds=10)
        ).decode('utf-8')
        # Create the account with the encrypted password
        new_account = await self._account_repository.create(
            user_id=new_user.id,
            dni=new_user.dni,
            password=encrypted_password,
            role=role,
        )
        return new_account
    
    async def validate_credentials(self, account: Account) -> AuthenticationDto:
        user_id = await self._user_repository.get_id_by_dni(account.dni)
        role, password_hashed_raw = await asyncio.gather(
            self._account_repository.get_role_by_user_id(user_id),
            self._account_repository.get_password_by_user_id(user_id)            
        )
        password_encode = account.password.encode('utf-8')
        password_hashed = password_hashed_raw.encode('utf-8')
        
        if not checkpw(password_encode, password_hashed):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Credenciales inválidas.'
            )
        
        return AuthenticationDto(user_id=user_id, role_id=role.value)