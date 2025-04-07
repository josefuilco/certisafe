from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import selectinload
from sqlmodel import select
from uuid import uuid4
from ...models import User, Condition, Faculty
from ..entities import UserEntity
from ..exceptions import CreationConflictException, UserNotFoundException

class UserRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    # Private method to map UserEntity to User
    def _map_user_entity_to_user(self, user_entity: UserEntity) -> User:
        return User(
            id=user_entity.id,
            names=user_entity.names,
            surnames=user_entity.surnames,
            email=user_entity.email,
            cellphone=user_entity.cellphone,
            dni=user_entity.dni,
        )

    # Public methods
    async def create(self, user: User) -> User:
        try:
            user_entity = UserEntity(
                id=str(uuid4()),
                names=user.names,
                surnames=user.surnames,
                email=user.email,
                cellphone=user.cellphone,
                dni=user.dni,
                condition_id=user.condition.id,
                faculty_id=user.faculty.id,
            )
            self._session.add(user_entity)
            await self._session.commit()
            await self._session.refresh(user_entity)

            return self._map_user_entity_to_user(user_entity)
        except SQLAlchemyError:
            self._session.rollback()
            raise CreationConflictException('El usuario ya se encuentra registrado.')
    
    async def find_by_id(self, user_id: str) -> User:
        statement = (
            select(UserEntity)
            .where(UserEntity.id == user_id)
            .options(
                selectinload(UserEntity.condition),
                selectinload(UserEntity.faculty)
            )
        )
        result = await self._session.execute(statement)
        user_entity = result.scalar_one_or_none()

        if not user_entity:
            raise UserNotFoundException()
        
        user_found = self._map_user_entity_to_user(user_entity)
        user_found.condition = Condition(id=user_entity.condition_id, name=user_entity.condition.name)
        user_found.faculty = Faculty(id=user_entity.faculty_id, name=user_entity.faculty.name)

        return user_found
    
    async def find_id_by_dni(self, dni: str) -> str:
        statement = select(UserEntity.id).where(UserEntity.dni == dni)
        result = await self._session.execute(statement)
        user_id = result.scalar_one_or_none()

        if not user_id:
            raise UserNotFoundException()

        return user_id