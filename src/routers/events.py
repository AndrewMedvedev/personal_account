from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from ..constants import PATH_ENDPOINT
from ..controllers import EventControl

events = APIRouter(prefix=f"{PATH_ENDPOINT}events", tags=["events"])


@events.get("/get")
async def get(page: int = 1, limit: int = 10) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=await EventControl().get_events(page=page, limit=limit),
    )
