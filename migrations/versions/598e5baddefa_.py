"""empty message

Revision ID: 598e5baddefa
Revises: 1e8376599437
Create Date: 2017-02-27 21:24:33.667171

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '598e5baddefa'
down_revision = '1e8376599437'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cards',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('artist', sa.String(length=80), nullable=True),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('year', sa.String(length=128), nullable=True),
    sa.Column('medium', sa.String(length=30), nullable=True),
    sa.Column('img', sa.String(length=30), nullable=False),
    sa.Column('starred', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cards')
    # ### end Alembic commands ###
