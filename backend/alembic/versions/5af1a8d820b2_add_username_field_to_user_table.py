"""add_username_field_to_user_table

Revision ID: 5af1a8d820b2
Revises: 8cd92ba41378
Create Date: 2025-08-12 15:33:09.027818

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5af1a8d820b2'
down_revision: Union[str, Sequence[str], None] = '8cd92ba41378'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Add username column to user table
    op.add_column('user', sa.Column('username', sa.String(), nullable=True))
    
    # Create unique index on username
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)


def downgrade() -> None:
    """Downgrade schema."""
    # Drop the username index
    op.drop_index(op.f('ix_user_username'), table_name='user')
    
    # Drop the username column
    op.drop_column('user', 'username')
