from app.core.entities.estate.estate import Estate
from app.infrastructure.db.entaties.estate import Estates


class EstateMapper:
    @staticmethod
    def to_domain(entity: Estates) -> Estate:
        return Estate(address=entity.address, coordinates=entity.coordinates)

    @staticmethod
    def to_entity(domain_model: Estate) -> Estates:
        return Estates(address=domain_model.address, coordinates=domain_model.coordinates)
