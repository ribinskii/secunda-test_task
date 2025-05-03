import logging

from fastapi import HTTPException, Request, status

from app.config import settings

logger = logging.getLogger(__name__)

PUBLIC_ROUTES = {
    "/docs",
    "/openapi.json",
    "/redoc",
    "/healthcheck",
    "/favicon.ico",
    "/static/swagger-ui.css",
    "/static/swagger-ui-bundle.js",
    "/static/swagger-ui-standalone-preset.js",
}


async def api_key_middleware(request: Request, call_next):
    if request.url.path in PUBLIC_ROUTES:
        return await call_next(request)

    api_key = request.headers.get(settings.API_KEY_NAME)

    if not api_key:
        logger.warning(f"Missing API key from {request.client.host}")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="API Key is missing")

    if api_key != settings.API_KEY:
        logger.warning(f"Invalid API key from {request.client.host}")
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid API Key")

    logger.debug(f"Valid API key from {request.client.host}")
    return await call_next(request)
