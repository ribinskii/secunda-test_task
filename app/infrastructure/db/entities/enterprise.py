from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.db.entities.base import Base


class Enterprises(Base):
    name: Mapped[str] = mapped_column(primary_key=True)
    phone: Mapped[str | None] = mapped_column(nullable=True)
    estate: Mapped[str | None] = mapped_column(ForeignKey("estates.address"), nullable=True)
    operation: Mapped[str | None] = mapped_column(ForeignKey("operations.name"), nullable=True)

    estates = relationship("Estates", back_populates="enterprises")
    operations = relationship("Operations", back_populates="enterprises")
