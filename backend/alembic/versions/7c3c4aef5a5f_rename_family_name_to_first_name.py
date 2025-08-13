"""rename_family_name_to_first_name

Revision ID: 7c3c4aef5a5f
Revises: 5af1a8d820b2
Create Date: 2025-08-13 18:03:58.457818

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7c3c4aef5a5f'
down_revision: Union[str, Sequence[str], None] = '5af1a8d820b2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Rename the column from family_name to first_name
    # This preserves all the data in the column
    op.alter_column('user', 'family_name', new_column_name='first_name')
    
    # Rename the index if it exists
    connection = op.get_bind()
    connection.execute(sa.text("ALTER INDEX IF EXISTS ix_user_family_name RENAME TO ix_user_first_name"))


def downgrade() -> None:
    """Downgrade schema."""
    # Rename the column back from first_name to family_name
    # This preserves all the data in the column
    op.alter_column('user', 'first_name', new_column_name='family_name')
    
    # Rename the index back if it exists
    connection = op.get_bind()
    connection.execute(sa.text("ALTER INDEX IF EXISTS ix_user_first_name RENAME TO ix_user_family_name"))
