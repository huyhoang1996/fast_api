"""baseline

Revision ID: ff4d26dc6d06
Revises: 
Create Date: 2021-04-14 16:33:54.704212

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff4d26dc6d06'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('hashed_password', sa.String()),
        sa.Column('is_active', sa.String()),
        sa.Column('when', sa.DateTime(), default=sa.func.now()))


def downgrade():
    op.drop_table('user')
