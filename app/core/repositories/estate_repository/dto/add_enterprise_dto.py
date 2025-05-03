from pydantic import BaseModel


class AddEstateDto(BaseModel):
    address: str
    coordinates: str | None = None
