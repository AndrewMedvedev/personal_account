from fastapi import HTTPException, Response, status
from src.classes.send_data_class import SendData
from src.classes.tokens_classes import check
from src.database.schemas import PredictModel


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

    async def predict(self) -> dict | HTTPException:
        check_tokens = check(
            access=self.token_access,
            refresh=self.token_refresh,
        )
        if type(check_tokens) == dict:
            recomendate = await SendData.send_data_recomendate(self.model)
            classifier = await SendData.send_data_classifier_applicants(
                self.model,
                directions=recomendate.get("data"),
            )
            self.response.set_cookie(
                key="access",
                value=check_tokens.get("access"),
            )
            return {
                "recomendate": recomendate.get("data"),
                "classifier": classifier.get("predictions"),
            }
        elif type(check_tokens) == str:
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
