from fastapi import Response
from src.classes.tokens_classes import ValidTokens
from src.classes.send_data_class import SendData

from fastapi.responses import JSONResponse


class Visitors:

    def __init__(
        self,
        token_access: str,
        token_refresh: str,
        response: Response,
        event_id: int = None,
    ) -> None:
        self.token_access = token_access
        self.token_refresh = token_refresh
        self.event_id = event_id
        self.response = response

    async def add_user(self) -> JSONResponse:
        check_tokens = await ValidTokens(
            token_access=self.token_access,
            token_refresh=self.token_refresh,
            response=self.response,
        ).valid()
        add = await SendData.visitor_add(
            event_id=self.event_id,
            user_id=check_tokens.get("user_id"),
        )
        if "access" in check_tokens:
            self.response.set_cookie(
                key="access",
                value=check_tokens.get("access"),
                samesite="none",
                httponly=True,
                secure=True,
            )
        return JSONResponse(
            content=add,
        )

    async def get_user_events(self) -> JSONResponse:
        check_tokens = await ValidTokens(
            token_access=self.token_access,
            token_refresh=self.token_refresh,
            response=self.response,
        ).valid()
        get = await SendData.visitor_get(
            user_id=check_tokens.get("user_id"),
        )
        if "access" in check_tokens:
            self.response.set_cookie(
                key="access",
                value=check_tokens.get("access"),
                samesite="none",
                httponly=True,
                secure=True,
            )
        return JSONResponse(
            content=get,
        )

    async def delete_user(self) -> JSONResponse:
        check_tokens = await ValidTokens(
            token_access=self.token_access,
            token_refresh=self.token_refresh,
            response=self.response,
        ).valid()
        delete = await SendData.visitor_delete(
            event_id=self.event_id,
            user_id=check_tokens.get("user_id"),
        )
        if "access" in check_tokens:
            self.response.set_cookie(
                key="access",
                value=check_tokens.get("access"),
                samesite="none",
                httponly=True,
                secure=True,
            )
        return JSONResponse(
            content=delete,
        )
