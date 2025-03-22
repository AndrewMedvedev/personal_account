import logging

from fastapi import status

from src.classes.send_data_class import SendPredict
from src.database.schemas import CustomResponse, PredictFree, PredictModel
from src.interfaces import PredictBase

log = logging.getLogger(__name__)


class Predict(PredictBase):

    def __init__(self) -> None:
        self.send_data = SendPredict()

    async def predict(
        self,
        model: PredictModel,
    ) -> CustomResponse:
        recomendate = await self.send_data.get_data_recomendate(model)
        classifier = await self.send_data.get_data_classifier_applicants(
            data=model,
            directions=recomendate,
        )
        result = {
            "recomendate": recomendate,
            "classifier": classifier,
        }
        return CustomResponse(
            status_code=status.HTTP_200_OK,
            body=result,
            message="Выполненно",
            name_endpoint="/predict",
        )

    async def predict_free(
        self,
        model: PredictFree,
    ) -> CustomResponse:
        classifier = await self.send_data.get_data_classifier_applicant(model)
        return CustomResponse(
            status_code=status.HTTP_200_OK,
            body=classifier,
            message="Выполненно",
            name_endpoint="/predict/free",
        )

    async def get_direction(
        self,
        direction_id: int,
    ) -> CustomResponse:
        direction = await self.send_data.get_data_directions(direction_id)
        return CustomResponse(
            status_code=status.HTTP_200_OK,
            body=direction,
            message="Выполненно",
            name_endpoint="/direction/{direction_id}",
        )

    async def get_points(
        self,
        direction_id: int,
    ) -> CustomResponse:
        points = await self.send_data.get_data_points(direction_id)
        return CustomResponse(
            status_code=status.HTTP_200_OK,
            body=points,
            message="Выполненно",
            name_endpoint="/points/{direction_id}",
        )

    async def get_exams(
        self,
        direction_id: int,
    ) -> CustomResponse:
        points = await self.send_data.get_data_exams(direction_id)
        return CustomResponse(
            status_code=status.HTTP_200_OK,
            body=points,
            message="Выполненно",
            name_endpoint="/points/{direction_id}",
        )
