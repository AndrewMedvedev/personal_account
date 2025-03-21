from fastapi import Response

from src.config import Settings
from src.database.schemas import (CustomResponse, DictGetDataTokenVK,
                                  DictGetDataVK, DictLinkVK)
from src.interfaces import OtherRegistrationBase

from .controls import create_codes
from .reuse_class import ReUse


class VK(OtherRegistrationBase):

    def __init__(self) -> None:
        self.settings = Settings
        self.response = Response
        self.reuse = ReUse()

    async def link(
        self,
    ) -> CustomResponse:
        codes = await create_codes()
        return await self.reuse.link(
            setting=self.settings.VK_AUTH_URL,
            dictlink=DictLinkVK(
                code_challenge=codes.get("code_challenge")
            ).model_dump(),
            code_verifier=codes.get("code_verifier"),
        )

    async def get_token(
        self,
        code: str,
        device_id: str,
        code_verifier: str,
    ) -> CustomResponse:
        return await self.reuse.get_token(
            dictgetdata=DictGetDataVK(
                code=code,
                device_id=device_id,
                code_verifier=code_verifier,
            ).model_dump(),
            setting=self.settings.VK_TOKEN_URL,
            service="vk",
        )

    async def registration(
        self,
        access: str,
        user_id: int,
    ) -> CustomResponse:
        return await self.reuse.registration(
            user_id=user_id,
            dictgetdatatoken=DictGetDataTokenVK(access_token=access).model_dump(),
            setting=self.settings.VK_API_URL,
            setting_reg=self.settings.REGISTRATION_VK,
            service="vk",
        )
