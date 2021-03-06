"""empty message

Revision ID: 21e1c7920c4d
Revises: c218d1e4fb52
Create Date: 2022-05-07 23:11:14.229630

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21e1c7920c4d'
down_revision = 'c218d1e4fb52'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('wishes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('puppies')
    op.add_column('owners', sa.Column('wish_id', sa.Integer(), nullable=True))
    op.drop_constraint(None, 'owners', type_='foreignkey')
    op.create_foreign_key(None, 'owners', 'wishes', ['wish_id'], ['id'])
    op.drop_column('owners', 'puppy_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('owners', sa.Column('puppy_id', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'owners', type_='foreignkey')
    op.create_foreign_key(None, 'owners', 'puppies', ['puppy_id'], ['id'])
    op.drop_column('owners', 'wish_id')
    op.create_table('puppies',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('wishes')
    # ### end Alembic commands ###
