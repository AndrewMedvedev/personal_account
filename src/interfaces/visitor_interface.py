from abc import ABC, abstractmethod

from fastapi.responses import JSONResponse, StreamingResponse


class VisitorBase(ABC):

    @abstractmethod
    async def add(self) -> JSONResponse:
        raise NotImplementedError

    @abstractmethod
    async def get(self) -> JSONResponse:
        raise NotImplementedError

    @abstractmethod
    async def delete(self) -> JSONResponse:
        raise NotImplementedError

    @abstractmethod
    async def make_qr(
        self,
        unique_string: str,
    ) -> StreamingResponse:
        raise NotImplementedError
