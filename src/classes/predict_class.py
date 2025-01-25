from src.classes.send_data_class import SendData
from src.classes.tokens_classes import check
from src.database.schemas.predict_schemas import PredictModel


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

    async def predict(self) -> dict:
        check_tokens = await check(
            access=self.token_access,
            refresh=self.token_refresh,
        )
        recomendate = await SendData.send_data_recomendate(self.model)
        classifier = await SendData.send_data_classifier_applicants(
            self.model,
            directions=recomendate.get("data"),
        )
        result = {
            "recomendate": recomendate.get("data"),
            "classifier": classifier.get("predictions"),
        }
        if "access" in check_tokens:
            result["access"] = check_tokens.get("access")

        return result
