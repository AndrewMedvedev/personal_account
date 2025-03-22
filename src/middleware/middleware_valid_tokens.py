import logging
from typing import Callable

from fastapi import Request, status
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from src.classes.tokens_classes import ValidTokens
from src.database.schemas.custom_response import CustomResponse

log = logging.getLogger(__name__)


class MiddlewareValidTokens(BaseHTTPMiddleware):

    def __init__(self, app, dispatch=None) -> None:
        self.valid_tokens = ValidTokens()
        super().__init__(
            app,
            dispatch,
        )

    async def dispatch(
        self,
        request: Request,
        call_next: Callable,
    ):
        try:
            if request.url.path in [
                "/docs",
                "/redoc",
                "/openapi.json",
            ]:
                return await call_next(request)
            if request.url.path.startswith("/set/token"):
                return await call_next(request)
            if request.url.path == "/logout/":
                return await call_next(request)
            if request.url.path == "/api/v1/predict/free":
                return await call_next(request)

            log.info(call_next)
            token_access = request.cookies.get("access")
            token_refresh = request.cookies.get("refresh")
            check_tokens = await self.valid_tokens.valid(
                token_access=token_access,
                token_refresh=token_refresh,
            )
            request.state.user_id = check_tokens.get("user_id")
            response = await call_next(request)
            if "access" in check_tokens:
                response.set_cookie(
                    key="access",
                    value=check_tokens.get("access"),
                    samesite="none",
                    httponly=True,
                    secure=True,
                )
            return response
        except Exception:
            return JSONResponse(
                content=CustomResponse(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    body="Токены не валидны",
                    message="Ошибка в выполнении",
                    name_endpoint="_",
                ).model_dump(),
                status_code=status.HTTP_401_UNAUTHORIZED,
            )
