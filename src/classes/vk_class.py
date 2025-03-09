import base64
import hashlib
import os

from fastapi import Response
from fastapi.responses import JSONResponse

from src.classes.reuse_class import ReUse
from src.classes.send_data_class import SendData
from src.config import Settings
from src.database.schemas import DictGetDataTokenVK, DictGetDataVK, DictLinkVK
from src.interfaces import OtherRegistrationBase


class VK(OtherRegistrationBase):

    def __init__(
        self,
        code: str = None,
        device_id: str = None,
        access: str = None,
        token_access: str = None,
        token_refresh: str = None,
    ) -> None:
        self.code = code
        self.device_id = device_id
        self.access = access
        self.token_access = token_access
        self.token_refresh = token_refresh
        self.send_data = SendData()
        self.settings = Settings
        self.response = Response
        self.reuse = ReUse

    async def link(
        self,
    ) -> JSONResponse:
        code_verifier = (
            base64.urlsafe_b64encode(os.urandom(128)).rstrip(b"=").decode("utf-8")
        )
        code_challenge = (
            base64.urlsafe_b64encode(
                hashlib.sha256(code_verifier.encode("utf-8")).digest()
            )
            .rstrip(b"=")
            .decode("utf-8")
        )
        return await self.reuse.link(
            setting=self.settings.VK_AUTH_URL,
            dictlink=DictLinkVK(code_challenge=code_challenge).model_dump(),
            code_verifier=code_verifier,
        )

    async def get_token(self, code_verifier: str) -> JSONResponse:
        return await self.reuse(
            func=self.send_data.get_token_user_vk,
        ).get_token(
            dictgetdata=DictGetDataVK(
                code=self.code,
                device_id=self.device_id,
                code_verifier=code_verifier,
            ).model_dump(),
        )

    async def registration(self) -> dict:
        user = await self.send_data.get_data_user_vk(
            DictGetDataTokenVK(access_token=self.access).model_dump()
        )
        user_data = {
            "first_name": user.get("first_name"),
            "last_name": user.get("last_name"),
            "id_vk": int(user.get("user_id")),
            "email": user.get("email"),
        }
        return await self.reuse().registration(
            user_data=user_data,
            token_access=self.token_access,
            token_refresh=self.token_refresh,
            send=self.send_data.registration_vk,
        )
