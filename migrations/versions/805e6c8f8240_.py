"""empty message

Revision ID: 805e6c8f8240
Revises: 8b348cb5fa6c
Create Date: 2022-12-18 22:15:30.981561

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '805e6c8f8240'
down_revision = '8b348cb5fa6c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('gender', sa.String(length=20), nullable=False),
    sa.Column('mass', sa.String(length=250), nullable=False),
    sa.Column('height', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('population', sa.String(length=250), nullable=False),
    sa.Column('terrain', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favourites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('characters_id', sa.Integer(), nullable=False),
    sa.Column('planets_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['characters_id'], ['characters.id'], ),
    sa.ForeignKeyConstraint(['planets_id'], ['planets.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('user', sa.Column('name', sa.String(length=250), nullable=False))
    op.drop_index('email', table_name='user')
    op.drop_index('email_2', table_name='user')
    op.drop_column('user', 'is_active')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_active', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False))
    op.create_index('email_2', 'user', ['email'], unique=False)
    op.create_index('email', 'user', ['email'], unique=False)
    op.drop_column('user', 'name')
    op.drop_table('favourites')
    op.drop_table('planets')
    op.drop_table('characters')
    # ### end Alembic commands ###
