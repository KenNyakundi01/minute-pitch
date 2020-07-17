"""Added column upvotes adn downvotes to relation pitches

Revision ID: c4f4e20e4fee
Revises: f389975736cb
Create Date: 2020-07-13 16:04:20.142612

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4f4e20e4fee'
down_revision = 'f389975736cb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitch', sa.Column('downvotes', sa.Integer(), nullable=True))
    op.add_column('pitch', sa.Column('upvotes', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitch', 'upvotes')
    op.drop_column('pitch', 'downvotes')
    # ### end Alembic commands ###
