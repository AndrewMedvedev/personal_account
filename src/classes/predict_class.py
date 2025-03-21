import logging

from fastapi import Response, status

from src.classes.send_data_class import SendPredict
from src.classes.tokens_classes import ValidTokens
from src.database.schemas import CustomResponse, PredictFree, PredictModel
from src.interfaces import PredictBase

log = logging.getLogger(__name__)


class Predict(PredictBase):

    def __init__(self) -> None:
        self.valid_tokens = ValidTokens()
        self.send_data = SendPredict()
        self.response = Response

    async def predict(
        self,
        model: PredictModel,
        token_access: str,
        token_refresh: str,
    ) -> CustomResponse:
        check_tokens = await self.valid_tokens.valid(
            token_access=token_access,
            token_refresh=token_refresh,
        )
        recomendate = await self.send_data.send_data_recomendate(model)
        classifier = await self.send_data.send_data_classifier_applicants(
            data=model,
            directions=recomendate,
        )
        if "access" in check_tokens:
            self.response.set_cookie(
                key="access",
                value=check_tokens.get("access"),
                samesite="none",
                httponly=True,
                secure=True,
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
        classifier = await self.send_data.send_data_classifier_applicant(model)
        return CustomResponse(
            status_code=status.HTTP_200_OK,
            body=classifier,
            message="Выполненно",
            name_endpoint="/predict/free",
        )

    async def get_direction(
        self,
        direction_id: int,
        token_access: str,
        token_refresh: str,
    ) -> CustomResponse:
        check_tokens = await self.valid_tokens.valid(
            token_access=token_access,
            token_refresh=token_refresh,
        )
        direction = await self.send_data.send_data_directions(direction_id)
        if "access" in check_tokens:
            self.response.set_cookie(
                key="access",
                value=check_tokens.get("access"),
                samesite="none",
                httponly=True,
                secure=True,
            )
        return CustomResponse(
            status_code=status.HTTP_200_OK,
            body=direction,
            message="Выполненно",
            name_endpoint="/direction/{direction_id}",
        )

    async def get_points(
        self,
        direction_id: int,
        token_access: str,
        token_refresh: str,
    ) -> CustomResponse:
        check_tokens = await self.valid_tokens.valid(
            token_access=token_access,
            token_refresh=token_refresh,
        )
        points = await self.send_data.send_data_points(direction_id)
        if "access" in check_tokens:
            self.response.set_cookie(
                key="access",
                value=check_tokens.get("access"),
                samesite="none",
                httponly=True,
                secure=True,
            )
        return CustomResponse(
            status_code=status.HTTP_200_OK,
            body=points,
            message="Выполненно",
            name_endpoint="/points/{direction_id}",
        )
