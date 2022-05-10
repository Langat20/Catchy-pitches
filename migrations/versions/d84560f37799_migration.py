""" Migration

Revision ID: d84560f37799
Revises: 
Create Date: 2022-05-10 17:34:54.554563

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'd84560f37799'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comments', 'posted')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('posted', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###