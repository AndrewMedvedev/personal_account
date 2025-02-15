import json
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
                token = await response.text()
                return json.loads(token)

    async def send_access_token(self) -> str:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url=Settings.VALIDATE_ACCESS,
                params={"access": self.token},
            ) as response:
                token = await response.text()
                return json.loads(token)


async def check(access: str, refresh: str) -> dict:
    if access is None:
        new_access = await SendTokens(refresh).send_refresh_token()
        if type(new_access) == dict:
            return {
                "access": new_access.get("access"),
                "email": new_access.get("email"),
            }
    return await SendTokens(access).send_access_token()
