"""Add model Chef with relationship to Recipe

Revision ID: 73f74cf34d01
Revises: 084f8f586abb
Create Date: 2024-07-17 13:39:54.044433

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '73f74cf34d01'
down_revision: Union[str, None] = '084f8f586abb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
