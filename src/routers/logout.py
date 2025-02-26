from fastapi import APIRouter, HTTPException, Response, status

router_logout = APIRouter(prefix="/logout", tags=["logout"])


@router_logout.get(
    "/",
    response_model=None,
)
async def logout(response: Response) -> HTTPException:
    response.delete_cookie(
        key="access",
        samesite=None,
        httponly=False,
        secure=True,
    )
    response.delete_cookie(
        key="refresh",
        samesite=None,
        httponly=False,
        secure=True,
    )
    return HTTPException(status_code=status.HTTP_200_OK)
