import asyncio
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config import settings, setup_logging
from app.infrastructure.controllers.rest_api.routers_bind import router_base

setup_logging(settings.LOG_LEVEL)
logger = logging.getLogger(__name__)


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     print("Lifespan_запущен")
#     task = asyncio.create_task(events_producer())
#     yield
#     task.cancel()
#     await engine.dispose()
#     try:
#         await task
#     except asyncio.CancelledError:
#         print("Фоновая задача остановлена")


app = FastAPI(
    # lifespan=lifespan,
    title="line_provider",
    description="API provides information about events that ca be bet on", version="0.0.1")

app.include_router(router_base)
