# ruff: noqa: ANN201 B008  B904
import logging

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.entities.estate.estate import Estate
from app.core.repositories.estate_repository.dto.add_enterprise_dto import AddEstateDto
from app.core.repositories.estate_repository.dto.update_enterprise_dto import UpdateEstateDto
from app.core.services.estate_service.estate_servise import EstateService
from app.infrastructure.db.repository.estate_repository import EstateRepositoryImpl
from app.infrastructure.db.session import get_db


logger = logging.getLogger(__name__)

router_estate = APIRouter()


@router_estate.post("", description="Добавляет адресс")
async def create_estate(estate: AddEstateDto = Depends(), session: AsyncSession = Depends(get_db)) -> Estate:
    return await EstateService(EstateRepositoryImpl(session=session)).add(estate=estate)


@router_estate.get("", description="Получает данные адресса по имени")
async def get_estate_by_name(estate_name: str, session: AsyncSession = Depends(get_db)) -> Estate:
    return await EstateService(EstateRepositoryImpl(session=session)).get_by_name(estate_name)


@router_estate.get("/estates", description="Получает все адресса")
async def get_all_estates(session: AsyncSession = Depends(get_db)) -> list[Estate]:
    return await EstateService(EstateRepositoryImpl(session=session)).get_all()


@router_estate.delete("", description="Удаляет адресс")
async def remove_estate(estate_name: str, session: AsyncSession = Depends(get_db)) -> Estate:
    return await EstateService(EstateRepositoryImpl(session=session)).remove(estate_name=estate_name)


@router_estate.patch("", description="Изменяет данные адресса")
async def update_estate(
    estate_name: str, estate_data: UpdateEstateDto = Depends(), session: AsyncSession = Depends(get_db)
) -> Estate:
    return await EstateService(EstateRepositoryImpl(session=session)).update(
        estate_name=estate_name, estate_data=estate_data
    )
