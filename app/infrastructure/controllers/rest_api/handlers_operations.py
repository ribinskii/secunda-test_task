# ruff: noqa: ANN201 B008  B904
import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.entities.operation.operation import Operation
from app.core.repositories.operation_repository.dto.add_operation_dto import AddOperationDto
from app.core.repositories.operation_repository.dto.update_enterprise_dto import UpdateOperationDto
from app.core.services.operation_service.operation_servise import OperationService
from app.infrastructure.db.repository.operation_repository import OperationRepositoryImpl
from app.infrastructure.db.session import get_db

logger = logging.getLogger(__name__)

router_operation = APIRouter()

@router_operation.post("/operation")
async def create_estate(operation: AddOperationDto, session: AsyncSession = Depends(get_db)) -> Operation:
    return await OperationService(OperationRepositoryImpl(session=session)).add(operation=operation)

@router_operation.get("/operation")
async def get_by_name(operation_name: str, session: AsyncSession = Depends(get_db)) -> Operation:
    return await OperationService(OperationRepositoryImpl(session=session)).get_by_name(operation_name=operation_name)

@router_operation.get("/operations")
async def get_all(session: AsyncSession = Depends(get_db)) -> list[Operation]:
    return await OperationService(OperationRepositoryImpl(session=session)).get_all()

@router_operation.delete("/operation")
async def remove(operation_name: str, session: AsyncSession = Depends(get_db)) -> Operation:
    return await OperationService(OperationRepositoryImpl(session=session)).remove(operation_name=operation_name)

@router_operation.patch("/operation/{operation_name}")
async def update(self, operation_name: str, operation_data: UpdateOperationDto, session: AsyncSession = Depends(get_db)) -> Operation:
    return await OperationService(OperationRepositoryImpl(session=session)).update(operation_name=operation_name, operation_data=operation_data)