from fastapi import APIRouter, HTTPException, Response, status

router_get_token = APIRouter(prefix="/get/token", tags=["get_token"])


@router_get_token.get(
    "/",
    response_model=None,
)
async def get_token(access: str, refresh: str, response: Response) -> HTTPException:
    response.set_cookie(
        key="access",
        value=access,
        samesite="none",
        httponly=True,
        secure=True,
    )
    response.set_cookie(
        key="refresh",
        value=refresh,
        samesite="none",
        httponly=True,
        secure=True,
    )
    return HTTPException(status_code=status.HTTP_200_OK)
