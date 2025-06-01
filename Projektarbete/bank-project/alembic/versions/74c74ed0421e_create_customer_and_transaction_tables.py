"""create customer and transaction tables

Revision ID: 74c74ed0421e
Revises: 577ee657bca1
Create Date: 2025-05-30 22:34:38.880782

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '74c74ed0421e'
down_revision: Union[str, None] = '577ee657bca1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
