from datetime import datetime, timedelta

from fastapi import APIRouter, Response, status

from src.responses import CustomResponse

router_set_token = APIRouter(prefix="/set/token", tags=["set_token"])


@router_set_token.get(
    "/{access}/{refresh}",
    response_model=None,
)
async def set_token(
    access: str,
    refresh: str,
    response: Response,
) -> CustomResponse:
    expires_access = timedelta(hours=2) + datetime.now()
    expires_refresh = timedelta(hours=5) + datetime.now()
    response.set_cookie(
        key="access",
        value=access,
        expires=expires_access.strftime("%a, %d %b %Y %H:%M:%S GMT"),
        samesite="none",
        httponly=True,
        secure=True,
    )
    response.set_cookie(
        key="refresh",
        value=refresh,
        expires=expires_refresh.strftime("%a, %d %b %Y %H:%M:%S GMT"),
        samesite="none",
        httponly=True,
        secure=True,
    )
    return CustomResponse(
        status_code=status.HTTP_200_OK,
        body=None,
    )
