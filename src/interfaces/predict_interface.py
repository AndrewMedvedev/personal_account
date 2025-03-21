from abc import ABC, abstractmethod

from fastapi.responses import JSONResponse


class PredictBase(ABC):

    @abstractmethod
    async def predict() -> JSONResponse:
        raise NotImplementedError

    @abstractmethod
    async def predict_free() -> float:
        raise NotImplementedError

    @abstractmethod
    async def get_direction() -> JSONResponse:
        raise NotImplementedError

    @abstractmethod
    async def get_points() -> JSONResponse:
        raise NotImplementedError
