from fastapi import APIRouter, Response, status

from src.responses import CustomResponse

router_logout = APIRouter(prefix="/logout", tags=["logout"])


@router_logout.get(
    "/",
    response_model=None,
)
async def logout(response: Response) -> CustomResponse:
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
    return CustomResponse(
        status_code=status.HTTP_204_NO_CONTENT,
        body=None,
    )
