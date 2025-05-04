from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.db.entities.base import Base


class Operations(Base):
    name: Mapped[str] = mapped_column(primary_key=True)
    parent_name: Mapped[str | None] = mapped_column(nullable=True)  # по хорошему нужно поставить внешний ключ

    enterprises = relationship("Enterprises", back_populates="operations")
