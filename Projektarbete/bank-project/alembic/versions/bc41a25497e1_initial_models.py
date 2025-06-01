"""Initial models

Revision ID: bc41a25497e1
Revises: 9ddb769b241e
Create Date: 2025-05-30 21:37:06.063623

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bc41a25497e1'
down_revision: Union[str, None] = '9ddb769b241e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
