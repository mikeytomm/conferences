"""empty message

Revision ID: f8460af6c28d
Revises: 7acdd55c52dc
Create Date: 2022-04-07 03:16:32.526962

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8460af6c28d'
down_revision = '7acdd55c52dc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order_details', sa.Column('det_qty', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('order_details', 'det_qty')
    # ### end Alembic commands ###
