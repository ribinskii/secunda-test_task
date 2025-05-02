# ruff: noqa: ANN201 B008  B904
import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.entities.enterprise.enterprise import Enterprise
from app.core.repositories.enterprise_repository.dto.add_enterprise_dto import AddEnterpriseDto
from app.core.services.enterprise_service.enterprise_service import EnterpriseService
from app.infrastructure.db.repository.enterprise_repository import EnterpriseRepositoryImpl
from app.infrastructure.db.session import get_db

logger = logging.getLogger(__name__)

router_enterprise = APIRouter()

@router_enterprise.get("/enterprises")
async def get_enterprises(session: AsyncSession = Depends(get_db)):
    await EnterpriseService(EnterpriseRepositoryImpl()).get_all(session=session)

@router_enterprise.post("/enterprise")
async def create_enterprise(enterprise: AddEnterpriseDto = Depends(), session: AsyncSession = Depends(get_db)):
    await EnterpriseService(EnterpriseRepositoryImpl()).add(dto=enterprise, session=session)