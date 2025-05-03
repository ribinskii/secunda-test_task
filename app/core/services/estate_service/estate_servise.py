from app.core.entities.estate.estate import Estate
from app.core.repositories.estate_repository.dto.add_enterprise_dto import AddEstateDto
from app.core.repositories.estate_repository.dto.update_enterprise_dto import UpdateEstateDto
from app.core.repositories.estate_repository.estate_repository import EstateRepository


class EstateService:
    def __init__(self, estate_repository: EstateRepository):
        self.estate_repository = estate_repository

    async def add(self, estate: AddEstateDto) -> Estate:
        return await self.estate_repository.add(estate=estate)

    async def get_by_name(self, estate_name: str) -> Estate:
        return await self.estate_repository.get_by_name(estate_name=estate_name)

    async def get_all(self) -> list[Estate]:
        return await self.estate_repository.get_all()

    async def remove(self, estate_name: str) -> Estate:
        return await self.estate_repository.remove(estate_name=estate_name)

    async def update(self, estate_name: str, estate_data: UpdateEstateDto) -> Estate:
        return await self.estate_repository.update(estate_name=estate_name, estate_data=estate_data)