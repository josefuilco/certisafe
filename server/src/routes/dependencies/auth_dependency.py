from fastapi import Depends
from src.configuration import get_async_session
from src.services import AuthService
from src.persistence.repositories import UserRepository, AccountRepository

def get_auth_service(session=Depends(get_async_session)) -> AuthService:
    user_repository = UserRepository(session=session)
    account_repository = AccountRepository(session=session)
    return AuthService(user_repository=user_repository, account_repository=account_repository)