from app.core.entities.enterprise.enterprise import Enterprise
from app.core.repositories.enterprise_repository.dto.add_enterprise_dto import AddEnterpriseDto
from app.core.repositories.enterprise_repository.dto.update_enterprise_dto import UpdateEnterpriseDto
from app.core.repositories.enterprise_repository.enterptise_repository import EnterpriseRepository


class EnterpriseService:
    def __init__(self, enterprise_repository: EnterpriseRepository):
        self.enterprise_repository = enterprise_repository

    async def add(self, dto: AddEnterpriseDto) -> Enterprise:
        return await self.enterprise_repository.add(
            dto=dto,
        )

    async def get_by_name(self, name) -> Enterprise:
        return await self.enterprise_repository.get_by_name(
            name=name,
        )

    async def get_all(self) -> list[Enterprise]:
        return await self.enterprise_repository.get_all()

    async def update(self, name_enterprise: str, dto: UpdateEnterpriseDto) -> Enterprise:
        return await self.enterprise_repository.update(
            name_enterprise=name_enterprise,
            dto=dto,
        )

    async def remove(self, name_enterprise: str) -> Enterprise:
        return await self.enterprise_repository.remove(
            name_enterprise=name_enterprise,
        )

    async def get_by_estate_name(self, estate_name: str) -> list[Enterprise]:
        return await self.enterprise_repository.get_by_estate_name(
            estate_name=estate_name,
        )

    async def get_by_operation_name(self, operation_name: str) -> list[Enterprise]:
        return await self.enterprise_repository.get_by_operation_name(
            operation_name=operation_name,
        )

    async def get_by_rectangle(
        self, extreme_left_diameter_point: str, extreme_right_diameter_point: str
    ) -> list[Enterprise]:
        return await self.enterprise_repository.get_by_rectangle(
            extreme_left_diameter_point, extreme_right_diameter_point
        )

    async def get_by_nest_operations(self, operation_name: str) -> list[Enterprise]:
        return await self.enterprise_repository.get_by_nest_operations(operation_name)
