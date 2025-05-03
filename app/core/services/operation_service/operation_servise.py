from app.core.entities.operation.operation import Operation
from app.core.repositories.operation_repository.dto.add_operation_dto import AddOperationDto
from app.core.repositories.operation_repository.dto.update_enterprise_dto import UpdateOperationDto
from app.core.repositories.operation_repository.operation_repository import OperationRepository


class OperationService:
    def __init__(self, operation_repository: OperationRepository):
        self.operation_repository = operation_repository

    async def add(self, operation: AddOperationDto) -> Operation:
        return await self.operation_repository.add(operation=operation)

    async def get_by_name(self, operation_name: str) -> Operation:
        return await self.operation_repository.get_by_name(operation_name=operation_name)

    async def get_all(self) -> list[Operation]:
        return await self.operation_repository.get_all()

    async def remove(self, operation_name: str) -> Operation:
        return await self.operation_repository.remove(operation_name=operation_name)

    async def update(self, operation_name: str, operation_data: UpdateOperationDto) -> Operation:
        return await self.operation_repository.update(operation_name=operation_name, operation_data=operation_data)