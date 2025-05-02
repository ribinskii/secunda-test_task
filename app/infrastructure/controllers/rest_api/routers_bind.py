from fastapi import APIRouter

from app.infrastructure.controllers.rest_api.handlers_enterprise import router_enterprise

router_base = APIRouter()

router_base.include_router(router_enterprise, prefix="/line_provider")