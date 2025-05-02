from abc import ABC, abstractmethod

from app.core.entities.enterprise.enterprise import Enterprise
from app.core.repositories.enterprise_repository.dto.add_enterprise_dto import AddEnterpriseDto
from app.core.repositories.enterprise_repository.dto.enterprise_dto import EnterpriseDto
from app.core.repositories.enterprise_repository.dto.update_enterprise_dto import UpdateEnterpriseDto
from sqlalchemy.ext.asyncio import AsyncSession


class EnterpriseRepository(ABC):
    @abstractmethod
    async def add(self, dto: AddEnterpriseDto, session: AsyncSession) -> EnterpriseDto:
        ...

    @abstractmethod
    async def get_by_name(self, name: str, session: AsyncSession) -> EnterpriseDto:
        ...

    @abstractmethod
    async def get_all(self, session: AsyncSession) -> list[EnterpriseDto]:
        ...

    # @abstractmethod
    # async def update(self, dto: UpdateEnterpriseDto, session: AsyncSession) -> Enterprise:
    #     ...
    #
    # @abstractmethod
    # async def remove(self, name: str, session: AsyncSession) -> Enterprise:
    #     ...

    @abstractmethod
    async def get_by_estate_name(self, estate_name: str, session: AsyncSession) -> list[EnterpriseDto]:
        ...

    # @abstractmethod
    # async def get_by_operation_name(self, operation_name: str, session: AsyncSession) -> list[Enterprise]:
    #     ...
    #
    # @abstractmethod
    # async def get_by_rectangle(self, extreme_left_diameter_point: str, extreme_right_diameter_point: str, session: AsyncSession) -> list[Enterprise]:
    #     ...
    #
    # @abstractmethod
    # async def get_by_nest_operations(self, operation_name: str, session: AsyncSession) -> list[Enterprise]:
    #     ...