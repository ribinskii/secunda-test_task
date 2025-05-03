from abc import ABC, abstractmethod

from app.core.entities.estate.estate import Estate
from app.core.entities.operation.operation import Operation
from app.core.repositories.operation_repository.dto.add_operation_dto import AddOperationDto
from app.core.repositories.operation_repository.dto.update_enterprise_dto import UpdateOperationDto


class OperationRepository(ABC):
    @abstractmethod
    async def add(self, operation: AddOperationDto) -> Operation:
        ...

    @abstractmethod
    async def get_by_name(self, operation_name: str) -> Operation:
        ...

    @abstractmethod
    async def get_all(self) -> list[Operation]:
        ...

    @abstractmethod
    async def remove(self, operation_name: str) -> Operation:
        ...

    @abstractmethod
    async def update(self, operation_name: str, operation_data: UpdateOperationDto) -> Operation:
        ...