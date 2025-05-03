from fastapi.openapi.utils import get_openapi
from app.config import settings
from fastapi import FastAPI


def setup_openapi(app: FastAPI):
    def custom_openapi():
        if app.openapi_schema:
            return app.openapi_schema

        openapi_schema = get_openapi(
            title=app.title,
            version=app.version,
            description=app.description,
            routes=app.routes,
        )

        openapi_schema["components"] = {
            "securitySchemes": {
                "APIKeyHeader": {
                    "type": "apiKey",
                    "name": settings.API_KEY_NAME,
                    "in": "header"
                }
            }
        }

        openapi_schema["security"] = [{"APIKeyHeader": []}]

        app.openapi_schema = openapi_schema
        return app.openapi_schema

    app.openapi = custom_openapi
    return app