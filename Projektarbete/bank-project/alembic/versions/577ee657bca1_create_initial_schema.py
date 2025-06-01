"""Create initial schema

Revision ID: 577ee657bca1
Revises: bc41a25497e1
Create Date: 2025-05-30 22:05:00.099929

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '577ee657bca1'
down_revision: Union[str, None] = 'bc41a25497e1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
