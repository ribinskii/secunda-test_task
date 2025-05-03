from pydantic import BaseModel


class Estate(BaseModel):
    address: str
    coordinates: dict | None = None
