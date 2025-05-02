from app.core.entities.enterprise.enterprise import Enterprise
from app.core.repositories.enterprise_repository.dto.enterprise_dto import EnterpriseDto
from app.infrastructure.db.entaties.enterprise import Enterprises


class EnterpriseMapper:
    @staticmethod
    def to_dto(entity: Enterprises) -> EnterpriseDto:
        return EnterpriseDto(
            name=entity.name,
            phone=entity.phone,
            estate=entity.estate,
            operation=entity.operation
            )


    @staticmethod
    def to_entity(domain_model: Enterprise) -> Enterprises:
        return Enterprises(
            name=domain_model.name,
            phone=domain_model.phone,
            estate=domain_model.estate,
            operation=domain_model.operation
        )
