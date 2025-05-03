from sqlalchemy import and_, func, or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.entities.enterprise.enterprise import Enterprise
from app.core.repositories.enterprise_repository.dto.add_enterprise_dto import AddEnterpriseDto
from app.core.repositories.enterprise_repository.dto.update_enterprise_dto import UpdateEnterpriseDto
from app.core.repositories.enterprise_repository.enterptise_repository import EnterpriseRepository
from app.infrastructure.db.entaties.enterprise import Enterprises
from app.infrastructure.db.entaties.estate import Estates
from app.infrastructure.db.entaties.operation import Operations
from app.infrastructure.db.mappers.enterprise_mapper import EnterpriseMapper


class EnterpriseRepositoryImpl(EnterpriseRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, dto: AddEnterpriseDto) -> Enterprise:
        new_enterprise = Enterprises(
            name=dto.name,
            phone=dto.phone,
            estate=dto.estate,
            operation=dto.operation,
        )
        self.session.add(new_enterprise)
        await self.session.commit()
        await self.session.refresh(new_enterprise)
        return EnterpriseMapper.to_domain(new_enterprise)

    async def get_by_name(self, name: str) -> Enterprise:
        query = select(Enterprises).filter(Enterprises.name == name)
        result = await self.session.execute(query)
        enterprise = result.scalars().first()
        return EnterpriseMapper.to_domain(enterprise)

    async def get_all(self) -> list[Enterprise]:
        query = select(Enterprises)
        result = await self.session.execute(query)
        enterprises = result.scalars().all()
        return [EnterpriseMapper.to_domain(event) for event in enterprises]

    async def update(self, name_enterprise: str, dto: UpdateEnterpriseDto) -> Enterprise:
        query = select(Enterprises).filter(Enterprises.name == name_enterprise)
        result = await self.session.execute(query)
        enterprise = result.scalars().first()
        update_data = dto.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            if field != "name":
                setattr(enterprise, field, value)

        self.session.add(enterprise)
        await self.session.commit()
        await self.session.refresh(enterprise)
        return EnterpriseMapper.to_domain(enterprise)

    async def remove(self, name_enterprise: str) -> Enterprise:
        result = await self.session.execute(select(Enterprises).filter(Enterprises.name == name_enterprise))
        enterprise = result.scalars().first()

        await self.session.delete(enterprise)
        await self.session.commit()
        return EnterpriseMapper.to_domain(enterprise)

    async def get_by_estate_name(self, estate_name: str) -> list[Enterprise]:
        query = select(Enterprises).filter(Enterprises.estate == estate_name)
        result = await self.session.execute(query)
        enterprises = result.scalars().all()
        return [EnterpriseMapper.to_domain(event) for event in enterprises]

    async def get_by_operation_name(self, operation_name: str) -> list[Enterprise]:
        query = select(Enterprises).filter(Enterprises.operation == operation_name)
        result = await self.session.execute(query)
        enterprises = result.scalars().all()
        return [EnterpriseMapper.to_domain(event) for event in enterprises]

    async def get_by_rectangle(
        self, extreme_left_diameter_point: tuple[float, float], extreme_right_diameter_point: tuple[float, float]
    ) -> list[Enterprise]:
        query = (
            select(Enterprises)
            .join(Estates)
            .where(
                and_(
                    Estates.coordinates.is_not(None),
                    func.jsonb_extract_path_text(Estates.coordinates, "longitude")
                    .cast(float)
                    .between(extreme_left_diameter_point[0], extreme_right_diameter_point[0]),
                    func.jsonb_extract_path_text(Estates.coordinates, "latitude")
                    .cast(float)
                    .between(extreme_left_diameter_point[1], extreme_right_diameter_point[1]),
                )
            )
        )

        result = await self.session.execute(query)
        enterprises = result.scalars().all()
        return [EnterpriseMapper.to_domain(enterprise) for enterprise in enterprises]

    async def get_by_nest_operations(self, operation_name: str) -> list[Enterprise]:
        subquery = select(Operations.name).where(
            or_(Operations.name == operation_name, Operations.parent_name == operation_name)
        )

        query = select(Enterprises).join(Operations).where(Enterprises.operation.in_(subquery))

        result = await self.session.execute(query)
        enterprises = result.scalars().all()

        return [EnterpriseMapper.to_domain(e) for e in enterprises]
