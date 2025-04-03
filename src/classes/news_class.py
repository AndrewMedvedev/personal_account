from fastapi import status

from src.config import Settings
from src.responses import CustomResponse

from .send_data_class import Send
from src.interfaces import NewsBase


class News(NewsBase):

    def __init__(self):
        self.send = Send()
        self.settings = Settings

    async def get_news(
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
                setting=self.settings.NEWS_GET,
            )
        ).get("body")
        return CustomResponse(
            status_code=status.HTTP_200_OK,
            body=result,
        )
