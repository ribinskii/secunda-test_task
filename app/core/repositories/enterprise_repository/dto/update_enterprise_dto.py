from pydantic import BaseModel

class UpdateEnterpriseDto(BaseModel):
    phone: str | None = None
    estate: str | None = None
    operation: str | None = None