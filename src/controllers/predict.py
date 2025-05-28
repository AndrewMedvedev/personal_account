from ..baseclasses import BaseControl
from ..rest import PredictApi
from ..schemas import PredictFreeSchema, PredictSchema


class PredictControl(BaseControl):
    def __init__(self):
        self.predict_api = PredictApi()

    async def predict(self, model: PredictSchema) -> dict:
        recomendate = await self.predict_api.get_data_recomendate(
            data=model.to_dict_get_data_recomendate()
        )
        self.logger.warning(recomendate)
        classifier = await self.predict_api.get_data_classifier_applicants(
            data=model, directions=recomendate
        )
        self.logger.warning(classifier)
        return {
            "recomendate": recomendate,
            "classifier": classifier,
        }

    async def predict_free(self, model: PredictFreeSchema) -> float:
        return await self.predict_api.get_data_classifier_applicant(data=model.to_dict())

    async def get_direction(
        self,
        direction_id: int,
    ) -> dict:
        return await self.predict_api.get_data_directions(direction_id=direction_id)

    async def get_points(
        self,
        direction_id: int,
    ) -> dict:
        return await self.predict_api.get_data_points(direction_id=direction_id)

    async def get_exams(
        self,
        direction_id: int,
    ) -> dict:
        return await self.predict_api.get_data_exams(direction_id=direction_id)
