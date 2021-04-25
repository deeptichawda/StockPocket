"""Trial 2

Revision ID: c5d66fda174a
Revises: 
Create Date: 2021-04-23 02:59:01.581839

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5d66fda174a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mobile', sa.String(), nullable=True),
    sa.Column('passwordHash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_mobile'), 'users', ['mobile'], unique=True)
    op.create_table('portfolio',
    sa.Column('mobile', sa.String(), nullable=False),
    sa.Column('sticker', sa.String(length=10), nullable=False),
    sa.ForeignKeyConstraint(['mobile'], ['users.mobile'], ),
    sa.PrimaryKeyConstraint('mobile', 'sticker')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('portfolio')
    op.drop_index(op.f('ix_users_mobile'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###