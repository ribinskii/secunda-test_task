from app.core.entities.operation.operation import Operation
from app.core.repositories.operation_repository.dto.add_operation_dto import AddOperationDto
from app.core.repositories.operation_repository.dto.update_enterprise_dto import UpdateOperationDto
from app.core.repositories.operation_repository.operation_repository import OperationRepository

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, func

from app.infrastructure.db.entaties.operation import Operations
from app.infrastructure.db.mappers.operaion_mapper import OperationMapper


class OperationRepositoryImpl(OperationRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, operation: AddOperationDto) -> Operation:
        new_estate = Operations(
            name=operation.name,
            parent_name=operation.parent_name,
        )
        self.session.add(new_estate)
        await self.session.commit()
        await self.session.refresh(new_estate)
        return OperationMapper.to_domain(new_estate)

    async def get_by_name(self, operation_name: str) -> Operation:
        query = select(Operations).filter(Operations.name == operation_name)
        result = await self.session.execute(query)
        estate = result.scalars().first()
        return OperationMapper.to_domain(estate)

    async def get_all(self) -> list[Operation]:
        query = select(Operations)
        result = await self.session.execute(query)
        estates = result.scalars().all()
        return list(map(OperationMapper.to_domain, estates))

    async def remove(self, operation_name: str) -> Operation:
        result = await self.session.execute(select(Operations).filter(Operations.name == operation_name))
        estate = result.scalars().first()

        await self.session.delete(estate)
        await self.session.commit()
        return OperationMapper.to_domain(estate)

    async def update(self, operation_name: str, operation_data: UpdateOperationDto) -> Operation:
        query = select(Operations).filter(Operations.name == operation_name)
        result = await self.session.execute(query)
        operations = result.scalars().first()
        update_data = operation_data.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            if field != "name":
                setattr(operations, field, value)

        self.session.add(operations)
        await self.session.commit()
        await self.session.refresh(operations)
        return OperationMapper.to_domain(operations)