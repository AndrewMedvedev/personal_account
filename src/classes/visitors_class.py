from io import BytesIO

import pyqrcode
from fastapi import Response, status
from fastapi.responses import StreamingResponse

from src.database.schemas import CustomResponse
from src.interfaces import VisitorBase

from .send_data_class import VisitorsSend
from .tokens_classes import ValidTokens


class Visitors(VisitorBase):

    def __init__(self) -> None:
        self.response = Response
        self.send_data = VisitorsSend()
        self.valid_tokens = ValidTokens()

    async def add(
        self,
        token_access: str,
        token_refresh: str,
        event_id: int,
    ) -> CustomResponse:
        check_tokens = await self.valid_tokens.valid(
            token_access=token_access,
            token_refresh=token_refresh,
        )
        add = await self.send_data.visitor_add(
            event_id=event_id,
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
        return CustomResponse(
            status_code=status.HTTP_200_OK,
            body=add,
            message="Выполненно",
            name_endpoint="/api/v1/visitors/add/{event_id}",
        )

    async def get(
        self,
        token_access: str,
        token_refresh: str,
    ) -> CustomResponse:
        check_tokens = await self.valid_tokens.valid(
            token_access=token_access,
            token_refresh=token_refresh,
        )
        get = await self.send_data.visitor_get(
            user_id=check_tokens.get("user_id"),
        )
        return CustomResponse(
            status_code=status.HTTP_200_OK,
            body=get,
            message="Выполненно",
            name_endpoint="/api/v1/visitors/get",
        )

    async def delete(
        self,
        token_access: str,
        token_refresh: str,
        event_id: int,
    ) -> CustomResponse:
        check_tokens = await self.valid_tokens.valid(
            token_access=token_access,
            token_refresh=token_refresh,
        )
        delete = await self.send_data.visitor_delete(
            event_id=event_id,
            user_id=check_tokens.get("user_id"),
        )
        return CustomResponse(
            status_code=status.HTTP_200_OK,
            body=delete,
            message="Выполненно",
            name_endpoint="/api/v1/visitors/delete/{event_id}",
        )

    async def make_qr(
        self,
        unique_string: str,
    ) -> StreamingResponse:
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
        return StreamingResponse(buffer, media_type="image/png", headers=headers)
