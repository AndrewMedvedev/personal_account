from fastapi import APIRouter, Response, HTTPException, status

router = APIRouter(prefix="/token", tags=["token"])


@router.get(
    "/get",
    response_model=None,
)
async def get_tokens(response: Response, access: str, refresh: str) -> HTTPException:
    response.set_cookie(
        key="access",
        value=access,
    )
    response.set_cookie(
        key="refresh",
        value=refresh,
    )
    return HTTPException(status_code=status.HTTP_200_OK)
