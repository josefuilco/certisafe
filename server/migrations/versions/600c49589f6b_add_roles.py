"""add roles

Revision ID: 600c49589f6b
Revises: f2e6df9c82e5
Create Date: 2025-03-31 00:57:29.768127

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '600c49589f6b'
down_revision: Union[str, None] = 'f2e6df9c82e5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
