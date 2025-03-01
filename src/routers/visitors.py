from fastapi import APIRouter, Request, Response, status
from fastapi.responses import JSONResponse, StreamingResponse

from src.classes import Visitors

router_visitors = APIRouter(prefix="/api/v1/visitors", tags=["visitors"])


@router_visitors.post("/add/{event_id}")
async def add(
    event_id: int,
    request: Request,
    response: Response,
) -> JSONResponse:
    try:
        access = request.cookies.get("access")
        refresh = request.cookies.get("refresh")
        return await Visitors(
            token_access=access,
            token_refresh=refresh,
            event_id=event_id,
            response=response,
        ).add_user()
    except Exception as e:
        return JSONResponse(
            content={"detail": str(e)},
            status_code=status.HTTP_401_UNAUTHORIZED,
        )


@router_visitors.get("/get")
async def get(
    request: Request,
    response: Response,
) -> JSONResponse:
    try:
        access = request.cookies.get("access")
        refresh = request.cookies.get("refresh")
        return await Visitors(
            token_access=access,
            token_refresh=refresh,
            response=response,
        ).get_user_events()
    except Exception as e:
        return JSONResponse(
            content={"detail": str(e)},
            status_code=status.HTTP_401_UNAUTHORIZED,
        )


@router_visitors.get(
    "/make/qr/{unique_string}",
    response_model=None,
)
async def make_qr(
    unique_string: str,
    request: Request,
    response: Response,
) -> StreamingResponse | JSONResponse:
    try:
        access = request.cookies.get("access")
        refresh = request.cookies.get("refresh")
        return await Visitors(
            token_access=access,
            token_refresh=refresh,
            response=response,
        ).make_qr(
            unique_string=unique_string,
        )
    except Exception as e:
        return JSONResponse(
            content={"detail": str(e)},
            status_code=status.HTTP_401_UNAUTHORIZED,
        )


@router_visitors.delete("/delete/{event_id}")
async def delete(
    event_id: int,
    request: Request,
    response: Response,
) -> JSONResponse:
    try:
        access = request.cookies.get("access")
        refresh = request.cookies.get("refresh")
        return await Visitors(
            token_access=access,
            token_refresh=refresh,
            event_id=event_id,
            response=response,
        ).delete_user()
    except Exception as e:
        return JSONResponse(
            content={"detail": str(e)},
            status_code=status.HTTP_401_UNAUTHORIZED,
        )
