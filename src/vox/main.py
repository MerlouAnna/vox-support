from importlib.metadata import version

from fastapi import FastAPI

from vox.api.v1.router import api_router
from vox.core.config import Settings, get_settings


# this is a "factory" function that creates and configures the FastAPI app instance
def create_app(settings: Settings | None = None) -> FastAPI:
    settings = settings or get_settings()
    app = FastAPI(
        title="Vox Support",
        description="Real time Vox Support agent",
        version=version("vox"),
        docs_url=None if settings.environment == "production" else "/docs",
    )
    # v1 is wired here w/o knowing the endpoints in it
    # this will pass all requests to the appropriate routers
    app.include_router(api_router, prefix="/api/v1")
    return app
