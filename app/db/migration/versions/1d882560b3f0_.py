"""empty message

Revision ID: 1d882560b3f0
Revises: 757689fa0a26
Create Date: 2023-02-18 03:06:00.318572

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d882560b3f0'
down_revision = '757689fa0a26'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('project', sa.Column('status', sa.BOOLEAN(), nullable=False))
    op.create_unique_constraint(op.f('uq__project__id'), 'project', ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('uq__project__id'), 'project', type_='unique')
    op.drop_column('project', 'status')
    # ### end Alembic commands ###
