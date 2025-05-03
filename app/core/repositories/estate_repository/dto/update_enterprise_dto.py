from pydantic import BaseModel


class UpdateEstateDto(BaseModel):
    coordinates: str | None = None
