from pydantic import BaseModel


class Operation(BaseModel):
    name: str
    parent_name: str | None = None
