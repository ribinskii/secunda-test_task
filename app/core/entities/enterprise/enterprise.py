from pydantic import BaseModel

class Enterprise(BaseModel):
    name: str
    phone: str | None = None
    estate: str | None = None
    operation: str | None = None