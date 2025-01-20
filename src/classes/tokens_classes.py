import aiohttp
from src.config import Settings


class SendTokens:

    def __init__(self, token: str) -> None:
        self.token = token

    async def send_refresh_token(self) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url=Settings.VALIDATE_REFRESH, params={"refresh": self.token}
            ) as response:
                return await response.text()

    async def send_access_token(self) -> str:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url=Settings.VALIDATE_ACCESS,
                params={"access": self.token},
            ) as response:
                return await response.text()
