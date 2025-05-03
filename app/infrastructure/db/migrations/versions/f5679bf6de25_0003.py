"""0003

Revision ID: f5679bf6de25
Revises: 17f6b9cb88e2
Create Date: 2025-05-03 19:24:53.160323

"""

from collections.abc import Sequence

from alembic import op
from sqlalchemy.sql import text


revision: str = "f5679bf6de25"
down_revision: str | None = "17f6b9cb88e2"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.execute(
        text("""
        INSERT INTO operations (name, parent_name) VALUES
        ('manufacturing', NULL),
        ('production', 'manufacturing'),
        ('assembly', 'production'),
        ('logistics', NULL),
        ('shipping', 'logistics'),
        ('warehousing', 'logistics'),
        ('retail', NULL);
    """)
    )

    op.execute(
        text("""
        INSERT INTO estates (address, coordinates) VALUES
        ('123 Main St', '{"lat": 40.7128, "lng": -74.0060}'),
        ('456 Oak Ave', '{"lat": 34.0522, "lng": -118.2437}'),
        ('789 Pine Rd', '{"lat": 41.8781, "lng": -87.6298}'),
        ('101 Elm Blvd', NULL),
        ('202 Maple Ln', '{"lat": 39.9526, "lng": -75.1652}');
    """)
    )

    op.execute(
        text("""
        INSERT INTO enterprises (name, phone, estate, operation) VALUES
        ('TechCorp', '+1234567890', '123 Main St', 'manufacturing'),
        ('LogiSolutions', '+1987654321', '456 Oak Ave', 'shipping'),
        ('RetailHub', '+1122334455', '789 Pine Rd', 'retail'),
        ('FactoryPlus', '+5566778899', '101 Elm Blvd', 'assembly'),
        ('StorageMaster', '+4433221100', '202 Maple Ln', 'warehousing'),
        ('QuickDeliver', '+7788990011', NULL, 'logistics'),
        ('CityRetail', '+9900112233', NULL, 'retail');
    """)
    )


def downgrade() -> None:
    op.execute(text("DELETE FROM enterprises;"))
    op.execute(text("DELETE FROM estates;"))
    op.execute(text("DELETE FROM operations;"))
