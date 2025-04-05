from fastapi import status

from src.config import Settings
from src.interfaces import EventsBase
from src.responses import CustomResponse

from .send_data_class import Send


class Events(EventsBase):
    def __init__(self):
        self.send = Send()
        self.settings = Settings

    async def get_events(
        self,
        page: int,
        limit: int,
    ):
        result = (
            await self.send.get_params_send(
                params={
                    "is_paginated": "true",
                    "page": page,
                    "limit": limit,
                },
                setting=self.settings.EVENTS_GET,
            )
        ).get("body")
        return CustomResponse(
            status_code=status.HTTP_200_OK,
            body=result,
        )
