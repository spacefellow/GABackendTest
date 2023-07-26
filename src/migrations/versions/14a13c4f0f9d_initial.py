"""initial

Revision ID: 14a13c4f0f9d
Revises: 
Create Date: 2023-07-25 17:55:47.105396

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14a13c4f0f9d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('missions',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rockets',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('cost', sa.Integer(), nullable=True),
    sa.Column('description', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('launches',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('details', sa.TEXT(), nullable=True),
    sa.Column('mission_id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['mission_id'], ['missions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('launches')
    op.drop_table('rockets')
    op.drop_table('missions')
    # ### end Alembic commands ###
