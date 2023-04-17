"""alter db

Revision ID: d6bfdd337869
Revises: dccf36ae49e4
Create Date: 2016-08-15 20:52:59.996814

"""

# revision identifiers, used by Alembic.
revision = 'd6bfdd337869'
down_revision = 'dccf36ae49e4'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('mail', sa.Column('descr', sa.String(length=255), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('mail', 'descr')
    ### end Alembic commands ###
