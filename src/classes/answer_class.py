from fastapi import Response
from src.classes.tokens_classes import check
from src.classes.send_data_class import SendData, check


class Answer:

    def __init__(
        self,
        message: str,
        token_access: str,
        token_refresh: str,
        response: Response,
    ) -> None:
        self.message = message
        self.token_access = token_access
        self.token_refresh = token_refresh
        self.response = response

    async def answer(self) -> dict:
        check_tokens = await check(
            access=self.token_access,
            refresh=self.token_refresh,
            responce=self.response,
        )
        data = await SendData.send_message_bot(self.message)
        result = {"answer": data["data"]["answer"]}
        if "access" in check_tokens:
            self.response.set_cookie(
                key="access",
                value=check_tokens.get("access"),
                samesite="none",
                httponly=True,
                secure=True,
            )
        return result
