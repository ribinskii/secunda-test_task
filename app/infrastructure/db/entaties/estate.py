from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.db.entaties.base import Base

class Estates(Base):
    address: Mapped[str] = mapped_column(primary_key=True)
    coordinates: Mapped[str] = mapped_column(nullable=True)

    enterprises = relationship('Enterprises', back_populates='estates')
