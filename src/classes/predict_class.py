from fastapi import Response
from fastapi.responses import JSONResponse

from src.classes.send_data_class import SendData
from src.classes.tokens_classes import ValidTokens
from src.database import PredictFree, PredictModel
from src.interfaces import PredictBase


class Predict(PredictBase):

    def __init__(
        self,
        token_access: str = None,
        token_refresh: str = None,
        response: Response = None,
        model: PredictModel = None,
    ) -> None:
        self.token_access = token_access
        self.token_refresh = token_refresh
        self.model = model
        self.response = response
        self.valid_tokens = ValidTokens
        self.send_data = SendData()

    async def predict(self) -> JSONResponse:
        check_tokens = await self.valid_tokens(
            token_access=self.token_access,
            token_refresh=self.token_refresh,
            response=self.response,
        ).valid()
        recomendate = await self.send_data.send_data_recomendate(self.model)
        classifier = await self.send_data.send_data_classifier_applicants(
            data=self.model,
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
        return JSONResponse(
            content={
                "recomendate": recomendate,
                "classifier": classifier,
            }
        )

    async def predict_free(
        self,
        model: PredictFree,
    ) -> float:
        classifier = await self.send_data.send_data_classifier_applicant(model)
        return classifier.get("probability")

    async def get_direction(self, direction_id: int) -> JSONResponse:
        check_tokens = await self.valid_tokens(
            token_access=self.token_access,
            token_refresh=self.token_refresh,
            response=self.response,
        ).valid()
        direction = await self.send_data.send_data_directions(direction_id)
        if "access" in check_tokens:
            self.response.set_cookie(
                key="access",
                value=check_tokens.get("access"),
                samesite="none",
                httponly=True,
                secure=True,
            )
        return JSONResponse(content=direction)

    async def get_points(self, direction_id: int) -> JSONResponse:
        check_tokens = await self.valid_tokens(
            token_access=self.token_access,
            token_refresh=self.token_refresh,
            response=self.response,
        ).valid()
        points = await self.send_data.send_data_points(direction_id)
        if "access" in check_tokens:
            self.response.set_cookie(
                key="access",
                value=check_tokens.get("access"),
                samesite="none",
                httponly=True,
                secure=True,
            )
        return JSONResponse(content=points)
