import json

import aiohttp

from src.config import Settings
from src.database import PredictFree, PredictModel


class SendData:

    async def send_data_recomendate(data: PredictModel) -> dict:
        async with aiohttp.ClientSession() as session:
            data = {
                "top_n": data.top_n,
                "user": {
                    "gender": data.gender,
                    "age": data.age,
                    "sport": data.sport,
                    "foreign": data.foreign,
                    "gpa": data.gpa,
                    "total_points": data.points,
                    "bonus_points": data.bonus_points,
                    "exams": data.exams,
                    "education": data.education,
                    "study_form": data.study_form,
                },
            }

            async with session.post(
                Settings.RECOMENDATE,
                json=data,
                ssl=False,
            ) as resp:
                rec = await resp.text()
                return json.loads(rec)

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
                        "direction": i[23::],
                    }
                )
                for i in directions
            ]

            async with session.post(
                Settings.CLASSIFIER,
                json=correct_data,
                ssl=False,
            ) as resp:
                rec = await resp.text()
                return json.loads(rec)

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
                Settings.CLASSIFIER_FREE,
                json=data,
                ssl=False,
            ) as resp:
                rec = await resp.text()
                return json.loads(rec)

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
