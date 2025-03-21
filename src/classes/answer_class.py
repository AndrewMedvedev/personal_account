from fastapi import Response, status

from src.config import Settings
from src.database.schemas import CustomResponse
from src.interfaces import AnswerBase

from .send_data_class import Send
from .tokens_classes import ValidTokens


class Answer(AnswerBase):

    def __init__(self) -> None:
        self.settings = Settings
        self.valid_tokens = ValidTokens()
        self.send_data = Send()
        self.response = Response

    async def get_answer(
        self,
        message: str,
        token_access: str,
        token_refresh: str,
    ) -> CustomResponse:
        check_tokens = await self.valid_tokens.valid(
            token_access=token_access,
            token_refresh=token_refresh,
        )
        data_send = data = {"question": message}
        data = await self.send_data.post_json_send(
            params=data_send,
            setting=self.settings.RAG_GigaChat_API,
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
            body=data,
            message="Выполненно",
            name_endpoint="/api/v1/answer/{message}",
        )
