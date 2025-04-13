"""add conditions

Revision ID: 53db116ff12c
Revises: 6f487fe180cc
Create Date: 2025-04-04 09:13:10.783467

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '53db116ff12c'
down_revision: Union[str, None] = '6f487fe180cc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

condition_table = sa.table(
    'conditions',
    sa.column('name', sa.String(25)),
)

def upgrade() -> None:
    op.bulk_insert(
        condition_table,
        [
            { 'name': 'Estudiante' },
            { 'name': 'Docente' },
            { 'name': 'Adminitrativo' },
        ]
    )


def downgrade() -> None:
    statement = sa.delete(condition_table).where(
        condition_table.c.name.in_(['estudiante', 'docente', 'adminitrativo'])
    )
    op.execute(statement)
