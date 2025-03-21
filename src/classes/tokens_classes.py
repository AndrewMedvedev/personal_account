import logging

from aiohttp import ClientSession

from src.config import Settings
from src.errors import TokenError

log = logging.getLogger(__name__)


class ValidTokens:

    def __init__(self) -> None:
        self.clientsession = ClientSession
        self.settings = Settings

    async def valid(
        self,
        token_access: str,
        token_refresh: str,
    ) -> dict:
        send_access = await self.__send_access_token(token_access)
        if isinstance(send_access, bool):
            send_refresh = await self.__send_refresh_token(token_refresh)
            return send_refresh
        return send_access

    async def __send_refresh_token(
        self,
        token_refresh: str,
    ) -> dict:
        async with self.clientsession() as session:
            async with session.get(
                url=f"{self.settings.VALIDATE_REFRESH}{token_refresh}",
            ) as response:
                token = await response.json()
                log.warning(token)
                if isinstance(token, bool):
                    raise TokenError(
                        name_func="__send_refresh_token",
                        message="Токены не валидны",
                    )
                return token

    async def __send_access_token(
        self,
        token_access: str,
    ) -> dict:
        async with self.clientsession() as session:
            async with session.get(
                url=f"{self.settings.VALIDATE_ACCESS}{token_access}",
            ) as response:
                token = await response.json()
                log.warning(token)
                return token
