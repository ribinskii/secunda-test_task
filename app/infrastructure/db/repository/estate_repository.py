from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.entities.estate.estate import Estate
from app.core.repositories.estate_repository.dto.add_enterprise_dto import AddEstateDto
from app.core.repositories.estate_repository.dto.update_enterprise_dto import UpdateEstateDto
from app.core.repositories.estate_repository.estate_repository import EstateRepository
from app.infrastructure.db.entaties.estate import Estates
from app.infrastructure.db.mappers.estate_mapper import EstateMapper


class EstateRepositoryImpl(EstateRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, estate: AddEstateDto) -> Estate:
        new_estate = Estates(
            address=estate.address,
            coordinates=estate.coordinates,
        )
        self.session.add(new_estate)
        await self.session.commit()
        await self.session.refresh(new_estate)
        return EstateMapper.to_domain(new_estate)

    async def get_by_name(self, estate_name: str) -> Estate:
        query = select(Estates).filter(Estates.address == estate_name)
        result = await self.session.execute(query)
        estate = result.scalars().first()
        return EstateMapper.to_domain(estate)

    async def get_all(self) -> list[Estate]:
        query = select(Estates)
        result = await self.session.execute(query)
        estates = result.scalars().all()
        return list(map(EstateMapper.to_domain, estates))

    async def remove(self, estate_name: str) -> Estate:
        result = await self.session.execute(select(Estates).filter(Estates.address == estate_name))
        estate = result.scalars().first()

        await self.session.delete(estate)
        await self.session.commit()
        return EstateMapper.to_domain(estate)

    async def update(self, estate_name: str, estate_data: UpdateEstateDto) -> Estate:
        query = select(Estates).filter(Estates.address == estate_name)
        result = await self.session.execute(query)
        estate = result.scalars().first()
        update_data = estate_data.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            if field != "name":
                setattr(estate, field, value)

        self.session.add(estate)
        await self.session.commit()
        await self.session.refresh(estate)
        return EstateMapper.to_domain(estate)
