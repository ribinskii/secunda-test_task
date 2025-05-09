# ruff: noqa: ANN201 B008  B904
import logging

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.entities.enterprise.enterprise import Enterprise
from app.core.repositories.enterprise_repository.dto.add_enterprise_dto import AddEnterpriseDto
from app.core.repositories.enterprise_repository.dto.update_enterprise_dto import UpdateEnterpriseDto
from app.core.services.enterprise_service.enterprise_service import EnterpriseService
from app.infrastructure.db.repository.enterprise_repository import EnterpriseRepositoryImpl
from app.infrastructure.db.session import get_db


logger = logging.getLogger(__name__)

router_enterprise = APIRouter()


@router_enterprise.post("", description="Добавляет организиацию")
async def create_enterprise(
    enterprise: AddEnterpriseDto = Depends(), session: AsyncSession = Depends(get_db)
) -> Enterprise:
    return await EnterpriseService(EnterpriseRepositoryImpl(session=session)).add(dto=enterprise)


@router_enterprise.get("", description="Получает организацию по имени")
async def get_enterprise(enterprise_name: str, session: AsyncSession = Depends(get_db)) -> Enterprise:
    return await EnterpriseService(EnterpriseRepositoryImpl(session=session)).get_by_name(name=enterprise_name)


@router_enterprise.get("/enterprises", description="Получает все организации")
async def get_enterprises(session: AsyncSession = Depends(get_db)) -> list[Enterprise]:
    return await EnterpriseService(EnterpriseRepositoryImpl(session=session)).get_all()


@router_enterprise.patch("", description="Изменяет данные организации")
async def patch_enterprise(
    name_enterprise: str, update_model: UpdateEnterpriseDto = Depends(), session: AsyncSession = Depends(get_db)
) -> Enterprise:
    return await EnterpriseService(EnterpriseRepositoryImpl(session=session)).update(
        name_enterprise=name_enterprise, dto=update_model
    )


@router_enterprise.delete("", description="Удаляет организацию")
async def delete_enterprise(name_enterprise: str, session: AsyncSession = Depends(get_db)) -> Enterprise:
    return await EnterpriseService(EnterpriseRepositoryImpl(session=session)).remove(name_enterprise=name_enterprise)


@router_enterprise.get("/enterprise_by_estate", description="Получает организацию по адресу")
async def get_by_estate_name(estate_name: str, session: AsyncSession = Depends(get_db)) -> list[Enterprise]:
    return await EnterpriseService(EnterpriseRepositoryImpl(session=session)).get_by_estate_name(
        estate_name=estate_name
    )


@router_enterprise.get(
    "/enterprise_by_operation",
    description="Получает организации по виду деятельности",
)
async def get_by_operation_name(operation_name: str, session: AsyncSession = Depends(get_db)) -> list[Enterprise]:
    return await EnterpriseService(EnterpriseRepositoryImpl(session=session)).get_by_operation_name(
        operation_name=operation_name
    )


@router_enterprise.get("/enterprise_by_rectangle", description="Получает оргинизации в прямоугольной области")
async def get_by_rectangle(
    extreme_left_diameter_point: str, extreme_right_diameter_point: str, session: AsyncSession = Depends(get_db)
) -> list[Enterprise]:
    return await EnterpriseService(EnterpriseRepositoryImpl(session=session)).get_by_rectangle(
        extreme_left_diameter_point=extreme_left_diameter_point,
        extreme_right_diameter_point=extreme_right_diameter_point,
    )


@router_enterprise.get(
    "/enterprise_by_nest_operations",
    description="Палучает организации по всем вложенным видам деятельности",
)
async def get_by_nest_operations(operation_name: str, session: AsyncSession = Depends(get_db)) -> list[Enterprise]:
    return await EnterpriseService(EnterpriseRepositoryImpl(session=session)).get_by_nest_operations(
        operation_name=operation_name
    )
