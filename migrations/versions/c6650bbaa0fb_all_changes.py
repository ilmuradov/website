"""all changes

Revision ID: c6650bbaa0fb
Revises: 6fd8a5cd817e
Create Date: 2022-02-24 18:56:35.175622

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c6650bbaa0fb'
down_revision = '6fd8a5cd817e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('body',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sec_title', sa.String(length=266), nullable=True),
    sa.Column('sec_body', sa.Text(), nullable=True),
    sa.Column('sec_timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_body_sec_timestamp'), 'body', ['sec_timestamp'], unique=False)
    op.create_table('footer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('third_title', sa.String(length=266), nullable=True),
    sa.Column('third_body', sa.Text(), nullable=True),
    sa.Column('third_timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_footer_third_timestamp'), 'footer', ['third_timestamp'], unique=False)
    op.create_table('head',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=266), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_head_timestamp'), 'head', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_head_timestamp'), table_name='head')
    op.drop_table('head')
    op.drop_index(op.f('ix_footer_third_timestamp'), table_name='footer')
    op.drop_table('footer')
    op.drop_index(op.f('ix_body_sec_timestamp'), table_name='body')
    op.drop_table('body')
    # ### end Alembic commands ###
