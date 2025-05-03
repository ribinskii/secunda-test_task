from pydantic import BaseModel


class Estate(BaseModel):
    address: str
    coordinates: str | None = None
