from pydantic import BaseModel

class AddOperationDto(BaseModel):
    name: str
    parent_name: str | None = None
