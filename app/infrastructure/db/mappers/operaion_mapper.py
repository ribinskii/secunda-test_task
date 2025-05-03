from app.core.entities.enterprise.enterprise import Enterprise
from app.core.entities.estate.estate import Estate
from app.core.entities.operation.operation import Operation
from app.infrastructure.db.entaties.estate import Estates
from app.infrastructure.db.entaties.operation import Operations


class OperationMapper:
    @staticmethod
    def to_domain(entity: Operations) -> Operation:
        return Operation(
            name=entity.name,
            parent_name=entity.parent_name,
            )


    @staticmethod
    def to_entity(domain_model: Operation) -> Operations:
        return Operations(
            name=domain_model.name,
            parent_name=domain_model.parent_name,
        )
