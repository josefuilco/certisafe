from bcrypt import hashpw, gensalt
from src.persistence.repositories import UserRepository, AccountRepository
from src.models import User, Account
from src.enums import Role

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