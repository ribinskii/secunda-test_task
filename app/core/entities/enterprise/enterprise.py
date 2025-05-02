from pydantic import BaseModel

class Enterprise(BaseModel):
    name: str
    phone: str
    estate: str
    operation: str