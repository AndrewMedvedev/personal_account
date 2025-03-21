from io import BytesIO

import pyqrcode
from fastapi import status
from fastapi.responses import StreamingResponse

from src.database.schemas import CustomResponse
from src.interfaces import VisitorBase

from .send_data_class import VisitorsSend


class Visitors(VisitorBase):

    def __init__(self) -> None:
        self.send_data = VisitorsSend()

    async def add(
        self,
        user_id: int,
        event_id: int,
    ) -> CustomResponse:
        add = await self.send_data.visitor_add(
            event_id=event_id,
            user_id=user_id,
        )
        return CustomResponse(
            status_code=status.HTTP_200_OK,
            body=add,
            message="Выполненно",
            name_endpoint="/api/v1/visitors/add/{event_id}",
        )

    async def get(
        self,
        user_id: int,
    ) -> CustomResponse:
        get = await self.send_data.visitor_get(
            user_id=user_id,
        )
        return CustomResponse(
            status_code=status.HTTP_200_OK,
            body=get,
            message="Выполненно",
            name_endpoint="/api/v1/visitors/get",
        )

    async def delete(
        self,
        user_id: int,
        event_id: int,
    ) -> CustomResponse:
        delete = await self.send_data.visitor_delete(
            event_id=event_id,
            user_id=user_id,
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
