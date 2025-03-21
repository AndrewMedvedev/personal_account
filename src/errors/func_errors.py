from fastapi import Request, status
from fastapi.responses import JSONResponse

from src.database.schemas import CustomResponse

from .errors import SendError, TokenError


async def token_error(
    request: Request,
    exc: TokenError,
) -> CustomResponse:
    return JSONResponse(
        content=(
            CustomResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                body=str(exc),
                message="Ошибка в выполнении",
                name_endpoint="_",
            )
        ).model_dump(),
        status_code=status.HTTP_401_UNAUTHORIZED,
    )


async def send_error(
    request: Request,
    exc: SendError,
) -> CustomResponse:
    return JSONResponse(
        content=(
            CustomResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                body=str(exc),
                message="Ошибка в выполнении",
                name_endpoint="_",
            )
        ).model_dump(),
        status_code=status.HTTP_401_UNAUTHORIZED,
    )
