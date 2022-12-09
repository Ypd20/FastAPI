"""create users table

Revision ID: 0e4012ebd85a
Revises: 6aa088d654ab
Create Date: 2022-12-09 18:21:51.203532

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e4012ebd85a'
down_revision = '6aa088d654ab'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key = True, unique = True),
        sa.Column('name', sa.String(100), nullable = False),
        sa.Column('email', sa.String(30000), nullable = False, unique = True),
        sa.Column('password', sa.String(15), nullable = False, unique = True),
    )


def downgrade() -> None:
    pass
