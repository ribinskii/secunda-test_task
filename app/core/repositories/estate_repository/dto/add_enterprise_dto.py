from pydantic import BaseModel


class AddEstateDto(BaseModel):
    address: str
    coordinates: dict | None = None
