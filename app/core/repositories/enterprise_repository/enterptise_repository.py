from abc import ABC, abstractmethod

from app.core.entities.enterprise.enterprise import Enterprise
from app.core.repositories.enterprise_repository.dto.add_enterprise_dto import AddEnterpriseDto
from app.core.repositories.enterprise_repository.dto.update_enterprise_dto import UpdateEnterpriseDto


class EnterpriseRepository(ABC):
    @abstractmethod
    async def add(self, dto: AddEnterpriseDto) -> Enterprise:
        ...

    @abstractmethod
    async def get_by_name(self, name: str) -> Enterprise:
        ...

    @abstractmethod
    async def get_all(self) -> list[Enterprise]:
        ...

    @abstractmethod
    async def update(self, name_enterprise: str, dto: UpdateEnterpriseDto) -> Enterprise:
        ...

    @abstractmethod
    async def remove(self, name_enterprise: str) -> Enterprise:
        ...

    @abstractmethod
    async def get_by_estate_name(self, estate_name: str) -> list[Enterprise]:
        ...

    @abstractmethod
    async def get_by_operation_name(self, operation_name: str) -> list[Enterprise]:
        ...

    @abstractmethod
    async def get_by_rectangle(self, extreme_left_diameter_point: str, extreme_right_diameter_point: str) -> list[Enterprise]:
        ...

    @abstractmethod
    async def get_by_nest_operations(self, operation_name: str) -> list[Enterprise]:
        ...