"""replace_username_with_family_last_name_v2

Revision ID: 8cd92ba41378
Revises: 98c79d1523ef
Create Date: 2025-08-12 15:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '8cd92ba41378'
down_revision: Union[str, Sequence[str], None] = '98c79d1523ef'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Add new columns
    op.add_column('user', sa.Column('family_name', sa.String(), nullable=True))
    op.add_column('user', sa.Column('last_name', sa.String(), nullable=True))
    
    # Split existing full_name data into family_name and last_name
    connection = op.get_bind()
    
    # Get all users with full_name
    users = connection.execute(sa.text("SELECT id, full_name FROM \"user\" WHERE full_name IS NOT NULL AND full_name != ''"))
    
    for user in users:
        user_id, full_name = user
        
        if full_name and ' ' in full_name:
            # Split by space - first part becomes family_name, rest becomes last_name
            name_parts = full_name.strip().split(' ', 1)
            family_name = name_parts[0]
            last_name = name_parts[1] if len(name_parts) > 1 else ''
            
            # Update the user record
            connection.execute(
                sa.text("UPDATE \"user\" SET family_name = :family_name, last_name = :last_name WHERE id = :user_id"),
                {"family_name": family_name, "last_name": last_name, "user_id": user_id}
            )
        elif full_name:
            # If no space, put everything in family_name
            connection.execute(
                sa.text("UPDATE \"user\" SET family_name = :family_name WHERE id = :user_id"),
                {"family_name": full_name.strip(), "user_id": user_id}
            )
    
    # Drop the old columns
    op.drop_column('user', 'full_name')
    op.drop_column('user', 'username')
    
    # Drop the old index using raw SQL to avoid issues
    connection.execute(sa.text("DROP INDEX IF EXISTS ix_user_username"))


def downgrade() -> None:
    """Downgrade schema."""
    # Add back the old columns
    op.add_column('user', sa.Column('username', sa.String(), nullable=True))
    op.add_column('user', sa.Column('full_name', sa.String(), nullable=True))
    
    # Recreate the username index
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=False)
    
    # Combine family_name and last_name back to full_name
    connection = op.get_bind()
    
    # Get all users with family_name or last_name
    users = connection.execute(sa.text("SELECT id, family_name, last_name FROM \"user\""))
    
    for user in users:
        user_id, family_name, last_name = user
        
        if family_name and last_name:
            full_name = f"{family_name} {last_name}".strip()
        elif family_name:
            full_name = family_name
        elif last_name:
            full_name = last_name
        else:
            full_name = None
        
        if full_name:
            connection.execute(
                sa.text("UPDATE \"user\" SET full_name = :full_name WHERE id = :user_id"),
                {"full_name": full_name, "user_id": user_id}
            )
    
    # Drop the new columns
    op.drop_column('user', 'family_name')
    op.drop_column('user', 'last_name') 