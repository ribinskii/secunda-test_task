from app.core.entities.enterprise.enterprise import Enterprise
from app.core.repositories.enterprise_repository.dto.add_enterprise_dto import AddEnterpriseDto
from app.core.repositories.enterprise_repository.dto.enterprise_dto import EnterpriseDto
from app.core.repositories.enterprise_repository.dto.update_enterprise_dto import UpdateEnterpriseDto
from app.core.repositories.enterprise_repository.enterptise_repository import EnterpriseRepository
from app.infrastructure.db.entaties.enterprise import Enterprises
from app.infrastructure.db.mappers.enterprise_mapper import EnterpriseMapper
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update

class EnterpriseRepositoryImpl(EnterpriseRepository):
    async def add(self, dto: AddEnterpriseDto, session: AsyncSession) -> EnterpriseDto:
        new_enterprise = Enterprises(
            name=dto.name,
            phone=dto.phone,
            estate=dto.estate,
            operation=dto.operation,
        )
        session.add(new_enterprise)
        await session.commit()
        await session.refresh(new_enterprise)
        return EnterpriseMapper.to_dto(new_enterprise)

    async def get_by_name(self, name: str, session: AsyncSession) ->EnterpriseDto:
        query = select(Enterprises).filter(Enterprises.name == name)
        result = await session.execute(query)
        events = result.scalars().first()
        return EnterpriseMapper.to_dto(events)

    async def get_all(self, session: AsyncSession) -> list[EnterpriseDto]:
        query = select(Enterprises)
        result = await session.execute(query)
        events = result.scalars().all()
        return [EnterpriseMapper.to_dto(event) for event in events]

    # async def update(self, dto: UpdateEnterpriseDto, session: AsyncSession) -> Enterprise:

    async def get_by_estate_name(self, estate_name: str, session: AsyncSession) -> list[EnterpriseDto]:
        query = (
            select(Enterprises)
            .filter(Enterprises.estate == estate_name)
        )
        result = await session.execute(query)
        events = result.scalars().all()
        return [EnterpriseMapper.to_dto(event) for event in events]


