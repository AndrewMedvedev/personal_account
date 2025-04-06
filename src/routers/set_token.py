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
        max_age=7200,
        samesite="none",
        httponly=True,
        secure=True,
        domain="https://online-service-for-applicants.onrender.com",
    )
    response.set_cookie(
        key="refresh",
        value=refresh,
        expires=expires_refresh.strftime("%a, %d %b %Y %H:%M:%S GMT"),
        max_age=18000,
        samesite="none",
        httponly=True,
        secure=True,
        domain="https://online-service-for-applicants.onrender.com",
    )
    return CustomResponse(
        status_code=status.HTTP_200_OK,
        body=None,
    )
