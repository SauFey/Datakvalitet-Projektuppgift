"""create tables

Revision ID: 9ddb769b241e
Revises: 679bd87d2bb4
Create Date: 2025-05-30 15:49:32.405045

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9ddb769b241e'
down_revision: Union[str, None] = '679bd87d2bb4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
