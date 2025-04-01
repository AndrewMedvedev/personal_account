from fastapi import Request, status

from src.responses import CustomBadResponse

from .errors import NotFoundError, SendError, TokenError


async def token_error(
    request: Request,
    exc: TokenError,
) -> CustomBadResponse:
    return CustomBadResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        message="Ошибка токенов",
        detail=str(exc),
    )


async def send_error(
    request: Request,
    exc: SendError,
) -> CustomBadResponse:
    return CustomBadResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        message="Ошибка отправки",
        detail=str(exc),
    )


async def not_found_error(
    request: Request,
    exc: NotFoundError,
) -> CustomBadResponse:
    return CustomBadResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        message="Элемент не найден",
        detail=str(exc),
    )
