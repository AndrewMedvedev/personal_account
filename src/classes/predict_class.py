from fastapi import Response, status
from fastapi.responses import JSONResponse

from src.classes.send_data_class import SendData
from src.classes.tokens_classes import ValidTokens
from src.database import PredictModel


class Predict:

    def __init__(
        self,
        token_access: str,
        token_refresh: str,
        model: PredictModel,
        response: Response,
    ) -> None:
        self.token_access = token_access
        self.token_refresh = token_refresh
        self.model = model
        self.response = response

    @staticmethod
    async def send(model: PredictModel) -> JSONResponse:
        recomendate = await SendData.send_data_recomendate(model)
        classifier = await SendData.send_data_classifier_applicants(
            model,
            directions=recomendate.get("data"),
        )
        return JSONResponse(
            content={
                "recomendate": recomendate.get("data"),
                "classifier": classifier.get("predictions"),
            }
        )

    async def predict(self) -> dict | JSONResponse:
        check_tokens = await ValidTokens(
            token_access=self.token_access,
            token_refresh=self.token_refresh,
            response=self.response,
        ).valid()
        match check_tokens:
            case True:
                self.send(self.model)
            case False:
                return JSONResponse(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                )
            case _:
                self.response.set_cookie(
                    key="access",
                    value=check_tokens.get("access"),
                    samesite="none",
                    httponly=True,
                    secure=True,
                )
                self.send(self.model)
