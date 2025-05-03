from fastapi import APIRouter

from app.infrastructure.controllers.rest_api.handlers_enterprise import router_enterprise
from app.infrastructure.controllers.rest_api.handlers_estate import router_estate
from app.infrastructure.controllers.rest_api.handlers_operations import router_operation

router_base = APIRouter()

router_base.include_router(router_enterprise, prefix="/enterprise")
router_base.include_router(router_estate, prefix="/estate")
router_base.include_router(router_operation, prefix="/operation")