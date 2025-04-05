from fastapi import APIRouter

from src.classes import Events
from src.responses import CustomResponse

router_events = APIRouter(prefix="/api/v1/events", tags=["events"])


@router_events.get("/get")
async def get(
    page: int = 1,
    limit: int = 10,
) -> CustomResponse:
    return await Events().get_events(
        page=page,
        limit=limit,
    )
