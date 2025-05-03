from pydantic import BaseModel


class UpdateOperationDto(BaseModel):
    parent_name: str | None = None
