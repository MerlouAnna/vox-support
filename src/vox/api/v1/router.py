# here we define which routers are part of
# v1 w/o knowing in which URL this version lives
# here lives the aggregator api_router
# it "aggregates" all the individual route modules
# this way main is less complicated
# and doesn't need to know what's in the aggregator

from fastapi import APIRouter

from vox.api.v1.routes import health

api_router = APIRouter()
api_router.include_router(health.router)
