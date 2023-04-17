"""alter db

Revision ID: db9e3d6db63c
Revises: deff2700efc6
Create Date: 2016-09-17 18:01:41.719985

"""

# revision identifiers, used by Alembic.
revision = 'db9e3d6db63c'
down_revision = 'deff2700efc6'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('resource_log')
    op.add_column('resource', sa.Column('modifydt', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('resource', 'modifydt')
    op.create_table('resource_log',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('resource_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('employee_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('comment', sa.VARCHAR(length=512), autoincrement=False, nullable=True),
    sa.Column('modifydt', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['employee_id'], [u'employee.id'], name=u'fk_employee_id_resource_log', onupdate=u'CASCADE', ondelete=u'CASCADE'),
    sa.ForeignKeyConstraint(['resource_id'], [u'resource.id'], name=u'fk_resource_id_resource_log', onupdate=u'CASCADE', ondelete=u'CASCADE'),
    sa.PrimaryKeyConstraint('id', name=u'resource_log_pkey')
    )
    ### end Alembic commands ###
