"""create blogs table

Revision ID: 6aa088d654ab
Revises: 
Create Date: 2022-12-09 10:48:26.243258

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6aa088d654ab'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
     op.create_table(
        'blogs',
        sa.Column('id', sa.Integer, primary_key=True, unique=True),
        sa.Column('title', sa.String(100), nullable=False),
        sa.Column('body', sa.String(30000), nullable=False),
    )


def downgrade() -> None:
    pass
