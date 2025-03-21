import logging

from aiohttp import ClientSession, ContentTypeError

from src.config import Settings
from src.database.schemas import PredictFree, PredictModel
from src.errors import SendError

log = logging.getLogger(__name__)


class VisitorsSend:

    def __init__(self):
        self.settings = Settings
        self.clientsession = ClientSession

    async def visitor_add(
        self,
        event_id: int,
        user_id: int,
    ) -> dict:
        async with self.clientsession() as session:
            async with session.post(
                url=f"{self.settings.VISITORS_ADD}{event_id}/{user_id}",
                ssl=False,
            ) as data:
                try:
                    data_json = await data.json()
                    log.warning(data_json)
                    if "detail" in data_json:
                        raise SendError(
                            name_func="visitor_add",
                            message="Неверные данные",
                        )
                    return data_json
                except ContentTypeError:
                    raise SendError(
                        name_func="visitor_add",
                        message="Неверные данные",
                    )

    async def visitor_get(
        self,
        user_id: int,
    ) -> dict:
        async with self.clientsession() as session:
            async with session.get(
                url=f"{self.settings.VISITORS_GET}{user_id}",
                ssl=False,
            ) as data:
                try:
                    data_json = await data.json()
                    log.warning(data_json)
                    if isinstance(data_json, dict) or data_json == []:
                        raise SendError(
                            name_func="visitor_get",
                            message="Неверные данные",
                        )
                    return data_json
                except ContentTypeError:
                    raise SendError(
                        name_func="visitor_get",
                        message="Неверные данные",
                    )

    async def visitor_delete(
        self,
        event_id: int,
        user_id: int,
    ) -> dict:
        async with self.clientsession() as session:
            async with session.delete(
                url=f"{self.settings.VISITORS_DELETE}{event_id}/{user_id}",
                ssl=False,
            ) as data:
                try:
                    data_json = await data.json()
                    log.warning(data_json)
                    if "detail" in data_json:
                        raise SendError(
                            name_func="visitor_delete",
                            message="Неверные данные",
                        )
                    return data_json
                except ContentTypeError:
                    raise SendError(
                        name_func="visitor_delete",
                        message="Неверные данные",
                    )


class Send:

    def __init__(self):
        self.clientsession = ClientSession

    async def post_json_send(
        self,
        params: dict,
        setting: str,
    ):
        async with self.clientsession() as session:
            async with session.post(
                url=setting,
                json=params,
                ssl=False,
            ) as data:
                try:
                    data_json = await data.json()
                    log.warning(data_json)
                    if "detail" in data_json:
                        raise SendError(
                            name_func="post_json_send",
                            message="Неверные данные",
                        )
                    return data_json
                except ContentTypeError:
                    raise SendError(
                        name_func="post_json_send",
                        message="Неверные данные",
                    )

    async def post_data_send(
        self,
        params: dict,
        setting: str,
    ):
        async with self.clientsession() as session:
            async with session.post(
                url=setting,
                data=params,
                ssl=False,
            ) as data:
                try:
                    data_json = await data.json()
                    log.warning(data_json)
                    if "detail" in data_json:
                        raise SendError(
                            name_func="post_data_send",
                            message="Неверные данные",
                        )
                    return data_json
                except ContentTypeError:
                    raise SendError(
                        name_func="post_data_send",
                        message="Неверные данные",
                    )

    async def get_params_send(
        self,
        params: dict,
        setting: str,
    ):
        async with self.clientsession() as session:
            async with session.get(
                url=setting,
                params=params,
                ssl=False,
            ) as data:
                try:
                    data_json = await data.json()
                    log.warning(data_json)
                    if "detail" in data_json:
                        raise SendError(
                            name_func="get_params_send",
                            message="Неверные данные",
                        )
                    return data_json
                except ContentTypeError:
                    raise SendError(
                        name_func="get_params_send",
                        message="Неверные данные",
                    )


class SendPredict:

    def __init__(self):
        self.settings = Settings
        self.clientsession = ClientSession

    async def send_data_recomendate(
        self,
        data: PredictModel,
    ) -> dict:
        async with self.clientsession() as session:
            data = {
                "gender": data.gender,
                "gpa": data.gpa,
                "points": data.points,
                "exams": data.exams,
            }

            async with session.post(
                self.settings.RECOMENDATE,
                json=data,
                ssl=False,
            ) as resp:
                directions = await resp.json()
                log.warning(directions)
                if "directions" not in directions:
                    raise SendError(
                        name_func="send_data_recomendate",
                        message="Неверные данные",
                    )
                return directions.get("directions")

    async def send_data_classifier_applicants(
        self,
        data: PredictModel,
        directions: list,
    ) -> dict:
        async with self.clientsession() as session:
            correct_data = {"applicants": []}
            array = [
                correct_data["applicants"].append(
                    {
                        "year": data.year,
                        "gender": data.gender,
                        "gpa": data.gpa,
                        "points": data.points,
                        "direction": str(i.get("name")),
                    }
                )
                for i in directions
            ]

            async with session.post(
                url=self.settings.CLASSIFIER,
                json=correct_data,
                ssl=False,
            ) as resp:
                data = await resp.json()
                log.warning(data)
                if "probabilities" not in data:
                    raise SendError(
                        name_func="send_data_classifier_applicants",
                        message="Неверные данные",
                    )
                return data.get("probabilities")

    async def send_data_classifier_applicant(
        self,
        data: PredictFree,
    ) -> dict:
        async with self.clientsession() as session:
            data = {
                "year": data.year,
                "gender": data.gender,
                "gpa": data.gpa,
                "points": data.points,
                "direction": data.direction,
            }

            async with session.post(
                url=f"{self.settings.CLASSIFIER_FREE}",
                json=data,
                ssl=False,
            ) as resp:
                rec = await resp.json()
                log.warning(rec)
                if "probability" not in rec:
                    raise SendError(
                        name_func="send_data_classifier_applicant",
                        message="Неверные данные",
                    )
                return rec.get("probability")

    async def send_data_directions(
        self,
        direction_id: int,
    ) -> dict:
        async with self.clientsession() as session:
            async with session.get(
                url=f"{self.settings.DIRECTION}{direction_id}",
                ssl=False,
            ) as data:
                direction = await data.json()
                log.warning(direction)
                if "description" not in direction:
                    raise SendError(
                        name_func="send_data_directions",
                        message="Неверные данные",
                    )
                return direction.get("description")

    async def send_data_points(
        self,
        direction_id: int,
    ) -> dict:
        async with self.clientsession() as session:
            async with session.get(
                url=f"{self.settings.DIRECTION_POINTS}{direction_id}",
                ssl=False,
            ) as data:
                direction_points_data = await data.json()
                log.warning(direction_points_data)
                if "history" not in direction_points_data:
                    raise SendError(
                        name_func="send_data_points",
                        message="Неверные данные",
                    )
                return direction_points_data.get("history")
