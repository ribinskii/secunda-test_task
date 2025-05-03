from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.infrastructure.db.entaties.base import Base
from sqlalchemy.dialects.postgresql import JSONB
class Estates(Base):
    address: Mapped[str] = mapped_column(primary_key=True)
    coordinates: Mapped[dict | None] = mapped_column(JSONB, nullable=True)

    enterprises = relationship('Enterprises', back_populates='estates')
