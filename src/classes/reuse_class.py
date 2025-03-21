import logging

from fastapi import Response, status

from src.classes.send_data_class import Send
from src.classes.tokens_classes import ValidTokens
from src.database.schemas import (CustomResponse, RegistrationVK,
                                  RegistrationYandex)
from src.interfaces import ReUseBase

log = logging.getLogger(__name__)


class ReUse(ReUseBase):

    def __init__(self):
        self.send = Send()
        self.valid_tokens = ValidTokens()
        self.response = Response

    async def link(
        self, setting: str, dictlink: dict, code_verifier: str
    ) -> CustomResponse:
        url = f"{setting}?{'&'.join([f'{k}={v}' for k, v in dictlink.items()])}"
        result = {"url": url, "code_verifier": code_verifier}
        return CustomResponse(
            status_code=status.HTTP_200_OK,
            body=result,
            message="Выполненно",
            name_endpoint="/link",
        )

    async def get_token(
        self,
        dictgetdata: dict,
        setting: str,
        service: str,
    ) -> CustomResponse:
        match service:
            case "vk":
                all_data_tokens = await self.send.post_json_send(
                    params=dictgetdata,
                    setting=setting,
                )
                return CustomResponse(
                    status_code=status.HTTP_200_OK,
                    body=all_data_tokens,
                    message="Выполненно",
                    name_endpoint="/get/token/",
                )
            case "yandex":
                all_data_tokens = await self.send.post_data_send(
                    params=dictgetdata,
                    setting=setting,
                )
                return CustomResponse(
                    status_code=status.HTTP_200_OK,
                    body=all_data_tokens,
                    message="Выполненно",
                    name_endpoint="/get/token/",
                )

    async def registration(
        self,
        token_access: str,
        token_refresh: str,
        dictgetdatatoken: dict,
        setting: str,
        setting_reg: str,
        service: str,
    ) -> CustomResponse:
        check_tokens = await self.valid_tokens.valid(
            token_access=token_access,
            token_refresh=token_refresh,
        )
        if "access" in check_tokens:
            self.response.set_cookie(
                key="access",
                value=check_tokens.get("access"),
                samesite="none",
                httponly=True,
                secure=True,
            )
        match service:
            case "vk":
                user = (
                    await self.send.post_json_send(
                        params=dictgetdatatoken,
                        setting=setting,
                    )
                ).get("user")
                log.info(user)
                user_data = RegistrationVK(
                    user_id=check_tokens.get("user_id"),
                    first_name=user.get("first_name"),
                    last_name=user.get("last_name"),
                    id_vk=int(user.get("user_id")),
                    email=user.get("email").lower(),
                ).model_dump()
                registration = await self.send.post_json_send(
                    params=user_data,
                    setting=setting_reg,
                )
                log.info(registration)
                return CustomResponse(
                    status_code=status.HTTP_200_OK,
                    body=registration,
                    message="Выполненно",
                    name_endpoint="/registration/",
                )
            case "yandex":
                user = await self.send.get_params_send(
                    params=dictgetdatatoken,
                    setting=setting,
                )
                log.info(user)
                user_data = RegistrationYandex(
                    user_id=check_tokens.get("user_id"),
                    first_name=user.get("first_name"),
                    last_name=user.get("last_name"),
                    id_yandex=user.get("id"),
                    login=user.get("login"),
                    email=user.get("default_email"),
                ).model_dump()
                registration = await self.send.post_json_send(
                    params=user_data,
                    setting=setting_reg,
                )
                log.info(registration)
                return CustomResponse(
                    status_code=status.HTTP_200_OK,
                    body=registration,
                    message="Выполненно",
                    name_endpoint="/registration/",
                )
