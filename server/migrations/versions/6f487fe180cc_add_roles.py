"""add roles

Revision ID: 6f487fe180cc
Revises: b4e503c14d7b
Create Date: 2025-04-03 12:35:50.791218

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from src.persistence.entities import RoleEntity

# revision identifiers, used by Alembic.
revision: str = '6f487fe180cc'
down_revision: Union[str, None] = 'b4e503c14d7b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

role_table = sa.table(
    'roles',
    sa.column('name', sa.String(25))
)

def upgrade() -> None:
    op.bulk_insert(
        role_table,
        [
           { 'name': 'Colaborador' },
           { 'name': 'Asistente' } 
        ]
    )

def downgrade() -> None:
    statement = sa.delete(role_table).where(
        role_table.c.name.in_(['colaborador', 'asistente'])
    )
    op.execute(statement)
