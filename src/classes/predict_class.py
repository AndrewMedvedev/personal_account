from fastapi import Response
from fastapi.responses import JSONResponse

from src.classes.send_data_class import SendData
from src.classes.tokens_classes import ValidTokens
from src.database import PredictModel


class Predict:

    def __init__(
        self,
        token_access: str,
        token_refresh: str,
        response: Response,
        model: PredictModel = None,
    ) -> None:
        self.token_access = token_access
        self.token_refresh = token_refresh
        self.model = model
        self.response = response

    async def predict(self) -> JSONResponse:
        check_tokens = await ValidTokens(
            token_access=self.token_access,
            token_refresh=self.token_refresh,
            response=self.response,
        ).valid()
        recomendate = await SendData.send_data_recomendate(self.model)
        classifier = await SendData.send_data_classifier_applicants(
            data=self.model,
            directions=recomendate,
        )
        if "access" in check_tokens:
            self.response.set_cookie(
                key="access",
                value=check_tokens.get("access"),
                samesite=None,
                httponly=True,
                secure=True,
            )
        return JSONResponse(
            content={
                "recomendate": recomendate,
                "classifier": classifier,
            }
        )

    async def get_direction(self, direction_id: int):
        check_tokens = await ValidTokens(
            token_access=self.token_access,
            token_refresh=self.token_refresh,
            response=self.response,
        ).valid()
        direction = await SendData.send_data_directions(direction_id)
        if "access" in check_tokens:
            self.response.set_cookie(
                key="access",
                value=check_tokens.get("access"),
                samesite=None,
                httponly=False,
                secure=True,
            )
        return JSONResponse(content=direction)

    async def get_points(self, direction_id: int):
        check_tokens = await ValidTokens(
            token_access=self.token_access,
            token_refresh=self.token_refresh,
            response=self.response,
        ).valid()
        points = await SendData.send_data_points(direction_id)
        if "access" in check_tokens:
            self.response.set_cookie(
                key="access",
                value=check_tokens.get("access"),
                samesite=None,
                httponly=False,
                secure=True,
            )
        return JSONResponse(content=points)
