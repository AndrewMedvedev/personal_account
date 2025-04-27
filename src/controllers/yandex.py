from uuid import UUID

from config import Settings

from ..rest import RegistrationApi, YandexApi
from ..schemas import (
    DictGetDataTokenYandexSchema,
    DictGetDataYandexSchema,
    DictLinkYandexSchema,
    RegistrationYandexSchema,
)
from ..utils import create_codes


class YandexControl:
    def __init__(self):
        self.yandex_api = YandexApi()
        self.registration_api = RegistrationApi()

    @staticmethod
    async def link() -> dict:
        codes = create_codes()
        dict_link = (
            DictLinkYandexSchema(code_challenge=codes["code_challenge"]).model_dump().items()
        )
        url = f"{Settings.YANDEX_AUTH_URL}?{'&'.join([f'{k}={v}' for k, v in dict_link])}"
        return {
            "link": url,
            "code_verifier": codes["code_verifier"],
        }

    async def get_token(
        self,
        code: str,
        code_verifier: str,
    ) -> dict:
        params = DictGetDataYandexSchema(
            code=code,
            code_verifier=code_verifier,
        ).model_dump()
        return await self.yandex_api.get_token(params=params)

    async def registration(self, access: str, user_id: UUID) -> None:
        user = await self.yandex_api.get_data(
            params=DictGetDataTokenYandexSchema(oauth_token=access).model_dump()
        )
        data = RegistrationYandexSchema(
            user_id=user_id,
            first_name=user.get("first_name"),
            last_name=user.get("last_name"),
            id_yandex=user.get("id"),
            login=user.get("login"),
            email=user.get("default_email"),
        ).model_dump()
        return await self.registration_api.registration_yandex(params=data)
