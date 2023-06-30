"""add content column to posts table

Revision ID: 74d7b6b2aebc
Revises: ad607dcdd694
Create Date: 2023-06-29 20:24:44.680283

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "74d7b6b2aebc"
down_revision = "ad607dcdd694"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
