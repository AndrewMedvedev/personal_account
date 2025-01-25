from src.classes.tokens_classes import check
from src.classes.send_data_class import SendData


class Answer:

    def __init__(
        self,
        message: str,
        token_access: str,
        token_refresh: str,
    ) -> None:
        self.message = message
        self.token_access = token_access
        self.token_refresh = token_refresh

    async def answer(self) -> dict:
        check_tokens = await check(
            access=self.token_access,
            refresh=self.token_refresh,
        )
        data = await SendData.send_message_bot(self.message)
        result = {"answer": data["data"]["answer"]}
        if "access" in check_tokens:
            result["access"] = check_tokens.get("access")
        return result
