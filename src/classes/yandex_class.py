from src.config import Settings
from src.database.schemas import (CustomResponse, DictGetDataTokenYandex,
                                  DictGetDataYandex, DictLinkYandex)
from src.interfaces import OtherRegistrationBase

from .controls import create_codes
from .reuse_class import ReUse


class Yandex(OtherRegistrationBase):

    def __init__(self) -> None:
        self.settings = Settings
        self.reuse = ReUse()

    async def link(
        self,
    ) -> CustomResponse:
        codes = await create_codes()
        return await self.reuse.link(
            setting=self.settings.YANDEX_AUTH_URL,
            dictlink=DictLinkYandex(
                code_challenge=codes.get("code_challenge")
            ).model_dump(),
            code_verifier=codes.get("code_verifier"),
        )

    async def get_token(
        self,
        code: str,
        code_verifier: str,
    ) -> CustomResponse:
        return await self.reuse.get_token(
            dictgetdata=DictGetDataYandex(
                code=code,
                code_verifier=code_verifier,
            ).model_dump(),
            setting=self.settings.YANDEX_TOKEN_URL,
            service="yandex",
        )

    async def registration(
        self,
        access: str,
        user_id: int,
    ) -> CustomResponse:
        return await self.reuse.registration(
            user_id=user_id,
            dictgetdatatoken=DictGetDataTokenYandex(oauth_token=access).model_dump(),
            setting=self.settings.YANDEX_API_URL,
            setting_reg=self.settings.REGISTRATION_YANDEX,
            service="yandex",
        )
