from fastapi import HTTPException, Response, status
from src.classes.tokens_classes import check
from src.classes.send_data_class import SendData


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

    async def answer(self) -> str | HTTPException:
        try:
            check_tokens = await check(
                access=self.token_access,
                refresh=self.token_refresh,
            )
            if type(check_tokens) == dict:
                self.response.set_cookie(
                    key="access",
                    value=check_tokens.get("access"),
                )
                data = await SendData.send_message_bot(self.message)
                return (data.get("data")).get("answer")
            elif type(check_tokens) == str:
                data = await SendData.send_message_bot(self.message)
                return (data.get("data")).get("answer")
        except: 
            return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)