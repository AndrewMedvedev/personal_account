from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse

from src.classes import Visitors
from src.database.schemas.custom_response import CustomResponse

router_visitors = APIRouter(prefix="/api/v1/visitors", tags=["visitors"])


@router_visitors.post("/add/{event_id}")
async def add(
    event_id: int,
    request: Request,
) -> CustomResponse:
    token_access = request.cookies.get("access")
    token_refresh = request.cookies.get("refresh")
    return await Visitors().add(
        token_access=token_access,
        token_refresh=token_refresh,
        event_id=event_id,
    )


@router_visitors.get("/get")
async def get(
    request: Request,
) -> CustomResponse:
    token_access = request.cookies.get("access")
    token_refresh = request.cookies.get("refresh")
    return await Visitors().get(
        token_access=token_access,
        token_refresh=token_refresh,
    )


@router_visitors.get(
    "/make/qr/{unique_string}",
    response_model=None,
)
async def make_qr(
    unique_string: str,
) -> StreamingResponse:
    return await Visitors().make_qr(
        unique_string=unique_string,
    )


@router_visitors.delete("/delete/{event_id}")
async def delete(
    event_id: int,
    request: Request,
) -> CustomResponse:
    token_access = request.cookies.get("access")
    token_refresh = request.cookies.get("refresh")
    return await Visitors().delete(
        token_access=token_access,
        token_refresh=token_refresh,
        event_id=event_id,
    )
