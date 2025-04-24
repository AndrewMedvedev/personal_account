from io import BytesIO

import pyqrcode
from fastapi.responses import StreamingResponse

from ..rest import VisitorApi


class VisitorControl:
    def __init__(self) -> None:
        self.visitor_api = VisitorApi()

    async def create_user(self, user_id: int, event_id: int) -> None:
        return await self.visitor_api.visitor_create(event_id=event_id, user_id=user_id)

    async def get_user_events(self, user_id: int) -> dict:
        return await self.visitor_api.visitor_get(user_id=user_id)

    async def delete_user(self, user_id: int, event_id: int) -> None:
        return await self.visitor_api.visitor_delete(event_id=event_id, user_id=user_id)

    @staticmethod
    async def make_qr(unique_string: str) -> StreamingResponse:
        buffer = BytesIO()
        qr = pyqrcode.create(
            f"https://events-zisi.onrender.com/api/v1/visitors/verify/{unique_string}"
        )
        qr.png(buffer, scale=6)
        buffer.seek(0)
        headers = {
            "Content-Type": "image/png",
            "Content-Disposition": 'attachment; filename="qr_code.png"',
        }
        return StreamingResponse(buffer, media_type="image/png", headers=headers)
