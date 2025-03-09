from abc import ABC, abstractmethod

from fastapi.responses import JSONResponse


class OtherRegistrationBase(ABC):

    @abstractmethod
    async def link(self) -> JSONResponse:
        raise NotImplementedError

    @abstractmethod
    async def get_token(
        self,
        code_verifier: str,
    ) -> JSONResponse:
        raise NotImplementedError

    @abstractmethod
    async def registration(self) -> JSONResponse:
        raise NotImplementedError
