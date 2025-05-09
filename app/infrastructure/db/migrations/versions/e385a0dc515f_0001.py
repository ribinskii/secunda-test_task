"""0001

Revision ID: e385a0dc515f
Revises:
Create Date: 2025-05-03 14:27:10.534368

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = "e385a0dc515f"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "estates",
        sa.Column("address", sa.String(), nullable=False),
        sa.Column("coordinates", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.PrimaryKeyConstraint("address"),
    )
    op.create_table(
        "operations",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("parent_name", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("name"),
    )
    op.create_table(
        "enterprises",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("phone", sa.String(), nullable=True),
        sa.Column("estate", sa.String(), nullable=True),
        sa.Column("operation", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(
            ["estate"],
            ["estates.address"],
        ),
        sa.ForeignKeyConstraint(
            ["operation"],
            ["operations.name"],
        ),
        sa.PrimaryKeyConstraint("name"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("enterprises")
    op.drop_table("operations")
    op.drop_table("estates")
    # ### end Alembic commands ###
