from typing import Callable

from fastapi import Request
from jose import JWTError
from starlette.middleware.base import BaseHTTPMiddleware

from .constants import SKIP_PATHS
from .exeptions import UnauthorizedHTTPError
from .jwt import send_tokens


class MiddlewareValidTokens(BaseHTTPMiddleware):
    SKIP_PATH: list[str] = SKIP_PATHS

    def __init__(self, app, dispatch=None) -> None:
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
            if request.method == "OPTIONS" or request.url.path in self.SKIP_PATHS:
                return await call_next(request)
            if request.url.path.startswith("/set/token"):
                return await call_next(request)
            token_access = request.cookies.get("access")
            token_refresh = request.cookies.get("refresh")
            if token_access is None or token_refresh is None:
                raise UnauthorizedHTTPError
            check_tokens = await send_tokens(
                access=token_access,
                refresh=token_refresh,
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
                    max_age=7200,
                )
        except JWTError:
            raise UnauthorizedHTTPError from None
        else:
            return response
