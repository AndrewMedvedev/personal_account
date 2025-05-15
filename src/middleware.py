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
            if request.method == "OPTIONS" or request.url.path in self.SKIP_PATH:
                return await call_next(request)
            token_access = request.headers.get("X-Access-Token", None)
            token_refresh = request.headers.get("X-Refresh-Token", None)
            if token_access is None or token_refresh is None:
                raise UnauthorizedHTTPError
            check_tokens = await send_tokens(
                access=token_access,
                refresh=token_refresh,
            )
            request.state.user_id = check_tokens["user_id"]
            response = await call_next(request)
            response.headers["X-Refresh-Token"] = token_refresh
            response.headers["X-Access-Token"] = token_refresh
            if "access" in check_tokens:
                response.headers["X-Access-Token"] = check_tokens["access"]
        except JWTError:
            raise UnauthorizedHTTPError from None
        else:
            return response
