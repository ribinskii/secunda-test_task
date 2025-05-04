from app.core.entities.enterprise.enterprise import Enterprise
from app.infrastructure.db.entities.enterprise import Enterprises


class EnterpriseMapper:
    @staticmethod
    def to_domain(entity: Enterprises) -> Enterprise:
        return Enterprise(name=entity.name, phone=entity.phone, estate=entity.estate, operation=entity.operation)

    @staticmethod
    def to_entity(domain_model: Enterprise) -> Enterprises:
        return Enterprises(
            name=domain_model.name,
            phone=domain_model.phone,
            estate=domain_model.estate,
            operation=domain_model.operation,
        )
