"""add roles

Revision ID: 600c49589f6b
Revises: f2e6df9c82e5
Create Date: 2025-03-31 00:57:29.768127

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from src.persistence.entities import RoleEntity


# revision identifiers, used by Alembic.
revision: str = '600c49589f6b'
down_revision: Union[str, None] = 'f2e6df9c82e5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.bulk_insert(
        RoleEntity.__table__,
        [
            { 'name': 'colaborador' },
            { 'name': 'asistente' },
        ]
    )


def downgrade() -> None:
    delete_statement = sa.delete(
        RoleEntity.__table__
    ).where(
        RoleEntity.__table__.c.name.in_(['colaborador', 'asistente'])
    )
    
    op.execute(delete_statement)
