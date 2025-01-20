from fastapi import HTTPException, status
from src.classes.send_data_class import SendData
from src.classes.tokens_classes import SendTokens
from src.database.schemas import PredictModel


class Predict:

    def __init__(
        self,
        token_access: str,
        token_refresh: str,
        model: PredictModel,
    ) -> None:
        self.token_access = token_access
        self.token_refresh = token_refresh
        self.model = model

    async def predict(self) -> dict | HTTPException:
        tkn_access = await SendTokens(self.token_access).send_access_token()
        tkn_refresh = await SendTokens(self.token_refresh).send_refresh_token()
        if tkn_access != False and tkn_refresh != False:
            recomendate = await SendData.send_data_recomendate(self.model)
            classifier = await SendData.send_data_classifier_applicants(
                self.model,
                directions=recomendate.get("data"),
            )
            return {
                "recomendate": recomendate.get("data"),
                "classifier": classifier.get("predictions"),
            }
        else:
            return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
