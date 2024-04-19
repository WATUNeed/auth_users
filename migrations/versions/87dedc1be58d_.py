"""empty message

Revision ID: 87dedc1be58d
Revises: 
Create Date: 2024-04-17 22:30:48.813055

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '87dedc1be58d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    gender_model = op.create_table('gender_table',
    sa.Column('name', sa.String(length=1), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('deleted_at', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('name')
    )
    role_model = op.create_table('role_table',
    sa.Column('name', sa.String(length=8), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('deleted_at', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('name')
    )
    op.create_table('user_table',
    sa.Column('id', sa.UUID(), server_default=sa.text('gen_random_uuid()'), nullable=False),
    sa.Column('role', sa.String(length=8), nullable=False),
    sa.Column('gender', sa.String(length=1), nullable=True),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('phone', sa.String(length=15), nullable=False),
    sa.Column('tg_id', sa.BigInteger(), nullable=True),
    sa.Column('first_name', sa.String(length=32), nullable=True),
    sa.Column('surname', sa.String(length=32), nullable=True),
    sa.Column('patronymic', sa.String(length=32), nullable=True),
    sa.Column('birthdate', sa.Date(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('deleted_at', sa.TIMESTAMP(), nullable=True),
    sa.ForeignKeyConstraint(['gender'], ['gender_table.name'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['role'], ['role_table.name'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('phone'),
    sa.UniqueConstraint('tg_id')
    )

    op.bulk_insert(
        role_model,
        [{'name': 'CLIENT'}]
    )
    op.bulk_insert(gender_model, [{'name': 'M'}, {'name': 'F'}])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_table')
    op.drop_table('role_table')
    op.drop_table('gender_table')
    # ### end Alembic commands ###