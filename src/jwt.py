import logging

from aiohttp import ClientSession

from config import settings

from .exeptions import UnauthorizedHTTPError

log = logging.getLogger(__name__)


async def send_tokens(access: str, refresh: str) -> dict | bool:
    async with (
        ClientSession() as session,
        session.get(url=f"{settings.VALIDATE_TOKENS}{access}/{refresh}") as data,
    ):
        response = await data.json()
        if isinstance(response, bool):
            raise UnauthorizedHTTPError
        return response
