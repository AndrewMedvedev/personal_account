from typing import Callable

import logging
from datetime import datetime, timedelta

from fastapi import Request, status
from starlette.middleware.base import BaseHTTPMiddleware

from src.classes.tokens_classes import ValidTokens
from src.errors import TokenError
from src.responses import CustomBadResponse

log = logging.getLogger(__name__)


class MiddlewareValidTokens(BaseHTTPMiddleware):
    SKIP_PATH = [
        "/docs",
        "/redoc",
        "/openapi.json",
        "/logout/",
        "/api/v1/predict/free",
        "/api/v1/events/get",
        "/api/v1/news/get",
    ]

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
            if request.url.path.startswith("/set/token"):
                return await call_next(request)
            if request.url.path in self.SKIP_PATH:
                return await call_next(request)
            log.info(call_next)
            token_access = request.cookies.get("access")
            token_refresh = request.cookies.get("refresh")
            if token_access is None or token_refresh is None:
                raise TokenError(
                    name_func="dispatch",
                    message="Токены не валидны",
                )
            check_tokens = await self.valid_tokens.valid(
                token_access=token_access,
                token_refresh=token_refresh,
            )
            request.state.user_id = check_tokens.get("user_id")
            response = await call_next(request)
            if "access" in check_tokens:
                expires_access = timedelta(hours=2) + datetime.now()
                response.set_cookie(
                    key="access",
                    value=check_tokens.get("access"),
                    expires=expires_access.strftime("%a, %d %b %Y %H:%M:%S GMT"),
                    samesite="none",
                    httponly=True,
                    secure=True,
                )
            return response
        except Exception as e:
            return CustomBadResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                message="Токены не валидны",
                detail=str(e),
            )
