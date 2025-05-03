import logging
from fastapi import FastAPI
from app.config import settings, setup_logging
from app.infrastructure.controllers.rest_api.middleware.mw_autorize import api_key_middleware
from app.infrastructure.controllers.rest_api.routers_bind import router_base
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

from app.infrastructure.controllers.rest_api.settings_swagger.autorize import setup_openapi

setup_logging(settings.LOG_LEVEL)
logger = logging.getLogger(__name__)

app = FastAPI(
    docs_url="/docs",
    title="line_provider",
    description="API provides information about events that ca be bet on", version="0.0.1")

app = setup_openapi(app)

app.middleware("http")(api_key_middleware)

app.include_router(router_base)
