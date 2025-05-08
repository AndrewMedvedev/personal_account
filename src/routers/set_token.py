from fastapi import APIRouter, Response
from fastapi.responses import JSONResponse

set_token = APIRouter(prefix="/set/token", tags=["set_token"])


@set_token.get("/{access}/{refresh}")
async def set_tokens(access: str, refresh: str) -> JSONResponse:
    response = JSONResponse(content={"message": "success"})
    response.headers.append(
        "Set-Cookie",
        "access=" + access + "; SameSite=None; Secure; HttpOnly; Max-Age=7200; Partitioned"
    )
    response.headers.append(
        "Set-Cookie",
        "refresh=" + refresh + "; SameSite=None; Secure; HttpOnly; Max-Age=18000; Partitioned"
    )
    return response
    # response.set_cookie(
    #     key="access",
    #     value=access,
    #     samesite="none",
    #     httponly=True,
    #     secure=True,
    #     max_age=7200,
    # )
    # response.set_cookie(
    #     key="refresh",
    #     value=refresh,
    #     samesite="none",
    #     httponly=True,
    #     secure=True,
    #     max_age=18000,
    # )
    return response
