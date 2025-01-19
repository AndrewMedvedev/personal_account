import json
import aiohttp
from src.config import Settings


class SendTokens:

    def __init__(self, token: str) -> None:
        self.token = token

    async def send_refresh_token(self) -> dict | bool:
        async with aiohttp.ClientSession() as session:
            data = {"refresh": self.token}
            async with session.post(
                Settings.VALIDATE_REFRESH,
                json=data,
            ) as resp:
                tkn = await resp.text()
                return json.loads(tkn)


    async def send_access_token(self) -> str:
        async with aiohttp.ClientSession() as session:
            data = {"access": self.token}
            async with session.post(
                Settings.VALIDATE_ACCESS,
                json=data,
            ) as resp:
                return await resp.text()
