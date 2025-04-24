import logging

from aiohttp import ClientSession

from config import Settings

from .exeptions import UnauthorizedHTTPError

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
            return await self.__send_refresh_token(token_refresh)
        return send_access

    async def __send_refresh_token(
        self,
        token_refresh: str,
    ) -> dict:
        async with (
            self.clientsession() as session,
            session.get(
                url=f"{self.settings.VALIDATE_REFRESH}{token_refresh}",
            ) as response,
        ):
            tkn = await response.json()
            if isinstance(tkn, bool):
                raise UnauthorizedHTTPError
            return tkn

    async def __send_access_token(
        self,
        token_access: str,
    ) -> dict:
        async with (
            self.clientsession() as session,
            session.get(
                url=f"{self.settings.VALIDATE_ACCESS}{token_access}",
            ) as response,
        ):
            token = await response.json()
            log.warning(token)
            return token
