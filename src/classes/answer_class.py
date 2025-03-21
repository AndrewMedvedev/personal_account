from fastapi import status

from src.config import Settings
from src.database.schemas import CustomResponse
from src.interfaces import AnswerBase

from .send_data_class import Send


class Answer(AnswerBase):

    def __init__(self) -> None:
        self.settings = Settings
        self.send_data = Send()

    async def get_answer(
        self,
        message: str,
    ) -> CustomResponse:
        data_send = data = {"question": message}
        data = await self.send_data.post_json_send(
            params=data_send,
            setting=self.settings.RAG_GigaChat_API,
        )
        return CustomResponse(
            status_code=status.HTTP_200_OK,
            body=data,
            message="Выполненно",
            name_endpoint="/api/v1/answer/{message}",
        )
