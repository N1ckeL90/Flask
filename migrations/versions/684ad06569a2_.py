"""empty message

Revision ID: 684ad06569a2
Revises: a4cfe4b30954
Create Date: 2023-03-10 19:25:49.666106

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '684ad06569a2'
down_revision = 'a4cfe4b30954'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), server_default='', nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tag')
    # ### end Alembic commands ###