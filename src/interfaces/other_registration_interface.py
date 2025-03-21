from abc import ABC, abstractmethod

from fastapi.responses import JSONResponse


class OtherRegistrationBase(ABC):

    @abstractmethod
    async def link() -> JSONResponse:
        raise NotImplementedError

    @abstractmethod
    async def get_token() -> JSONResponse:
        raise NotImplementedError

    @abstractmethod
    async def registration() -> JSONResponse:
        raise NotImplementedError
