from config import Settings

from ..rest import RegistrationApi, VKApi
from ..schemas import (
    DictGetDataTokenVKSchema,
    DictGetDataVKSchema,
    DictLinkVKSchema,
    RegistrationVKSchema,
)
from ..utils import create_codes


class VKControl:
    def __init__(self):
        self.vk_api = VKApi()
        self.registration_api = RegistrationApi()

    @staticmethod
    async def link() -> dict:
        codes = create_codes()
        dict_link = DictLinkVKSchema(code_challenge=codes["code_challenge"]).model_dump().items()
        url = f"{Settings.VK_AUTH_URL}?{'&'.join([f'{k}={v}' for k, v in dict_link])}"
        return {
            "link": url,
            "code_verifier": codes["code_verifier"],
        }

    async def get_token(self, code: str, device_id: str, code_verifier: str) -> dict:
        params = DictGetDataVKSchema(
            code=code,
            device_id=device_id,
            code_verifier=code_verifier,
        ).model_dump()
        return await self.vk_api.get_token(params=params)

    async def registration(self, access: str, user_id: int) -> None:
        user = (await self.vk_api.get_data(
            params=DictGetDataTokenVKSchema(access_token=access).model_dump()
        ))["user"]
        data = RegistrationVKSchema(
            user_id=user_id,
            first_name=user.get("first_name"),
            last_name=user.get("last_name"),
            id_vk=int(user.get("user_id")),
            email=user.get("email").lower(),
        ).model_dump()
        return await self.registration_api.registration_vk(params=data)
