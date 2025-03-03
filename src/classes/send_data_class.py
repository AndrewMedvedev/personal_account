import json

import aiohttp

from src.config import Settings
from src.database import PredictFree, PredictModel


class SendData:

    def __init__(self):
        self.client_session = aiohttp.ClientSession()
        self.settings = Settings

    async def send_data_recomendate(
        self,
        data: PredictModel,
    ) -> dict:
        async with self.client_session as session:
            data = {
                "gender": data.gender,
                "foreign_citizenship": data.foreign_citizenship,
                "military_service": data.military_service,
                "gpa": data.gpa,
                "points": data.points,
                "bonus_points": data.bonus_points,
                "exams": data.exams,
            }

            async with session.post(
                self.settings.RECOMENDATE,
                json=data,
                ssl=False,
            ) as resp:
                rec = await resp.text()
                directions = json.loads(rec)
                return directions.get("directions")

    async def send_data_classifier_applicants(
        self,
        data: PredictModel,
        directions: list,
    ) -> dict:
        async with self.client_session as session:
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
                rec = await resp.text()
                data = json.loads(rec)
                return data.get("probabilities")

    async def send_data_classifier_applicant(
        self,
        data: PredictFree,
    ) -> dict:
        async with self.client_session as session:
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
                rec = await resp.text()
                return json.loads(rec)

    async def send_data_directions(
        self,
        direction_id: int,
    ) -> dict:
        async with self.client_session as session:
            async with session.get(
                url=f"{self.settings.DIRECTION}{direction_id}",
                ssl=False,
            ) as data:
                direction_data = await data.text()
                direction = json.loads(direction_data)
                return direction.get("description")

    async def send_data_points(
        self,
        direction_id: int,
    ) -> dict:
        async with self.client_session as session:
            async with session.get(
                url=f"{self.settings.DIRECTION_POINTS}{direction_id}",
                ssl=False,
            ) as data:
                direction_points_data = await data.text()
                cl = json.loads(direction_points_data)
                return cl.get("history")

    async def send_message_bot(
        self,
        message: str,
    ) -> dict:
        async with self.client_session as session:
            data = {
                "question": message,
            }
            async with session.post(
                url=self.settings.RAG_GigaChat_API,
                json=data,
                ssl=False,
            ) as data:
                answer_data = await data.text()
                return json.loads(answer_data)

    async def visitor_add(
        self,
        event_id: int,
        user_id: int,
    ) -> dict:
        async with self.client_session as session:
            async with session.post(
                url=f"{self.settings.VISITORS_ADD}{event_id}/{user_id}",
                ssl=False,
            ) as data:
                add_data = await data.text()
                return json.loads(add_data)

    async def visitor_get(
        self,
        user_id: int,
    ) -> dict:
        async with self.client_session as session:
            async with session.get(
                url=f"{self.settings.VISITORS_GET}{user_id}",
                ssl=False,
            ) as data:
                get_data = await data.text()
                return json.loads(get_data)

    async def visitor_delete(
        self,
        event_id: int,
        user_id: int,
    ) -> dict:
        async with self.client_session as session:
            async with session.delete(
                url=f"{self.settings.VISITORS_DELETE}{event_id}/{user_id}",
                ssl=False,
            ) as data:
                delete_data = await data.text()
                return json.loads(delete_data)
