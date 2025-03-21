from fastapi import APIRouter, Response, status

from src.database.schemas import CustomResponse

router_set_token = APIRouter(prefix="/set/token", tags=["set_token"])


@router_set_token.get(
    "/{access}/{refresh}",
    response_model=None,
)
async def set_token(
    access: str,
    refresh: str,
    response: Response,
) -> dict:
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
    return CustomResponse(
        status_code=status.HTTP_200_OK,
        body=None,
        message="Выполненно",
        name_endpoint="/set/token/{access}/{refresh}",
    )
