from io import BytesIO

import pyqrcode
from fastapi import Response
from fastapi.responses import JSONResponse, StreamingResponse

from src.classes.send_data_class import SendData
from src.classes.tokens_classes import ValidTokens


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
        self.valid_tokens = ValidTokens
        self.send_data = SendData()

    async def add_user(self) -> JSONResponse:
        check_tokens = await self.valid_tokens(
            token_access=self.token_access,
            token_refresh=self.token_refresh,
            response=self.response,
        ).valid()
        add = await self.send_data.visitor_add(
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
        check_tokens = await self.valid_tokens(
            token_access=self.token_access,
            token_refresh=self.token_refresh,
            response=self.response,
        ).valid()
        get = await self.send_data.visitor_get(
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
        check_tokens = await self.valid_tokens(
            token_access=self.token_access,
            token_refresh=self.token_refresh,
            response=self.response,
        ).valid()
        delete = await self.send_data.visitor_delete(
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

    async def make_qr(
        self,
        unique_string: str,
    ) -> StreamingResponse:
        check_tokens = await self.valid_tokens(
            token_access=self.token_access,
            token_refresh=self.token_refresh,
            response=self.response,
        ).valid()
        buffer = BytesIO()
        qr = pyqrcode.create(
            f"https://events-fastapi.onrender.com/api/v1/visitors/verify/{unique_string}"
        )
        qr.png(buffer, scale=6)
        buffer.seek(0)
        headers = {
            "Content-Type": "image/png",
            "Content-Disposition": 'attachment; filename="qr_code.png"',
        }
        if "access" in check_tokens:
            self.response.set_cookie(
                key="access",
                value=check_tokens.get("access"),
                samesite="none",
                httponly=True,
                secure=True,
            )
        return StreamingResponse(buffer, media_type="image/png", headers=headers)
