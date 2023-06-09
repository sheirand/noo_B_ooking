"""trying to fix string lenght

Revision ID: aba7fd2ebc69
Revises: 06c1a873daf5
Create Date: 2023-05-14 12:10:44.256800

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aba7fd2ebc69'
down_revision = '06c1a873daf5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_property_city', table_name='property')
    op.drop_index('ix_property_country', table_name='property')
    op.drop_column('property', 'title')
    op.drop_column('property', 'city')
    op.drop_column('property', 'country')
    op.drop_index('ix_user_email', table_name='user')
    op.drop_column('user', 'email')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.create_index('ix_user_email', 'user', ['email'], unique=False)
    op.add_column('property', sa.Column('country', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('property', sa.Column('city', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('property', sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.create_index('ix_property_country', 'property', ['country'], unique=False)
    op.create_index('ix_property_city', 'property', ['city'], unique=False)
    # ### end Alembic commands ###
