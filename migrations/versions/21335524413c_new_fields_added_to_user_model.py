"""new fields added to User model

Revision ID: 21335524413c
Revises: 6903725a74ba
Create Date: 2020-01-06 23:46:00.487486

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21335524413c'
down_revision = '6903725a74ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
