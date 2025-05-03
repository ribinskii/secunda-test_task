from pydantic import BaseModel


class UpdateEstateDto(BaseModel):
    coordinates: dict | None = None
