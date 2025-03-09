from abc import ABC, abstractmethod

from fastapi.responses import JSONResponse


class ReUseBase(ABC):

    @staticmethod
    @abstractmethod
    async def link(setting: str, dictlink: dict, code_verifier: str) -> JSONResponse:
        raise NotImplementedError

    @abstractmethod
    async def get_token(
        self,
        dictgetdata: dict,
    ) -> JSONResponse:
        raise NotImplementedError

    @abstractmethod
    async def registration(
        self,
        user_data: dict,
        token_access: str,
        token_refresh: str,
        send,
    ) -> JSONResponse:
        raise NotImplementedError
