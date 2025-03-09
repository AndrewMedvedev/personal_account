from fastapi.responses import JSONResponse

from src.classes.send_data_class import SendData
from src.classes.tokens_classes import ValidTokens
from src.interfaces import ReUseBase


class ReUse(ReUseBase):

    def __init__(self, func=None):
        self.func = func
        self.send_data = SendData()
        self.valid_tokens = ValidTokens

    @staticmethod
    async def link(setting: str, dictlink: dict, code_verifier: str) -> JSONResponse:
        url = f"{setting}?{'&'.join([f'{k}={v}' for k, v in dictlink.items()])}"
        return JSONResponse(content={"url": url, "code_verifier": code_verifier})

    async def get_token(self, dictgetdata: dict) -> JSONResponse:
        return JSONResponse(content=await self.func(dictgetdata))

    async def registration(
        self,
        user_data: dict,
        token_access: str,
        token_refresh: str,
        send,
    ) -> JSONResponse:
        check_tokens = await self.valid_tokens(
            token_access=token_access,
            token_refresh=token_refresh,
        ).valid()
        user_data["user_id"] = check_tokens.get("user_id")
        result = await send(user_data)
        return JSONResponse(content=result)
