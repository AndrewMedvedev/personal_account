from uuid import UUID

from config import settings

from ..rest import RegistrationApi, VKApi
from ..schemas import (
    DictGetDataTokenVKSchema,
    DictGetDataVKSchema,
    DictLinkVKSchema,
    RegistrationVKSchema,
)
from ..utils import RedisOtherAuth, create_codes


class VKControl:
    def __init__(self):
        self.vk_api = VKApi()
        self.redis = RedisOtherAuth()
        self.registration_api = RegistrationApi()

    async def link(self) -> str:
        codes = create_codes()
        await self.redis.add_code(schema=codes)
        dict_link = (
            DictLinkVKSchema(state=codes.state, code_challenge=codes.code_challenge)
            .model_dump()
            .items()
        )
        return f"{settings.VK_AUTH_URL}?{'&'.join([f'{k}={v}' for k, v in dict_link])}"

    async def get_token(self, code: str, device_id: str, state: str) -> str:
        data_state = await self.redis.get_code(key=state)
        params = DictGetDataVKSchema(
            code=code, device_id=device_id, code_verifier=data_state, state=state
        ).model_dump()
        result = await self.vk_api.get_token(params=params)
        return result["access_token"]

    async def registration(self, code: str, device_id: str, state: str, user_id: UUID) -> None:
        token = await self.get_token(code=code, device_id=device_id, state=state)
        user = (
            await self.vk_api.get_data(
                params=DictGetDataTokenVKSchema(access_token=token).model_dump()
            )
        )["user"]
        data = RegistrationVKSchema(
            user_id=user_id,
            first_name=user.get("first_name"),
            last_name=user.get("last_name"),
            id_vk=int(user.get("user_id")),
            email=user.get("email").lower(),
        ).model_dump()
        return await self.registration_api.registration_vk(params=data)
