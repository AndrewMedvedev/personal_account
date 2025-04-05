from abc import ABC, abstractmethod

from fastapi.responses import JSONResponse, StreamingResponse


class VisitorBase(ABC):
    @abstractmethod
    async def add() -> JSONResponse:
        raise NotImplementedError

    @abstractmethod
    async def get() -> JSONResponse:
        raise NotImplementedError

    @abstractmethod
    async def delete() -> JSONResponse:
        raise NotImplementedError

    @abstractmethod
    async def make_qr() -> StreamingResponse:
        raise NotImplementedError
