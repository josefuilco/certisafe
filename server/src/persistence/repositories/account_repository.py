from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from sqlmodel import select
from ...models import Account
from ...enums import Role
from ..entities import AccountEntity
from ..exceptions import CreationConflictException, AccountNotFoundException

class AccountRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def create(self, user_id: str, dni: str, password: str, role: Role) -> Account:
        try:
            account_entity = AccountEntity(
                password=password,
                user_id=user_id,
                role_id=role.value
            )
            self._session.add(account_entity)
            await self._session.commit()
            await self._session.refresh(account_entity)

            current_account = Account(
                dni=dni,
                password=password,
                role_id=role.value
            )

            return current_account
        except SQLAlchemyError:
            self._session.rollback()
            raise CreationConflictException('El usuario ya se encuentra registrado.')
    
    async def get_password_by_user_id(self, user_id: str) -> str:
        statement = (
            select(AccountEntity.password)
            .where(AccountEntity.user_id == user_id)
        )
        result = await self._session.execute(statement)
        password = result.scalar_one_or_none()

        if not password:
            raise AccountNotFoundException()

        return password
    
    async def update_password_by_user_id(self, user_id: str, new_password: str) -> None:
        statement = (
            select(AccountEntity)
            .where(AccountEntity.user_id == user_id)
        )
        result = await self._session.execute(statement)
        account_entity = result.scalar_one_or_none()

        if not account_entity:
            raise AccountNotFoundException()

        account_entity.password = new_password
        await self._session.commit()