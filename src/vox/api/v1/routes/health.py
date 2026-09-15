# here we just define that there is a health checkpoint - deosn;t matetr where we wire it

from typing import Literal

from fastapi import APIRouter  # the class allows to declare endpoint w/o app object
from pydantic import BaseModel

router = APIRouter(tags=["health"])


class HealthResponse(BaseModel):
    status: Literal["OK"]


@router.get("/health")
async def health() -> HealthResponse:
    """Health check endpoint"""
    return HealthResponse(status="OK")
