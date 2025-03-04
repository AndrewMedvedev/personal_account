from abc import ABC, abstractmethod

from fastapi.responses import JSONResponse


class PredictBase(ABC):

    @abstractmethod
    async def predict(self) -> JSONResponse:
        raise NotImplementedError

    @abstractmethod
    async def predict_free(self) -> float:
        raise NotImplementedError

    @abstractmethod
    async def get_direction(
        self,
        direction_id: int,
    ) -> JSONResponse:
        raise NotImplementedError

    @abstractmethod
    async def get_points(
        self,
        direction_id: int,
    ) -> JSONResponse:
        raise NotImplementedError
