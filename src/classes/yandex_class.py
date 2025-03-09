import base64
import hashlib
import os

from fastapi import Response
from fastapi.responses import JSONResponse

from src.classes.reuse_class import ReUse
from src.classes.send_data_class import SendData
from src.config import Settings
from src.database.schemas import (DictGetDataTokenYandex, DictGetDataYandex,
                                  DictLinkYandex)
from src.interfaces import OtherRegistrationBase


class Yandex(OtherRegistrationBase):

    def __init__(
        self,
        code: str = None,
        access: str = None,
        token_access: str = None,
        token_refresh: str = None,
    ) -> None:
        self.code = code
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
            setting=self.settings.YANDEX_AUTH_URL,
            dictlink=DictLinkYandex(code_challenge=code_challenge).model_dump(),
            code_verifier=code_verifier,
        )

    async def get_token(self, code_verifier: str) -> JSONResponse:
        return await self.reuse(
            func=self.send_data.get_token_user_yandex,
        ).get_token(
            dictgetdata=DictGetDataYandex(
                code=self.code,
                code_verifier=code_verifier,
            ).model_dump(),
        )

    async def registration(self):
        user = await self.send_data.get_data_user_yandex(
            DictGetDataTokenYandex(oauth_token=self.access).model_dump()
        )
        print(user)
        user_data = {
            "first_name": user.get("first_name"),
            "last_name": user.get("last_name"),
            "id_yandex": user.get("id"),
            "login": user.get("login"),
            "email": user.get("default_email"),
        }
        return await self.reuse().registration(
            user_data=user_data,
            token_access=self.token_access,
            token_refresh=self.token_refresh,
            send=self.send_data.registration_yandex,
        )
