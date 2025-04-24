from typing import Callable

from datetime import UTC, datetime, timedelta

from fastapi import Request
from jose import JWTError
from starlette.middleware.base import BaseHTTPMiddleware

from .constants import SKIP_PATHS
from .exeptions import UnauthorizedHTTPError
from .jwt import ValidTokens


class MiddlewareValidTokens(BaseHTTPMiddleware):
    SKIP_PATH: list[str] = SKIP_PATHS

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
            token_access = request.cookies.get("access")
            token_refresh = request.cookies.get("refresh")
            if token_access is None or token_refresh is None:
                raise UnauthorizedHTTPError
            check_tokens = await self.valid_tokens.valid(
                token_access=token_access,
                token_refresh=token_refresh,
            )
            request.state.user_id = check_tokens.get("user_id")
            response = await call_next(request)
            if "access" in check_tokens:
                expires_access = timedelta(hours=2) + datetime.now(tz=UTC)
                response.set_cookie(
                    key="access",
                    value=check_tokens.get("access"),
                    expires=expires_access.strftime("%a, %d %b %Y %H:%M:%S GMT"),
                    samesite="none",
                    httponly=True,
                    secure=True,
                )
        except JWTError:
            raise UnauthorizedHTTPError from None
        else:
            return response
