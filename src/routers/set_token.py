from datetime import UTC, datetime, timedelta

from fastapi import APIRouter, Response

set_token = APIRouter(prefix="/set/token", tags=["set_token"])


@set_token.get("/{access}/{refresh}")
async def set_tokens(access: str, refresh: str, response: Response) -> Response:
    expires_access = timedelta(hours=2) + datetime.now(tz=UTC)
    expires_refresh = timedelta(hours=5) + datetime.now(tz=UTC)
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
    return {"message": "success"}
