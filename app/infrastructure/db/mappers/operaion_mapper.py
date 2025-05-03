from app.core.entities.operation.operation import Operation
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
