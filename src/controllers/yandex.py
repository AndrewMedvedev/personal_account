from uuid import UUID

from config import settings

from ..rest import RegistrationApi, YandexApi
from ..schemas import (
    DictGetDataTokenYandexSchema,
    DictGetDataYandexSchema,
    DictLinkYandexSchema,
    RegistrationYandexSchema,
)
from ..utils import RedisOtherAuth, create_codes


class YandexControl:
    def __init__(self):
        self.yandex_api = YandexApi()
        self.redis = RedisOtherAuth()
        self.registration_api = RegistrationApi()

    async def link(self) -> str:
        codes = create_codes()
        await self.redis.add_code(schema=codes)
        dict_link = (
            DictLinkYandexSchema(state=codes.state, code_challenge=codes.code_challenge)
            .model_dump()
            .items()
        )
        return f"{settings.YANDEX_AUTH_URL}?{'&'.join([f'{k}={v}' for k, v in dict_link])}"

    async def get_token(self, code: str, state: str) -> str:
        data_state = await self.redis.get_code(key=state)
        params = DictGetDataYandexSchema(
            code=code,
            code_verifier=data_state,
        ).model_dump()
        result = await self.yandex_api.get_token(params=params)
        return result["access_token"]

    async def registration(self, code: str, state: str, user_id: UUID) -> None:
        token = await self.get_token(code=code, state=state)
        user = await self.yandex_api.get_data(
            params=DictGetDataTokenYandexSchema(oauth_token=token).model_dump()
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
