import json

import aiohttp

from src.config import Settings
from src.database import PredictFree, PredictModel


class SendData:

    async def send_data_recomendate(data: PredictModel) -> dict:
        async with aiohttp.ClientSession() as session:
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
                Settings.RECOMENDATE,
                json=data,
                ssl=False,
            ) as resp:
                rec = await resp.text()
                directions = json.loads(rec)
                return directions.get("directions")

    async def send_data_classifier_applicants(
        data: PredictModel, directions: list
    ) -> dict:
        async with aiohttp.ClientSession() as session:
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
                url=Settings.CLASSIFIER,
                json=correct_data,
                ssl=False,
            ) as resp:
                rec = await resp.text()
                data = json.loads(rec)
                return data.get("probabilities")

    async def send_data_classifier_applicant(data: PredictFree) -> dict:
        async with aiohttp.ClientSession() as session:
            data = {
                "year": data.year,
                "gender": data.gender,
                "gpa": data.gpa,
                "points": data.points,
                "direction": data.direction,
            }

            async with session.post(
                url=f"{Settings.CLASSIFIER_FREE}",
                json=data,
                ssl=False,
            ) as resp:
                rec = await resp.text()
                return json.loads(rec)

    async def send_data_directions(direction_id: int) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url=f"{Settings.DIRECTION}{direction_id}",
                ssl=False,
            ) as data:
                direction_data = await data.text()
                direction = json.loads(direction_data)
                return direction.get("description")

    async def send_data_points(direction_id: int) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url=f"{Settings.DIRECTION_POINTS}{direction_id}",
                ssl=False,
            ) as data:
                direction_points_data = await data.text()
                cl = json.loads(direction_points_data)
                return cl.get("history")

    async def send_message_bot(message: str) -> dict:
        async with aiohttp.ClientSession() as session:
            data = {
                "question": message,
            }
            async with session.post(
                url=Settings.RAG_GigaChat_API,
                json=data,
                ssl=False,
            ) as data:
                answer_data = await data.text()
                return json.loads(answer_data)
