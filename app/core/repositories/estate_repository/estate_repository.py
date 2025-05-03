from abc import ABC, abstractmethod

from app.core.entities.estate.estate import Estate
from app.core.repositories.estate_repository.dto.add_enterprise_dto import AddEstateDto
from app.core.repositories.estate_repository.dto.update_enterprise_dto import UpdateEstateDto


class EstateRepository(ABC):
    @abstractmethod
    async def add(
        self,
        estate: AddEstateDto,
    ) -> Estate: ...

    @abstractmethod
    async def get_by_name(self, estate_name: str) -> Estate: ...

    @abstractmethod
    async def get_all(self) -> list[Estate]: ...

    @abstractmethod
    async def remove(self, estate_name: str) -> Estate: ...

    @abstractmethod
    async def update(self, estate_name: str, estate_data: UpdateEstateDto) -> Estate: ...
