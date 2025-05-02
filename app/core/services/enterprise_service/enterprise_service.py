from app.core.entities.enterprise.enterprise import Enterprise
from app.core.repositories.enterprise_repository.dto.add_enterprise_dto import AddEnterpriseDto
from app.core.repositories.enterprise_repository.enterptise_repository import EnterpriseRepository
from sqlalchemy.ext.asyncio import AsyncSession

class EnterpriseService:
    def __init__(self, enterprise_repository: EnterpriseRepository):
        self.enterprise_repository = enterprise_repository

    async def get_all(self, session: AsyncSession) -> list[Enterprise]:
        return await self.enterprise_repository.get_all(session=session)

    async def add(self, dto: AddEnterpriseDto, session: AsyncSession) -> Enterprise:
        return await self.enterprise_repository.add(dto=dto, session=session)

    async def get_by_name(self, name, session: AsyncSession) -> Enterprise:
        # доп бизнес логика
        return await self.enterprise_repository.get_by_name(name=name, session=session)

    async def get_by_estate_name(self, estate_name: str, session: AsyncSession) -> list[Enterprise]:
        return await self.enterprise_repository.get_by_estate_name(estate_name=estate_name, session=session)

    async def get_by_operation_name(self, operation_name: str, session: AsyncSession) -> list[Enterprise]:
        return await self.enterprise_repository.get_by_operation_name(operation_name=operation_name, session=session)

    async def get_by_rectangle(self, extreme_left_diameter_point: str, extreme_right_diameter_point: str, session: AsyncSession) -> list[Enterprise]:
        return await self.enterprise_repository.get_by_rectangle(extreme_left_diameter_point, extreme_right_diameter_point, session)

    async def get_by_nest_operations(self, operation_name: str, session: AsyncSession) -> list[Enterprise]:
        return await self.enterprise_repository.get_by_nest_operations(operation_name, session)


