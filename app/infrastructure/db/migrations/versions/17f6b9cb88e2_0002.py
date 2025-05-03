"""0002

Revision ID: 17f6b9cb88e2
Revises: e385a0dc515f
Create Date: 2025-05-03 14:27:33.366781

"""
from collections.abc import Sequence

from alembic import op
from sqlalchemy.sql import text

# revision identifiers, used by Alembic.
revision: str = "17f6b9cb88e2"
down_revision: str | None = "e385a0dc515f"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute(text("""
    CREATE OR REPLACE FUNCTION check_operation_depth() RETURNS TRIGGER AS $$
    DECLARE
        depth INTEGER;
    BEGIN
        IF NEW.parent_name IS NULL THEN
            RETURN NEW;
        END IF;
        
        WITH RECURSIVE operation_hierarchy AS (
            SELECT name, parent_name, 1 AS level
            FROM operations
            WHERE name = NEW.parent_name
            
            UNION ALL
            
            SELECT o.name, o.parent_name, h.level + 1
            FROM operations o
            JOIN operation_hierarchy h ON o.name = h.parent_name
            WHERE h.level < 3
        )
        SELECT MAX(level) INTO depth FROM operation_hierarchy;
        
        IF depth >= 3 THEN
            RAISE EXCEPTION 'Operation hierarchy depth cannot exceed 3 levels';
        END IF;
        
        RETURN NEW;
    END;
    $$ LANGUAGE plpgsql;
    """))

    op.execute(text("""
    CREATE TRIGGER validate_operation_depth
    BEFORE INSERT OR UPDATE ON operations
    FOR EACH ROW EXECUTE FUNCTION check_operation_depth();
    """))


def downgrade() -> None:
    """Downgrade schema."""
    op.execute(text("DROP TRIGGER IF EXISTS validate_operation_depth ON operations;"))
    op.execute(text("DROP FUNCTION IF EXISTS check_operation_depth();"))