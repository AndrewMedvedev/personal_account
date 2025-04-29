from fastapi import APIRouter, Response

set_token = APIRouter(prefix="/set/token", tags=["set_token"])


@set_token.get("/{access}/{refresh}")
async def set_tokens(access: str, refresh: str, response: Response) -> Response:
    response.set_cookie(
        key="access",
        value=access,
        samesite="strict",
        httponly=True,
        secure=True,
        max_age=7200,
    )
    response.set_cookie(
        key="refresh",
        value=refresh,
        samesite="strict",
        httponly=True,
        secure=True,
        max_age=18000,
    )
    return {"message": "success"}
