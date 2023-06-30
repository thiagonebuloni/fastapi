"""add last few columns to posts table

Revision ID: da26d2ffb805
Revises: 3437a57d4fc8
Create Date: 2023-06-30 06:47:59.746411

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "da26d2ffb805"
down_revision = "3437a57d4fc8"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "posts",
        sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"),
    )

    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("NOW()"),
        ),
    )
    pass


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
